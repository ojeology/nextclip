# How to add a verified job to BRYME

BRYME's differentiator is that it **verifies** opportunities and never scrapes a job
board. Do not copy a Jobberman / LinkedIn / Indeed/Glassdoor headline into a
record. Open the **exact employer or ATS page** and record what it actually says.

## Steps

1. **Find a primary source.** The employer's own careers site, or the exact ATS
   leaf page (Greenhouse / Workable / Lever / their domain). A search-result card
   or a repost is only a lead, never proof a role is live.

2. **Record it in `content/jobs-inbox.json`.** Use one object per role. Run
   `python3 scripts/import-jobs.py --dry-run` to see the template and validate.

   ```bash
   python3 scripts/import-jobs.py --dry-run
   ```
   Fix any problems it reports. Required fields and honest `status` are enforced.
   `status` must be one of: `open_when_checked`, `verified`,
   `application_checked`, `tested`, `closed`, `needs_recheck`.

3. **Be honest about verification.** BRYME records *when* a source was opened,
   not a promise it is still live. Use `verifiedAt` + `lastVerified` = the day
   you actually checked. Never claim payment or acceptance you didn't get.

4. **`jobPosting.eligible` is opt-in and gated.** Only set it to `true` when the
   role is genuinely open **and** you recorded a real `description`,
   `datePosted` and `validThrough`, and the source is the employer's own page.
   The importer refuses to mark it eligible without those fields. `hiringOrganization`
   is always the employer — never BRYME.

5. **Merge.** For the first time, or on any change:
   ```bash
   python3 scripts/import-jobs.py
   ```

6. **Allowlist (only genuinely current/indexable roles).** Add the detail route
   to `content/index-allowlist.json`, e.g. `/jobs/<id>/`. Leave empty or unverified
   hubs `noindex`.

7. **Rebuild and gate.**
   ```bash
   npm run build
   npm test
   ```
   The deterministic build + quality/HTTP gates must pass. For eligible
   JobPosting pages the Indexing API queue is generated automatically.

## Rules

- No invented verification claims, no fake jobs, no mass-scraping.
- `salary`/`compensationRaw` only when the source confirms it.
- Never mark a closed/expired job as currently available; update `status` to
  `closed` and remove it from `jobPosting` eligibility.
- Every externally sourced role gets an explicit `SOURCE:` attribution and an
  `Apply on <source>` link. BRYME is not the employer.
