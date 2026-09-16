# AI 生图提示词工程指南

阶段五设计执行时按设计类型套用。适用于 `ImageGen` 工具及用户自行使用的 Midjourney / Stable Diffusion / 即梦等工具。

## 通用提示词结构

高质量设计生图提示词遵循以下层级，按重要性从高到低排列：

```
[设计类型] + [主体内容/场景] + [风格] + [构图/版式] + [配色] + [光线/氛围] + [细节质感] + [文字处理] + [质量词]
```

**核心原则**：
- 主体和风格必须明确，这是画面的骨架
- 配色给具体色名或色系，不要只说"好看的颜色"
- 文字类设计（海报/banner）需明确说明文字内容与位置，但须知 AI 生图对中文文字渲染仍不稳定——建议生图后用图像编辑工具叠加文字，或生图时用英文占位
- 质量词兜底提升完成度

## 质量词通用库（英文，置末尾）

`high quality, professional design, sharp focus, detailed, clean composition, premium look, 8k, print-ready`

负面提示词（避免常见缺陷）：
`blurry, low quality, distorted, cluttered, messy, watermark, signature, extra text, typos, deformed, ugly, oversaturated`

## 按设计类型的提示词模板

### 海报 / 主视觉
```
[主题] poster design, [主体描述], [风格] style, [构图], [配色] color palette, [氛围], [细节质感],
professional poster layout, high quality poster, print-ready
```
**示例**（咖啡店极简海报）：
```
minimalist coffee shop poster design, a single coffee cup with steam rising on clean background,
minimalist style with lots of negative space, centered composition, warm beige and dark brown
color palette with one terracotta accent, cozy morning atmosphere, subtle paper texture,
professional poster layout, high quality, print-ready
```

### Logo / 品牌标识
```
[品牌名] logo design, [图形概念], [风格] style, [配色], simple scalable icon, vector style,
clean lines, professional branding, on white background
```
**示例**（咖啡品牌字母标）：
```
letter M logo design for coffee brand, formed by coffee bean shape and steam line, minimalist
flat style, dark brown and cream color, simple scalable icon, vector style, clean lines,
professional branding, on white background, high quality
```
> Logo 提示词注意：强调 `simple`、`scalable`、`vector style`、`clean lines`，避免复杂细节；要求 `on white background` 便于抠图；AI 生成的 Logo 多为位图，需提示用户最终矢量化。

### Banner / 头图
```
[主题] banner design for [平台/用途], [主体], [风格] style, [构图留文字空间], [配色],
[氛围], [宽高比说明], professional web banner, high quality
```
**示例**（促销 banner）：
```
summer sale banner design for e-commerce, fresh fruits and sunlight, flat illustration style
with gradient accents, composition with empty space on left for text overlay, vibrant orange
and green color palette, energetic summer atmosphere, wide horizontal banner, professional
web banner, high quality
```
> Banner 提示词注意：明确说明 `empty space for text overlay`（留文字位），方便后期叠加文案。

### 封面
```
[类型] cover design for [载体], [主题/标题意境], [风格] style, [构图], [配色], [氛围],
[质感], professional cover layout, high quality
```
**示例**（年度报告封面）：
```
annual report cover design, abstract geometric growth arrow rising, modern corporate minimalist
style, centered composition with grid layout, deep blue and silver color palette, professional
and forward-looking atmosphere, subtle foil stamping texture, professional cover layout, high quality
```

### 插画
```
[场景描述] illustration, [主体], [风格] style, [构图], [配色], [光线/氛围], [细节质感],
[情绪], high quality illustration
```
**示例**（温暖咖啡馆插画）：
```
cozy coffee shop interior illustration, a barista making coffee by the window with plants,
warm hand-drawn watercolor style, wide angle composition, warm earth tones with soft yellow
light, soft morning sunlight through window, watercolor paper texture, peaceful and warm mood,
high quality illustration
```

