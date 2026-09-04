# LiblibAI 视频一键拔 (Chrome 扩展)

在 [liblib.art](https://www.liblib.art) 的模型 / 作品页面，一键抓取并下载示例**视频 (mp4/webm/mov)** 和**图片**。

原理：后台监听页面加载时发往 liblib CDN（`*.liblib.cloud` 等）的媒体请求，自动收集真实下载地址，点一下就保存到本地，无需手动开 DevTools 找链接。

## 安装（开发者模式加载）

1. 打开 Chrome，地址栏输入 `chrome://extensions/` 回车。
2. 打开右上角的 **开发者模式 (Developer mode)**。
3. 点 **加载已解压的扩展程序 (Load unpacked)**。
4. 选择本文件夹：`~/Projects/liblib-video-grabber`。
5. 扩展出现在列表里，建议点工具栏拼图图标把它 **固定 (Pin)** 到地址栏右侧。

## 使用（最简单：页面右下角大按钮）

1. 打开任意 liblib.art 的模型 / 作品详情页，让视频加载一下。
2. 抓到视频后，页面**右下角会自动冒出一个蓝色大按钮**：`⬇ 下载全部视频 (N)`。
3. **点一下，全部视频就开始下载**，存到下载目录的 `liblib/` 子文件夹。完事。

### 进阶：工具栏弹窗（想挑着下/下图片时用）

1. 点浏览器右上角的扩展图标。
2. 弹窗里列出抓到的视频和图片，可单条 **下载**，或 **下载全部视频**。
   - **复制链接**：把所有地址复制到剪贴板。
   - **刷新** / **清空**：重读列表 / 清掉当前标签页记录。

## 文件结构

| 文件 | 作用 |
| --- | --- |
| `manifest.json` | 扩展配置（MV3、权限、域名） |
| `background.js` | Service Worker，用 webRequest 抓取 CDN 媒体地址 |
| `content.js` | 页面内兜底扫描 `<video>` / `og:video` |
| `popup.html` / `popup.js` | 弹窗界面与一键下载逻辑 |

## 说明 / 排错

- 没抓到？先在页面里把视频**滚动到可见并点开播放**，再点弹窗的「刷新」。视频是懒加载的，没加载就不会有请求。
- 想支持别的站点：在 `manifest.json` 的 `host_permissions` 和 `background.js` 的 `MEDIA_FILTER.urls` 里加上对应域名即可。
- 仅供个人学习/备份使用，请尊重原作者版权与平台规则。
