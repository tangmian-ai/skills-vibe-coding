# AI 作品与文件整理报告

生成日期：2026-06-17  
整理范围：`/Users/edy/Desktop`、`/Users/edy/Documents`、`/Users/edy/Downloads`、`/Users/edy/skills`、部分 `.codex/.cursor` 线索。  
处理方式：只读扫描和归类，没有移动、删除或改动原始项目文件。

## 1. 总结

这台电脑上最能代表你的 AI 方向的资产，不是零散 prompt，而是一套围绕「AI 生产工作流」的系统化作品：

1. **视频反推与生成工作台**：从视频/图片反推、参考素材绑定、Dify 路由、生成记录、结果对比到 Agent 协作规则。
2. **Prompt / Workflow 采集器**：把公开 prompt、视频案例、LibTV 工作流线索抓取后进入本地审核台。
3. **Skills 能力库**：把经验沉淀为可安装、可分发、可复用的 Agent Skill，并有内部集合页。
4. **Vibe Coding 原型**：大量 HTML/JS 本地工具页，把想法快速变成交互原型、流程图、评估器和可分享 demo。
5. **内容生产研究资产**：小红书/Plog、热点反推、视频工作流、素材与生成记录，形成可复盘的数据资产。

如果要对外展示，建议把你的定位写成：

> AI 工作流与 Agent Skill 构建者，擅长用 Vibe Coding 快速把业务经验沉淀成可运行工具、可复用 Skill 和可验证的内容生产流水线。

## 2. 代表作品清单

### A. 视频反推与生成工作台

位置：`/Users/edy/Documents/视频`

这是当前最完整、最能代表你的 AI 作品。它不是单页 demo，而是一个本地视频生产工作台：

- 主页面：`video-pipeline-prototype.html`，标题为“通用视频生成 Workflow 原型”。
- 备用工作台：`video-prompt-workbench.html`，标题为“视频 Prompt 反推工作台”。
- 后端入口：`video-prompt-server.mjs`，负责本地服务和 Dify 调用。
- Agent 规则：`agent-readme.md`、`agent-soul.md`。
- 关键 Skill：`skills/reverse-video-prompt-completeness/SKILL.md`。
- 可交付包：`video-workbench-codex-package/README-CODEX.md`，可发给同事让 Codex 检查环境并启动工作台。

扫描到的规模：

- 约 364 个文件，约 95 MB。
- 37 个生成运行记录。
- 21 个分析作业记录。
- 17 个自动化提交记录。
- 最新生成运行：`run-20260616-151643`。
- 最新分析作业：`job-20260609-154840`。

代表价值：

- 把“视频反推 prompt”升级为“workflow state + Dify route + Agent patch”的系统。
- 明确规定 Agent 不直接覆盖 prompt，而是输出 patch、重跑节点和风险清洗建议。
- 把动作、运镜、字幕、口播、音频、参考素材槽位、Dify 输入都纳入生成前门禁。

适合展示方式：

- 作品集首推。
- 可以截图展示 `video-pipeline-prototype.html`、`content-pipeline-mindmap.html`、`unique-hotspot-evaluator.html`。
- 对外分享前必须移除 `.env`、Dify key、内部 URL 和生成记录里的私有资源链接。

### B. Video Workflow Collector

位置：`/Users/edy/Desktop/Video Workflow Collector`

这是视频 Prompt / 工作流采集台，保留 MeiGen、YouMind 单条 prompt 抓取，同时新增 LibTV、ClipVela、VisioArt 工作流线索抓取。

关键文件：

- `README.md`
- `collector.py`
- `AGENT_WORKFLOW.md`
- `agents/agent-a-evidence.md`
- `agents/agent-b-gaoding-quality.md`
- `schema/video-workflow-record.md`
- `public/index.html`
- `public/guide.html`
- `data/prompts.json`

扫描到的规模：

- 约 3721 个文件，约 744 MB。
- `data/prompts.json` 中有 259 条记录。
- 来源分布：MeiGen 100、LibTV 99、YouMind 60。
- `evidenceStatus` 为 `verified_video` 的记录共 259 条。
- `effectMatchStatus` 为 `partial` 的记录共 259 条。

代表价值：

