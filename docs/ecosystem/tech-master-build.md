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
