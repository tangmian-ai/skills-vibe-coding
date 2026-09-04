"""
Scan Poster Overlay — ComfyUI Custom Node
Applies a Y2K surveillance / scan-poster HUD overlay to any uploaded image.
No prompt needed. Fully automatic.

Detection priority:
  1. SEGS input from Impact-Pack (if connected)
  2. YOLOv8-nano via ultralytics (if installed)
  3. Heuristic fallback (always works)
"""

import torch
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import math

# ═══════════════════════════════════════════════════════════════
# Colour themes
# ═══════════════════════════════════════════════════════════════

THEMES = {
    "green": {
        "primary":   (0, 255, 80),
        "secondary": (0, 180, 60),
        "dim":       (0, 100, 35),
        "text":      (0, 255, 80),
        "tint_rgba": (0, 20, 5, 45),
        "hex_label": "#33CC00",
    },
    "red": {
        "primary":   (255, 50, 50),
        "secondary": (200, 35, 35),
        "dim":       (130, 25, 25),
        "text":      (255, 55, 55),
        "tint_rgba": (25, 0, 0, 45),
        "hex_label": "#E71D36",
    },
    "cyan": {
        "primary":   (0, 220, 255),
        "secondary": (0, 165, 210),
        "dim":       (0, 95, 125),
        "text":      (0, 220, 255),
        "tint_rgba": (0, 12, 28, 45),
        "hex_label": "#1A78BC",
    },
    "blue": {
        "primary":   (75, 105, 255),
        "secondary": (55, 80, 200),
        "dim":       (35, 55, 140),
        "text":      (80, 115, 255),
        "tint_rgba": (5, 5, 28, 45),
        "hex_label": "#4060FF",
    },
}

# ═══════════════════════════════════════════════════════════════
# Label pools (auto-assigned when YOLO unavailable)
# ═══════════════════════════════════════════════════════════════

YOLO_LABEL_MAP = {
    "person": "HUMAN", "man": "MALE", "woman": "FEMALE",
    "dog": "CANINE", "cat": "FELINE", "bird": "AVIAN",
    "car": "VEHICLE", "truck": "VEHICLE", "bus": "VEHICLE",
    "bicycle": "BICYCLE", "motorcycle": "MOTORCYCLE",
    "bottle": "CONTAINER", "cup": "CONTAINER",
    "laptop": "DEVICE", "cell phone": "DEVICE", "tv": "DISPLAY",
    "chair": "FURNITURE", "couch": "FURNITURE", "bed": "FURNITURE",
    "book": "DOCUMENT", "clock": "TIMEPIECE",
    "backpack": "GEAR", "umbrella": "EQUIPMENT",
    "handbag": "ACCESSORY", "tie": "ACCESSORY",
    "horse": "EQUINE", "cow": "BOVINE", "sheep": "OVINE",
}

GENERIC_LABELS = [
    "DETECTED", "IDENTIFIED", "TRACKED",
    "CLASSIFIED", "ANALYZED", "LOCKED",
]

DETAIL_LABELS = [
    "DETAIL ANALYZED", "FEATURE EXTRACTED", "TEXTURE MAPPED",
    "PATTERN DETECTED", "DETAIL ENHANCED", "REGION SCANNED",
]

CCTV_CODES = [
    "CCTV TR521", "CCTV_01", "CAM_A7", "SURV_03",
    "MON_B2", "SEC_12", "SCAN_07", "REC_A1",
]


# ═══════════════════════════════════════════════════════════════
# Font helper
# ═══════════════════════════════════════════════════════════════

_font_cache: dict = {}

def _get_font(size: int) -> ImageFont.FreeTypeFont:
    if size in _font_cache:
        return _font_cache[size]

    candidates = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/System/Library/Fonts/SFMono-Regular.otf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for p in candidates:
        try:
            font = ImageFont.truetype(p, size)
            _font_cache[size] = font
            return font
        except (IOError, OSError):
            continue

    try:
        font = ImageFont.load_default(size=size)
    except TypeError:
        font = ImageFont.load_default()
    _font_cache[size] = font
    return font


# ═══════════════════════════════════════════════════════════════
# Geometry helpers
# ═══════════════════════════════════════════════════════════════

