/* BRYME Telegram bot logic — pure module.
 * server.js feeds it Telegram updates and a `send` function that performs
 * HTTP calls to the Telegram Bot API. All content comes from the shared
 * posts index (content/posts-index.json) — never hard-coded copies.
 *
 * Callback data vocabulary (stable, <=64 bytes):
 *   cat:<category>   open a category snippet
 *   latest           newest posts menu
 *   art:<slug>       one article snippet
 */
"use strict";

const CATEGORIES = [
  { key: "money",         label: "💰 Make Money",      emoji: "💰" },
  { key: "tech",          label: "🤖 Tech & AI",       emoji: "🤖" },
  { key: "sports",        label: "⚽ Sports",          emoji: "⚽" },
  { key: "entertainment", label: "🎬 Movies & Anime",  emoji: "🎬" },
  { key: "trading",       label: "📈 Trading",         emoji: "📈" },
  { key: "internet",      label: "🌐 Internet",        emoji: "🌐" },
  { key: "comics",        label: "😂 Comics",          emoji: "😂" }
];
const CAT_BY_KEY = {};
CATEGORIES.forEach((c) => (CAT_BY_KEY[c.key] = c));

/* Mini App route path per category */
function miniRoute(category) {
  return category === "entertainment" ? "movies" : category;
}

/* Destination-aware Mini App button URL.
 * The destination rides in TWO carriers so no Telegram client quirk
 * (fragment stripping / param injection / redirects) can drop it:
 *   1. query param  r=<route>   (e.g. miniapp?api=X&r=money)
 *   2. URL fragment  #/<route>  (e.g. miniapp?api=X&r=money#/money)
 * The app reads hash first, then r, then Telegram startapp params. */
function btnUrl(miniAppBase, route) {
  const sep = miniAppBase.indexOf("?") > -1 ? "&" : "?";
  return miniAppBase + sep + "r=" + encodeURIComponent(route) + "#/" + route;
}

function clip(text, n) {
  text = String(text || "").trim();
  return text.length > n ? text.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : text;
}

function homeKeyboard() {
  const rows = [];
  const row = [];
  CATEGORIES.forEach((c) => {
    row.push({ text: c.label, callback_data: "cat:" + c.key });
    if (row.length === 2) { rows.push(row.splice(0, 2)); }
  });
  if (row.length) rows.push(row.slice());
  rows.push([{ text: "🆕 Latest Posts", callback_data: "latest" }]);
  return { inline_keyboard: rows };
}

function homeText() {
  return "🔥 BRYME\n\n«What do you want to explore?»";
}

function categoryMessage(posts, category, miniAppBase) {
  const cat = CAT_BY_KEY[category];
  if (!cat) return { text: "😕 Unknown section. Pick one below:", keyboard: homeKeyboard() };
  const list = posts.filter((p) => p.category === category);
  if (!list.length) {
    return {
      text: "«" + cat.label.toUpperCase() + "»\n\nNothing new here yet. Check back soon. 🌱",
      keyboard: { inline_keyboard: [[{ text: "🆕 Latest Posts", callback_data: "latest" }], [{ text: "🏠 Menu", callback_data: "home" }]] }
    };
  }
  const top = list[0];
  const more = list.length > 1 ? "\n\n +" + (list.length - 1) + " more in this section." : "";
  return {
    text: "«" + cat.label.toUpperCase() + "»\n\n" + clip(top.title, 90) + "\n\n" + clip(top.excerpt, 220) + more,
    keyboard: {
      inline_keyboard: [
        [{ text: cat.emoji + " Open in BRYME", web_app: { url: btnUrl(miniAppBase, miniRoute(category)) } }],
        [{ text: "🔄 Another one", callback_data: "cat:" + category }, { text: "🆕 Latest", callback_data: "latest" }]
      ]
    }
  };
}

function latestMessage(posts, miniAppBase) {
  const list = posts.slice(0, 8);
  if (!list.length) {
    return { text: "Nothing published yet. Check back soon. 🌱", keyboard: homeKeyboard() };
  }
  const rows = list.map((p) => [{
    text: p.categoryLabel.split(" ").slice(1).join(" ") + ": " + clip(p.title, 32),
    web_app: { url: btnUrl(miniAppBase, "article/" + p.slug) }
  }]);
  rows.push([{ text: "🏠 Menu", callback_data: "home" }]);
  return { text: "🆕 LATEST ON BRYME\n\nTap to read inside BRYME:", keyboard: { inline_keyboard: rows } };
}

function articleMessage(posts, slug, miniAppBase) {
  const p = posts.find((x) => x.slug === slug);
  if (!p) {
    return {
      text: "😕 We couldn't find that article.\n\nCheck the latest BRYME posts instead.",
      keyboard: { inline_keyboard: [[{ text: "🆕 Latest Posts", callback_data: "latest" }], [{ text: "🏠 Menu", callback_data: "home" }]] }
    };
  }
  return {
    text: "«" + clip(p.title, 90).toUpperCase() + "»\n\n" + clip(p.excerpt, 240) + "\n\n🚀 Continue reading in BRYME",
    keyboard: {
      inline_keyboard: [
        [{ text: "🚀 Open in BRYME", web_app: { url: btnUrl(miniAppBase, "article/" + p.slug) } }],
        [{ text: "🏠 Menu", callback_data: "home" }]
      ]
    }
  };
}

