// 负责监听网络请求，捕获 liblib CDN 上的视频/图片地址，按标签页分别存储。

const MEDIA_FILTER = {
  urls: [
    "*://*.liblib.cloud/*",
    "*://*.liblibai.com/*",
    "*://*.liblibai-online.com/*",
    "*://*.liblib.art/*"
  ]
};

function classify(url) {
  const path = url.split("?")[0].toLowerCase();
  if (/\.(mp4|webm|mov|m4v)$/.test(path)) return "video";
  if (/\.(jpe?g|png|webp|gif|avif)$/.test(path)) return "image";
  return null;
}

function keyFor(tabId) {
  return "media_" + tabId;
}

function keyForPrompt(tabId) {
  return "prompts_" + tabId;
}

async function addPrompts(tabId, prompts) {
  if (tabId == null || tabId < 0 || !Array.isArray(prompts)) return;
  const key = keyForPrompt(tabId);
  const store = await chrome.storage.session.get(key);
  const list = store[key] || [];
  let changed = false;
  for (const p of prompts) {
    if (!p || !p.text) continue;
    const text = String(p.text).slice(0, 5000);
    if (list.some((x) => x.text === text)) continue;
    list.push({ label: p.label || "prompt", text });
    changed = true;
  }
  if (changed) await chrome.storage.session.set({ [key]: list });
}

async function addMedia(tabId, url, forcedType) {
  if (tabId == null || tabId < 0) return;
  if (url.startsWith("blob:") || url.startsWith("data:")) return;
  const type = forcedType || classify(url);
  if (!type) return;

  const key = keyFor(tabId);
  const store = await chrome.storage.session.get(key);
  const list = store[key] || [];
  if (list.some((m) => m.url === url)) return;

  list.push({ url, type, ts: Date.now() });
  await chrome.storage.session.set({ [key]: list });
  updateBadge(tabId, list);
  notifyTab(tabId, list);
}

function notifyTab(tabId, list) {
  const videos = list.filter((m) => m.type === "video").length;
  chrome.tabs.sendMessage(tabId, { type: "mediaUpdate", videos }).catch(() => {});
}

function fileNameFromUrl(url) {
  try {
    const path = new URL(url).pathname;
    return decodeURIComponent(path.substring(path.lastIndexOf("/") + 1) || "video.mp4");
  } catch (e) {
    return "video.mp4";
  }
}

async function downloadAllVideos(tabId) {
  const store = await chrome.storage.session.get(keyFor(tabId));
  const list = store[keyFor(tabId)] || [];
  list
    .filter((m) => m.type === "video")
    .forEach((m) =>
      chrome.downloads.download({
        url: m.url,
        filename: "liblib/" + fileNameFromUrl(m.url),
        saveAs: false
      })
    );
  return list.filter((m) => m.type === "video").length;
}

function updateBadge(tabId, list) {
  const count = list.filter((m) => m.type === "video").length;
  chrome.action.setBadgeBackgroundColor({ color: "#2f6fed" });
  chrome.action.setBadgeText({ tabId, text: count ? String(count) : "" });
}

chrome.webRequest.onCompleted.addListener((details) => {
  if (classify(details.url)) addMedia(details.tabId, details.url);
}, MEDIA_FILTER);

// 页面跳转到新地址时清空该标签页旧记录
chrome.tabs.onUpdated.addListener((tabId, changeInfo) => {
  if (changeInfo.url) {
    chrome.storage.session.remove([keyFor(tabId), keyForPrompt(tabId)]);
    chrome.action.setBadgeText({ tabId, text: "" });
  }
});

chrome.tabs.onRemoved.addListener((tabId) => {
  chrome.storage.session.remove([keyFor(tabId), keyForPrompt(tabId)]);
});

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "add" && sender.tab) {
    addMedia(sender.tab.id, msg.url, msg.mediaType);
    return;
  }
  if (msg.type === "addPrompt" && sender.tab) {
    addPrompts(sender.tab.id, msg.prompts);
    return;
  }
  if (msg.type === "getPrompts") {
    chrome.storage.session.get(keyForPrompt(msg.tabId)).then((s) => {
      sendResponse(s[keyForPrompt(msg.tabId)] || []);
    });
    return true;
  }
  if (msg.type === "downloadAll") {
    const tabId = (sender.tab && sender.tab.id) != null ? sender.tab.id : msg.tabId;
    downloadAllVideos(tabId).then((n) => sendResponse(n));
    return true;
  }
  if (msg.type === "ping") {
    const tabId = sender.tab && sender.tab.id;
    if (tabId == null) {
      sendResponse({ videos: 0 });
      return true;
    }
    chrome.storage.session.get(keyFor(tabId)).then((s) => {
      const list = s[keyFor(tabId)] || [];
      sendResponse({ videos: list.filter((m) => m.type === "video").length });
    });
    return true;
  }
  if (msg.type === "getMedia") {
    chrome.storage.session.get(keyFor(msg.tabId)).then((s) => {
      sendResponse(s[keyFor(msg.tabId)] || []);
    });
    return true;
  }
  if (msg.type === "clear") {
    chrome.storage.session
      .remove([keyFor(msg.tabId), keyForPrompt(msg.tabId)])
      .then(() => {
        chrome.action.setBadgeText({ tabId: msg.tabId, text: "" });
        sendResponse(true);
      });
    return true;
  }
});