- 建立了“抓取与证据”和“稿定迁移与质量”的双 Agent 分工。
- 用 `evidenceStatus` 避免把营销页、模板文案、封面图误判成真实视频案例。
- 能作为视频工作流数据库和反推 prompt 审核台使用。

适合展示方式：

- 作为“AI 视频案例采集与证据审核系统”展示。
- 可以搭配 `AGENT_WORKFLOW.md` 说明你的 Agent 工作流设计能力。

### C. Prompt Hub Collector

位置：`/Users/edy/Desktop/Prompt Hub Collector`

这是通用 Prompt 收集器，自动从公开网站抓取 prompt，并提供本地审核台。

关键文件：

- `README.md`
- `collector.py`
- `public/index.html`
- `public/guide.html`
- `data/prompts.json`

扫描到的规模：

- 约 795 个文件，约 128 MB。
- `data/prompts.json` 中有 441 条 prompt。
- 来源分布：MeiGen 335、YouMind 106。
- 抓取运行记录 5 次。

代表价值：

- 把 prompt 收集、去重、评分、风险标记、翻译、审核和同步都放到一个本地工具里。
- 适合展示为“Prompt 数据资产化工具”。

适合展示方式：

- 对外展示时可以保留功能说明，清空 `data/prompts.json`、`data/runs.json`、`data/media/` 后再打包。

### D. Gaoding Skills / Skill 集合页

位置：`/Users/edy/skills`

这是内部 Agent Skill 集合页，使用 React/Vite 构建，数据入口是 `static/skills.json`，对外提供 skill 发现、预览和安装复制。

关键文件：

- `README.md`
- `AGENTS.md`
- `static/skills.json`
- `skills/project-charter-interviewer/SKILL.md`
- `skills/gaoding-vpn-rules/SKILL.md`
- `skills/kimgo-workbench-member-sync/SKILL.md`

扫描到的规模：

- 约 78 个文件，约 3.5 MB。
- `static/skills.json` 记录了 9 个 skill / service 入口。
- Git 最新提交：`c39e12a`，日期 2026-06-09。

当前集合入口：

- `project-process-visualizer`：项目过程可视化。
- `agent-lite-cli`：Agent Lite CLI FAT 测试。
- `ai-tool-share`：HTML 分享服务入口。
- `gaoding-vpn-rules`：公司域名 VPN/代理分流规则。
- `project-charter-interviewer`：立项访谈官。
- `kimgo-workbench-member-sync`：Kimgo 成员本地工作台同步。
- `aetheris-cli-entry`：Aetheris CLI 入口。
- `user-voice-analyst`：用户声音分析助手。
- `support-feedback-export`：用户反馈 CSV 导出。

代表价值：

- 这部分代表你的“AI 能力沉淀”能力：把一次性经验变成可安装、可维护、可分发的 Skill。
- `project-charter-interviewer` 体现业务闭环和 Project Charter 思维。
- `kimgo-workbench-member-sync` 体现本地工作台、快照同步、Dify 配置检查和成员侧隔离。
- `gaoding-vpn-rules` 体现把 IT 排障经验封装为可执行规则生成器。

适合展示方式：

- 作为“Skill 作者 / Agent 能力库维护者”重点展示。
- 可展示集合页截图、`static/skills.json` 数据契约、任一 `SKILL.md` 的结构。

### E. 小红书 / Plog 自动化研究资产

位置：`/Users/edy/Documents/New project/xhs_research`

这是体量最大的研究资产目录，和小红书 Plog、素材抓取、样式分析、自动化生成、PSD 包等相关。

扫描到的规模：

- 约 5487 个文件，约 5.2 GB。
- 包含 `runs/`、`automation2_brief/`、`automation2_psd/`、`codex_ai_previews/`、`plog_poster_tools/`、`github_xhs_skills/` 等目录。

代表价值：

- 体现内容生产研究、素材抓取、风格分析和自动生成实验。
- 能作为“AI 内容设计研究库”使用。

适合展示方式：

- 不建议整体外发，体量大且素材复杂。
- 建议只挑选 `workbench_overview.html`、`plog_weekly_summary.html`、`codex_ai_previews/latest_codex_preview.png` 等非敏感成果做展示。

