# 灵感图库清单与访问策略

阶段二灵感采集前查阅。所有访问通过 `web-access` skill 的 CDP 能力（直连用户本地浏览器，携带登录态）。先跑 `check-deps.mjs`，操作前向用户展示账号封禁风险须知。

## 图库速查表

| 图库 | 域名 | 擅长 | 语言 | 登录态 | 反爬强度 |
|------|------|------|------|--------|----------|
| Pinterest | pinterest.com | 综合/海报/插画/品牌 | 英文 | 常需 | 中高 |
| 花瓣网 | huaban.com | 综合/国内设计/插画 | 中文 | 部分需 | 中 |
| Behance | behance.net | 专业作品集/品牌/包装/Logo | 英文 | 部分需 | 中 |
| Dribbble | dribbble.com | UI/网页/App/视觉 | 英文 | 部分需 | 中 |
| 站酷 | zcool.com.cn | 国内综合/海报/品牌/插画 | 中文 | 部分需 | 低中 |
| Unsplash | unsplash.com | 免费高质量摄影素材 | 英文 | 否 | 低 |
| Pexels | pexels.com | 免费摄影/视频素材 | 英文 | 否 | 低 |

## 各图库访问策略

### Pinterest（pinterest.com）— 综合首选

最强综合灵感库，瀑布流聚合全球设计。

- **搜索 URL**：`https://www.pinterest.com/search/pins/?q={关键词}`，关键词用 `+` 连接，需 URL 编码中文
- **登录**：搜索结果部分可见，深入浏览/保存需登录。用户日常浏览器通常已登录；遇登录墙按 web-access 流程提示用户登录
- **图片提取**：瀑布流，先 `/scroll` 多次触发懒加载；用 `/eval` 提取 `img` 的 `src`（注意取原图 `orig` 而非缩略图，Pinterest 图片节点常带 `data-pin-media` 属性指向大图）
- **检索 JS 示例**：`Array.from(document.querySelectorAll('img[srcset]')).map(i=>i.src).filter(s=>s.includes('i.pinimg'))`
- **注意**：Pinterest 对自动化检测较严，控制访问频率，不要短时密集翻页；如触发验证，降级用 WebSearch 搜 `pinterest {关键词}` 找到图板

### 花瓣网（huaban.com）— 国内设计首选

国内设计师主力采集库，中文搜索、本土设计氛围足。

- **搜索 URL**：`https://huaban.com/search/{关键词}`（中文关键词直接拼入，需 URL 编码）
- **登录**：搜索可浏览，采集/关注需登录
- **图片提取**：瀑布流，先 `/scroll`；花瓣图片 CDN 域名为 `hbimg.huabanimg.com`，用 `/eval` 提取
- **检索 JS 示例**：`Array.from(document.querySelectorAll('img')).map(i=>i.src).filter(s=>s.includes('hbimg'))`
- **注意**：花瓣近年部分内容需登录可见，若大量图片显示占位，提示用户登录

### Behance（behance.net）— 专业作品集

Adobe 旗下专业设计师作品集平台，适合看完整项目（品牌系统、包装系列、海报组）。

- **搜索 URL**：`https://www.behance.net/search?search={关键词}`
- **登录**：可浏览，登录后可关注/保存
- **特点**：内容是"项目"而非单图，一个项目页含多张图。适合进入项目页 `/screenshot` 截取，或 `/eval` 提取项目内图片
- **图片提取**：项目页图片在 `.project-image img` 或 `img[data-src]`，提取 `src`/`data-src`
- **适合**：Logo 品牌系统、包装系列、海报组、UI 案例

### Dribbble（dribbble.com）— UI/视觉

UI/网页/App 视觉设计的标杆社区，单图为主、质量高。

- **搜索 URL**：`https://dribbble.com/search/{关键词}`
- **登录**：可浏览
- **图片提取**：作品图在 `figure picture img` 或 `img[srcset]`，CDN 域 `cdn.dribbble.com`
- **检索 JS 示例**：`Array.from(document.querySelectorAll('img')).map(i=>i.src).filter(s=>s.includes('cdn.dribbble'))`
- **适合**：UI 设计、App 视觉、网页 banner、图标、动效截图

### 站酷（zcool.com.cn）— 国内综合

国内老牌设计师社区，本土商业设计氛围足，海报/品牌/插画齐全。

- **搜索 URL**：`https://www.zcool.com.cn/search/content?word={关键词}`
- **登录**：可浏览
- **特点**：含文章/作品/招聘多类型，搜索结果需筛选"作品"
- **适合**：国内商业海报、国潮风、中文排版参考

### Unsplash / Pexels — 免费素材库

非设计参考，而是**素材来源**（背景图、产品场景图、人物照）。当用户需要摄影素材拼入设计时取用。

- Unsplash：`https://unsplash.com/s/photos/{关键词}`，图片 `images.unsplash.com`，提供免费商用高清图
- Pexels：`https://www.pexels.com/search/{关键词}/`
- **用法**：提取原图 URL 直接下载，作为设计素材层使用

## 采集执行要点

1. **先滚后取**：瀑布流站点（Pinterest/花瓣/Dribbble）先 `/scroll` 3-5 次触发懒加载，否则只能拿到首屏少量图
2. **取大图弃缩略**：提取时过滤 CDN 域名，优先取 `orig`/`originals`/大尺寸版本，避免拿到 236px 缩略图
3. **公开图下载、登录图截图**：拿到 URL 后，公开图直接 `curl` 下载到临时目录用 Read 展示；需登录态才能访问的，在浏览器 tab 内 `/screenshot`
4. **控制频率**：单站短时不要密集翻 10+ 页，3-5 页通常够选 4-8 张好图；触发风控就降级
5. **关 tab**：采集完用 `/close` 关闭自建 tab，保留用户原 tab

## 降级方案

当浏览器/CDP 不可用且无法解决时：
1. 用 `WebSearch` 搜 `{关键词} design inspiration`、`{关键词} poster design`，从结果摘要中提炼风格描述与设计趋势
2. 结合 [`style-library.md`](style-library.md) 的风格特征，向用户用文字描述 2-3 个视觉方向
3. 明确告知"未能获取实时参考图，以下为基于经验的风格描述"，跳过图片直接进入方向确认
