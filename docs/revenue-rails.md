# Revenue rails — the plan that waits its turn

**Sequencing rule (Part H, unchanged):** audience → commercial demand → monetise. Nothing in this document activates anything. It exists so that when the gates flip, they flip in the right order with the disclosures already in place.

## Current status (7 September 2026)

- No ads, no affiliate links, no paid placements — stated publicly at [/disclosure/](/disclosure/).
- `site.config.json` → `affiliate.enabled: false`. The per-article disclosure note renders automatically on any guide tagged `affiliate: true` **only** after that gate is on.
- AdSense: `caId` empty, disabled — application follows the custom domain.

## The activation order, when the time comes

1. **Custom domain live** (checklist: `docs/custom-domain-migration-checklist.md`).
2. **Traffic floor** — the 2–4-week GSC re-pull (already queued) shows which guides earn attention. Monetise attention that exists; do not pre-monetise pages nobody reads.
3. **Programme accounts opened and terms read** — programmes change terms; verify at signup, not from memory or third-party blogs.
4. **Links inserted per the placement rules below**, guides tagged `affiliate: true`, `affiliate.enabled: true` → the disclosure notes appear automatically.
5. **Disclosure page updated** to name the actual programmes (the page promises this explicitly).
6. **AdSense application** — ads stack on a site whose trust pages (disclosure, editorial policy, corrections log) already exist.

## Candidate inventory (to evaluate, not to assume)

| Guide cluster | Candidate programmes | Honest-fit note |
|---|---|---|
| choosing-a-grammar-checker, choosing-ai-writing-tools | Grammarly, ProWritingAid | Only the tests in the guide decide rank order; free tier often wins — say so |
| accounting-software, invoicing-software | FreshBooks, QuickBooks, Xero | Writer-scale framing: sole traders rarely need enterprise tiers |
| payment-platforms-for-writers, cross-border-writing-business | Wise, Payoneer | Highest Layer-B relevance on the site; fees-vs-spread honesty is the article's whole point — links must not soften it |
| choosing-pdf-and-document-tools | Adobe, PandaDoc | Free-tier-first guidance already in the article |
| project-and-client-tools | Notion/alternatives | weakest fit; only if terms + fit survive evaluation |

Every programme's existence, terms and commission structure must be verified at its own partner page when the account is opened — none are asserted here.

## Placement rules (the Part H contract, operationalised)

1. Links live **inside comparison tables and step lists where the tool genuinely wins on the guide's stated criteria** — never in the verification record, opportunity pages, or status labels.
2. **Free-first**: if the free option serves the writer, the free option is the recommendation; the paid link sits beside it, marked.
3. **Marked in context** ("the paid plan", "commission if you subscribe") — not bare URLs, not footnote confessions.
4. Any guide carrying a money link gets `affiliate: true` → the top-of-article note appears. No exceptions, no "small ones".
5. Old articles are never retro-linked without a re-read and re-verification date bump.
6. **The Layer-B trust line is the moat**: the moment an opportunity listing or rate figure could be bought, the site is done. Nothing in this plan touches the record.

## Compliance checkpoints (verify current guidance at launch)

- US: FTC material-connection disclosure (clear, conspicuous, before the link).
- UK: ASA/CAP rules for affiliate content — same spirit, check current wording.
- Privacy page gains an affiliate/cookies line before any tracking-bearing link ships.

## What this batch shipped

- `/disclosure/` — the public commitment (indexable, linked from the footer Legal column).
- The config gate + `affiliate_note()` component + front-matter wiring — monetisation becomes a config flip plus tagged articles, with disclosure rendered by code, not memory.
