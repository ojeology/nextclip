# BRYME Quality Roadmap

## Objective

Make the existing BRYME ecosystem difficult to ignore because its pages are useful, trustworthy, distinctive, technically clean and connected — not because it has more URLs.

This roadmap deliberately prioritises strengthening, consolidating and correctly classifying existing pages. It does **not** authorise mass page generation.

## North-star standard

Every important page should answer five questions immediately:

1. Who is this for?
2. What specific problem or decision does it solve?
3. Why should the reader trust this page?
4. What should the reader do next?
5. When was the information last checked?

## Page quality score

Use a 0–5 score for every retained page:

| Dimension | 0 | 5 |
|---|---|---|
| Search intent | unclear or duplicated | exact intent answered quickly |
| Original value | generic summary | distinctive analysis, data, test, tool or first-hand evidence |
| Evidence | unsupported claims | visible sources, method and limitations |
| Freshness | stale or undated | visible review date and update trigger |
| Trust | unclear ownership | author/editorial context, disclosures and corrections path |
| Completeness | thin or unfinished | practical answer, examples, edge cases and next step |
| Internal architecture | orphaned | hub, siblings, tool and next-step links |
| UX/performance | difficult to use | fast, accessible, mobile-friendly and stable |

**Target:** important pages score at least 4 in every dimension. A page does not need to be long to score well.

## Page decisions

Every existing route must receive one decision:

- **A — Flagship:** retain, strengthen, promote and link from hubs.
- **B — Useful support:** retain, improve clarity and link into a cluster.
- **C — Product/entity page:** retain if the database/tool purpose is clear; enrich with unique useful fields.
- **D — Archive:** retain as historical material with date/status context; do not present stale information as current.
- **E — Merge or redirect:** overlapping pages with one clearly stronger canonical destination.
- **F — Noindex:** genuinely thin, temporary, filter, search or low-value variations that should not compete.

No page is deleted solely because it has low traffic.

## Phase 0 — Deployment and measurement baseline

**Goal:** establish a trustworthy starting point before further changes.

- Confirm the latest Render deployment is live.
- Verify homepage, all seven desk hubs, privacy, robots, root sitemap and catalogue sitemap.
- Capture Search Console exports:
  - indexed pages;
  - excluded pages and reasons;
  - impressions/clicks by URL;
  - Core Web Vitals;
  - queries by desk.
- Capture GA4 baseline:
  - engaged sessions;
  - returning users;
  - tool usage;
  - outbound clicks;
  - top landing pages.
- Preserve a dated release manifest and build output counts.

**Exit criteria:** production checks green, baseline stored, no accidental URL changes.

## Phase 1 — P0/P1 technical stability

**Goal:** remove failure modes before editorial polishing.

- Run the complete release suite in GitHub Actions.
- Fix browser test dependencies and investigate every real console, overflow and accessibility failure.
- Verify:
  - HTTP status codes;
  - redirects and redirect chains;
  - canonical URLs;
  - robots rules;
  - all sitemap references;
  - sitemap/allowlist agreement;
  - no soft 404s;
  - no accidental noindex;
  - public-file containment;
  - security headers;
  - exposed secrets;
  - analytics and consent behaviour.
- Keep the generated publish tree deterministic.
- Keep the Render build command hard-failing when a generator fails.

**Exit criteria:** full static and browser gates pass; production smoke tests pass.

## Phase 2 — Page inventory and classification

**Goal:** understand all existing pages before changing indexation.

Create a CSV or JSON inventory containing:

- URL and desk;
- page type;
- indexability state;
- sitemap membership;
- word count where meaningful;
- last-modified/review date;
- inbound-link count;
- Search Console clicks/impressions;
- quality score;
- recommended decision A–F;
- owner and next review date.

Do not use word count as the only thin-content test. A calculator, database record, catalogue entity or archive page is judged by its product purpose and unique value.

**Exit criteria:** every route has a deliberate decision and no route is indexable by accident.

## Phase 3 — Flagship clusters

**Goal:** make the best existing content unmistakably authoritative.

For each desk, select 10–20 flagship pages. For every flagship:

- rewrite the opening to match the exact intent;
- add the answer or decision framework near the top;
- add evidence and source links;
- state scope, geography and limitations;
- add a visible reviewed/updated date;
- add author/editorial context where appropriate;
- add 3–6 contextual internal links;
- connect to one relevant tool, database or next action;
- add a correction/report-outdated route;
- test mobile layout and accessibility.

Build each cluster as:

`Hub → Flagship guide → Supporting guides → Tool/database → Related next steps`

## Desk programmes

### BRYME Writers

- Protect the 142-record opportunity database as a product.
- Verify every official URL before changing rates, requirements or eligibility.
- Keep historical or unavailable guidance explicitly labelled.
- Add a standard opportunity information block:
  - official source;
  - last verified;
  - submission method;
  - requirements;
  - geography;
  - pay and conditions;
  - AI policy;
  - rights;
  - response expectations;
  - report-outdated control.
- Make country and writing-type hubs genuinely useful, not just filters.
- Promote the State of Paid Writing report and writing calendar.

### BRYME Tech

