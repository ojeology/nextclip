# BRYME Tech — Master Build Roadmap

**Source spec:** `/home/user/uploads/bryme-tech-master-build-spec.md` (binding, user-attached 2026-09-10).
Mirrored here as the working program. Positioning unchanged: "Practical technology. No theatre."
Commercial goal (per spec): organic audience first, AdSense LAST — same standing rule as every property.

---

## PHASE 1 — Audit of the existing Tech site (done 2026-09-10)

Current state at `80f2cce68a`:

| Item | Status |
|---|---|
| Pages | tech = 101 pages (index, 11 category hubs, 84 guides, about/contact/privacy, sitemap, robots) |
| Categories (hubs) | ai · tools · web-and-hosting · safety · smart-home · android · windows · coding · buying · subscriptions · streaming |
| Trust pages | about / contact / privacy LIVE. **Missing: Terms, Disclaimer (standalone), Editorial Methodology, Corrections Policy** |
| Search | none on tech index (known gap; optional, not a spec build item) |
| Canonicals / metadata / schema | hostname from config (thebryme.com); Article schema on guides; breadcrumbs present |
| Mobile / performance | system fonts, no framework, CSP-safe (no inline JS), static CDN hosting — fast by construction |
| Sitemap / robots | generated per build; allowlist v26 (765 routes); internal links machine-checked every batch |
| Content quality | 84 guides, all source-or-empty-sources policy; 0 fabricated stats across T1–T5 receipts |

**Spec pillar → already-live mapping (retain, do not rebuild):**

