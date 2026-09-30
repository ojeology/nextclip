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
