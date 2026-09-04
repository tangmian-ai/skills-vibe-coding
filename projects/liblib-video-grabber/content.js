// 在 liblib 页面里扫描 DOM，把 <video>/<source>/og:video 里的地址也补充上报，
// 作为 webRequest 抓取的兜底（有些地址可能在打开弹窗时才以非媒体后缀加载）。

function collect() {
  const urls = new Set();

  document.querySelectorAll("video").forEach((v) => {
    if (v.currentSrc) urls.add(v.currentSrc);
    if (v.src) urls.add(v.src);
  });
  document.querySelectorAll("source").forEach((s) => {
    if (s.src) urls.add(s.src);
  });
  document
    .querySelectorAll(
      'meta[property="og:video"], meta[property="og:video:url"], meta[property="og:video:secure_url"], meta[name="twitter:player:stream"]'
    )
    .forEach((m) => {
      if (m.content) urls.add(m.content);
    });

  urls.forEach((u) => {
    try {
      const abs = new URL(u, location.href).href;
      if (abs.startsWith("blob:") || abs.startsWith("data:")) return;
      chrome.runtime.sendMessage({ type: "add", url: abs });
    } catch (e) {
      /* ignore */
    }
  });
}

// ---- 页面内浮动大按钮（傻瓜一键下载） ----
let fab = null;
let isTopFrame = window.top === window.self;

function ensureFab() {
  if (!isTopFrame || fab) return;
  fab = document.createElement("button");
  fab.id = "liblib-grabber-fab";
  fab.style.cssText = [
    "position:fixed",
    "right:20px",
    "bottom:20px",
    "z-index:2147483647",
    "display:none",
    "align-items:center",
    "gap:8px",
    "padding:12px 18px",
    "border:none",
    "border-radius:999px",
    "background:linear-gradient(135deg,#2f6fed,#4480ff)",
    "color:#fff",
    "font-size:15px",
    "font-weight:700",
    "font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif",
    "box-shadow:0 6px 20px rgba(47,111,237,.45)",
    "cursor:pointer"
  ].join(";");
  fab.addEventListener("mouseenter", () => (fab.style.transform = "scale(1.04)"));
  fab.addEventListener("mouseleave", () => (fab.style.transform = "scale(1)"));
  fab.addEventListener("click", () => {
    chrome.runtime.sendMessage({ type: "downloadAll" }, (n) => {
      flash(`已开始下载 ${n || ""} 个视频 ↓`);
    });
  });
  document.body.appendChild(fab);
}

function flash(text) {
  if (!fab) return;
  const old = fab.dataset.label || "";
  fab.textContent = text;
  setTimeout(() => updateFab(parseInt(fab.dataset.count || "0", 10)), 1800);
}

function updateFab(videoCount) {
  ensureFab();
  if (!fab) return;
  fab.dataset.count = String(videoCount);
  if (videoCount > 0) {
    fab.dataset.label = `⬇ 下载全部视频 (${videoCount})`;
    fab.textContent = fab.dataset.label;
    fab.style.display = "inline-flex";
  } else {
    fab.style.display = "none";
  }
}

chrome.runtime.onMessage.addListener((msg) => {
  if (msg && msg.type === "mediaUpdate") updateFab(msg.videos);
});

// 接收 inject.js（页面真实环境）抓到的 prompt，转发给后台
window.addEventListener("message", (event) => {
  if (event.source !== window) return;
  const data = event.data;
  if (!data || data.source !== "liblib-grabber-prompt") return;
  if (Array.isArray(data.prompts) && data.prompts.length) {
    chrome.runtime.sendMessage({ type: "addPrompt", prompts: data.prompts });
  }
});

function refreshCount() {
  if (!isTopFrame) return;
  chrome.runtime.sendMessage({ type: "ping" }, (res) => {
    if (res && typeof res.videos === "number") updateFab(res.videos);
  });
}

collect();
ensureFab();
refreshCount();

const observer = new MutationObserver(() => collect());
observer.observe(document.documentElement, {
  childList: true,
  subtree: true,
  attributes: true,
  attributeFilter: ["src"]
});

setInterval(collect, 2000);
