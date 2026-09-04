# Skills & Vibe Coding

## Skills

- [`video-camera-movement`](skills/video-camera-movement/) — 视频运镜提示词结构化 skill。

## Vibe Coding Projects

### [`video-prompt-workbench`](projects/video-prompt-workbench/)

**构建原因：** AI 视频需求常以一句模糊的 brief 开始，分镜、提示词、模型选择和交付流程容易脱节。

**你能得到：** 一个将需求拆解、提示词组织和工作流选择放到同一界面的前端原型，可作为 AI 视频工具的交互与产品设计参考。

### [`video-camera-movement`](projects/video-camera-movement/)

**构建原因：** 同一个运镜词在不同模型和场景中常被错误理解，缺少一份可验证、可复用的提示词基准。

**你能得到：** 中英双语的运镜分类、室内外测试矩阵、完整 prompt 示例，以及用于生成测试表的 Python 脚本。

### [`comfyui-scan-poster`](projects/comfyui-scan-poster/)

**构建原因：** 为海报加入扫描、识别框和监控 HUD 视觉时，手动排版重复且难以随主体位置变化。

**你能得到：** 一个 ComfyUI 自定义节点，支持检测主体后自动叠加 scan-poster 视觉；内含 YOLO、Impact-Pack 和启发式三种识别回退路径及工作流示例。

### [`liblib-video-grabber`](projects/liblib-video-grabber/)

**构建原因：** 在网页上整理灵感视频时，真实媒体地址往往隐藏在懒加载请求中，逐个打开开发者工具效率很低。

**你能得到：** 一个 Chrome MV3 扩展原型，可收集已加载的视频和图片地址，并提供单条或批量下载入口；仅适用于个人学习与素材备份，并应遵守平台规则与版权要求。

真实配置、账号信息、API Key、Cookie、内部服务地址和运行日志均未包含在此仓库中。
