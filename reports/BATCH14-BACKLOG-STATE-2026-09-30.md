# Batch 14 backlog state, 30 September 2026

The pw.org backlog rebuild was started for batch 14 and stopped partway:

- **80 of 849** magazine detail pages fetched
- **66** of those carry an official submissions URL

pw.org rate-limits the detail-page fetches, which is why this is slow and why
batch 13 shipped 7 markets from 84 usable pages rather than more. The run is
fully resumable and the method is committed:

```
python3 scripts/rebuild-pw-backlog.py --out research/rebuild --stage 2
```

The cache lives under `research/`, which is **not committed** (and in this
workspace did not survive one snapshot), so the stage-2 run should simply be
repeated when batch 14 begins. Stage 1 takes about 25 seconds and reproduces
the same 849 slugs; only stage 2 is slow.

Next step for batch 14: resume stage 2, take the newly-profiled candidates,
fetch each publication's OWN guidelines page, and read the pay language. Nothing
from pw.org may be recorded as a rate.

## pw.org rate-limits the whole client, not just concurrency

A stage-2 run reached roughly 100 detail pages and was then refused with **429 on
every request** — the backoff inside `get()` (four tries, up to 16s) was not
enough, because the refusal continued past it. The failure mode was wasteful
rather than harmful: each remaining slug burned its four tries and then recorded
`fetch-failed`, which is dropped on the next load, so no bad data was kept — but
it would have spent hours doing it against 749 slugs, and deepened the block.

`scripts/rebuild-pw-backlog.py` now stops instead of continuing:

- `get()` counts consecutive `403`/`429` refusals across URLs and raises
  `RateLimited` at five in a row. One URL exhausts its own four tries (counter
  4); the next URL's first refusal trips it. A transient block followed by a
  success resets the counter, so an intermittent 403 does not end a run.
- `Retry-After` is honoured when it is a number of seconds, capped at 60 — a
  longer one is the server asking us to come back later, which is what stopping
  is for.
- `stage2()` catches it, **saves the cache**, writes `detail.json`, prints how
  many pages are still missing, and `main()` exits **2**. Exit 0 means every
  slug was attempted; it does not mean every slug succeeded.
- `--delay N` sets the pause between fetches (default 0.3s). The block lifted
  within minutes, so the limit looks like a short window: pace, not a long
  cool-down, is the fix.

Checked offline with a stubbed `urlopen`: five consecutive refusals raise, a
success resets the counter, a single 403 followed by a 200 returns normally,
`Retry-After: 3600` sleeps 60, and a rate-limited `stage2()` returns `None` with
the cache intact.

State after the block: 105 cache rows, 102 usable, **100 with a guidelines URL**
(one row in every 30 fail and are retried, never recorded).

Recovery command:

```
python3 scripts/rebuild-pw-backlog.py --out research/rebuild --stage 2 --delay 1
```