def _clamp_box(bbox, w, h):
    return (
        max(0, min(bbox[0], w - 1)),
        max(0, min(bbox[1], h - 1)),
        max(1, min(bbox[2], w)),
        max(1, min(bbox[3], h)),
    )


def _dominant_hex(pil_img: Image.Image, bbox) -> str:
    x1, y1, x2, y2 = bbox
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(pil_img.width, x2), min(pil_img.height, y2)
    if x2 <= x1 or y2 <= y1:
        return "#808080"
    crop = pil_img.crop((x1, y1, x2, y2)).resize((1, 1), Image.BILINEAR)
    r, g, b = crop.getpixel((0, 0))[:3]
    return f"#{r:02X}{g:02X}{b:02X}"


def _box_area(bbox):
    return max(0, bbox[2] - bbox[0]) * max(0, bbox[3] - bbox[1])


def _iou_ratio(a, b):
    """Overlap area of *a* divided by area of *a*."""
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    area_a = _box_area(a)
    if area_a == 0:
        return 0
    return (ix * iy) / area_a


# ═══════════════════════════════════════════════════════════════
# Object detection — three strategies
# ═══════════════════════════════════════════════════════════════

def _detect_yolo(pil_img: Image.Image):
    try:
        from ultralytics import YOLO
        model = YOLO("yolov8n.pt")
        results = model(np.array(pil_img), verbose=False)
        boxes = []
        for r in results:
            for b in r.boxes:
                x1, y1, x2, y2 = b.xyxy[0].tolist()
                cls = r.names[int(b.cls[0])]
                conf = float(b.conf[0])
                if conf > 0.30:
                    mapped = YOLO_LABEL_MAP.get(cls.lower(), cls.upper())
                    boxes.append({
                        "bbox": (int(x1), int(y1), int(x2), int(y2)),
                        "label": mapped,
                        "conf": conf,
                    })
        return boxes or None
    except Exception:
        return None