/* Create the bot. deps: { getPosts(), miniAppBase, apiBaseUrl, send(method, payload), answerCallback(id, text) } */
function createBot(deps) {
  const { getPosts, miniAppBase, send, answerCallback } = deps;
  /* When the Mini App is hosted on the FRONTEND domain (recommended:
   * https://bryme.onrender.com/miniapp/) it needs to be told where the
   * backend API lives — the app reads ?api= from its URL. When the Mini App
   * is hosted by the backend itself, no parameter is needed. */
  const apiParam = deps.apiBaseUrl
    ? (deps.apiBaseUrl.indexOf("?") > -1 ? "&" : "?") + "api=" + encodeURIComponent(deps.apiBaseUrl.replace(/\/+$/, ""))
    : "";
  const base = miniAppBase + apiParam;

  function deliver(chatId, msg) {
    return send("sendMessage", {
      chat_id: chatId,
      text: msg.text,
      parse_mode: "",
      disable_web_page_preview: true,
      reply_markup: msg.keyboard
    }).catch(() => {});
  }

  function handleStart(chatId, arg) {
    const cat = (arg || "").trim().toLowerCase();
    if (cat && CAT_BY_KEY[cat]) {
      return deliver(chatId, categoryMessage(getPosts(), cat, base));
    }
    if (cat === "latest") return deliver(chatId, latestMessage(getPosts(), base));
    const slug = cat;
    if (slug) {
      const p = getPosts().find((x) => x.slug === slug);
      if (p) return deliver(chatId, articleMessage(getPosts(), slug, base));
    }
    return deliver(chatId, { text: homeText(), keyboard: homeKeyboard() });
  }

  /* Free-text intent -> section. First match wins. */
  const TEXT_MAP = [
    [/\b(money|make money|earn|earning|income|hustle)\b/i, "money"],
    [/\b(sport|sports|football|soccer|score|scores|fixture|fixtures|table|league|la liga)\b/i, "sports"],
    [/\b(tech|ai|a\.i|artificial|robot|gpt)\b/i, "tech"],
    [/\b(movie|movies|film|films|series|serie|anime|cinema|entertainment|watch|trailer)\b/i, "entertainment"],
    [/\b(trading|trade|trader|crypto|forex|stock|stocks|market)\b/i, "trading"],
    [/\b(internet|website|websites|tool|tools|online)\b/i, "internet"],
    [/\b(comic|comics|banter|funny|meme)\b/i, "comics"],
    [/\b(latest|new|news|fresh|update|updates)\b/i, "latest"]
  ];
  function textIntent(t) {
    const s = String(t || "").toLowerCase();
    for (let i = 0; i < TEXT_MAP.length; i++) if (TEXT_MAP[i][0].test(s)) return TEXT_MAP[i][1];
    return null;
  }

  return {
    handleUpdate(update) {
      try {
        const msg = update.message;
        const cb = update.callback_query;
        if (msg && msg.text) {
          const parts = msg.text.split(/\s+/);
          const cmd = (parts[0] || "").replace(/@.*$/, "").toLowerCase();
          if (cmd === "/start") return handleStart(msg.chat.id, parts.slice(1).join(" "));
          if (cmd === "/menu" || cmd === "/help" || cmd === "/home") return handleStart(msg.chat.id);
          if (cmd === "/latest") return handleStart(msg.chat.id, "latest");
          const intent = textIntent(msg.text);
          if (intent === "latest") return deliver(msg.chat.id, latestMessage(getPosts(), base));
          if (intent) return deliver(msg.chat.id, categoryMessage(getPosts(), intent, base));
          return deliver(msg.chat.id, {
            text: "🔥 BRYME\n\n«What do you want to explore?»\n(Tip: you can also type — try “make money”, “sports” or “comics”.)",
            keyboard: homeKeyboard()
          });
        }
        if (cb && cb.data) {
          const chatId = cb.message && cb.message.chat ? cb.message.chat.id : cb.from && cb.from.id;
          const done = answerCallback(cb.id).catch(() => {});
          if (cb.data === "home") return done.then(() => deliver(chatId, { text: homeText(), keyboard: homeKeyboard() }));
          if (cb.data === "latest") return done.then(() => deliver(chatId, latestMessage(getPosts(), base)));
          if (cb.data.startsWith("cat:")) return done.then(() => deliver(chatId, categoryMessage(getPosts(), cb.data.slice(4), base)));
          if (cb.data.startsWith("art:")) return done.then(() => deliver(chatId, articleMessage(getPosts(), cb.data.slice(4), base)));
          return done;
        }
      } catch (e) {
        /* never expose internals to users */
        const chatId = (update.message && update.message.chat && update.message.chat.id) ||
                       (update.callback_query && update.callback_query.from && update.callback_query.from.id);
        if (chatId) deliver(chatId, { text: "😕 Something went wrong on our side. Try again from the menu.", keyboard: homeKeyboard() });
      }
      return Promise.resolve();
    }
  };
}

module.exports = { createBot, CATEGORIES, homeText, homeKeyboard, categoryMessage, latestMessage, articleMessage, miniRoute };
