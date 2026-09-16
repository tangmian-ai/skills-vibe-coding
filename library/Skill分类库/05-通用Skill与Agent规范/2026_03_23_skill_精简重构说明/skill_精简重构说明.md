---
name: Skill 精简重构
overview: 将 17 个嵌套文件重构为 1 个 Skill + 15 个扁平 Reference，按需读取最小化 token。每个 reference 控制在 8-40 行。
todos:
  - id: delete-old-files
    content: 删除所有旧文件（17 个），清空 references/ 子目录
    status: completed
  - id: rewrite-skill
    content: 重写 skill.md（~43 行）：Prompt 模板 + 两阶段交互 + A/B/C 触发条件 + Reference 路由索引
    status: completed
  - id: create-prompt-formula
    content: 新建 references/prompt-公式.md（~40 行）：8 个字段的专有填充规则
    status: completed
  - id: create-visual-standard
    content: 新建 references/视觉标准.md（~20 行）：小红书品质核心要点
    status: completed
  - id: create-mode-refs
    content: 新建 3 个模式文件（模式A-复刻/模式B-定制/模式C-虚拟IP.md，各 ~10-12 行）
    status: completed
  - id: create-banned-words
    content: 新建 references/违禁词.md（~35 行）：13 条违禁规则关键词列表
    status: completed
  - id: create-portrait-files
    content: 新建 5 个人像文件（人像-职场/校园/自媒体/通用生活/虚拟角色.md，各 ~8-25 行）
    status: completed
  - id: create-copy-files
    content: 新建 4 个文案文件（文案-职场/校园/自媒体/通用生活.md，各 ~8 行）
    status: completed
isProject: false
---

# 小红书 Skill 精简重构计划

## 现状问题

原结构 17 个文件（含 2 层嵌套 + 2 个 sub-skill + 2 个备份），主要问题：

- `爆款生成公式.md` 与 `skill.md` 的 A/B/C 逻辑完全重复
- `设计原则与标准.md` 中 70% 是 LLM 已知的通用设计学
- 2 个 sub-skill（行业人像特征/文案专家指南）仅做路由，价值低
- 每次执行需递归读取多层嵌套文件，token 浪费严重

---

## 目标结构（1 skill + 15 references，全部扁平）

```
skill.md                             ← ~43 行（必读，含 Prompt 模板）
references/
├── prompt-公式.md                   ← ~40 行（必读）
├── 视觉标准.md                      ← ~20 行（必读）
├── 模式A-复刻.md                    ← ~12 行（按需，2图+文案时读）
├── 模式B-定制.md                    ← ~10 行（按需，1图+文案时读）
├── 模式C-虚拟IP.md                  ← ~10 行（按需，0图+文案时读）
├── 违禁词.md                        ← ~35 行（文案阶段按需）
├── 人像-职场.md                     ← ~8 行（按需）
├── 人像-校园.md                     ← ~8 行（按需）
├── 人像-自媒体.md                   ← ~12 行（按需）
├── 人像-通用生活.md                  ← ~25 行（按需，10 子类各 1 行）
├── 人像-虚拟角色.md                  ← ~20 行（按需，叠加任意赛道）
├── 文案-职场.md                     ← ~8 行（按需，含字数规则）
├── 文案-校园.md                     ← ~8 行（按需）
├── 文案-自媒体.md                   ← ~8 行（按需）
└── 文案-通用生活.md                  ← ~8 行（按需）
```

---

## 按需读取策略与 token 估算

每次请求 Agent 按以下逻辑读取，最小化 token：

- **必读（每次）**：skill.md(43) + prompt-公式.md(40) + 视觉标准.md(20) = **~103 行**
- **模式判断**：根据输入图片数量读 1 个模式文件 = **~10 行**
- **文案阶段**：1 个文案赛道文件(~~8) + 违禁词.md(~~35) = **~43 行**
- **人像阶段**：1 个人像赛道文件(~8-25)，虚拟角色模式额外 +20
- **典型请求总读取：~164 行**（原结构需读取 ~400+ 行，节省约 60%）

---

## 各文件内容说明

