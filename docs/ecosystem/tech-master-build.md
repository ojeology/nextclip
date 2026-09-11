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