### F. LibTV Workflow Extractor Extension

位置：`/Users/edy/Desktop/libtv-workflow-extractor-extension`

这是一个浏览器扩展项目，用来辅助提取 LibTV 工作流信息。

关键文件：

- `manifest.json`
- `content-script.js`
- `content-script.css`
- `popup.html`
- `popup.js`
- `options.html`
- `options.js`
- `background.js`

扫描到的规模：

- 9 个文件，约 136 KB。

代表价值：

- 作为采集系统的补充，说明你不只做页面工具，也能写浏览器端采集插件。

### G. AI 视频内容生产分享包

位置：`/Users/edy/Downloads/content-pipeline-share`

这是可分享的内容生产工作流包。

关键文件：

- `content-pipeline.html`：标题为“AI 视频内容生产 · 工作流自动化”，主标题是“把高赞热点变成少人工参与的自动化工作流”。
- `hotspot-evaluation-plan.html`：标题为“视频热点反推评估方案”。
- `content-pipeline/`：包含流程截图，如 `workflow-config.png`、`audit-regenerate.png`、`multi-plan.png`。
- `test/`：包含方案视频样例。

扫描到的规模：

- 12 个文件，约 25 MB。

代表价值：

- 这是最适合直接拿来汇报或分享的“成品包”。
- 可以作为“AI 视频内容生产工作流自动化”的作品展示入口。

## 3. 按文件类型整理

### Skill / Agent

建议归类为“AI 能力沉淀”：

- `/Users/edy/skills`
- `/Users/edy/Documents/视频/skills/reverse-video-prompt-completeness`
- `/Users/edy/Documents/视频/.agents/skills/gaoding-vpn-rules`
- `/Users/edy/Desktop/Video Workflow Collector/agents`
- `/Users/edy/Desktop/Video Workflow Collector/AGENT_WORKFLOW.md`

### Vibe Coding 原型

建议归类为“可演示本地工具”：

- `/Users/edy/Documents/视频/video-pipeline-prototype.html`
- `/Users/edy/Documents/视频/video-prompt-workbench.html`
- `/Users/edy/Documents/视频/hotspot-evaluation-plan.html`
- `/Users/edy/Documents/视频/unique-hotspot-evaluator.html`
- `/Users/edy/Documents/视频/content-pipeline-mindmap.html`
- `/Users/edy/Documents/视频/agent-workbench-plan.html`
- `/Users/edy/Downloads/content-pipeline-share/content-pipeline.html`
- `/Users/edy/Downloads/world-pulse.html`

### Prompt / Workflow 数据

建议归类为“数据资产，不直接外发”：

- `/Users/edy/Desktop/Prompt Hub Collector/data`
- `/Users/edy/Desktop/Video Workflow Collector/data`
- `/Users/edy/Documents/视频/generation-runs`
- `/Users/edy/Documents/视频/analysis-jobs`
- `/Users/edy/Documents/视频/automation-submissions`
- `/Users/edy/Documents/New project/xhs_research/runs`
- `/Users/edy/Documents/New project/xhs_research/automation2_brief`
- `/Users/edy/Documents/New project/xhs_research/automation2_psd`

### 可交付包

建议归类为“可转交同事，但需清敏”：

- `/Users/edy/Documents/视频/video-workbench-codex-package`
- `/Users/edy/Desktop/PromptHubCollector-20260430.zip`
- `/Users/edy/Desktop/PromptHubCollector-20260527.zip`
- `/Users/edy/Desktop/libtv-workflow-extractor-extension.zip`
- `/Users/edy/Downloads/content-pipeline-share.zip`

注意：凡是包含 `.env`、Dify key、公司内网 URL、真实资源 URL、账号登录态、浏览器 profile 的包，都不应直接发到公司外部。

### 素材 / 截图 / 视频

建议归类为“展示素材或实验素材”：

- 桌面截图：`/Users/edy/Desktop/截屏2026-06-04...`、`/Users/edy/Desktop/截屏2026-06-09...`、`/Users/edy/Desktop/截屏2026-06-11...`
- 下载目录的生成图：`/Users/edy/Downloads/ChatGPT Image ...png`
- 下载目录的视频样例：`/Users/edy/Downloads/*.mp4`
- 字体包：`/Users/edy/Downloads/稿定字体包-*`