def _detect_heuristic(w, h):
    boxes = []
    cx, cy = w // 2, h // 2
    bw = int(w * random.uniform(0.28, 0.42))
    bh = int(h * random.uniform(0.35, 0.55))
    ox = int(w * random.uniform(-0.04, 0.04))
    oy = int(h * random.uniform(-0.04, 0.04))
    boxes.append({
        "bbox": _clamp_box(
            (cx - bw // 2 + ox, cy - bh // 2 + oy,
             cx + bw // 2 + ox, cy + bh // 2 + oy), w, h),
        "label": random.choice(GENERIC_LABELS),
        "conf": round(random.uniform(0.88, 0.99), 2),
    })

    thirds = [
        (w // 3, h // 3), (2 * w // 3, h // 3),
        (w // 3, 2 * h // 3), (2 * w // 3, 2 * h // 3),
    ]
    random.shuffle(thirds)
    for i in range(random.randint(1, 2)):
        tx, ty = thirds[i]
        bw2 = int(w * random.uniform(0.10, 0.20))
        bh2 = int(h * random.uniform(0.10, 0.20))
        box = _clamp_box(
            (tx - bw2 // 2, ty - bh2 // 2,
             tx + bw2 // 2, ty + bh2 // 2), w, h)
        if _iou_ratio(box, boxes[0]["bbox"]) < 0.25:
            boxes.append({
                "bbox": box,
                "label": random.choice(GENERIC_LABELS),
                "conf": round(random.uniform(0.68, 0.94), 2),
            })
    return boxes


def _segs_to_boxes(segs):
    if segs is None:
        return None
    try:
        _, seg_list = segs
        if not seg_list:
            return None
        boxes = []
        for s in seg_list:
            bb = s.bbox
            lbl = (getattr(s, "label", None) or "OBJECT").upper()
            lbl = YOLO_LABEL_MAP.get(lbl.lower(), lbl)
            boxes.append({
                "bbox": (int(bb[0]), int(bb[1]), int(bb[2]), int(bb[3])),
                "label": lbl,
                "conf": round(float(getattr(s, "confidence", 0.90) or 0.90), 2),
            })
        return boxes or None
    except Exception:
        return None


# ═══════════════════════════════════════════════════════════════
# Drawing primitives
# ═══════════════════════════════════════════════════════════════

def _draw_brackets(draw, bbox, color, thickness=2, ratio=0.22):
    """L-shaped surveillance-style corner brackets."""
    x1, y1, x2, y2 = bbox
    ln = max(8, int(min(x2 - x1, y2 - y1) * ratio))
    for (sx, sy, dx, dy) in [
        (x1, y1, 1, 1), (x2, y1, -1, 1),
        (x1, y2, 1, -1), (x2, y2, -1, -1),
    ]:
        draw.line([(sx, sy), (sx + dx * ln, sy)], fill=color, width=thickness)
        draw.line([(sx, sy), (sx, sy + dy * ln)], fill=color, width=thickness)


def _draw_crosshair(draw, cx, cy, size, color, thickness=1):
    s = size // 2
    draw.line([(cx - s, cy), (cx + s, cy)], fill=color, width=thickness)
    draw.line([(cx, cy - s), (cx, cy + s)], fill=color, width=thickness)
    gap = s // 3
    r = s // 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                 outline=color, width=thickness)


def _text_with_bg(draw, xy, text, font, fg, bg_alpha=130):
    x, y = xy
    tb = draw.textbbox((x, y), text, font=font)
    p = 3
    draw.rectangle(
        [tb[0] - p, tb[1] - p, tb[2] + p, tb[3] + p],
        fill=(0, 0, 0, bg_alpha),
    )
    draw.text((x, y), text, fill=fg, font=font)


# ═══════════════════════════════════════════════════════════════
# Main ComfyUI node
# ═══════════════════════════════════════════════════════════════

class ScanPosterOverlay:
    """One-click Y2K surveillance scan-poster overlay — no prompt needed."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "color_theme": (
                    ["green", "red", "cyan", "blue", "random"],
                    {"default": "green"},
                ),
                "num_detail_boxes": (
                    "INT", {"default": 2, "min": 0, "max": 4, "step": 1},
                ),
                "scan_line_opacity": (
                    "FLOAT", {"default": 0.10, "min": 0.0, "max": 0.50, "step": 0.02},
                ),
                "vignette_strength": (
                    "FLOAT", {"default": 0.55, "min": 0.0, "max": 1.0, "step": 0.05},
                ),
                "tint_strength": (
                    "FLOAT", {"default": 0.15, "min": 0.0, "max": 0.50, "step": 0.05},
                ),
                "noise_strength": (
                    "FLOAT", {"default": 0.03, "min": 0.0, "max": 0.20, "step": 0.01},
                ),
                "seed": (
                    "INT", {"default": 0, "min": 0, "max": 0xFFFFFFFF},
                ),
            },
            "optional": {
                "segs_opt": ("SEGS",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "execute"
    CATEGORY = "image/effects"

    def execute(
        self, image, color_theme, num_detail_boxes,
        scan_line_opacity, vignette_strength, tint_strength,
        noise_strength, seed, segs_opt=None,
    ):
        results = []
        for i in range(image.shape[0]):
            if seed > 0:
                random.seed(seed + i)
                np.random.seed((seed + i) % (2**31))

            pil = Image.fromarray(
                (image[i].cpu().numpy() * 255).astype(np.uint8)
            ).convert("RGB")

            out = self._render(
                pil, color_theme, num_detail_boxes,
                scan_line_opacity, vignette_strength,
                tint_strength, noise_strength, segs_opt,
            )

            results.append(
                torch.from_numpy(np.array(out).astype(np.float32) / 255.0)
            )

        return (torch.stack(results),)

    # ─── render pipeline ────────────────────────────────────

    def _render(
        self, img, theme_name, n_details, sl_opacity,
        vig_str, tint_str, noise_str, segs_opt,
    ):
        if theme_name == "random":
            theme_name = random.choice(list(THEMES.keys()))
        theme = THEMES[theme_name]

        w, h = img.size
        scale = min(w, h) / 1024.0

        fonts = {
            "sm": _get_font(max(10, int(12 * scale))),
            "md": _get_font(max(12, int(16 * scale))),
            "lg": _get_font(max(14, int(22 * scale))),
        }

        # ── detect objects ──────────────────────────────────
        boxes = _segs_to_boxes(segs_opt)
        if boxes is None:
            boxes = _detect_yolo(img)
        if boxes is None:
            boxes = _detect_heuristic(w, h)

        # ── base layer (with colour tint) ───────────────────
        base = img.convert("RGBA")
        if tint_str > 0:
            r0, g0, b0, a0 = theme["tint_rgba"]
            alpha = min(255, int(a0 * (tint_str / 0.15)))
            tint_layer = Image.new("RGBA", (w, h), (r0, g0, b0, alpha))
            base = Image.alpha_composite(base, tint_layer)

        # ── HUD overlay layer ───────────────────────────────
        hud = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(hud)

        th = max(1, int(2 * scale))       # bracket thickness
        margin = int(14 * scale)
        lh = int(18 * scale)              # line height

        # ── 1. bounding boxes ───────────────────────────────
        for idx, b in enumerate(boxes):
            bbox = _clamp_box(b["bbox"], w, h)
            col_a = theme["primary"] + (220,)

            _draw_brackets(draw, bbox, col_a, th)

            if idx == 0:
                bcx = (bbox[0] + bbox[2]) // 2
                bcy = (bbox[1] + bbox[3]) // 2
                _draw_crosshair(
                    draw, bcx, bcy, int(24 * scale),
                    theme["dim"] + (140,), max(1, int(scale)),
                )

            prefix = "SUBJECT" if idx == 0 else random.choice(
                ["TARGET", "OBJECT", "ELEMENT"]
            )
            label = f"{prefix}: {b['label']}"

            lx = bbox[0]
            ly = bbox[1] - int(20 * scale)
            if ly < 5:
                ly = bbox[3] + int(5 * scale)
            _text_with_bg(
                draw, (lx, ly), label, fonts["sm"],
                theme["text"] + (230,),
            )

            hex_str = _dominant_hex(img, bbox)
            hx_x = max(bbox[0], bbox[2] - int(62 * scale))
            hx_y = bbox[1] + int(4 * scale)
            if hx_y < ly + int(16 * scale) and hx_y > ly - int(16 * scale):
                hx_y = bbox[3] - int(16 * scale)
            draw.text(
                (hx_x, hx_y), hex_str,
                fill=theme["secondary"] + (170,), font=fonts["sm"],
            )

            conf_txt = f"{b['conf']:.0%}"
            draw.text(
                (bbox[0] + int(4 * scale), bbox[3] - int(16 * scale)),
                conf_txt,
                fill=theme["dim"] + (170,), font=fonts["sm"],
            )

        # ── 2. detail callout boxes ─────────────────────────
        if n_details > 0 and boxes:
            det_sz = max(55, int(min(w, h) * 0.16))

            corners = [
                (margin, h - margin - det_sz - lh * 2),
                (w - margin - det_sz, h - margin - det_sz - lh * 2),
                (margin, margin + lh * 4),
                (w - margin - det_sz, margin + lh * 4),
            ]
            random.shuffle(corners)

            for di in range(min(n_details, len(boxes), len(corners))):
                bb = boxes[di % len(boxes)]["bbox"]
                scx = (bb[0] + bb[2]) // 2
                scy = (bb[1] + bb[3]) // 2
                half = max(20, min(bb[2] - bb[0], bb[3] - bb[1]) // 3)
                src = _clamp_box(
                    (scx - half, scy - half, scx + half, scy + half), w, h,
                )

                crop = img.crop(src).resize(
                    (det_sz, det_sz), Image.LANCZOS,
                )
                tx, ty = corners[di]

                hud.paste(crop.convert("RGBA"), (tx, ty))

                bdr = max(1, int(1.5 * scale))
                draw.rectangle(
                    [tx - bdr, ty - bdr,
                     tx + det_sz + bdr, ty + det_sz + bdr],
                    outline=theme["primary"] + (200,), width=bdr,
                )

                dcx = tx + det_sz // 2
                dcy = ty + det_sz // 2
                line_col = theme["dim"] + (110,)
                draw.line(
                    [(scx, scy), (dcx, dcy)],
                    fill=line_col, width=max(1, int(scale)),
                )

                r = int(3 * scale)
                draw.ellipse(
                    [scx - r, scy - r, scx + r, scy + r],
                    outline=theme["primary"] + (200,),
                    width=max(1, int(scale)),
                )

                dl = random.choice(DETAIL_LABELS)
                draw.text(
                    (tx, ty + det_sz + int(4 * scale)),
                    dl, fill=theme["text"] + (190,), font=fonts["sm"],
                )

        # ── 3. system info text ─────────────────────────────
        date_str = (
            f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        )
        ts = (
            f"{random.randint(0,23):02d}:"
            f"{random.randint(0,59):02d}:"
            f"{random.randint(0,59):02d}"
        )
        cctv = random.choice(CCTV_CODES)
        progress = random.randint(65, 99)

        # top-left
        tl_lines = [
            "SYSTEM: Y2K-SURV",
            f"DATE: {date_str}",
            f"HEX: {theme['hex_label']}",
        ]
        for i, t in enumerate(tl_lines):
            _text_with_bg(
                draw, (margin, margin + i * lh),
                t, fonts["sm"], theme["text"] + (200,),
            )

        # top-right
        for i, t in enumerate([cctv, ts]):
            tb = draw.textbbox((0, 0), t, font=fonts["md"])
            tw = tb[2] - tb[0]
            _text_with_bg(
                draw, (w - margin - tw, margin + i * lh),
                t, fonts["md"], theme["text"] + (230,),
            )

        # bottom-left
        bl_lines = ["DATA UPDATE",
                     f"SCENE {random.randint(1,20):02d}/{random.randint(20,30):02d}"]
        for i, t in enumerate(bl_lines):
            _text_with_bg(
                draw, (margin, h - margin - (2 - i) * lh),
                t, fonts["sm"], theme["text"] + (180,),
            )

        # bottom-right: progress text
        ptxt = f"PROGRESS: {progress}%"
        tb = draw.textbbox((0, 0), ptxt, font=fonts["sm"])
        ptw = tb[2] - tb[0]
        _text_with_bg(
            draw, (w - margin - ptw, h - margin - 2 * lh),
            ptxt, fonts["sm"], theme["text"] + (200,),
        )

        # ── 4. progress bar (bottom edge) ──────────────────
        bar_h = max(3, int(4 * scale))
        bar_y = h - int(8 * scale) - bar_h
        draw.rectangle(
            [margin, bar_y, w - margin, bar_y + bar_h],
            fill=(40, 40, 40, 100),
        )
        fill_w = int((w - 2 * margin) * progress / 100)
        draw.rectangle(
            [margin, bar_y, margin + fill_w, bar_y + bar_h],
            fill=theme["primary"] + (200,),
        )

        # ── composite HUD onto base ────────────────────────
        result = Image.alpha_composite(base, hud)

        # ── 5. scan lines ──────────────────────────────────
        if sl_opacity > 0:
            sl = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            sl_d = ImageDraw.Draw(sl)
            spacing = max(2, int(3 * scale))
            a = int(sl_opacity * 255)
            for y_pos in range(0, h, spacing):
                sl_d.line([(0, y_pos), (w, y_pos)], fill=(0, 0, 0, a))
            result = Image.alpha_composite(result, sl)

        # ── 6. vignette (radial) ───────────────────────────
        if vig_str > 0:
            yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
            dist = np.sqrt(
                ((xx - w / 2) / (w / 2)) ** 2
                + ((yy - h / 2) / (h / 2)) ** 2
            )
            dist = np.clip(dist, 0, 1.5)
            mask = np.clip(dist ** 2.0 * vig_str, 0, 1)
            vig_arr = np.zeros((h, w, 4), dtype=np.uint8)
            vig_arr[:, :, 3] = (mask * 255).astype(np.uint8)
            vig_layer = Image.fromarray(vig_arr, "RGBA")
            result = Image.alpha_composite(result, vig_layer)

        # ── 7. noise grain ─────────────────────────────────
        if noise_str > 0:
            r_arr = np.array(result).astype(np.float32)
            noise = np.random.normal(0, noise_str * 255, (h, w, 1))
            noise = np.repeat(noise, 4, axis=2)
            noise[:, :, 3] = 0
            r_arr = np.clip(r_arr + noise, 0, 255)
            result = Image.fromarray(r_arr.astype(np.uint8), "RGBA")

        return result.convert("RGB")


# ═══════════════════════════════════════════════════════════════
# ComfyUI registration
# ═══════════════════════════════════════════════════════════════

NODE_CLASS_MAPPINGS = {
    "ScanPosterOverlay": ScanPosterOverlay,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ScanPosterOverlay": "Scan Poster Overlay 📡",
}
