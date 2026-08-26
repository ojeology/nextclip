# BRYME Telegram Bot + Mini App — setup & operations

The full flow: **Telegram bot → backend API → Mini App deep links → BRYME content**,
all from one content source (`content/posts-index.json`, rebuilt from the same
files the website renders).

```
BRYME content (JSON + HTML)  ──scripts/build-posts-index.js──▶  content/posts-index.json
                                                                      │
                                                       server/server.js (Render web service)
                                                       ├── GET /api/posts/latest
                                                       ├── GET /api/posts/category/:cat
                                                       ├── GET /api/posts/:slug
                                                       ├── POST /telegram/webhook  (bot logic)
                                                       └── serves miniapp/  (Telegram Mini App)
```

## 1. Create the bot (BotFather, ~2 minutes)

1. In Telegram, open **@BotFather** → `/newbot` → name it (e.g. `BRYME`), pick a username (e.g. `bryme_discovery_bot`).
2. Copy the **bot token** → service env var `TELEGRAM_BOT_TOKEN`.
3. **Attach the Mini App domain**: BotFather → `/mybots` → your bot → *Bot Settings* → *Menu Button* → set URL to `https://YOUR-SERVICE.onrender.com/#/home` and text `BRYME`.
4. (Recommended) Also *Bot Settings → Web App URL* same value, so `web_app` buttons work everywhere.
5. Put the username (without @) into `site.config.json` → `"telegramBotUsername"`, then run:
   `python3 scripts/wire-telegram-ctas.py` to add the website → bot links.

## 2. Deploy the backend (Render)

- New **Web Service** from this repo, **Root Directory: `server`**, Start: `node server.js`, health check `/healthz`. (Blueprint provided at `server/render.yaml`.)
- Env vars:
  | var | required | notes |
  |---|---|---|
  | `TELEGRAM_BOT_TOKEN` | yes | from BotFather, secret |
  | `TELEGRAM_WEBHOOK_SECRET` | recommended | random string; setup tool generates one |
  | `MINI_APP_URL` | yes | `https://YOUR-SERVICE.onrender.com` (public HTTPS origin) |
- Free plan is fine; the service is stateless.

## 3. Register the webhook (one command)

```
TELEGRAM_BOT_TOKEN=... node scripts/setup-telegram.js --set-webhook https://YOUR-SERVICE.onrender.com
TELEGRAM_BOT_TOKEN=... node scripts/setup-telegram.js --set-menu-button https://YOUR-SERVICE.onrender.com
```

The tool prints the generated `TELEGRAM_WEBHOOK_SECRET` — add it to the service env and redeploy.

## 4. Publishing content (single source of truth)

After publishing/changing articles on the site, rebuild the index and deploy:

```
node scripts/build-posts-index.js     # regenerates content/posts-index.json + posts-bodies.json
git add content/posts-index.json content/posts-bodies.json && git commit -m "content: refresh index" && git push
```

Render redeploys the service; the bot and Mini App serve the new content immediately
(the server re-reads the files by mtime — no restart needed if you edit them in place).

## 5. Verify the flow

- `GET /healthz` → `{"ok":true,"posts":N}`
- `GET /api/posts/latest?limit=5` → published posts only
- `GET /api/posts/category/money` → money posts
- `GET /api/posts/<slug>` → full article incl. body; unknown slug → 404 JSON with fallback route
- Telegram: `/start` → menu; tap 💰 Make Money → snippet + *Open in BRYME*; 🆕 Latest Posts → list of article buttons; `t.me/<bot>?start=sports` from the website → straight to Sports.

## Security notes

- The bot token lives only in env vars; the webhook rejects requests without the secret header.
- Only **published** content is indexed. Drafts (`status != "published"`) never reach Telegram.
- The Mini App works in a plain browser too (Telegram SDK is optional at runtime) — safe for dev.
