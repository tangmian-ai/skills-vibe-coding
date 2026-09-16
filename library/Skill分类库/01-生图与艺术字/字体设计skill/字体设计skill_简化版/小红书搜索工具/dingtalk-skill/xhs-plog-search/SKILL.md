---
name: xhs-plog-search
description: 小红书文字PLOG选题前期检索。用于「PLOG选题总监」智能体在制定本期主题前，调用 Tavily 联网搜索小红书及外部网页上和文字PLOG模板（颜色拼贴、上下文字、变形文字、手写体、Color Weekly、摄影花鸟字、美食探店、涂鸦手账等玩法）相关的标题/链接/摘要，返回结构化 Markdown 表格作为调研输入。当用户说"做小红书调研"、"查一下小红书最近流行什么"、"本期选题"、"plog 选题"、"文字plog 检索"时使用。
license: Proprietary
compatibility: 需要 curl 与 python3，运行环境必须可访问 https://api.tavily.com
metadata:
  author: skills-vibe-coding
  version: "1.0"
  upstream: tavily-search
---

# 小红书文字PLOG 检索 Skill

本 Skill 给「PLOG选题总监」智能体提供本周小红书及外部网页的文字PLOG玩法检索能力。返回的结果只作为「选题来源」，玩法分类与模板化判断仍依据知识库《小红书文字PLOG模板调研知识库》。

## 何时使用本 Skill

- 用户要求生成本期/本周大主题或小主题
- 用户说"做一组小红书调研"、"先去查一下"、"看看最近流行什么"
- 用户给定大主题方向，要求基于小红书趋势展开

## 工作流（必读）

每次接到选题任务，按下面顺序执行，不要跳步：

1. 先连通性测试：
   ```bash
   bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --ping
   ```
   - 输出 `✓ tavily ok` 才能继续。
   - 失败时根据提示让用户更新 API Key（命令见下文）。

2. 列出可检索的大主题：
   ```bash
   bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --list
   ```

3. 根据用户意图选择方式：
   - 跑全部大主题：`bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh`
   - 跑指定大主题（模糊匹配）：`bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh -t 颜色`
   - 跑多个大主题（逗号分隔）：`bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh -t "颜色,上下文字"`
   - 自定义检索词：`bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh -q "五一plog 文字封面"`

4. 把检索结果（Markdown 表格）作为「本期小红书检索输入」直接喂给后续生成步骤，结合知识库展开 6-8 个小主题。

5. 严禁基于知识库直接编造点赞/收藏数据。结果中没有的字段，统一标注「未获取」。

## 常用命令速查

| 场景 | 命令 |
|---|---|
| 连通性检查 | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --ping` |
| 列出大主题 | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --list` |
| 跑指定大主题 | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh -t 颜色` |
| 跑全部 | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh` |
| 自定义检索词 | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh -q "五一plog"` |
| 改条数 | `bash ... -t 颜色 -n 8` |
| 进阶检索 | `bash ... -t 颜色 --depth advanced` |
| 更换 API Key | `bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --set-key tvly-xxx` |

## 输出格式

脚本 stdout 输出标准 Markdown，包含：

- 顶部：检索时间、本次大主题
- 每个大主题下：每条检索词一张结果表格，列为「# / 标题 / 来源域名 / 链接 / 摘要」
- 末尾：附给智能体的指令模板，提示如何继续生成小主题

## 输出消费规则（智能体必须遵守）

- 检索结果优先级高于知识库判断。
- 结果中没有真实热度的，统一标注「未获取」，禁止编造「爆火/高赞/千赞」。
- 把每条标题、来源、摘要作为本期小主题的依据。
- 同一大主题下展开 6-8 个小主题，玩法保持统一，仅场景不同。
- 输出字段必须按知识库《小红书文字PLOG模板调研知识库》第九章规定。

## 配置说明

- API Key 优先从脚本同目录下的 `.tavily_key` 读取；缺失时回退到内置默认 Key。
- 关键词清单在 `assets/keywords.json`，用户/管理员可直接编辑增删大主题与检索词，无需改脚本。

## 参考

- 知识库：《小红书文字PLOG模板调研知识库》
- 检索引擎：Tavily Search API
