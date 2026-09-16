#!/usr/bin/env bash
# xhs-plog-search / scripts/search.sh
# 小红书文字PLOG选题前期检索（Tavily Search）
# 依赖：curl + python3
#
# 用法：
#   bash search.sh --ping                          # 连通性检查
#   bash search.sh --list                          # 列出可用大主题
#   bash search.sh                                 # 跑全部大主题
#   bash search.sh -t 颜色                          # 只跑名称包含"颜色"的大主题
#   bash search.sh -t "颜色,上下文字"                # 多个大主题，用逗号分隔
#   bash search.sh -q "五一plog 文字封面"             # 自定义检索词，不读 keywords.json
#   bash search.sh -t 颜色 -n 8                     # 每个检索词返回 8 条
#   bash search.sh -t 颜色 --depth advanced         # 进阶检索（更慢更细）
#   bash search.sh --set-key tvly-xxx              # 永久保存 Tavily API Key

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd -P)"
KEY_FILE="$SCRIPT_DIR/.tavily_key"
KEYWORDS_FILE="$SKILL_DIR/assets/keywords.json"
TAVILY_URL="https://api.tavily.com/search"

DEFAULT_KEY="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"

# ── 工具函数 ────────────────────────────────────────────────────────────────

die()  { echo "错误：$*" >&2; exit 1; }
info() { echo "$*" >&2; }

require() {
  command -v "$1" >/dev/null 2>&1 || die "缺少依赖：$1"
}

require curl
require python3

load_key() {
  if [[ -f "$KEY_FILE" ]]; then
    cat "$KEY_FILE"
  else
    printf '%s' "$DEFAULT_KEY"
  fi
}

# ── 命令解析 ────────────────────────────────────────────────────────────────

ACTION="run"          # run | ping | list | setkey
TOPIC_FILTER=""
QUERY=""
N=""
DEPTH=""
NEW_KEY=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ping)        ACTION="ping"; shift ;;
    --list)        ACTION="list"; shift ;;
    --set-key)     ACTION="setkey"; NEW_KEY="${2:-}"; shift 2 ;;
    -t|--topic)    TOPIC_FILTER="${2:-}"; shift 2 ;;
    -q|--query)    QUERY="${2:-}"; shift 2 ;;
    -n|--count)    N="${2:-}"; shift 2 ;;
    --depth)       DEPTH="${2:-}"; shift 2 ;;
    -h|--help)
      sed -n '1,30p' "$0" | sed 's/^# //;s/^#//'
      exit 0
      ;;
    *) die "未知参数：$1（用 -h 查看帮助）" ;;
  esac
done

# ── 子命令：保存 Key ────────────────────────────────────────────────────────

if [[ "$ACTION" == "setkey" ]]; then
  [[ -z "$NEW_KEY" ]] && die "缺少 API Key，用法：--set-key tvly-xxxxx"
  printf '%s' "$NEW_KEY" > "$KEY_FILE"
  info "✓ 已保存 Tavily API Key 到 $KEY_FILE"
  exit 0
fi

# ── 子命令：连通性检查 ──────────────────────────────────────────────────────

KEY="$(load_key)"
[[ -z "$KEY" ]] && die "未找到 Tavily API Key，先执行 --set-key"

