// 运行在页面真实环境(MAIN world)，劫持 fetch / XHR，
// 从接口返回的 JSON 里递归找出含 prompt 的字段，postMessage 给内容脚本。

(function () {
  const TAG = "liblib-grabber-prompt";

  // 递归扫描对象，收集 key 含 prompt 的字符串值（以及常见的负向提示词）
  function scanPrompts(obj, out, depth) {
    if (depth > 6 || obj == null) return;
    if (Array.isArray(obj)) {
      obj.forEach((v) => scanPrompts(v, out, depth + 1));
      return;
    }
    if (typeof obj !== "object") return;
    for (const key of Object.keys(obj)) {
      const val = obj[key];
      const k = key.toLowerCase();
      if (typeof val === "string") {
        const text = val.trim();
        if (!text) continue;
        if (k.includes("prompt") || k === "tags" || k === "caption") {
          out.push({ label: key, text });
        }
      } else if (typeof val === "object") {
        scanPrompts(val, out, depth + 1);
      }
    }
  }

  function handleJson(json) {
    try {
      const found = [];
      scanPrompts(json, found, 0);
      if (found.length) {
        window.postMessage({ source: TAG, prompts: found }, "*");
      }
    } catch (e) {
      /* ignore */
    }
  }

  function tryParse(text) {
    if (!text || text.length > 2_000_000) return null;
    const t = text.trimStart();
    if (!t.startsWith("{") && !t.startsWith("[")) return null;
    try {
      return JSON.parse(text);
    } catch (e) {
      return null;
    }
  }

  // ---- 劫持 fetch ----
  const origFetch = window.fetch;
  if (origFetch) {
    window.fetch = function (...args) {
      return origFetch.apply(this, args).then((res) => {
        try {
          res
            .clone()
            .text()
            .then((t) => {
              const json = tryParse(t);
              if (json) handleJson(json);
            })
            .catch(() => {});
        } catch (e) {
          /* ignore */
        }
        return res;
      });
    };
  }

  // ---- 劫持 XHR ----
  const origOpen = XMLHttpRequest.prototype.open;
  const origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function (...args) {
    this.addEventListener("load", function () {
      try {
        const type = this.responseType;
        if (type === "" || type === "text") {
          const json = tryParse(this.responseText);
          if (json) handleJson(json);
        } else if (type === "json" && this.response) {
          handleJson(this.response);
        }
      } catch (e) {
        /* ignore */
      }
    });
    return origOpen.apply(this, args);
  };
  XMLHttpRequest.prototype.send = function (...args) {
    return origSend.apply(this, args);
  };
})();