- **skill.md**（~43 行）：Prompt 模板结构（Seedream 格式）、两阶段交互流程、A/B/C 触发条件（仅 3 行判断，不含执行细节）、Reference 路由索引
- **references/prompt-公式.md**（~40 行）：8 个 Prompt 字段的专有填充规则 -- 人物描边+肤质词组、四大爆款构图+填充示例、精准高亮策略、配色 60/30/10、装饰元素限制
- **references/视觉标准.md**（~20 行）：小红书封面品质 6 标准核心要点（仅非通用条目），3:4 比例
- **references/模式A-复刻.md**（~12 行）：强制替换项（人物/文案/氛围）+ 风格复刻项（排版/字体/图层/配色照搬参考图）
- **references/模式B-定制.md**（~10 行）：人物保持原图 + 氛围/视觉按规则生成
- **references/模式C-虚拟IP.md**（~10 行）：虚拟/真人分支判断 + 默认虚拟卡通 + 氛围/视觉按规则生成
- **references/违禁词.md**（~35 行）：13 类平台违禁规则，压缩为关键词列表
- **references/人像-*.md**（5 个，各 ~8-25 行）：各赛道人像场景/情绪/动作特征关键词
- **references/文案-*.md**（4 个，各 ~8 行）：各赛道核心人设 + 爆款公式 + 主副标题策略 + 封面字数规则

---

## 删除/精简清单

**删除全部 17 个旧文件**，重建 16 个新文件（1 skill + 15 references）。具体精简：

- 删除 2 个备份文件
- 删除 2 个 sub-skill（路由逻辑内联到 skill.md）
- `设计原则与标准.md`（173 行 → 20 行）：删除版式四大原则详解、字间距/行距数值、字体选用散文式解释
- `爆款生成公式.md`（115 行 → 40 行）：删除与 skill.md 重复的 A/B/C 模式判断逻辑
- `skill.md`（145 行 → 43 行）：删除第 4 节"三步构建流程"、A/B/C 执行细节拆为 3 个 reference、冗长注释和 Agent 说明文字
- `通用生活赛道人像`（58 行 → 25 行）：10 个子类从每类 4-5 条压缩为各 1 行
- 封面字数规则从 skill.md 移入各文案赛道文件

**保留的专有知识**（LLM 不具备）：

- Seedream Prompt 模板格式 + 3:4 比例
- 人物描边规则 + 性别肤质 Prompt 关键词
- 四大爆款构图 + 填充示例
- 精准高亮策略（像素级描述、严禁抽象指令）
- 配色 60/30/10 + 装饰限 3 个 + 网感 Emoji
- A/B/C 三种模式的强制替换/风格复刻/规则生成逻辑
- 违禁词 13 类（小红书平台专有）
- 各赛道文案爆款公式 + 封面字数规则
- 虚拟角色 4 种风格 Prompt 关键词

---

## Skill 撰写注意事项（总结）

基于本次精简重构经验，后续 Skill 撰写应遵循以下原则：

### 1. 结构层面
- **扁平化**：避免 sub-skill 嵌套，所有 reference 置于同一级目录，减少递归读取
- **单一职责**：skill.md 只做路由与核心逻辑；reference 只承载数据/规则，不做路由分发
- **按需拆分**：按「使用场景是否相同」拆分 reference。不同场景（如不同赛道、不同模式）应独立成文件，便于按需读取

### 2. Token 优化
- **最小必读集**：skill.md + 每次必用 reference 控制在 100 行以内
- **按需加载**：场景/赛道/模式类内容拆成独立 reference，每次只读命中的 1 个
- **单文件行数**：reference 单文件建议 8–40 行，过长会导致整块读取浪费 token

### 3. 内容取舍
- **只注入专有知识**：LLM 已具备的通用知识（如基础设计原则、排版常识）不必写入，避免 token 浪费
- **平台/领域特规优先**：违禁词、平台规范、特定模型 Prompt 格式、行业公式等应保留
- **删繁就简**：用关键词/列表代替长段散文，用示例代替冗长说明

### 4. 避免重复
- **逻辑唯一归属**：同一逻辑只写一处。若多处引用，用「读取 xx reference」指向，严禁复制粘贴
- **路由集中**：触发条件、模式判断、reference 索引统一写在 skill.md，不在 reference 内重复

### 5. 避免 Reference 嵌套（官方规范）

**Cursor 官方建议**：`Keep references one level deep - link directly from SKILL.md to reference files. Deeply nested references may result in partial reads.`

- **仅一层引用**：skill.md 直接链接 reference 文件；reference 文件**严禁**再引用其他 reference
- **两类信息分离**：
  - **路由逻辑**（该读哪些 reference）→ 仅放在 skill.md
  - **模式/业务规则**（如何填充、分支判断等）→ 放在 reference 中，但不写「读取 xxx」「参考 references/xxx」
- **正确写法**：reference 中用「按 prompt-公式 规则生成」「从对应赛道人像规则获取」等规则描述，由 skill.md 的路由索引决定实际读取哪些文件
- **错误写法**：reference 中出现 `参考 references/prompt-公式.md`、`读取 references/人像-xxx.md` 等

### 6. 命名与组织
- **见名知意**：reference 文件名应能直接反映内容（如 `人像-职场.md`、`模式A-复刻.md`）
- **路由清晰**：skill.md 中明确标注每个 reference 的读取时机和触发条件