- Make Android, Windows, web development, hosting, DNS, cloud, AI, cybersecurity, APIs and SaaS clusters visibly connected.
- Add tested context: device, software version, date, limitations and who should not follow the advice.
- Keep tools beside explanations and examples.
- Remove or noindex duplicate utility states and parameter variants.

### BRYME Money

- Put jurisdiction in the title, H1, introduction and relevant schema where rules differ.
- Separate education from advice.
- Date all rates, thresholds, tax, mortgage and regulatory claims.
- Show assumptions in every calculator.
- Never use guaranteed-profit language.
- Prioritise risk, costs, downside and uncertainty before upside.

### BRYME Sport

- Keep current data pages timestamped with named sources.
- Treat old matchweeks and transfer windows as archives.
- Avoid indexable filter, sort, date and temporary-state combinations.
- Link evergreen explainers into current data hubs.
- Validate fixtures, tables and scorers after every data update.

### BRYME Entertainment

- Keep editorial reviews, guides and explainers as the prose core.
- Catalogue pages need unique facts, synopsis, credits, themes, review/context and legitimate viewing information where available.
- Watch pages must provide more than a thin embed or link.
- Keep catalogue sitemap separation, then use Search Console to decide whether any entity family needs noindex treatment.
- Do not add film pages solely to increase URL count.

### BRYME Fitness

- Keep advice practical and evidence-aware.
- State who should not follow a protocol and when to seek medical advice.
- Link programmes to exercise explanations and calculators.
- Avoid miracle, guaranteed-outcome and unsupported medical claims.

### BRYME Home & DIY

- Organise around problems and decisions: diagnose, maintain, repair, compare and call a professional.
- Put safety warnings before hazardous instructions.
- Clearly separate homeowner checks from electrical, gas, structural and hazardous-material work.
- Connect repair guides to calculators, checklists and seasonal tools.

## Phase 4 — Entity and database quality

**Goal:** make programmatic pages useful without pretending every record is an article.

For each entity family, define a minimum useful record:

- clear identity;
- unique summary;
- relevant fields;
- source or provenance;
- date/status;
- limitations;
- related records;
- next useful action.

If a family cannot meet the minimum, choose archive, noindex, merge or sitemap separation. Do not leave thousands of near-identical pages indexable by default.

## Phase 5 — Internal architecture

Run a quarterly graph audit:

- zero indexed orphans;
- every flagship linked from a hub;
- every support page linked to siblings;
- tools linked from relevant guides;
- no random link stuffing;
- no broken or misleading anchors;
- breadcrumbs agree with canonical routes.

Use descriptive anchors based on the reader’s task, not repeated keyword variants.

## Phase 6 — Trust and editorial operations

Publish and maintain:

- About;
- Contact;
- Editorial Policy;
- Privacy;
- Terms;
- Corrections;
- author/editor information;
- advertising and affiliate disclosures;
- update and verification policy;
- report-outdated controls.

Create a monthly freshness queue:

- Money regulatory/tax/finance claims;
- Sport current data;
- Writers opportunities;
- Tech version-sensitive instructions;
- Fitness health-sensitive claims;
- Home safety guidance;
- Entertainment availability and catalogue facts.

## Phase 7 — Distribution and monetisation

Only after quality and deployment are stable:

- claim BRYME on Pinterest;
- publish a small number of useful pins from existing pages;
- use answer-first community participation;
- continue Bing queue submission within quota;
- maintain IndexNow;
- evaluate newsletter performance;
- test carefully labelled affiliate relationships;
- keep ads separate from applications and editorial controls;
- never let monetisation reduce trust or mobile usability.

## Weekly operating cycle

### Monday — evidence and freshness

- review time-sensitive records;
- verify sources;
- update only where evidence changed.

### Tuesday — flagship improvement

- strengthen 2–5 high-priority pages;
- add sources, examples, links and next steps.

### Wednesday — technical quality

- run build and static gates;
- inspect errors, redirects, canonicals and sitemap changes.

### Thursday — user and distribution

- review search queries and user behaviour;
- publish a small number of useful Pinterest/community posts.

### Friday — release control

- review diff;
- confirm URL count and indexability changes;
- run production smoke probes;
- deploy only when all gates are green.

## Success metrics

Do not use raw URL count as the primary metric.

Track:

- indexed high-quality pages;
- impressions and clicks by desk;
- query-to-page intent match;
- returning users;
- engaged sessions;
- tool starts and completions;
- opportunity-detail interactions;
- report-outdated/correction response time;
- internal-link coverage;
- Core Web Vitals;
- index coverage errors;
- Bing/Google discovery;
- newsletter signups;
- qualified outbound clicks;
- revenue per useful session, not ad density.

## Change-control rules

Before every significant change:

1. record the affected route family;
2. record expected URL and sitemap impact;
3. preserve a rollback point;
4. run the build;
5. run static validation;
6. run browser validation where applicable;
7. inspect canonical, robots, schema and internal links;
8. deploy;
9. recheck production;
10. record the result in the audit register.

No mass generation. No invented sources. No unsupported rates. No casual URL migrations. No deletion without evidence.