tavily_call() {
  local q="$1" n="$2" depth="$3"
  python3 - "$KEY" "$q" "$n" "$depth" "$TAVILY_URL" <<'PY'
import sys, json, urllib.request, urllib.error

key, q, n, depth, url = sys.argv[1:]
body = {
    "api_key": key,
    "query": q,
    "search_depth": depth or "basic",
    "max_results": int(n) if n else 6,
    "include_answer": False,
    "include_images": False,
    "include_raw_content": False,
    "topic": "general",
}
data = json.dumps(body).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        sys.stdout.write(r.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    sys.stderr.write(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
    sys.exit(2)
except Exception as e:
    sys.stderr.write(f"ERR: {e}")
    sys.exit(3)
PY
}

if [[ "$ACTION" == "ping" ]]; then
  if out=$(tavily_call "ping" "1" "basic" 2>&1); then
    if echo "$out" | python3 -c "import sys,json;d=json.load(sys.stdin);print('ok' if 'results' in d else 'bad')" 2>/dev/null | grep -q ok; then
      echo "✓ tavily ok"
      exit 0
    fi
    echo "× tavily 异常返回：$out" >&2
    exit 1
  else
    echo "× tavily 调用失败：$out" >&2
    exit 1
  fi
fi

# ── 加载关键词清单 ──────────────────────────────────────────────────────────

load_topics() {
  python3 - "$KEYWORDS_FILE" <<'PY'
import sys, json
path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    cfg = json.load(f)
out = {
    "max_results_per_query": cfg.get("max_results_per_query", 6),
    "search_depth": cfg.get("search_depth", "basic"),
    "topics": cfg.get("topics", []),
}
print(json.dumps(out, ensure_ascii=False))
PY
}

if [[ "$ACTION" == "list" ]]; then
  python3 - "$KEYWORDS_FILE" <<'PY'
import sys, json
with open(sys.argv[1], "r", encoding="utf-8") as f:
    cfg = json.load(f)
for t in cfg.get("topics", []):
    print("- " + t["name"])
PY
  exit 0
fi

# ── 实际检索 ────────────────────────────────────────────────────────────────

CFG=$(load_topics)
DEFAULT_N=$(echo "$CFG" | python3 -c "import sys,json;print(json.load(sys.stdin)['max_results_per_query'])")
DEFAULT_DEPTH=$(echo "$CFG" | python3 -c "import sys,json;print(json.load(sys.stdin)['search_depth'])")
N="${N:-$DEFAULT_N}"
DEPTH="${DEPTH:-$DEFAULT_DEPTH}"

# 自定义查询模式：直接跑一条
if [[ -n "$QUERY" ]]; then
  TASK_JSON=$(python3 -c "
import json
print(json.dumps({'topics':[{'name':'自定义检索','queries':['$QUERY']}]}, ensure_ascii=False))
")
else
  TASK_JSON=$(echo "$CFG" | python3 -c "
import sys, json
cfg = json.load(sys.stdin)
flt = '''$TOPIC_FILTER'''.strip()
topics = cfg['topics']
if flt:
    needles = [s.strip() for s in flt.replace('，', ',').split(',') if s.strip()]
    topics = [t for t in topics if any(n in t['name'] or t['name'] in n for n in needles)]
print(json.dumps({'topics': topics}, ensure_ascii=False))
")
fi

TOPIC_COUNT=$(echo "$TASK_JSON" | python3 -c "import sys,json;print(len(json.load(sys.stdin)['topics']))")
[[ "$TOPIC_COUNT" -eq 0 ]] && die "没有匹配到任何大主题。可执行 --list 查看全部。"

# Markdown 头
NOW=$(date "+%Y-%m-%d %H:%M:%S")
TOPIC_NAMES=$(echo "$TASK_JSON" | python3 -c "import sys,json;print('、'.join(t['name'] for t in json.load(sys.stdin)['topics']))")

echo "# 小红书文字PLOG 检索结果"
echo
echo "生成时间：$NOW"
echo "检索引擎：Tavily Search"
echo "本次大主题：$TOPIC_NAMES"
echo "每条检索词返回：$N 条；检索深度：$DEPTH"
echo
echo "> 本结果作为本期小红书检索输入。请基于此结合知识库展开 6-8 个小主题。"
echo

# 遍历 topic / query
QUERIES_LIST=$(echo "$TASK_JSON" | python3 -c "
import sys, json
cfg = json.load(sys.stdin)
for t in cfg['topics']:
    for q in t['queries']:
        print(f\"{t['name']}\t{q}\")
")

while IFS=$'\t' read -r tname q; do
  [[ -z "$tname" ]] && continue
  if [[ "$tname" != "$LAST_TOPIC" ]]; then
    echo
    echo "## 大主题：$tname"
    LAST_TOPIC="$tname"
  fi
  echo
  echo "### 检索词：$q"
  echo
  echo "| # | 标题 | 来源 | 链接 | 摘要 |"
  echo "|---|---|---|---|---|"

  if resp=$(tavily_call "$q" "$N" "$DEPTH" 2>/tmp/tavily_err); then
    echo "$resp" | python3 - <<'PY'
import sys, json
from urllib.parse import urlparse

def cell(s, n):
    if s is None: return ""
    s = str(s).replace("\n", " ").replace("|", "丨").strip()
    return s[:n]

raw = sys.stdin.read()
try:
    d = json.loads(raw)
except Exception as e:
    print(f"| - | 解析失败 | - | - | {e} |")
    sys.exit(0)

results = d.get("results", []) or []
if not results:
    print("| - | (无结果) | - | - | - |")
else:
    for i, r in enumerate(results, 1):
        title = cell(r.get("title"), 60)
        url = r.get("url", "")
        try:
            host = urlparse(url).hostname or ""
            if host.startswith("www."): host = host[4:]
        except Exception:
            host = ""
        summary = cell(r.get("content"), 100)
        print(f"| {i} | {title} | {cell(host,30)} | {url} | {summary} |")
PY
  else
    err=$(cat /tmp/tavily_err 2>/dev/null || echo "未知错误")
    echo "| - | 检索失败 | - | - | ${err//|/丨} |"
  fi
done <<< "$QUERIES_LIST"

# 末尾给智能体的指令模板
cat <<EOF

---

## 给智能体的指令模板

请基于上面的检索结果，结合知识库《小红书文字PLOG模板调研知识库》：

1. 判断本期值得做的小主题方向。
2. 在大主题「$TOPIC_NAMES」下展开 6-8 个小主题（不同场景变体）。
3. 严格按知识库第九章字段输出。
4. 没有真实点赞/收藏数据时，不要编造，标注「未获取」。
EOF
