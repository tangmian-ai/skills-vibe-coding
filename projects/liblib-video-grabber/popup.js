let currentTabId = null;
let mediaList = [];
let promptList = [];

const listEl = document.getElementById("list");
const countEl = document.getElementById("count");
const promptsEl = document.getElementById("prompts");

function fileNameFromUrl(url) {
  try {
    const path = new URL(url).pathname;
    const base = path.substring(path.lastIndexOf("/") + 1) || "file";
    return decodeURIComponent(base);
  } catch (e) {
    return "file";
  }
}

function download(url) {
  chrome.downloads.download({
    url,
    filename: "liblib/" + fileNameFromUrl(url),
    saveAs: false
  });
}

function copyText(text, btn) {
  navigator.clipboard.writeText(text);
  if (btn) {
    const old = btn.textContent;
    btn.textContent = "已复制";
    setTimeout(() => (btn.textContent = old), 1200);
  }
}

function renderPrompts() {
  promptsEl.innerHTML = "";
  if (!promptList.length) return;

  const title = sectionTitle(`提示词 / Prompt (${promptList.length})`);
  promptsEl.appendChild(title);

  promptList.forEach((p) => {
    const card = document.createElement("div");
    card.className = "prompt-card";

    const head = document.createElement("div");
    head.className = "phead";
    const label = document.createElement("span");
    label.className = "plabel";
    label.textContent = p.label || "prompt";
    const copyBtn = document.createElement("button");
    copyBtn.textContent = "复制";
    copyBtn.addEventListener("click", () => copyText(p.text, copyBtn));
    head.appendChild(label);
    head.appendChild(copyBtn);

    const text = document.createElement("div");
    text.className = "ptext";
    text.textContent = p.text;

    card.appendChild(head);
    card.appendChild(text);
    promptsEl.appendChild(card);
  });
}

function render() {
  renderPrompts();
  const videos = mediaList.filter((m) => m.type === "video");
  const images = mediaList.filter((m) => m.type === "image");
  countEl.textContent = `${videos.length} 视频 · ${images.length} 图片`;
  document.getElementById("downloadAll").disabled = videos.length === 0;
  document.getElementById("copyAll").disabled = mediaList.length === 0;

  if (mediaList.length === 0) {
    listEl.innerHTML =
      '<div class="empty">还没抓到媒体文件。<br/>请在 liblib 页面里点开 / 播放一下视频，再点「刷新」。</div>';
    return;
  }

  listEl.innerHTML = "";
  if (videos.length) {
    listEl.appendChild(sectionTitle("视频"));
    videos.forEach((m) => listEl.appendChild(itemRow(m)));
  }
  if (images.length) {
    listEl.appendChild(sectionTitle("图片"));
    images.forEach((m) => listEl.appendChild(itemRow(m)));
  }
}

function sectionTitle(text) {
  const d = document.createElement("div");
  d.className = "section-title";
  d.textContent = text;
  return d;
}

function itemRow(m) {
  const row = document.createElement("div");
  row.className = "item";

  const thumb = document.createElement(m.type === "video" ? "video" : "img");
  thumb.className = "thumb";
  thumb.src = m.url;
  if (m.type === "video") {
    thumb.muted = true;
    thumb.preload = "metadata";
  }
  row.appendChild(thumb);

  const meta = document.createElement("div");
  meta.className = "meta";
  const name = document.createElement("div");
  name.className = "name";
  name.textContent = fileNameFromUrl(m.url);
  name.title = m.url;
  const badge = document.createElement("div");
  badge.className = "badge";
  badge.textContent = m.type === "video" ? "视频" : "图片";
  meta.appendChild(name);
  meta.appendChild(badge);
  row.appendChild(meta);

  const btn = document.createElement("button");
  btn.className = "primary";
  btn.textContent = "下载";
  btn.addEventListener("click", () => download(m.url));
  row.appendChild(btn);

  return row;
}

function load() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tab = tabs[0];
    if (!tab) return;
    currentTabId = tab.id;
    chrome.runtime.sendMessage({ type: "getMedia", tabId: currentTabId }, (res) => {
      mediaList = res || [];
      render();
    });
    chrome.runtime.sendMessage({ type: "getPrompts", tabId: currentTabId }, (res) => {
      promptList = res || [];
      renderPrompts();
    });
  });
}

document.getElementById("downloadAll").addEventListener("click", () => {
  mediaList.filter((m) => m.type === "video").forEach((m) => download(m.url));
});

document.getElementById("copyAll").addEventListener("click", () => {
  const text = mediaList.map((m) => m.url).join("\n");
  navigator.clipboard.writeText(text);
  const btn = document.getElementById("copyAll");
  const old = btn.textContent;
  btn.textContent = "已复制";
  setTimeout(() => (btn.textContent = old), 1200);
});

document.getElementById("refresh").addEventListener("click", load);

document.getElementById("clear").addEventListener("click", () => {
  chrome.runtime.sendMessage({ type: "clear", tabId: currentTabId }, () => {
    mediaList = [];
    promptList = [];
    render();
  });
});

load();