这些不是核心代码资产，但可以用于补充作品展示、页面设计和视频实验。

## 4. 推荐桌面整理结构

如果后续要实际移动文件，建议先按这个结构新建文件夹，再逐步迁移。当前我没有移动文件。

```text
~/Desktop/AI作品集/
├─ 01-视频反推与生成工作台/
│  ├─ Documents-视频-主项目-快捷方式
│  ├─ 关键页面截图
│  └─ 可展示说明.md
├─ 02-Prompt与Workflow采集器/
│  ├─ Prompt Hub Collector
│  ├─ Video Workflow Collector
│  └─ libtv-workflow-extractor-extension
├─ 03-Skills能力库/
│  ├─ Gaoding Skills
│  ├─ reverse-video-prompt-completeness
│  └─ Project Charter / Kimgo / VPN Rules
├─ 04-Vibe-Coding原型/
│  ├─ hotspot-evaluation-plan.html
│  ├─ unique-hotspot-evaluator.html
│  ├─ content-pipeline-mindmap.html
│  └─ content-pipeline-share
├─ 05-研究数据与素材/
│  ├─ xhs_research-只保留索引或样例
│  ├─ generation-runs-只保留代表样例
│  └─ screenshots-and-videos
└─ 99-不可外发-含密钥或登录态/
   ├─ .env
   ├─ browser-profile
   └─ data/media 原始缓存
```

## 5. 对外展示优先级

第一优先级：

- `/Users/edy/Documents/视频`
- `/Users/edy/Desktop/Video Workflow Collector`
- `/Users/edy/skills`
- `/Users/edy/Downloads/content-pipeline-share`

第二优先级：

- `/Users/edy/Desktop/Prompt Hub Collector`
- `/Users/edy/Desktop/libtv-workflow-extractor-extension`
- `/Users/edy/Documents/New project/xhs_research`

第三优先级：

- 截图、生成视频、字体包、安装包、旧 zip。

## 6. 可直接用于作品集的描述

### 一句话版

我用 Vibe Coding 把 AI 内容生产、视频反推、Prompt 采集和 Agent 协作流程做成本地工作台与可复用 Skill，让经验可以被运行、被审核、被迁移、被交付。

### 项目版

1. **视频反推与生成工作台**：构建了从源视频分析、参考素材绑定、prompt 完整性校验、Dify route 调用到生成结果记录的本地 AI 视频生产流水线。
2. **Video Workflow Collector**：设计并实现视频 prompt / 工作流采集台，用 Agent 分工区分证据抓取、稿定迁移和主控验收，避免模板内容误入真实案例库。
3. **Prompt Hub Collector**：实现本地 prompt 抓取、去重、质量评分、风险标记、翻译、审核和同步工具，把 prompt 从灵感素材变成可管理数据资产。
4. **Gaoding Skills 集合页**：维护内部 Skill 集合，将项目过程、立项访谈、VPN 规则、成员工作台同步等经验封装为可安装的 Agent Skill。
5. **AI 视频内容生产自动化方案**：沉淀热点筛选、独一性风险、同款反推价值、延展性评估和生产优先级，形成可分享 HTML 报告与工作流原型。

## 7. 风险与清理建议

需要保密：

- `.env`
- Dify API key
- 公司内网 URL
- 浏览器 profile / 登录态缓存
- 真实素材原始 URL
- `data/media` 中未清理的采集素材

建议清理或隔离：

- 重复 zip：保留最新版本，旧版本归档。
- 下载目录里的安装包：Chrome、Codex、Cursor、Tiger 等可移入“安装包归档”。
- 字体包：统一移入“设计资源/字体包”。
- `xhs_research`：只保留代表样例到作品集，其余作为研究库，不直接展示。

## 8. 扫描备注

- 本次没有移动、删除、压缩任何原文件。
- `Photos Library.photoslibrary` 因系统权限未读取。
- `Library`、`.codex`、`.cursor` 中大量应用缓存和插件依赖只作为线索参考，不纳入作品主清单。
- 如果要做下一步，可以基于本报告创建一个真正的 `AI作品集` 文件夹，并只放清敏后的代表材料。
