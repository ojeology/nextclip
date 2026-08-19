# Writing catalogue — how to add a site

User flow:

1. `/make-money/` — pick **country**, then **Writing**
2. `/make-money/writing-opportunities/?country=nigeria` — the catalogue
3. `/make-money/writing-opportunities/{slug}/` — full guide, only after a row is published

Source file: `content/writing-opportunities.json`

Nothing on those pages is invented. If you did not email them, you cannot claim a reply time. If you did not get paid, you cannot mark `gotPaid`. Draft rows never appear.

## Rhythm

1. Research a site. Save the apply URL and what they actually ask for.
2. Write to them if you are going to feature them.
3. Log the row below. Keep `status` as `"draft"` until the notes are honest and dated.
4. Set `"status": "published"` when you will stand behind the row.
5. Rebuild: `node scripts/build-static-foundation.js`
6. Film three published rows. The video should already be useful if nobody clicks.

## A published row

```json
{
  "id": "short-id",
  "slug": "short-id",
  "name": "The publication name",
  "status": "draft",
  "featuredInVideo": 1,
  "niches": ["tech", "explainers"],
  "siteUrl": "https://example.com/",
  "applyUrl": "https://example.com/write-for-us",
  "applyMethod": "email",
  "acceptsArticles": true,
  "submissionsOpen": true,
  "submissionsCheckedOn": "2026-08-19",
  "payStatus": "unknown",
  "payNotes": "What their page or reply actually said about pay.",
  "paymentMethods": [],
  "countryPolicy": {
    "Nigeria": "unknown"
  },
  "countriesAccepted": [],
  "countriesRejected": [],
  "writerCountry": "Nigeria",
  "contacted": false,
  "contactedOn": null,
  "replied": null,
  "repliedOn": null,
  "landedGig": false,
  "gotPaid": false,
  "lastChecked": "2026-08-19",
  "whatTheyWant": "Pitch, finished draft, word count, niche — only what they published or told you.",
  "guidelines": ["Their actual rules, one per line."],
  "howToSubmit": ["Step 1 as they describe it.", "Step 2."],
  "whoItsNotFor": "Who should skip this one.",
  "notes": "What you personally did and saw.",
  "unknowns": ["whether they accept Nigeria", "reply time"],
  "sources": [{ "name": "Write for us page", "url": "https://example.com/write-for-us" }]
}
```

## How each catalogue field is allowed to be filled

| Card field | Allowed source |
|---|---|
| Accepts articles | Their current contributor page |
| Submissions open / closed | Same page, with `submissionsCheckedOn` |
| Pay | Their page or their email. Not another blog |
| Your country | `countryPolicy["Nigeria"]` = `accepted` / `rejected` / `unknown`. Default is unknown |
| Reply | Only from your application: replied date minus sent date, or “no reply after X days”. Never a guessed average |

`countryPolicy` keys must match the **name** on the country buttons (`Nigeria`, not `nigeria`).

## The build will refuse a published row when

- `name`, `slug`, `lastChecked` or `writerCountry` is missing
- there is no `siteUrl` or `applyUrl`
- there is no real substance (`notes`, `whatTheyWant`, `guidelines`, or a genuine contact)
- you set `replied`, `gotPaid`, `landedGig` or a reply window without `contacted: true`

`payStatus`: `paid` | `unpaid` | `mixed` | `unknown`.

## Adding another path later (design, VA, …)

Do not invent a catalogue. Add a path in `paths` with `"status": "later"` until you have first-hand rows. Then we give it the same country → list → guide treatment as writing.

## After a video goes live

```json
"youtubeVideoUrl": "https://www.youtube.com/watch?v=XXXXXXXXXXX",
"youtubeVideoTitle": "I pitched 3 sites from Lagos. Here is who replied."
```