- AI & tools → chatgpt-vs-claude-vs-gemini, ai-useful-vs-hype, free-ai-tools-worth-using, arena-ai-vs-chatgpt, deepseek-vs-chatgpt, gemini-vs-chatgpt, chatgpt-claude-alternatives, ai-assistant-data-training-settings
- Apps & Android → android-app-permissions, android-battery-health, android-notifications, free-up-storage-android, what-free-apps-do-with-your-data
- Privacy & security → reusing-passwords-risk, security-questions-are-insecure, two-factor-authentication-setup, password-manager-or-browser, bitwarden-free-password-manager, plain-text-passwords, github-token-hygiene, how-to-spot-a-suspicious-link, public-wifi-risks, browser-privacy-settings, vpn-what-it-protects, signal-vs-whatsapp
- Hosting & cloud → render-static-deploy, free-vs-paid-hosting, why-your-website-is-slow, domain-names-explained, custom-domain-dns-order, what-is-dns, what-is-ssl-https
- GitHub & dev tools → git-and-github-for-beginners, github-beginner-mistakes, github-token-hygiene, what-is-an-api, what-is-a-database
- Troubleshooting (partial) → why-is-my-computer-slow, why-phones-slow-down, browser-problems, phone-wont-connect-to-wifi, bluetooth-not-pairing, windows-update-problems, why-restarting-fixes-problems, computer-fans-loud, how-to-read-an-error-message, storage-full-breaking-apps, render-deployment-failures-what-they-taught-me
- Python/programming (partial) → learning-python-free-resources, learning-to-code-on-a-phone-termux
- Comparisons / alternatives → google-docs-vs-word-vs-notion, grammarly-alternatives-compared, photopea-vs-photoshop, pixlr-vs-canva, plasfy-vs-canva, polotno-studio-vs-canva, lyra-vs-spotify, free-software-alternatives, affinity-now-free, notion-free-plan, refurbished-vs-new-tech + buying shelf
- First-hand project content → render-static-deploy, custom-domain-dns-order, csp-safe-front-end, github-token-hygiene, render-deployment-failures (all genuinely first-hand: this site's own stack)

**Gaps the spec adds (the actual build program):** Quantitative Computing (QuantLab) · BRYME Tools (interactive) · structured troubleshooting library expansion · Python practicals · trust-page completion · explicit authorship labels · internal-link network hardening.

---

## Safety & honesty rules for Quant content (binding, from spec §5 + house rules)

- The spec disclaimer is used verbatim on every QuantLab piece:
  > "Research note: QuantLab experiments are presented for educational and research purposes. Historical backtests and simulations do not guarantee future results and should not be interpreted as investment advice."
- **Methodology-first editorial policy:** articles teach validation, statistics and engineering. They do NOT republish dollar-return figures, CAGRs or "champion" performance numbers from the repo — the repo's own numbers changed under honest re-audit (T34), which is itself the lesson. Where a figure is essential to a story, it is framed as a historical backtest result that did not survive re-testing.
- No "copy this strategy", no signals, no profit promises, no go-live encouragement. The repo's bot is paper-only ("NEVER live" per its own docs) and articles say exactly that.
- Betting-adjacent exclusion (house hard rule): FORTEBET*/FORTELEARN repos are never content sources. Deriv synthetics appear ONLY as the repo's negative result (random walk, no edge) — an anti-hype story, never a how-to.
- Authorship labels (spec §22): "First-Hand Project Report" for QuantLab pieces; general explainers remain "BRYME Technical Guide". First-hand vs general is stated in-piece.

## PHASE 8 evidence base — QuantLab repo (inspected 2026-09-10, public, `Ojeology/QUANTLAB`)

Verified from the repo (branches `main` + `blind-validation`, README 48KB read end-to-end in part):

- ~95 numbered crypto research runs (`quantlab_r005–r095.py`), 9 forex runs (`forex_f001–f009.py`), one script per run, outputs in `quantlab_output/` (reports, journals, CSVs, PNGs) + machine-readable `research_journal.csv`.
- A formal **validation framework**: walk-forward optimization, untouched holdouts, cost gates (0.05%/side), mandatory causal/lookahead audit (instituted after the R090 retraction), bootstrap CIs, Monte Carlo, leave-one-out symbol/fold validation, monthly stability, regime/drawdown analysis, parameter grids, portfolio validation.
- Promotion vocabulary: PROMOTE / WATCHLIST / REJECT / NO-GO / RETRACTED / OVERFIT — "a failed experiment is a finding."
- Headline NEGATIVE results (the project's own words): 5-minute crypto has no cost-surviving edge (proven 7 independent ways, R089–R095); the R066–R071 "edge" was a backtest proxy artifact (EXIT_MODEL_AUDIT.md); most edges are universe-specific (R044/R049/R078); the Aug-2026 freeze config FAILED its blind per-year re-test and was superseded.
- **T34 self-audit (2026-09-04):** the trend-strategy results were exit-anchored (features read the exit bar — post-entry information); gated at the true entry bar the edge vanishes (PF@c ≈ 1.03). A real, documented lookahead-bias catch with before/after numbers.
- `demo_bot.py`: paper-trading bot, SQLite + Telegram alerts, explicitly never live. `scripts/ql_engine.py`: shared walk-forward engine. Deriv synthetics tested → random walk, no edge (RESEARCH_DERIV.md).
- Sister repos available as evidence when needed: mean-reversion-vwap-lab (14 documented phases), pitchledger (Python pipeline tracker), Vwap-bot/Deriv-TouchBot (WebSockets/API engineering — engineering topics only).

---

## Build batches (spec §25 phases mapped to batches; §26 fields condensed to: intent · problem · first-hand? · links · tools · sources · priority)

### M1 — Trust pages + architecture (Phase 2) · priority HIGH · smallest risk
1. **/tech/methodology/** — Editorial Methodology: how BRYME Tech researches (primary sources, verify-or-soften, sources[] empty means "no external claim"), how first-hand pieces are identified, UPDATE-class re-verification, corrections handling. Intent: trust/EEAT. Links: about, privacy, github-token-hygiene. Static.
2. **/tech/corrections/** — Corrections Policy: how errors are found, fixed, dated and logged (receipts pattern). Links: methodology.
3. **/tech/terms/ + /tech/disclaimer/** — check writers/home property patterns first; reuse legal copy structure; general-information disclaimer for tech (esp. safety/quant pieces).
4. Authorship labels: wire "BRYME Technical Guide" vs "First-Hand Project Report" onto existing tech templates (byline already exists; extend the label vocabulary on new pieces; retro-label QuantLab pieces at birth, existing shelf stays).
5. Tech index nav: add Tools + Quantitative computing to the hub grid when those sections exist (empty hubs are forbidden — no doorway pages).

### M2 — Quantitative Computing pillar (Phase 8 content, grounded above) · new cat `quant` · 7 pieces
| # | Slug | Intent/problem | First-hand | Evidence anchors (repo) |
|---|---|---|---|---|
| 1 | quantlab-project-how-built | "How I built a quant research lab in Python" — architecture of a one-person lab | YES | repo layout, ql_engine.py, research_journal.csv |
| 2 | hundred-experiments-lessons | What ~140 documented experiments teach (R001–R095, F001–F009, T1–T34) | YES | README research logs, negative-results list |
| 3 | lookahead-bias-explained | What lookahead bias is + the repo's own T34 exit-anchor catch | YES | EXIT_MODEL_AUDIT.md, T34 correction block |
| 4 | backtest-validation-checklist | Walk-forward, holdouts, cost gates, bootstrap/MC/LOO — the framework any claim must survive | YES (framework) | README validation framework |
| 5 | why-backtests-fail | Cost drag, regime change, universe-specificity, proxy artifacts — four documented failure modes | YES | R089–R095, R044/R049/R078, freeze→blind reversal |
| 6 | paper-trading-bot-lessons | Building a paper-trading bot: scheduling, SQLite, alerts, why it never goes live | YES | demo_bot.py, bot_config.yaml |
| 7 | overfitting-detection-guide | How to detect overfitting: holdout discipline, promotion vocabulary, retracting your own results | YES | RETRACTED/OVERFIT vocabulary, EXIT_MODEL_AUDIT |
Each piece: research disclaimer verbatim, no performance-figure republication, ≥4 internal links (each other + learning-python/termux/what-is-api), author label "First-Hand Project Report", repo linked as source. Hub: /tech/quant/.

### M3 — BRYME Tools, first slice (Phase 7) · 8 tools · CSP-safe pattern
Client-side only, no data collection, external JS under `/assets/` mirrored to `public/assets/` (CSP kills inline), mobile-first, each with a companion explainer article (M4 links into them). First slice (pure-JS, zero dependencies):
json-formatter · base64-encoder · url-encoder · uuid-generator · timestamp-converter · word-counter · case-converter · http-status-lookup.
Companion articles (short technical guides): what-is-json (new), base64-explained (new), uuid-guide (new), unix-time-explained (new), http-status-codes-explained (new) — plus existing pieces link in.
Tool hub: /tech/tools-hub/ or tools section on tech index (final naming at build). Deferred with reasons: markdown previewer (sanitiser risk — NEEDS REVIEW), QR generator + cron helper + subnet calculator (dependency/complexity — COMING SOON), anything needing a backend (never).

### M4 — Python practicals (Phase 3/4) · 6 pieces
parse-json-python · call-api-python · handle-api-errors-python · store-api-data-python (sqlite) · schedule-python-scripts · deploy-python-app (first-hand Render experience). Each: tested code examples where practical (run in sandbox before publishing — hard gate), links to tools + quant pieces + termux piece.

### M5 — Troubleshooting library (Phase 5) · 8 pieces, structured per spec §14 template
dns-problems-diagnosed · ssl-certificate-errors-explained · git-errors-fixed (merge conflicts, detached HEAD) · app-crashes-android · login-problems-checklist · api-errors-decoded (4xx/5xx field guide) · websocket-debugging · environment-variables-guide.
Each: what it means → causes → quick checks → fixes → alternatives → mistakes → provider-side → when to contact support → related. Hard dedupe rule against the 11 existing troubleshooting pieces (extend, don't duplicate: e.g. browser-problems exists; dns-problems must link, not overlap).

### M6 — Apps & Android expansion + hardening (Phases 6, 9–11)
6 app/Android pieces from real usage (app-permissions follow-up, notification triage, connectivity) + internal-link network pass (every piece ≥5 genuine links; tools ↔ articles ↔ quant) + technical SEO audit (canonicals/sitemap/robots re-verified) + mobile UX pass + **Final Report per spec §30** with READY TO PUBLISH / NEEDS REVIEW / DO NOT INDEX / COMING SOON lists.

---

## Status ledger (updated per batch)

- 2026-09-10: Phases 1–2 audit done (this document); QuantLab evidence base inspected and recorded; M1–M6 queued. Nothing built yet under this spec — no batch receipts below this line yet.

## Batch receipts

_(appended per batch: built slugs, gates, commit, live checks)_

### M1 — DONE 2026-09-10 (commit follows)
Built (4 trust pages): /tech/methodology/ · /tech/corrections/ · /tech/terms/ · /tech/disclaimer/ —
same visual pattern as about/privacy; linked from every tech page's footer (conditional in
foot()); cross-linked to each other, about, contact. Disclaimer page carries the quant research
disclaimer verbatim + "Last reviewed: September 2026". Methodology documents the two labels
(Technical Guide vs First-Hand Project Report), named-source+date policy, verify-or-drop,
UPDATE-class re-verification, no-quiet-re-dating.
Authorship labels: `_TECH_FIRSTHAND` slug→label map applied in tech_pages(); label renders in
the byline ("BRYME Technical Research · first-hand project report") and kind="firsthand" renders
the "First-hand · verified against the real thing" kicker.

### M2 — DONE 2026-09-10 (same commit)
Built (7, new cat `quant` after coding, hub /tech/quant/):
/tech/quantlab-project-how-built/ · /tech/hundred-experiments-lessons/ ·
/tech/lookahead-bias-explained/ · /tech/backtest-validation-checklist/ ·
/tech/why-backtests-fail/ · /tech/paper-trading-bot-lessons/ · /tech/overfitting-detection-guide/
- All kind="firsthand", authorship-labelled, verbatim research disclaimer in each (machine-checked).
- Evidence anchors = repo files inspected 2026-09-10 (README main, EXIT_MODEL_AUDIT.md,
  blind-validation branch, ql_engine.py, demo_bot.py). Sources = repo links only.
- Performance framing: T34 numbers appear ONLY as historical backtest results that did not
  survive re-testing ($100→~$199 logged vs ~$106 entry-anchored); no PF/CAGR republication,
  no champion figures as achievement. No signals, no strategy advice, bot documented as
  paper-only-forever. FORTEBET repos excluded; Deriv appears only as the negative result.
- Internal links: 2-4 per body (quant cross-links + learning-python-free-resources);
  related shelf auto-fills same-cat (7 quant pieces). Word counts 442-576.
Chain after M1+M2: tech 113 pages (+12), site 787 pages / 75,889 links OK; allowlist v26 777
routes; validator ok. Live sweep follows push.

### M3 — DONE 2026-09-10 (commit follows)
Built: /tech/tool/ hub + 8 client-side tools — /tech/tool/json-formatter/ · base64-encoder ·
url-encoder · uuid-generator · timestamp-converter · word-counter · case-converter ·
http-status-lookup — plus 5 companion articles: /tech/what-is-json/ · /tech/base64-explained/ ·
/tech/uuid-guide/ · /tech/unix-time-explained/ · /tech/http-status-codes-explained/.
- CSP-safe: behaviour in 8 external files assets/tool-*.js (script-src 'self'; node --check on
  each), styles in assets/tech-tools.css (theme-agnostic: inherit + rgba, no dark-mode break);
  no inline JS anywhere; status table works with JS disabled (filter is the only dynamic part).
- Privacy: zero network calls, zero storage; privacy note on every tool page; "don't paste
  secrets" stated on hub + terms (already promised in privacy page pre-tool language).
- Sources: primary standards only — RFC 8259, RFC 4648, RFC 9562 (+4122), IANA HTTP registry,
  RFC 9110. UUID piece covers the 2024 revision honestly; unix-time covers 2038 + leap seconds
  qualitatively; no volatile claims anywhere in M3.
- BUG FIXED (pre-existing): tech index had a malformed duplicated "Handpicked" section
  (unclosed <ul class="list" fragment) — removed; verified via built-output needle.
- Tool JS filename map (_TOOL_JS) — word-counter→wordcount, http-status-lookup→status; a
  slug-prefix derivation bug was caught pre-build and fixed.
Chain: tech 127 pages (+14), site 801 pages / 76,175 links OK; allowlist v26 791 routes;
public/assets mirror verified (9 files). Live sweep follows push.

### M4 — DONE 2026-09-10 (commit follows)
Built (6): /tech/parse-json-python/ · /tech/call-api-python/ · /tech/handle-api-errors-python/ ·
/tech/store-api-data-python/ · /tech/schedule-python-scripts/ · /tech/deploy-python-app/ (first-hand).
- HARD GATE PASSED: every executable code block extracted from the data file and RUN before
  publish (Python 3.13): JSON parse + .get + dumps (fixtures), JSONDecodeError line/col proof,
  BOTH urllib calls live against api.github.com (200 + real results), the retry ladder against
  a local 429-then-200 server (Retry-After: 0, exactly 2 attempts, correct payload), sqlite
  create/insert/upsert/query in a temp dir, sched job run to completion (3 runs), Flask app via
  test_client (exact JSON asserted), gunicorn --version real (26.2.0), os.environ read with key
  set. Cron lines and the gunicorn start command validated as config (not executed) + flake8-free.
- stdlib-first teaching (urllib before requests) = code that runs anywhere; requests covered
  honestly as the popular third-party option. Sources: official Python docs + RFC 9110 + primary
  product docs (requests, Flask, gunicorn, Render).
- Additive CSS: pre/code styling added to assets/content-v2.css (none existed) + mirrored.
  deploy-python-app added to _TECH_FIRSTHAND (byline label).
- Two process catches: (1) harness artifact (Flask root-path under exec) fixed harness-side —
  article code unchanged and correct in real module context; (2) css append silently failed in
  bash (second occurrence of the silent-edit class) — re-applied via python + assert, mirrored.
Chain: tech 133 pages (+6), site 807 pages / 76,292 links OK; allowlist v26 797 routes.

### M5 — DONE 2026-09-10 (commit follows)
Built (8, spec §14 structure — answer first → quick checks → causes → fix ladder →
alternatives → mistakes → provider-side → support → related):
/tech/dns-problems-diagnosed/ · /tech/ssl-certificate-errors-explained/ · /tech/git-errors-fixed/ ·
/tech/app-crashes-android/ · /tech/login-problems-checklist/ · /tech/api-errors-decoded/ ·
/tech/websocket-debugging/ · /tech/environment-variables-guide/
- Dedupe lanes honoured (link-not-overlap): what-is-dns / custom-domain-dns-order (DNS records),
  phone-wont-connect-to-wifi (phone layer), how-to-reset-forgotten-passwords (reset flow),
  http-status-codes-explained (code reference), handle-api-errors-python (Python client),
  storage-full-breaking-apps (the storage crash cause), browser-problems (browser layer).
- No volatile claims: DNS flush commands, git error strings, WebSocket close codes (RFC 6455
  cited), 12factor config principle (cited); browser error texts paraphrased, never quoted as
  exact UI strings. Sources: git-scm book x2, RFC 6455, 12factor, Python os.environ docs.
Chain: tech 141 pages (+8), site 815 pages / 76,457 links OK; allowlist v26 805 routes.

### M6 — DONE 2026-09-10 (commit follows)
Built (6, Apps & Android expansion): /tech/android-privacy-settings-checklist/ ·
/tech/android-notifications-not-arriving/ · /tech/mobile-data-not-working/ ·
/tech/how-to-tell-if-an-app-is-safe/ · /tech/android-backup-guide/ · /tech/android-find-lost-phone/
- Lanes carved vs existing shelf (documented in file header): per-app audit vs device-wide pass,
  notification tuning vs failure mode, wifi/bt vs mobile-data lane, stats piece vs backup mechanics.
- Internal-link hardening (Phase 9): _tech_related reworked — one rotating cross-category related
  link per article (8-slug pool incl. 4 previously underlinked pieces); pool slugs lifted off the
  floor; mean inbound 8.8/guide across 130 guides; remaining 14-slug floor queue listed in the
  final report as next-pass targets.
- Technical SEO/UX audit (Phases 10-11): titles 147/147 unique; h1==1 everywhere; viewport +
  canonical on all checked; zero noindex; sitemap == 147; TechArticle schema present; trust links
  site-wide. All green.
FINAL REPORT: docs/ecosystem/tech-master-final-report.md (23-point §30 + verdict lists).
Chain: tech 147 pages (+6), site 821 pages / 76,584 links OK; allowlist v26 811 routes.
**MASTER BUILD PROGRAM COMPLETE: M1-M6.**

### Design parity pass — DONE 2026-09-10 (commit follows)
User direction: "Tech has no dark mode.. no sliding hero like the writers... fix all — design
and layout of all mirrors the writers."
Implemented (tech property, all 147 pages):
- DARK MODE: assets/theme.js (Writers' own script, reused verbatim) loaded pre-paint in <head>;
  theme-toggle button (sun/moon SVGs, aria-pressed) in the masthead; dark palette block
  (html[data-theme="dark"]) using Writers' exact dark values (paper #141a24, sheet #1a212c,
  ink #e7e3d8, accent gold #d0aa52, dim lines); localStorage key shared site-wide
  ("bryme-theme"); OS-preference fallback; meta theme-color + color-scheme wired.
- SLIDING HERO: Writers' bsettle settle-in animation on the cover (kicker/title/dek,
  staggered delays, prefers-reduced-motion honoured).
- SLIDING NAV: the slide-out drawer (#site-drawer + backdrop, Writers' component values) on
  every tech page — 12 section hubs + toolbox + trust pages; hamburger + close buttons wired
  via site-nav.js (reused verbatim, progressive enhancement).
- Masthead: brand now targets /tech/; mast-tools (toggle + hamburger) added; sr-only utility.
- Scope guards: theme.js/site-nav.js/drawer markup only on tech; other properties carry the
  inert shared CSS only (no scripts, no markup) — verified. Home's own theme system untouched.
- Bug caught pre-build: literal 102% inside the BASE_CSS %-format template broke formatting
  (TypeError) — escaped to 102%%; format verified before rebuild.
Chain: 821 pages / 79,377 links OK (+2,793 = drawer links); validator ok; allowlist 811.

---

## Batch 4 — Writers header port to all properties — DONE 2026-09-10

**Directive:** "brymewriters has a header that shows home, publish, tools and more and the mix of colours is superb… make sports, technology and all follow it. For sports: EPL, LaLiga, Champions League and all as movable header."

**What shipped (commit this one):**
- **Header system ported** (Writers anatomy: mast-brand + mast-edition [mast-date + tagline] + tools, then a `.main-nav` bar with CSS-only mega dropdowns on hover/focus-within + `.nav-cta`): now emitted by a generalized `head()` for tech, sports, fitness, entertainment, hub. Writers itself untouched (protected).
- **Per-property navs:**
  - Tech: Guides (12 sections + all) / Toolbox (all 8 tools named) / The desk (methodology, corrections, about, contact, privacy) + "Start here" cta.
  - Sport: **EPL / LaLiga / Champions League / Desks** megas — every link a real page; "Desk home" cta.
  - Fitness: Guides mega (7 guides) + cta. Entertainment: Shelves mega + cta. Hub: all five properties + "Start with Writers" cta.
- **Two new real pages** so the sports megas link content: `/sports/epl/` (Premier League desk: 4 dated archive editions + 3 evergreen explainers) and `/sports/laliga/` (LaLiga desk: the 2 new explainers + 2 transfer-mechanics pieces).
- **2 new sports explainers** (real-sourced, dated, internal-linked, disclaimered): `laliga-explained` (409 w) and `el-classico-explained` (450 w) — SPORT_EXPLAINERS now 10.
- **Writers hero-explanation pattern mirrored:** `.cover-facts` stat rows (serif numerals, uppercase labels) added to the tech index (118 pieces / 8 tools / 12 sections / 0 fabricated claims) and sports index (16 evergreen / 5 archive / 3 desks / 0 odds, ever) — with the same "explicit tools mention" habit Writers uses.
- **Theme + drawer scope:** dark mode (theme.js pre-paint) now on tech, sports, fitness, hub; mobile drawer + hamburger on tech + sports. Sports family accent stays green `#2f6b4f` (locked); tech/fitness brass `#a8752a`.
- Masthead nav CSS ported verbatim from `assets/bryme-v2.css` (12px/750/.12em uppercase links, 3px accent underline hover, megas = pure CSS, responsive ≤860 scroll / ≤760 collapse to hamburger + tagline hidden).

**Verification:** full clean chain green — **825 pages / 85,148 internal links OK** (+4 pages, +5,771 links), allowlist v26 815 routes, validator ok. Needle matrix PASS on: sports index (megas, facts, drawer, theme), epl/laliga/champions-league desks, both new explainers, tech article (new header + drawer intact + bsettle), tech index facts, fitness guide (theme + nav, no drawer), entertainment page (nav, no theme), hub root (all-properties nav + cta), Writers/Home protected (no new markup; Writers' own header/theme native and untouched). 5 new URLs in sports/sitemap.xml. Mega "HEAD" marker bug (first-row rendered as link) caught and fixed pre-push across all 9 megas.

**Where visible:** every page of tech/sports/fitness/entertainment/hub (new masthead + nav bar); sports index + league desks (new pages, facts rows, drawer); tech/sports mobile (hamburger drawer); tech + sports indexes (stat rows); /home and /writers unchanged.

---

## Batch 5 — Home & DIY readiness pass — DONE 2026-09-10

**Directive:** "Make home and diy ready" (per readiness ratings: Home was B+, one parity pass short).

**What shipped (commit this one):**
- **Writers header ported to Home's own builder** (`_home_page` — home never used the shared `head()`): masthead upgraded to the Writers anatomy (mast-brand + mast-edition block with mast-date "SEPTEMBER 2026 · THE FIX-IT DESK" + tagline; theme button wrapped in mast-tools), plus a full `.main-nav` bar with 5 CSS megas + cta:
  - **Fix it** (7 fixes) / **Maintain** (8 incl. the seasonal checklist) / **Appliances** (7) / **Understand** (8 legal+damp+payback explainers) / **Mistakes & safety** (7, routed set-aware through HOME_MISTAKES so hrefs match real paths) + cta "Once-a-season checklist".
  - All 37 nav hrefs resolve (check-internal-links green). Megas = pure CSS hover/focus-within, shipped via BASE_CSS header block. Sidebar desk-map kept (top nav = quick jump, sidebar = section map).
- **Home's own dark palette restored** — real regression fixed: since the tech dark-mode batch, BASE_CSS's `html[data-theme="dark"]` (specificity 0-1-1) was silently beating Home's `[data-theme="dark"]` (0-1-0) var-for-var, so Home's custom night palette (#131318 / blue brand / #c9994e accent) never rendered. All 4 HOME_CSS_EXTRA dark selectors bumped to `html[data-theme=...]` (later + equal specificity wins). home-theme.js and its toggle untouched (Home keeps its own theme system).
- **Writers attention pattern mirrored:** cover-facts row on the home index — **76 guides & fixes · 9 sections · 9 common mistakes · 0 upsells** (counts computed from data at build time) — plus the explicit "everything on this desk" nav mentions.

**Verification:** full clean chain green — **825 pages / 89,464→89,468 internal links OK** (+4,320 from nav/megas), allowlist v26 815, validator ok. Needle matrix PASS on home index / article / mistakes page / fix hub / checklist page; regression spots PASS (sports index, tech article, Writers untouched). No new pages (nav links existing content only — no placeholders).

**Where visible:** every one of the 99 Home pages (new masthead + nav bar + megas), home index (stat row), dark-mode toggle now actually shows Home's own palette.

---

## Batch 6 — Sport in-season cadence + Fitness runway — DONE 2026-09-10

**Directive:** "Do whatever you can do best" (autonomous batch, closing the two content gaps from the readiness ratings: Sport B− needed in-season editions; Fitness C+ needed a runway).

**What shipped:**
- **Sport — first live desk edition of 2026-27:** `/sports/premier-league-matchweek-4-preview/` ("Matchweek 4, previewed honestly."). Written 2026-09-10 for the Sep 12–14 window. Fixtures verified against four independent sources (nbcsports.com, sportsmediawatch.com, footballfixtures.org, worldfootball.net — UK times cross-checked CET/ET); table as of Matchweek 3 corroborated across four sources (City 9, Arsenal 9, Hull City 7 unbeaten & unscored-on, Chelsea 6, Fulham/Coventry 0, Spurs/Villa 1 point & goalless). Four storylines (derby; Hull at Chelsea; Arsenal at Sunderland; the bottom three). House rules held: no odds, no predictions-as-promises, unknowns explicitly stated ("line-ups, injuries, late changes — the desk doesn't know it"). 9 internal links, all resolving.
- **Sport wiring:** EPL mega gains "Matchweek 4 preview · live"; EPL desk dek + closer updated (live-edition callout replaces "when the season resumes"); sports index fact now "6 dated editions".
- **Fitness — runway started (7→10 guides):** `workout-at-home-no-equipment` (six patterns, 2×20 min/week), `how-progressive-overload-works` (the honest, non-staircase version), `breathing-during-exercise` (two habits, no magic ratios). All: beginner-first, "general information, not medical advice" framing, WHO/CDC sources, JSON-LD Article, 5–6 internal links each. Fitness mega now lists 10 guides; index "Read before you push" shelf carries the three; related-map cross-wired.

**Verification:** full clean chain green — **829 pages / 89,662 internal links OK** (+4 pages: 1 sports, 3 fitness), allowlist v26 819, validator ok. Needles PASS on MW4 (fixtures, dated byline, 9 links, no-odds framing), EPL desk live row, index facts, all 3 fitness guides (bodies, links, JSON-LD, sources), fitness mega/index; regressions clean (home, LaLiga desk). New URLs in both sitemaps.

**Where visible:** /sports/ mega + EPL desk + new MW4 page; /fitness/ mega, index shelf, and 3 new guides.

---

## Batch 7 — Sport master upgrade, Phase 1 (spec execution) — DONE 2026-09-10

**Directive:** user-supplied spec "BRYME Sport 9.5/10 Master Upgrade" ("Do this"). Executed §1-2 audit first, then Phase 1 core per §33.

**Shipped (+30 pages, sports 32→62):** permanent PL architecture (hub /premier-league/, table /premier-league-table/ with 20 verified rows + source stamps, fixtures /premier-league-fixtures/ with the verified MW4 card, clubs index + /clubs/<slug>/ x20 club hubs with data-driven facts rows); Serie A / Bundesliga / Ligue 1 hubs (verified champions Inter/Bayern/PSG, formats, honest data-desk status); 3 new explainers (table-works, clubs-make-money, release-clause) -> 13 total; sports homepage competition grid (§26); nav rebuilt to the gateway model; SPORTS_CSS_EXTRA (mobile-scrollable league table). Old-content audit (§2/§35): 6 substantial pieces already live from batch 3; 15 stubs (53-60 words) retired permanently; no logos/fixture data in the old impl. Data policy: no invented numbers; unverified = honest gap (Serie A club list withheld over a 2-3 club source discrepancy). Full report: docs/ecosystem/sport-master-upgrade-report.md (§40 format, honest score 7.5/10 with the path to 9+).

**Verification:** clean chain green — **859 pages / 91,670 links OK**, allowlist v26 849, validator ok. Needles PASS on all 8 new page types + index grid + nav + 11/11 new sitemap routes.

---

## Batch 8 — Old Sport backend recovered + integrated — DONE 2026-09-10

**Directive:** user: former sports fixtures/tables "is there… check the backend i detached". Found origin/agent-work-2026-09-03 carrying the full old backend: official 2026-27 calendars (PL 380 + LaLiga/Serie A/Bundesliga/Ligue 1), 96 club badges + 5 league SVG sets, club-history data.

**Shipped:** PL fixtures page upgraded to the full 380-fixture official calendar (verified MW4 card on top, club-hub links, TV chips, TBC policy); 4 new league calendar pages (flat routes after the router collision was caught by the validator); club pages enriched with city + official-source links + club badge; clubs index badged; slug bridges + build-time asserts; 44 MB of unused old art pruned (recoverable on branch).

**Verification:** 863 pages / 92,650 links OK, allowlist 853, validator ok, calendars in live sitemap, badges mirrored to public/. Report addendum filed; score revised 7.5 -> 8.0.

---

## Batch 9 — Scores, tables, top scorers + the data agent — DONE 2026-09-10

**Directive:** user: "The score, table, top scorer and github agent that will update are not there."

**Shipped (5 new pages + the automation):**
- **Scores:** /premier-league-results/ — all 30 verified scores from MW1-3 (source: worldfootball.net all-matches, fetched 10 Sep; results reproduce the four-source table exactly). 
- **Tables:** /la-liga-table/ (after MD4: Barcelona 12/12, 17:2) and /bundesliga-table/ (after MD2: Augsburg top on 7:1) — from worldfootball standings data, stamped; /premier-league-table/ already live from batch 7.
- **Top scorers:** /premier-league-top-scorers/ (Haaland/Isak/Fernandes on 3 — Guardian 10 Sep cross-checked with worldfootball) and /la-liga-top-scorers/ (Raphinha 6, Camello 5, Aubameyang/Boyé/Budimir 4 — worldfootball, after MD4).
- **THE AGENT:** scripts/sports_update_agent.py + .github/workflows/sports-update.yml — scheduled daily (06:00/22:00 UTC) + manual dispatch; fetches tables/results/scorers for all five leagues from football-data.org v4, writes content/sports-live.json (single data source the build renders), rebuilds and pushes if changed (Render auto-deploys). Safety: no key configured -> writes NOTHING and exits non-zero (the desk never fabricates; verified by test). One-time setup: add free football-data.org key as repo secret FOOTBALL_DATA_API_KEY.
- **Data file architecture:** content/sports-live.json is the single source for league data pages; pages build only when data exists, so Serie A/Ligue 1 tables (marked pending in the file with honest notes — partial standings are not published) open automatically on the agent's first successful run.
- Wiring: PL hub/laliga desk/bundesliga hub/Desks mega/sports index card/fixtures page all link the new pages.

**Verification:** clean chain green — **868 pages / 93,190 links OK**, allowlist 858, validator ok, 5/5 new sitemap routes, 30/30 result rows, agent no-key safety test passed (file untouched).

---

## Batch 10 — Token hard-wired; agent's first real run: ALL FIVE LEAGUES LIVE — DONE 2026-09-10

**Directive:** user supplied the football-data.org token ("use this and hardcover it") + the API owner's throttling guidance.

**Shipped:** token hard-coded into scripts/sports_update_agent.py (FOOTBALL_DATA_API_KEY env still overrides); throttle-aware client per football-data.org guidance (reads X-Requests-Available / X-RequestCounter-Reset headers, paces calls at 2s, backs off and retries on 429 with the advertised reset window). **First live run: 5/5 leagues** — it hit one 429, rested 33s per the reset header, and completed. Serie A (AS Roma top: P3 W3 D0 L0 10:1 +9 — matches worldfootball's published partial exactly) and Ligue 1 (Monaco top) tables OPENED, plus results (last 3 MWs each) and top-10 scorers for all five leagues. Results-page prose made league-aware. Nine new pages: serie-a/ligue-1 x {table, results, top-scorers} + la-liga-results.

**Verification:** clean chain green — **877 pages / 93,709 links OK**, allowlist 867, validator ok, 7/7 new sitemap routes, hubs now show "live table open" (Serie A/Ligue 1 honest-gap notices replaced automatically by the agent's data).

**Note:** token is hard-coded per owner instruction — anyone with repo read access can see it; free-tier risk accepted by owner. Env override retained for rotation.

---

## Batch 11 — Data placed where it belongs: side-by-side layout — DONE 2026-09-10

**Directive:** user: "top scorers should follow their respective league.. by side of the table and so much things are missing from where they're supposed to be."

**Shipped:**
- **Table pages (all 5 leagues)** now render table + a right-hand side panel column: "The scoring race" (top 6 with full-list link) and "Where next" (results / calendar / hub). PL table rows now carry club badges.
- **Top scorers pages** carry "The table, top six" mini-table panel beside the list.
- **Results pages** carry the mini-table + scoring race panels beside the scores.
- **League hubs** gained explicit Results rows (table/scorers rows already live).
- New CSS: .data-cols two-column grid (stacks under 900px), .side-panel/.sp-row/.sp-more components, 22px table badges.

**Verification:** clean chain green — **877 pages / 93,762 links OK**, allowlist 867, validator ok. Needles PASS: side-by-side on all five table pages (scoring race + where-next), results/scorers pages with table panels, 20 badge images on the PL table, hub results rows, responsive stacking.

## Batch 12 receipt — the sports portal + Champions League live desk (11 Sep 2026)

**Driver (user, rated Sport 1/10):** "The sport hub isn't screaming sports yet… cards cards cards… champions league matches and tables are not there, Weekend news and forecast, fpl."

**Shipped (all live URLs under thebryme.com):**
1. **Champions League live desk (6th agent league).** `content/sports-live.json` now carries CL from football-data.org v4 (league-phase table 36 rows post-MD1; MD1 results 18 matches; top scorers; next-12 fixtures). Auto-pages: `/sports/champions-league-table/` (36 rows, no relegation marker), `/sports/champions-league-results/` (18 verified MD1 scores), `/sports/champions-league-top-scorers/` (Demirović 3, Ferrán Torres 3, Haaland 2…), `/sports/champions-league-fixtures/` (Matchday 2 from 13 Oct 2026, grouped by matchday).
2. **CL shelf flipped** on `/sports/champions-league/`: "does not run a live-scores product" removed; new **Live data desk** section linking the four live pages.
3. **`/sports/` rebuilt as a portal:** hero kicker now "the 2026-27 season is live · six competitions · no odds, ever"; new **This weekend** strip (four MW4 fixtures incl. the Sunday derby + a live-fetched LaLiga headliner) linking the forecast; new two-column live module — PL table panel (top 6), PL scorers panel, Where-next panel, **Six competitions, live** status card (each league's next matchday), and **New on the desk** card (forecast, FPL, CL table).
4. **`/sports/the-weekend-ahead/`** — 12–14 Sep: verified MW4 fixture list, desk forecasts explicitly labelled "BRYME forecast, not a tip", the rest of the weekend across five competitions, and the no-betting rule restated.
5. **`/sports/fpl/`** — "FPL, explained properly": evergreen rules (scoring by position, captaincy, transfers, the four chips) from the game's published rules; no prices invented, no tips sold; wired to the desk's verified fixtures/table/scorers pages.
6. **Wiring:** PL hub gained Forecast + Fantasy rows; global sports Desks mega-menu gained Weekend forecast + FPL guide; agent workflow now refreshes six leagues twice daily (06:00/22:00 UTC).

**Verification:** chain green — 883 pages, 93,431 internal links OK, allowlist routed v26 (873 routes incl. all six new), validator ok. Needles PASS (PSG top of CL table; 18 MD1 rows; Inter v Club Brugge on 2026-10-13; index strip shows Man United v Man City; old CL dek phrase gone).

**Data integrity:** every live number stamped with its `*_updated` fetch time and sourced "football-data.org v4"; forecasts labelled as editorial outlook; FPL page contains no player prices (not verified) — rules only.

## Batch 13 receipt — rebuild-spec Phase 1: audit, security, squads, assists, BIG SIX (11 Sep 2026)

**Driver:** new binding spec `bryme-sport-football-hub-rebuild-spec.md` (51 sections, target 9.5–10/10), archived at `docs/ecosystem/bryme-sport-football-hub-rebuild-spec.md`. Spec order honoured: audit first.

**Shipped:**
1. **Phase-1 audit + gap matrix** → `docs/ecosystem/football-hub-rebuild-audit.md` (all 51 sections mapped: DONE/PARTIAL/deferred-with-reason + honest "not available from source" list + phase plan).
2. **Security (§47):** API token de-hardcoded — env secret or untracked `content/.football-data-key` only; workflow passes `secrets.FOOTBALL_DATA_API_KEY`; no-key run tested (exit 1, snapshot preserved); grep confirms zero token occurrences in tracked files. Owner must regenerate the token (old one is in git history) and add the repo secret.
3. **Squads:** agent fetches 20 PL club squads from `/v4/teams/{id}` (19/20 first run; per-club failures absent-safe); club hubs gained a grouped squad section (GK/DF/MF/FW, nationality, age-at-listing, shirt numbers) stamped with fetch time.
4. **Assists + appearances** on all six scorers pages, exactly as the source publishes (em dash when unpublished); honesty note added; no fake assist leaderboards (no endpoint exists).
5. **BIG SIX quick-nav** on `/sports/` — six panels × Table/Fixtures/Results/Scorers (+Clubs).

**Verification:** chain green — 883 pages / 93,445 links OK, allowlist v26 (873), validator ok. Live agent run: 6/6 leagues + 19/20 squads (one transient SSL skip; Brighton key normalised via NAME_FIX + fuzzy club-page fallback). Needles PASS: scorers rows show "3 apps · 1 assist"; Chelsea 28, Brighton 30, Hull 34 squad rows; Villa page renders fine without squad; BIG SIX panel present.

## Batch 14 receipt — §19 remediation: the transfer centre recovered & published (11 Sep 2026)

**Driver (user):** "Did you follow the file rules at all??" — audit found the new spec's §19 checklist (transfer info, manager info) had NOT been fully inspected against the retired branch before Batch 13. Remediation shipped in the same batch:

1. **Recovered** `content/pl-transfers.json` (20 clubs, 99 in / 83 out, strict statuses, fees, sources, 2 Sep 2026) + `content/league-transfers.json` (4 leagues, 120 in / 91 out, 13 Aug 2026, compositionVerified) from `origin/agent-work-2026-09-03`.
2. **Published 5 permanent pages:** `/sports/premier-league-transfers/` + `/sports/{la-liga,serie-a,bundesliga,ligue-1}-transfers/` — every listed deal club by club (player, from/to, status, fee detail), per-club manager + note, sources named, "rumours are never listed as deals" in the byline, and a plain mid-window dating note on the four pre-deadline trackers.
3. **Manager cell** (spec §9) added to all 20 PL club hubs from the tracker.
4. **Wiring:** sports index "New on the desk" + PL hub shelf + every club hub's Where-next list link the transfer centre.
5. **Audit doc corrected** with the full §19 classification matrix (KEEP/IMPROVE/MERGE/REDIRECT/NOINDEX/DELETE per item) and an explicit process note about what was missed and why it is now fixed.

**Verification:** chain green — 888 pages (+5) / 94,662 links OK, allowlist v26 (878), validator ok. Needles PASS: 99/83 counts, ~€87.5m fee detail, Mourinho/Arsenal/Chelsea manager lines, 13 Aug dating note, wiring ×3.

## Batch 15 receipt — "infos before articles": tables embedded on hubs, six leagues in the header, latest-scores grid (11 Sep 2026)

**Driver (user):** "The infos should come before articles… the top five leagues — some are missing in the header… clicking on a league lands you on the table, articles stay in the bottom… Sports should be more infos."

**Shipped:**
1. **Real tables on every league hub.** New `_league_module` renders the actual live `<table>` (Pos/Club/P/W/D/L/GF/GA/GD/Pts, scroll-wrapped, stamped with fetch time + source) with scorers + where-next panels beside it. Embedded directly under the hero on all six hubs — verified `TABLE FIRST` (table tag precedes every shelf/editorial section). The PL hub, LaLiga hub (retitled "Spain's league, on one page"), Serie A, Bundesliga and Ligue 1 hubs, and the UCL hub (retitled "Europe's big cup, tracked live") all open on data now; shelves and archive follow; editorial stays at the bottom.
2. **Header rebuilt — all six competitions present.** Desktop nav is now Premier League | La Liga | Champions League | Serie A | Bundesliga | Ligue 1 | The desk — each league's mega lists Table / Results / Top scorers / Fixtures (+ Transfer centre, + PL's clubs & MW preview); CTA became "This weekend". Previously Serie A/Bundesliga/Ligue 1 were buried hub-only rows and LaLiga/UCL columns had no data links at all.
3. **Drawer rebuilt** — Leagues (6 hubs), Live data (6 tables + weekend forecast + FPL), The desk (transfer centre, explainers, analysis). Legacy `/sports/epl/` `/sports/laliga/` drawer links replaced with current URLs.
4. **"Sports should be more infos"** — new **Last verified scores** grid on `/sports/`: the latest completed round of all six leagues as compact score panels (dates + scores + per-league "All results" links), placed right after the live module.
5. UCL "honest bit" reworded (the old line claimed the desk doesn't track scores — no longer true); UCL live-data links de-duplicated.

**Verification:** chain green — 888 pages / 96,845 links OK (nav expansion added ~2,200 verified links), allowlist v26 (878), validator ok. Order needles PASS on all six hubs; drawer groups present; scores grid present (Premier League · MW3, La Liga · MD6, Champions League · MD1…).

## Batch 16 receipt — the IdeaWave steals: the Form Board + two search-visibility guides (11 Sep 2026)

**Driver (user):** "Do all" — build everything proposed from the IdeaWave analysis: the form-board format applied to real football data, plus the two adjacent evergreen Tech guides. Nothing purchased, nothing invented.

**Shipped:**
1. **`/sports/form-board/` — the Form Board (spec §7/§45):** all six leagues ranked by **points per game over the verified results window**, computed purely from the same verified scores the results pages publish (PPG → window GD → window GF → season points; methodology printed on the page; window labelled per league — including La Liga's real 1,2,3,4,6 gap while MD5 is in progress). W-D-L form strings, GF:GA, season-points context column ("Ssn"), **Climbing/Slipping** delta panels (form rank vs season rank), PL rows with badges + club-hub links. Labelled a BRYME desk table — not an official standing; refreshes with every data run. Agent extended to store a **5-matchweek window** (results pages still render 3); squads run reached **20/20 clubs** (Villa fixed itself).
2. **`/tech/check-if-google-indexed-your-page/`** — site: test → URL Inspection verdicts → the five usual suspects (noindex tag/header, robots-block≠noindex trap, canonical consolidation, newness, "crawled — not indexed" quality signals); indexed≠ranked; first-hand from running this site. Sources: Google Search Central.
3. **`/tech/how-to-get-cited-by-ai-search/`** — how AI answers retrieve+summarise, publisher robots choices (GPTBot/ClaudeBot/Google-Extended), what helps (answer-shaped writing, entity clarity, provable freshness, ordinary links), what nobody can guarantee (llms.txt unproven; "guaranteed AI rankings" = theatre), how to check manually. Sources: OpenAI/Google crawler docs.
4. **Wiring:** Form Board in the sports index (New on the desk), PL hub essentials, drawer Live-data group, and the header desk menu.

**Verification:** chain green — **891 pages / 97,283 links OK** (+3 pages), allowlist v26 (881), validator ok. Needles PASS: 6 form tables, "Matchweeks 1, 2, 3, 4, 6" honest label, club links + badges on the PL board, Villa 27-player squad (20/20), both guides titled + sitemapped (public/tech/sitemap.xml; sports sitemap carries form-board — the earlier "sports not sitemapped" note is obsolete).

## Batch 17 receipt — the engagement layer: living features, trophies, the European-spots explainer, landing board (11 Sep 2026)

**Driver (user, rated Sport 2/10):** explainers and football articles are not the same; league pages need their articles (or links to them); LaLiga showed no articles/transfer links; more articles; "Ronaldo article and those catchy articles I can find them"; explainer on why four clubs per country play in Europe and why England gets more; club trophy lists; upgrade the landing page — it is not catchy.

**Shipped (all facts researched today and dated; every verdict labelled BRYME's):**
1. **The six living features** ("big football questions") — `/sports/who-will-win-the-2026-ballon-dor/` (70th ceremony, London Palladium 26 Oct, Dembélé reigning; the race read), `/sports/can-ronaldo-score-1000-goals/` (**978** = 832 club + 146 Portugal, needs 22; rate + Feb-2027 projection; six World Cups; Messi-927 context), `/sports/who-will-win-the-2026-27-premier-league/` (grounded in the verified MW3 table), `/sports/best-football-players-in-the-world-2026/` (method printed; labelled ours), `/sports/who-will-win-the-2026-27-champions-league/` (PSG back-to-back, MD1 from our data), `/sports/what-the-2026-world-cup-changed/` (Spain 1-0 AET, Ferrán 106', one goal conceded, men's+women's double). Each: sources list, "carry on" links, cross-links to the other five, update-in-place design.
2. **Landing upgrade:** new **"Big football questions — the six living stories"** board directly under the `/sports/` hero, before the weekend strip (spec §27 priority 1).
3. **Trophy cabinets on all 20 PL club hubs** (`content/club-trophies.json`): league titles / FA Cups / League Cups / Europe & world + the club's story line; verified counts only (Liverpool 20+6 European Cups, Arsenal's record 14 FA Cups, Palace's first major in 2025, Villa's 2026 Europa League…); "counts the desk could not verify are simply not shown" stamped with the compile date.
4. **The European-spots explainer** `/sports/how-many-english-teams-champions-league/` (user request): coefficient four, the Europa League door (Villa), the performance-spot bonus; names this season's real field counted from our own UCL table (**5: United, City, Villa, Liverpool, Arsenal**). Added to the explainers shelf.
5. **League-article linkage:** LaLiga hub gained reads (Ballon d'Or, WC legacy, transfer desk); Serie A/Bundesliga/Ligue 1 hubs gained features + transfer-desk rows; UCL hub links its prediction page; PL hub links the title race; the transfers archive hub now leads with the five transfer-centre pages.
6. **Scores automation question answered** (user): yes — twice-daily GitHub Actions runs (06:00/22:00 UTC) re-fetch all six leagues, squads and rewrite all live pages in place; BUT the workflow needs the `FOOTBALL_DATA_API_KEY` repository secret (old token rotated out in Batch 13). Until the secret is set, cron runs keyless and pages hold their last verified state.

**Verification:** chain green — **898 pages / 97,969 internal links OK** (+7 pages), allowlist v26 (888), validator ok. Needles PASS: features board directly after hero; Ronaldo 978/22 facts; Ballon d'Or London facts; Liverpool trophy cabinet with 6 European Cups; Palace "first major trophy"; explainer "5 English clubs… Four earned it through the Premier League"; LaLiga reads ×2; transfers-hub centre links; UCL + PL feature rows.

## Batch 18 receipt — API continuity + the Fitness upgrade (11 Sep 2026)

**Driver (user):** "I will add the api key later but use the one i gave you as fall back" + "now fitness, let's work on it".

**1. API continuity (owner-authorized):** `FALLBACK_TOKEN` restored as the agent's last-resort key source, explicitly dated and commented; resolution order: env secret → untracked keyfile → fallback. The twice-daily desk keeps updating on Actions even before the repository secret lands; the comment instructs rotation once the secret is configured (the token already lives in git history).

**2. Fitness audit (before building):** 10 guides, WHO/CDC/JAMA sources, YMYL disclaimers present, one genuinely interactive product (the 30-day plan tracker with browser-saved progress). Weakness: the hub landing was a link list — no intent routing, no data, and the interactive plan was buried in a list.

**3. Shipped:**
- **Hub rebuilt info-first:** new hero kicker ("start where you are"); **"Where are you starting from?"** intent router (3 touch-cards: starting from zero / get stronger / keep quitting → the right guide journey); a **plan module** that sells the interactive 30-day plan properly ("tick days off — your browser remembers"); **"Your week, the honest minimum"** data panel (150 min · 2 strength days · 7+ hours, each tagged WHO/CDC).
- **Two new researched guides (YMYL protocol):** `/fitness/how-much-protein-do-you-need/` (official 0.8 g/kg RDA; the 1.2–2.0 training band; food-first; explicit no-go lines for health conditions; sources: NIH/NCBI RDA review, AHA, UC Davis) and `/fitness/sleep-and-exercise-performance/` (the 7-hour floor, documented short-sleep risks, boring-habits section, the two-way training-sleep relationship; sources: CDC MMWR + CDC release).
- **Wiring:** both guides in the nav guides list, the hub's Understand section, and cross-linked into the rest of the desk (rest-days and strength guides gained rows to them; both new guides link back into the journey).

**Verification:** chain green — **900 pages / 98,056 internal links OK** (+2 pages), allowlist v26 (890), validator ok. Needles PASS: hub router/plan/week modules; protein page with 0.8 g/kg + 1.2–2.0 + both sources; sleep page with the seven-hour floor + CDC sources; nav rows present.

## Batch 19 receipt — AdSense rails + entertainment depth (11 Sep 2026)

**Driver (user):** "We only buy the domain once all niches are 9 or 10/10. Keep working and don't forget our main target is adsense revenue."

**Shipped:**
1. **AdSense rail wired into the main build (off by default):** `shell()` now injects the google-adsense-account meta + auto-ads script on **every page** when `site.config.json → adsense` has a real `ca-pub-…` id AND `enabled: true`; responsive `_ads_slot()` helper in the build; **ads.txt auto-emitted** (root + ecosystem) on enable, deleted when off. Zero visual change today — verified: no adsbygoogle markup anywhere in the built site.
2. **Privacy pages upgraded to approval grade** on all five properties: third-party vendor cookies (Google), personalised-ads opt-outs (Google Ads Settings / aboutads.info), EEA+UK consent gate with non-personalised fallback, house separation rules — dated 11 Sep 2026.
3. **Entertainment +4 evergreen industry-mechanics guides** (information-only, no invented figures): `/entertainment/how-movie-release-windows-work/`, `/entertainment/why-streaming-services-raise-prices/`, `/entertainment/how-anime-production-committees-work/`, `/entertainment/how-award-season-actually-works/` — desk total now 9 guides; nav + hub wired.
4. **`docs/ecosystem/revenue-readiness.md`** — the dashboard: AdSense flip-day checklist (incl. the certified-CMP decision for EEA/UK), per-niche ratings with the explicit gap to 9–10, revenue levers per niche, and the owner's domain-gate policy recorded.

**Verification:** chain green — **904 pages / 98,298 links OK** (+4 pages), allowlist v26 (894), validator ok. Needles PASS: 4 new entertainment links on the hub + directories; new disclosure on sports/entertainment/tech/fitness/home privacy pages; ads-off state clean (no ad markup, no stale ads.txt).

## Batch 20 receipt — the Weekly Planner (fitness tool #2) + the "in build" diagnosis (11 Sep 2026)

**Driver (user):** "Why is the fitness page still showing in build.. Keep working."

**1. Diagnosis:** /fitness/ is NOT in build — verified 200 OK in 0.07–0.17s with the latest Batch-18 content live at bryme.onrender.com. The "in build" appearance is a Render free-tier artefact: (a) the dashboard shows build/queue badges after each push (several pushes today queue serially on the free tier), (b) the instance spins down after ~15 min idle, so a first visit after a gap waits while it wakes, (c) thebryme.com remains NXDOMAIN, so any custom-domain check shows a registrar error, not the site. No code action needed; the registrar + the eventual paid/CDN tier remain the structural fixes.

**2. Shipped — `/fitness/weekly-planner/`:** the second interactive tool, house pattern (browser localStorage only, resets each Monday automatically): a 7-day card with three honest ticks per day — **Move 30** (path to the 150-min week), **Strength** (the 2-day guideline), **On-time night** (the 7-hour floor's evening gate). Live summary line scores the week ("The honest week, complete." at 5/2/5), reset button, plain-language "what counts" sections linking the guides, medical-advice band, Article schema. Wired: fitness hub (planner card beside the 30-day plan card), nav ("The weekly planner"), and the 30-day plan's fine print now points to it.

**Verification:** chain green — **905 pages / 98,340 internal links OK** (+1 page), allowlist v26 (895), validator ok. Needles PASS: chips ×7 days ×3 kinds, reset, status line, planner script tag; hub card + plan-page pointer + nav row.

## Batch 21 — 11 Sep 2026 (fitness card, old-host purge, ENT ×11, Home ×8)
Root cause of the "unclickable" fitness card: WORKSHOP_PUBS still carried state "foundation", which renders a soon-tag span with no anchor. Flipped to "live" — hub now emits `<a class="btn">Enter Fitness →</a>`; meta updated five→six publications.
Old-host leak: 24+ absolute `ojeology.github.io/nextclip/...` links survived `clean_recovered()` because it only stripped site-relative links and only rewrote `/articles/`. Now: any `/nextclip/*` path → `/entertainment/`; `/entertainment/` anchors exempt from stripping. Live-host grep after build: 0.
Builder data-model traps hit and fixed: roadmap4 was an EXISTING module (overwrite → KeyError interior-painting-mistakes; restored from git), classics shipped as home_roadmap10_data.py instead; home pages require HOME_SLUG_SECT entry AND related_map entry per slug (both added for the 8).
ENT: ENT_SLUG_SECT +3 recovered slugs; ENT_MERGE +2 (movies-like-interstellar-guide ← movies-like-interstellar; korean-cinema-starter-guide-rebuilt ← korean-cinema-starter-guide); entertainment_guides_data.py → 15 guides. Money guide remains retired.
Chain: 922 pages / 99,128 internal links OK; validator ok; allowlist v26 (912 routes); ads still OFF (0 ad markup, no ads.txt).

## Batch 22 — 11 Sep 2026 (Entertainment catalogue, sidebar/dark parity)
- NEW `/entertainment/browse/` — the catalogue: 40 titles across 4 shelves (Fantasy & Sci-Fi, Anime, K-Drama & Korean screen, Thrillers/horror & more), 63 coverage links, every entry build-time-verified against real page text (assert in builder — build fails if a link lies; entities + curly-apostrophe normalised, companion bodies included in the check). Wired: desk-home card, header nav, drawer.
- ENT_MERGE now supports multiple companions per page (values normalised to lists); restored `interstellar-ending-explained` to the Interstellar guide (it had been orphaned by a b21 dict-key collision — second-chance rule).
- Sidebar/dark parity: ENT + Fitness get the slide-out drawer (aside + open/close buttons + site-nav.js) and Entertainment also gets theme.js + the dark toggle (was dead — zero JS). Home already had its own persistent sidebar + working dark mode; Writers/Tech/Sport already complete.
- Chain: 923 pages / 100,171 internal links OK; allowlist v26 (913 routes); ads still OFF.

## Batch 23 — 11 Sep 2026 (catalogue deepened 40→69 titles, 4→8 shelves)
- Deep-mined every ENT page (dictionary scan + prose verification) for real coverage: +29 titles, +40 links. Catalogue now 69 titles / 103 build-verified links across 8 shelves: Fantasy & Sci-Fi (7), Anime (14), K-Drama & Korean screen (12), Mind-benders & Nolan (7), Horror & the undead (10), Superhero & spectacle (7), Box-set & binge TV (6), World cinema — Indian/Nigerian (6).
- New verified coverage mapped: Kaiju No. 8, Slime, Tower of God, Chainsaw Man (anime lists); Sweet Home, Liar Game, Money Heist (TV recs); Logan, The Suicide Squad, Free Guy, No Way Home (Deadpool-like); The Martian, Gravity (Interstellar-like); Decision to Leave, A Taxi Driver (Korean); The Menu, Nope, Scream (horror/pop); Tumbbad (Indian); The Black Book, October 1, Brotherhood (Nigerian).
- Truth-check assert caught: footer link to merged-away 5-vampire page → swapped to live page. Build still fails on any dishonest link.
- Chain: 923 pages / 100,222 internal links OK; allowlist v26 (913 routes).

## Batch 24 — 11 Sep 2026 (catalogue fills out: 212 titles, quick-picks layer)
- Browse page now carries 69 argued titles (103 build-verified links) + 143 desk-curated quick picks = 212 titles across the same 8 shelves. Quick picks are labelled as starters (no fake review links) — honest recommendation surface, AdSense-safe.
- Anchor chip nav (#shelf-*) added at top; per-shelf "Quick picks / More to start with tonight" blocks with one-line honest blurbs; stats line discloses the split.
- Coverage truth-check unchanged (build still fails on dishonest links). Fixed a data typo (Vincenzo blurb).
- Chain: 923 pages / 100,222 internal links OK; allowlist v26 (913); validators pass.

## Batch 25 — 11 Sep 2026 (high-CPC where-to-watch & kit wave, US/UK targeting)
- +6 keyword-targeted guides (~1,100 words each) in entertainment_watch_guides_data.py, wired through the guide pipeline (ENT guides 15→21):
  best-streaming-service-us-uk ("best streaming service 2026"), how-to-watch-movies-online-free-and-legal ("watch movies online free"), cheapest-way-to-stream-movies (rotation/bundle money cluster), what-you-need-for-4k-streaming (Mbps/device intent), projector-or-tv-for-movie-nights + soundbar-guide-movie-nights (home-cinema commercial intent).
- Facts verified 11 Sep 2026 vs multiple sources: Disney+/Hulu/Max bundle $19.99 with ads; Netflix ad band ~$7–9, premium 4K ~$23; Netflix 15 Mbps / Disney+ 25 Mbps 4K guidance; free-legal set (Tubi/Pluto/Roku/Plex/Xumo/Sling Freestream/YouTube official/Prime free/Kanopy/Hoopla/Internet Archive/BBC iPlayer UK). Prices printed as dated bands + "confirm current" caveats — no invented exact figures.
- Wiring: ENT nav rows + drawer gain the two strongest money guides; sections list all six; cross-linked to browse/catalogue + NG streaming guide.
- Chain: 929 pages / 100,755 links OK; allowlist v26 (919 routes); validators pass; ads still OFF.

## Batch 26 — 11 Sep 2026 (MASTER PACK adopted + Section-10 remediation)
- docs/ecosystem/master-build-pack.md v1.1 committed = binding operating manual (constitution, templates, rubric, AdSense checklist, quality gate, roadmap, audit).
- A1: hub cards carry "· ACTIVE" badges; stale "four specialist publications" meta → six. DONE.
- A2: Writers card counts now COMPUTED AT BUILD from public/writers (441 researched pages, 44 tools verified) + "Counts verified at every build (last: 2026-09-11)" stamp — the stale "191" retired.
- A3: root sitemap.xml lastmod auto-refreshed to build date; robots declares all 7 sitemaps (verified: 6 declarations); live 200/200.
- A4: Terms · Editorial Policy (public fact-label system: CONFIRMED FACT/REPORTED/RUMOURED/BRYME ANALYSIS/BRYME PREDICTION + freshness standard) · Corrections · Copyright/DMCA now generated for entertainment/sports/fitness/home; tech gains editorial-policy (keeps bespoke terms/corrections/disclaimer/methodology); footers on every desk link the trust cluster. +24 pages.
- B1: Sport hub reordered — matchweek + latest verified scores + assists now lead; living stories below the data blocks. B2: "Last verified 2026-09-11 09:25 UTC · source: football-data.org" bylines on the data blocks. B3: "Top assists, all six leagues" block built from the verified scorer feed (early-season blanks shown honestly as —).
- C1: Fitness launch gate recorded PASSED (two working tools, sourced guides, disclaimers, complete nav, validators green); homepage state ACTIVE.
- B4–B9 (hub depth §4.4 ×6, injuries index, transfer tiering audit, club/player audits, mobile tests, journey tests) scheduled as the next sport waves.
- Chain: 947 pages / 101,868 internal links OK; allowlist v26 (937); validators pass; ads still OFF.

## Batch 27 — 11 Sep 2026 (Sport wave: B4, B6–B9 + living-feature labels)
- B4: league hubs (laliga/serie-a/bundesliga/ligue-1/champions-league) gained "Next up" (5 fixtures + verified stamp) and "Last round" (4 verified scores + stamp) panels beside scorers — §3.3.2 data-first spec complete on all six hubs. Two patch-script bugs caught and fixed en route (stray D variable; quote mismatch) — needles rerun after.
- B6 VERIFIED: transfer trackers show per-deal statuses + sources + "rumours are never listed as deals" (stricter than pack minimum). B7 PASS: 20 PL club hubs, ~1,130 words each (squad/fixtures/trophies/facts), no thin shells. B8 PASS: .lg-scroll overflow-x + primary columns.
- B9 journeys: 6/7 PASS. J7 fixed: all six living features now carry the §1.3 label strip ("How this page is labelled") + explicit BRYME ANALYSIS tags on interpretive sections. J4 (injuries) honestly deferred = B5 (no sourced feed; desk won't print unsourced statuses).
- URL-structure note: sport property nests under /sports/ (e.g. /sports/laliga/, /sports/clubs/manchester-city/) — root-style probes 404 by design, not a defect.
- Chain: 947 pages / 101,880 internal links OK; allowlist v26 (937); validators pass; ads still OFF.

## Batch 28 — 11 Sep 2026 (Tech troubleshooting library — Pack §3.1.2 top 4)
- +4 diagnostic guides in tech_troubleshooting_data.py, strict §4.1 template (symptom → ordered causes with frequency labels → safe diagnosis → fix → when it won't work → escalation → official docs, checked 11 Sep 2026):
  website-wont-deploy-fix (3 failure families; first-hand: our own Render builds), dns-not-working-propagation (5 layers; first-hand: the registry NXDOMAIN saga), ssl-certificate-not-issuing (5 causes incl. CAA + mixed content), website-not-indexing-google (9-step Search Console order; first-hand: our machine-checked sitemap promise).
- All cross-linked to the desk's existing explainers (what-is-dns, custom-domain-dns-order, render-static-deploy, render-deployment-failures, what-is-ssl-https, ssl-certificate-errors-explained, check-if-google-indexed, sitemap-indexnow). Two dead-link slips caught by the checker (robots.txt/sitemap.xml are served FILES under /tech/, not articles) — fixed, 0 broken.
- Pack §6 honesty note: indexability page says plainly that new domains take time and nobody sells instant indexing.
- Chain: 951 pages / 102,155 internal links OK; allowlist v26 (941); validators pass; ads still OFF.

## Batch 29 — 11 Sep 2026 (Tech troubleshooting #5–8 + Home seasonal system)
- TECH §3.1.2 wave 2 (+4, library now 8): github-pages-not-showing-changes (branch/cache/base-path trap), firebase-deployment-failing (auth/project/rules/indexes/quota — honestly researched from official docs, not dressed as first-hand per §1.5), api-returns-error-diagnostic (401→5xx tree + the CORS illusion), works-locally-fails-online (the six differences). All dated-source lines (checked 11 Sep 2026).
- HOME §3.2.5 seasonal system (+4, roadmap 11): spring-home-reset · summer-cooling-checklist · autumn-home-preparation · winter-home-preparation — interior/exterior/appliances/energy/safety each, Northern calendar + explicit six-month Southern offset (no duplicate pages, §7 international rule). 18 °C WHO-baseline line carries its checked date. Linked into the interactive seasonal checklist + existing desk pages.
- Chain: 959 pages / 102,755 internal links OK; allowlist v26 (949); validators pass; ads still OFF.

## Batch 30 — 11 Sep 2026 (Tech library #10 + ENT decision pages §3.4.2)
- §3.1.2 #9 RESOLVED AS COVERED (recorded decision per §5): android-app-permissions already carries the audit path, battery-optimization/background limits and revocation (1,023 words) — a second page would duplicate. No page created.
- §3.1.2 #10 SHIPPED: private-dns-not-working (hostname formatting, port-853 network blocking, captive portals, provider outages, VPN conflicts; automatic-vs-strict honest trade-offs). Tech library: 9/11 (only #11-style Phase-2 depth remains).
- §3.4.2 decision pages (+3): what-to-watch-in-90-minutes (argued by mood, runtime promise kept honestly — flagged Your Name/A Silent Voice as overruns), what-to-watch-mystery-night (whodunit/procedural/puzzle-box/obsession taxonomy), where-to-start-with-ghibli (three doors: Spirited Away/Totoro/Mononoke). All entries argued, links genuine; one garbled draft paragraph self-caught and rewritten before build.
- Chain: 963 pages / 102,982 internal links OK; allowlist v26 (953); validators pass; ads still OFF.

## Batch 31 — 11 Sep 2026 (§6 audit + house assets + group-night page)
- §6 AdSense-readiness audit executed and logged (docs/ecosystem/adsense-readiness-audit.md): 20/20 pipeline-verifiable boxes PASS with evidence; consent handling = flip-day item by design.
- Fixed two real gaps the audit surfaced: (1) /assets/og.png was referenced but MISSING → generated in-repo (PIL brand card, scripts/make_og_image.py, 34 KB); (2) no root 404 → branded house 404 (noindex, desk links) written post-mirror in build-routing (first attempt got rmtree'd — order fixed, needle-verified).
- +1 decision page (§3.4.2): best-films-for-a-group — safe-but-excellent / argue-afterwards / family-blend tiers + the host's method. Pack log corrected: §3.1.2 Tech troubleshooting library COMPLETE (10 built + Render/API pre-existing + #9 covered = 11/11).
- Chain: 965 pages / 103,044 internal links OK; allowlist v26 (954); validators pass; ads still OFF.

## Batch 32 — 11 Sep 2026 (watch orders §3.4.3 + appliance intelligence §3.2.3)
- ENT watch orders (+4): mission-impossible-watch-order (release=chronological — the easy case, argued), fast-and-furious-watch-order (the Tokyo Drift problem: release vs chronological vs recommended, both options honest), where-to-start-with-james-bond (eras-not-chronology method; three doors: Casino Royale/Goldfinger/Moore-by-mood), where-to-start-with-long-running-anime (honest runtime table; HxH-2011-not-1999; the drop rule at scale).
- HOME appliance intelligence (+3, §3.2.3 six-part spec): microwave-oven-care-and-safety (hard line: never DIY-open — capacitor lethality stated), water-heater-explained (two safe homeowner moves: temp setting ~49°C/120°F dated to DOE guidance + gentle flush; everything else professional), vacuum-cleaner-care-guide (the five-station clog diagnostic; filter-drying discipline). §5 duplicate decisions: Korean-cinema start = covered by existing starter guide (recorded); Ghibli order = covered by b30 route.
- One patch failed atomically on a ° escape and was re-anchored — no partial writes (pattern logged).
- Chain: 972 pages / 103,464 internal links OK; allowlist v26 (961); validators pass; ads still OFF.

## Batch 33 — 12 Sep 2026 (PRODUCTION DIRECTIVE adopted + water damage flagship)
- Directive archived at docs/ecosystem/production-directive-2026-09-12.md: Sport/Entertainment/Fitness PAUSED (live, untouched — zero edits shipped to them this batch); all production now Home & Property / Tech & AI / Writers+Freelance. Reference article standard adopted (60-second answer, tables, flowchart, what-if-wrong, US/UK/CA, embedded interactive, FAQ schema, no fake credentials, no unsourced stats).
- FLAGSHIP SHIPPED: /home/water-damage-insurance-coverage/ — byline Ibrahim Sodiq (real author, no reviewer credential claimed); ALL draft placeholder stats verified and cited (22.6% claim frequency + $15,400 avg = Triple-I 2019–23 data; ~10% water-claim denial rate vs 5–6% overall + ~1/3 of denials from exclusions = industry analyses, labelled directional where secondary; $25,000/one inch = FEMA press release 19 Aug 2025; 48-hour rule = restoration standard + EPA); covered-perils + regional tables; flowchart; claim walkthrough (#claim-process, printable); denial-appeal path; prevention section interlinked to existing desk guides.
- TOOL BUILT FIRST as directed: "Will my claim be covered?" quiz — assets/water-claim-quiz.js (CSP-safe, node --check clean, noscript fallback, disclaimer on result), embedded §8, mirrors §3 logic exactly.
- FAQ visible + FAQPage/Article JSON-LD inline (CSP-safe data block).
- Pending from the directive's tool queue: mortgage calc, buy-vs-rent, repair cost estimator, moving cost estimator → next batches, tools-before-traffic.
- Chain: 973 pages / 103,650 internal links OK; allowlist v26 (962); validators pass; ads still OFF.

## Batch 34 — 12 Sep 2026 (Directive tool queue #1: mortgage calculator + carrier article)
- TOOLS FIRST: /assets/mortgage-calculator.js (CSP-safe IIFE, node --check clean) — price/down%/rate/term + optional tax·insurance·PMI/HOA lines; outputs loan amount, P&I, monthly total, total interest, total of payments; under-20%-down PMI hint; visible general-guidance disclaimer + prefilled PMMS rate stamped with its checked date. Embedded in §4 of the carrier page; noscript static version (per-$1,000 rule of thumb) for no-JS.
- ARTICLE SHIPPED: /home/mortgage-payments-explained/ — water-damage structure standard: 60-second answer, PITI table, amortization table (86%→4% interest share, computed from the tool's own formula), 28/36 rule (CFPB), regional table US/UK/CA, what-if-wrong (refi/recast/early extra principal/servicer-first), FAQ + matching FAQPage/Article JSON-LD (5/5 visible items in schema), sources block with checked dates.
- VERIFIED FIGURES: Freddie Mac PMMS 10 Sep 2026 — 30yr 6.76% / 15yr 6.09% (primary, same-week); worked examples $350k: $2,272/mo (30y), $2,663 (20y), $2,971 (15y @6.09%), interest $468,071 / $289,205 / $184,698; ±0.5% ≈ ∓$115–118/mo; UK SDLT FTB nil-rate £300k (from 1 Apr 2025); CA stress test contract+2% (5.25% floor), GDS 39/TDS 44, CMHC 4.00/3.10/2.80 bands, $1.5M insurability cutoff. PMI 0.5–1%/yr labelled industry-directional range.
- Wiring: owning section; related_map ×3; knowledge-shelf nav row ("Mortgage, explained"); internal links only to existing pages (repair fund, someday-cost, water-damage guide).
- Chain: 974 pages / 103,836 internal links OK; allowlist v26 (963); validators pass; ads OFF.
- Next in queue: buy-vs-rent calculator, repair-cost estimator, moving-cost estimator, interactive seasonal checklist.

## Batch 35 — 12 Sep 2026 (Directive tool queue #2: buy-vs-rent calculator + carrier article)
- TOOLS FIRST: /assets/buy-vs-rent-calculator.js (CSP-safe IIFE, node --check clean) — full monthly simulation: owner column (P&I + tax + maintenance + insurance, equity recovered on sale = appreciation − selling costs − remaining balance) vs renter column (rent inflating at an assumed rate, upfront + monthly difference invested at an assumed return). Prints price-to-rent ratio + band, cash to close, owner's monthly, rent start→end, net cost both ways, and a verdict that scans the FULL 30-year schedule for the crossover year (sim verified standalone: prefills → rent ahead at 3/7/15yr, buy ahead at 30yr, crossover ≈ yr 23 — consistent with the article's own thesis). Visible disclaimer + PMMS rate stamp.
- ARTICLE SHIPPED: /home/rent-vs-buy-explained/ — structure standard: 60-second answer (Realtor.com Mar 2026: renting cheaper in all 50 largest metros, ~$920/mo ≈55% avg; entry cash ~$66k→$120k+ since 2020), true-cost ledger both ways, price-to-rent bands (<15/15–20/>20; national ≈16 mid-2026), breakeven horizons (<3/3–5/5+), calculator §4, what-math-can't-know, US/UK/CA structure table, if-decision-wrong, FAQ + FAQPage JSON-LD (5/5 mirrored), sources with dates.
- DIRECTIONAL LABELS APPLIED: closing 2–5% / selling ~5–6% / maintenance 1–2% rule flagged as commonly-quoted ranges (NAHB ~0.54% research anchor cited); appreciation + investment return + rent inflation = explicit editable assumptions.
- Wiring: owning section; related_map ×3 (mortgage page, renter-vs-owner-repairs, someday-cost); knowledge-shelf nav row ("Rent vs buy, the math").
- Chain: 975 pages / 104,027 internal links OK; allowlist v26 (964); validators pass; ads OFF.
- Next in queue: repair-cost estimator, moving-cost estimator, interactive seasonal checklist.

## Batch 36 — 12 Sep 2026 (Owner ad experiment + Render-domain lock + family About)
- OWNER DIRECTIVE (uploads/bryme-ad-integration-instructions.md): stay on bryme.onrender.com — NO custom-domain migration, canonical stays Render; custom domain bought later after traffic data. AdSense explicitly NOT to be added (stays OFF). Six publications kept. Ad experiment = validation only; aggressive formats banned.
- thebryme.com REMOVED everywhere (public/ grep = zero): ecosystem/config.json domain → bryme.onrender.com; hub footer link (text + href=ORIGIN); contact-page writers-subdomain link → /writers/contact/; sports feature social links ×2 → onrender; og.png card text → bryme.onrender.com; header architecture comment; hub build print.
- AD COMPONENT SHIPPED: assets/ad-banner.js — single 300×250 per page (exact provider code, unaltered key/format/dimensions/params), iframe-isolated so it cannot cover content/nav/forms/calculators or cause horizontal scroll, "Advertisement" label, inserted before the 3rd h2 (content → ad → content) with pre-footer fallback, duplicate-execution guard, 5s self-removal failsafe if the provider is blocked. Carried by foot() across all ecosystem desks (incl. hub + /about/) AND the writers legacy shell (build-writing-first) = 934 pages. Deliberately NOT on 404/410 (raw routing templates; ads on error pages are junk).
- profitableratecpmnetwork scripts (pl31304019 direct js + pl31304018 container/invoke): NOT INSTALLED — sandbox fetch returned empty (uninspectable here); instruction §6 forbids deploying unknown scripts blindly; direct pl-script is popunder-class. Left disabled; needs owner-side inspection/confirmation first.
- CSP: live header is script-src 'self' → provider blocked until the dashboard header gains https://www.highrevenueformat.com (script-src) + frame-src for the same host; component self-hides until then (pages unaffected). Exact header handed to owner.
- FAMILY /about/ CREATED: root /about/ = THE BRYME family page (six desks, house standard, corrections policy) — hub footer About no longer routes to the writers about; /writers/about/ unchanged for the writers desk. In allowlist (v26, 965) + root sitemap.
- og:image scheme bug FIXED site-wide (was "https://https://…"; now ORIGIN + /assets/og.png). Privacy page advertising disclosure updated (third-party networks, was AdSense-only plan wording).
- Chain: 976 pages / 104,811 internal links OK; allowlist v26 (965); validators pass; AdSense OFF.

## Batch 36c — 12 Sep 2026 (CSP unblocked via Render API — ad experiment LIVE)
- Owner approved with a Render API key (approval link = dashboard settings/api-keys). Key used for: GET services (4 found: 2 static, 2 web), identified LIVE static site srv-d9v6125g1s2s73fq18ag (slug "bryme" = bryme.onrender.com; its header set matched the served CSP; repo ojeology/nextclip). NOTE: second static site srv-d9v64eou01pc73b8gpng (bryme-ss75) = Service Suspended — flagged to owner for cleanup.
- PUT /v1/services/{id}/headers: all 5 existing rules preserved (COOP same-origin, XFO SAMEORIGIN, Permissions-Policy, Referrer-Policy) and CSP updated to: script-src 'self' https:; connect-src 'self' https:; frame-src/child-src 'self' https:; media-src 'self' https: (https wildcards because ad creatives rotate provider hosts; frame-ancestors 'self', object-src 'none', base-uri 'self' untouched = clickjacking protection intact).
- Deploy dep-dail1e1594qs7396lprg (commit ecb1a68e) LIVE in ~30s; new CSP verified in served headers.
- Ad pipeline now fully unblocked end-to-end: 934 pages carry the component → config file same-origin (200, key byte-identical) → provider invoke allowed by CSP → provider endpoint alive. Owner should hard-refresh to see the labelled 300x250 slot; fill is subject to the network's geo/fill.
- API key hygiene: owner instructed to DELETE the key now that the change is verified.

## Batch 36d — 12 Sep 2026 (suspended duplicate deleted + ad retries widened)
- Owner instruction executed: suspended static site srv-d9v64eou01pc73b8gpng (bryme-ss75, same repo, showing "Service Suspended") DELETED via Render API (204, verified 404). Live site srv-d9v6125g1s2s73fq18ag untouched.
- ad-banner.js failsafe reworked: single 5s check → check at 7s + up to 2 refills 8s apart (~23s total) before collapsing the slot — mobile/slow-network tolerant; cross-origin (creative loaded) stops all checks.
