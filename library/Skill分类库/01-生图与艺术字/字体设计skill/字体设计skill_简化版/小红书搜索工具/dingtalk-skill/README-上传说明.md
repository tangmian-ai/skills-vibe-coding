# xhs-plog-search 钉钉 Skill 包 上传说明

这是「PLOG选题总监」智能体的联网检索 Skill，符合 [AgentSkills 规范](https://agentskills.io/specification)。

## 一、Skill 包内容

```
xhs-plog-search/
├── SKILL.md                # 必需：YAML frontmatter + agent 使用说明
├── assets/
│   └── keywords.json       # 大主题关键词清单（可编辑）
└── scripts/
    └── search.sh           # 实际调用 Tavily Search 的 bash 脚本
```

打包好的 zip：`xhs-plog-search.zip`

## 二、上传到钉钉

1. 打开钉钉 → 企业 AGENT 平台 → 你的「PLOG选题」智能体
2. 左侧点 `Skill`
3. 点 `+ 添加 Skill`
4. 上传 `xhs-plog-search.zip`
5. 上传成功后 Skill 会出现在列表里
6. 右上角点 **保存** 和 **发布**

## 三、首次使用

发布后，在右侧测试框输入：

```text
先 ping 一下 xhs-plog-search，确认能联网。
```

智能体应执行：

```bash
bash <CURRENT_SKILL_MD_PATH_DIR>/scripts/search.sh --ping
```

返回 `✓ tavily ok` 即正常。

接着试一次小检索：

```text
用 xhs-plog-search 查"颜色+文字拼贴plog"，再结合知识库给我 6 个小主题。
```

智能体应自动：

1. 调用 `bash .../scripts/search.sh -t 颜色`
2. 拿到 Markdown 检索结果
3. 结合知识库展开 6 个小主题

## 四、可用命令

| 场景 | 智能体可调用的命令 |
|---|---|
| 连通性检查 | `bash .../scripts/search.sh --ping` |
| 列出大主题 | `bash .../scripts/search.sh --list` |
| 跑指定大主题 | `bash .../scripts/search.sh -t 颜色` |
| 多个大主题 | `bash .../scripts/search.sh -t "颜色,上下文字"` |
| 跑全部 | `bash .../scripts/search.sh` |
| 自定义检索词 | `bash .../scripts/search.sh -q "五一plog 文字封面"` |
| 改条数 | `bash .../scripts/search.sh -t 颜色 -n 8` |
| 进阶检索 | `bash .../scripts/search.sh -t 颜色 --depth advanced` |
| 更换 API Key | `bash .../scripts/search.sh --set-key tvly-xxxxx` |

> `<CURRENT_SKILL_MD_PATH_DIR>` 是钉钉运行时自动替换的占位符，无需手动改。

## 五、修改关键词

直接编辑 `xhs-plog-search/assets/keywords.json`：

- 加大主题：往 `topics` 数组里追加一段
- 改检索词：改对应大主题下的 `queries` 数组
- 改单次返回条数：`max_results_per_query`
- 检索深度：`search_depth` 可选 `basic` / `advanced`

改完重新打包 zip 上传，或者通过钉钉的 Skill 编辑页面直接修改（视钉钉 UI 是否支持）。

## 六、API Key 管理

- 默认 Key 已内置在 `scripts/search.sh`：`tvly-dev-3RKJ2y-...`
- 优先从 `scripts/.tavily_key` 读取，可通过 `--set-key` 永久写入
- 切换 Key：让智能体执行 `bash .../scripts/search.sh --set-key tvly-xxxxx`

## 七、人设里要补的一句话

为了让智能体真的会调用这个 Skill，把这段加到「PLOG选题」的人设里：

```text
## 联网检索规则
当用户要求做小红书调研、生成本期主题、查热点时，必须先调用 Skill 「xhs-plog-search」。
- 默认先 --ping 确认连通。
- 优先用 -t 跟随用户给定的大主题方向。
- 把 Skill 返回的 Markdown 表格作为本期检索输入。
- 知识库只用于判断玩法分类、模板化价值和输出字段，不替代检索。
- Skill 没有返回的数据（点赞/收藏），统一标注「未获取」，禁止编造。
```

## 八、依赖说明

钉钉运行环境必须有：

- `bash`
- `curl`（向 https://api.tavily.com 发请求）
- `python3`（解析 JSON）

绝大多数 Linux 容器都自带。如果上传后报错缺依赖，再做 fallback。

## 九、Tavily 免费额度

- 1000 次/月
- 一次跑 8 大主题 × 3 检索词 ≈ 24 次
- 即使每周跑 5 次完整调研也消耗不到一半额度
- 监控用量：https://app.tavily.com
