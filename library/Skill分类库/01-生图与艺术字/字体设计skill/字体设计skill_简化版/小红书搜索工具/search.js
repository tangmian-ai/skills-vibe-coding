#!/usr/bin/env node
import { writeFileSync, mkdirSync, existsSync, readFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));

const API_KEY = process.env.TAVILY_API_KEY;
if (!API_KEY) {
  console.error("[错误] 未读取到 TAVILY_API_KEY。请检查 .env 文件，并使用 `npm run search` 运行。");
  process.exit(1);
}

const TAVILY_URL = "https://api.tavily.com/search";

function loadConfig() {
  const file = resolve(__dirname, "关键词清单.json");
  return JSON.parse(readFileSync(file, "utf8"));
}

async function tavilySearch(query, { max_results, search_depth }) {
  const body = {
    api_key: API_KEY,
    query,
    search_depth,
    max_results,
    include_answer: false,
    include_images: false,
    include_raw_content: false,
    topic: "general"
  };
  const res = await fetch(TAVILY_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Tavily ${res.status}: ${text.slice(0, 300)}`);
  }
  return res.json();
}

function safeCell(s, n = 80) {
  return String(s ?? "")
    .replace(/\r?\n/g, " ")
    .replace(/\|/g, "丨")
    .slice(0, n)
    .trim();
}

function hostOf(url) {
  try { return new URL(url).hostname.replace(/^www\./, ""); }
  catch { return ""; }
}

function pickTopics(cliArgs) {
  if (cliArgs.length === 0) return null;
  return cliArgs.map(name => name.trim()).filter(Boolean);
}

function tsName() {
  const d = new Date();
  const pad = n => String(n).padStart(2, "0");
  return `${d.getFullYear()}${pad(d.getMonth()+1)}${pad(d.getDate())}_${pad(d.getHours())}${pad(d.getMinutes())}`;
}

async function main() {
  const cfg = loadConfig();
  const cliArgs = process.argv.slice(2);
  const filter = pickTopics(cliArgs);

  const topics = filter
    ? cfg.大主题.filter(t => filter.some(f => t.name.includes(f) || f.includes(t.name)))
    : cfg.大主题;

  if (topics.length === 0) {
    console.error(`[错误] 没有匹配到任何大主题。已知大主题：\n  - ${cfg.大主题.map(t => t.name).join("\n  - ")}`);
    process.exit(1);
  }

  const max_results = cfg.max_results_per_query ?? 6;
  const search_depth = cfg.search_depth ?? "basic";

  let md = "";
  md += `# 小红书文字PLOG 检索结果\n\n`;
  md += `生成时间：${new Date().toLocaleString("zh-CN", { hour12: false })}\n`;
  md += `检索引擎：Tavily Search\n`;
  md += `本次大主题：${topics.map(t => t.name).join("、")}\n\n`;
  md += `> 直接把本文件粘贴到钉钉「PLOG选题」智能体，作为本周小红书检索输入。智能体应基于此结果，结合知识库展开 6-8 个小主题。\n\n---\n`;

  for (const t of topics) {
    md += `\n## 大主题：${t.name}\n`;
    for (const q of t.queries) {
      md += `\n### 检索词：${q}\n\n`;
      md += `| # | 标题 | 来源 | 链接 | 摘要 |\n|---|---|---|---|---|\n`;
      try {
        const data = await tavilySearch(q, { max_results, search_depth });
        const list = Array.isArray(data.results) ? data.results : [];
        if (list.length === 0) {
          md += `| - | (无结果) | - | - | - |\n`;
        }
        list.forEach((r, i) => {
          md += `| ${i + 1} | ${safeCell(r.title, 60)} | ${safeCell(hostOf(r.url), 30)} | ${r.url} | ${safeCell(r.content, 100)} |\n`;
        });
        process.stderr.write(`[ok] ${t.name} / ${q} → ${list.length}\n`);
      } catch (e) {
        md += `| - | 检索失败 | - | - | ${safeCell(e.message, 100)} |\n`;
        process.stderr.write(`[err] ${t.name} / ${q}: ${e.message}\n`);
      }
    }
  }

  md += `\n---\n\n## 给智能体的指令模板\n\n复制下面这段连同上面的检索结果，一起发给钉钉「PLOG选题」智能体：\n\n\`\`\`text\n本期大主题：${topics.map(t => t.name).join("、")}\n以下是本周小红书检索结果，请你：\n1. 基于检索结果判断本期值得做的小主题方向。\n2. 在该大主题下展开 6-8 个小主题（不同场景变体）。\n3. 严格按知识库《小红书文字PLOG模板调研知识库》的字段输出。\n4. 没有真实点赞/收藏数据时，不要编造，标注「未获取」。\n\n（粘贴上方表格）\n\`\`\`\n`;

  const outDir = resolve(__dirname, "outputs");
  if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });
  const outFile = resolve(outDir, `搜索结果_${tsName()}.md`);
  writeFileSync(outFile, md, "utf8");

  console.log(md);
  console.error(`\n[done] 已保存：${outFile}`);
}

main().catch(e => {
  console.error("[fatal]", e);
  process.exit(1);
});