### UI / App 视觉
```
[屏幕类型] UI design for [产品], [核心内容/功能], [风格] style, [配色], [布局],
clean interface, [设计系统倾向], high quality UI, dribbble style
```
**示例**（音乐 App 播放页）：
```
music player screen UI design for streaming app, album art with playback controls, modern
glassmorphism style, dark theme with purple gradient accents, centered layout with bottom
control bar, clean interface, apple music inspired, high quality UI, dribbble style
```

### 包装
```
[产品] packaging design, [包装形态], [风格] style, [主视觉], [配色], [质感工艺],
[排版信息位], professional packaging, product photography, high quality
```
**示例**（茶叶礼盒）：
```
premium tea gift box packaging design, square rigid box with sleeve, modern chinese style
guochao, mountain and cloud illustration with gold foil, deep green and gold color palette,
matte finish with embossed texture, layout with brand name on top and product info below,
professional packaging, product photography, high quality
```

### 名片
```
business card design for [行业/人], [风格] style, [配色], [布局: 正反面], [质感],
[工艺], clean typography layout, professional, high quality
```

## 中英文提示词写法

不同工具语言偏好不同，**同时提供中英文两版**：

- **ImageGen / 即梦 / 国产工具**：中文提示词效果通常更好，描述具体
- **Midjourney / SD**：英文提示词为主，关键词逗号分隔，权重靠位置前置
- **通用写法**：英文用逗号分隔的关键词短语；中文用自然描述句

**中文版示例**（咖啡海报）：
```
极简风格咖啡店海报设计，画面中央一只冒热气的咖啡杯，纯净背景，大量留白，居中构图，
暖米色与深棕色配色搭配一点赤陶橙点缀，温馨清晨氛围，细腻纸张质感，专业海报版式，
高质量，印刷级
```

## 关键参数建议（供用户自行生成时）

| 参数 | 说明 | 常用值 |
|------|------|--------|
| 比例 `--ar` | Midjourney 宽高比 | 海报 `--ar 2:3`/`3:4`，banner `--ar 16:9`/`3:1`，方图 `--ar 1:1` |
| 风格化 `--s` | Midjourney 风格强度 | 设计类建议 `--s 250-750` |
| 质量 `--q` | Midjourney 质量 | `--q 2`（最高） |
| 种子 `--seed` | 复现/微调 | 系列图固定 seed 保持一致 |
| 步数 steps | SD 采样步数 | 设计类 30-40 |
| CFG | SD 提示词权重 | 7-9 |

## 文字处理重要提示

AI 生图（含 ImageGen）对**文字渲染仍不可靠**，尤其中文。处理策略：

1. **海报/banner 等含文案设计**：生图时只生成背景/主视觉，留出文字空间（提示词写 `empty space for text`），文字用图像编辑工具（PS/Canva/Figma）后期叠加
2. **必须含文字时**：提示词写英文，且接受可能需多次重生成；中文文字几乎必然出错，强烈建议后期叠加
3. **Logo 文字**：生成图形主体，文字部分矢量化后另排，不依赖 AI 生文字
4. 向用户说明此局限，并提供"生图 + 后期叠字"的完整方案，而非只给一张文字错乱的图

## 迭代修正常用调整词

| 问题 | 调整 |
|------|------|
| 太复杂乱 | 加 `minimal`、`clean`、`simple`、`lots of negative space` |
| 太单调 | 加 `rich details`、`layered composition`、`textured` |
| 风格不明显 | 强化风格词前置，加参考艺术家 `in the style of ...` |
| 配色不对 | 明确具体色名 `navy blue and gold`，加 `color palette: ...` |
| 构图失衡 | 加 `centered`、`rule of thirds`、`symmetrical`、`dynamic diagonal` |
| 质感塑料 | 加 `paper texture`、`film grain`、`matte finish`、`natural lighting` |
| 不够高级 | 加 `premium`、`editorial`、`sophisticated`、`refined` |
