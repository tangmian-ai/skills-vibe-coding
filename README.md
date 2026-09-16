# Skills & Vibe Coding

## Skills

每个目录均以 `SKILL.md` 为入口；需要时读取其 `references/`、`templates/`、`assets/` 或 `examples/`。

### Static & Commercial Visuals

- [`image-generation-production`](skills/image-generation-production/) — 品牌、电商与内容视觉的生图规格、参考图控制和交付 QA。
- [`typography-art-text`](skills/typography-art-text/) — 艺术字、立体字与文字生图的风格路由和 Prompt 结构。
- [`brand-ecommerce-creative`](skills/brand-ecommerce-creative/) — 品牌 Kit 到社媒、电商、直播、印刷与 KV 的商业视觉适配。
- [`app-resource-adaptation`](skills/app-resource-adaptation/) — 已批准活动方案的 App 横幅、入口卡片、弹窗和信息流资源位适配。
- [`creative-qc-compliance`](skills/creative-qc-compliance/) — 视觉质量、参考图一致性、文案、权利与投放风险质检。
- [`design-assistant`](skills/design-assistant/) — 从需求拆解、灵感对齐到视觉执行的设计助理工作流。

### Project Discovery & Operations

- [`project-charter-interviewer`](skills/project-charter-interviewer/) — 通过结构化访谈澄清目标、范围、风险、依赖和衡量指标，输出可评审的 Project Charter。

### Video & Content Systems

- [`video-camera-movement`](skills/video-camera-movement/) — 视频运镜提示词结构化 Skill。
- [`reverse-video-prompt-completeness`](skills/reverse-video-prompt-completeness/) — 视频反推 Prompt 的动作、运镜、声音、参考素材和线路完整性检查。
- [`cinematic-director`](skills/cinematic-director/) — 剧本、分镜、关键帧、连续性与 AI 视频导演工作流。
- [`content-pipeline`](skills/content-pipeline/) — 从选题评估到内容生产、审核和归档的 AI 内容流程。

## Skill Library

[`library/Skill分类库/`](library/Skill分类库/) 是支撑这些 Skill 的资料层，收录可复用的模板、案例、媒体、工作流和整理报告，不把它当作可直接安装的 Skill。

- `01-生图与艺术字`：生图方法、艺术字/字体设计、参考图控制与 ComfyUI 海报工作流。
- `02-视频与动态视觉`：视频反推、镜头语言和视频 Prompt 工作台资料。
- `03-内容生产与自动化工作流`：内容生产 SOP、热点评估和 Dify 工作流。
- `04-品牌电商与投放视觉`：品牌、电商、社媒、直播、印刷和 KV 延展技能。
- `05-通用Skill与Agent规范`：路由、合规、设计助手与 Skill 模板。

资料库中的文件均为可编辑的原始或整理副本。涉及人像、品牌、平台截图和商业素材时，使用前需完成相应的授权与合规复核。

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
