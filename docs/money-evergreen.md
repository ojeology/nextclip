# Money evergreen publication

The canonical hub is `https://thebryme.com/money/`. The published static artifact is `public/`; `/money/` and `/ecosystem/money/` are routed and source mirrors. The 13 researched guides live in `content/money-guides/manifest.json` (title, URL, description, review date and source links) and adjacent `*.html` body fragments. Read the source manifest before changing a guide: trade mechanics vary by product and jurisdiction.

## Editing / releasing a Money page

1. Verify primary source links and any date-dependent legal or regulatory claims. Check the four target markets (US, UK, Canada and Australia) separately. Do not imply that a broker, strategy, indicator, trade setup or tool guarantees a return. An illustrative risk calculation is **not** a promise that a stop order will execute at the trigger price.
2. Edit the manifest entry and its HTML fragment. Set `reviewed` to the actual source-review date only after reviewing all affected pages; this is a shared publication review stamp. For an update to an existing Money page, edit `scripts/money_desk_data.py` and, when relevant, `scripts/build-ecosystem.py` instead.
3. Run `python3 scripts/build-money-desk.py` to regenerate just Money's ecosystem, routed and public pages, the routed allowlist and sitemap indexes. **Do not** run `scripts/build-routing.py` directly against the routed tree. A normal `npm run build` does not read the guide manifest; always run the Money-only generator first.
4. Run `npm run validate:money`, `npm run validate:money:browser`, `npm run validate`, `npm run test:http`, `npm test`, and `npm audit --audit-level=high`. The browser gates require `npx playwright install --with-deps chromium` on a fresh Linux machine.
5. Run the site's full deterministic build (`SOURCE_DATE_EPOCH=<review-date-as-UTC-seconds> npm run build`) as the CI job does; rerun the gates and verify the resulting diff is intentional. Commit the generated `ecosystem/money/`, `money/`, `public/money/`, routed allowlist and sitemap files with the source change. Render serves `public/` and auto-deploys `main` after a push.

Money guide links to financial/regulatory sources are for information, not recommendations of a particular firm. Avoid unsupported claims about cost-per-click, earnings, win rates, universal leverage limits, taxes or cross-border permissions. New site pages are not included in the writing-only RSS feed or news sitemap just because they have a review date.
