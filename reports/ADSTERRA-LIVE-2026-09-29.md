# Adsterra Native Banner — live on thebryme.com

**Date:** 2026-09-29 · **Commit:** `6da74fb` · **Deploy:** live (Render, ~84 s)

---

## What went live

The **Adsterra Native Banner**, taken from your own snippet, at the bottom of every
content page — after `</main>`, before `<footer>`. It never interrupts an article.

| | |
|---|---|
| Key | `7cf8bb4b0854f64ff4f20a3a19146e91` |
| Host | `pl31572329.profitableratecpmnetwork.com` |
| Placement | Bottom of page, below all content |
| Coverage | 2,579 content pages |
| Excluded | 1,359 noindex stub / soft-redirect pages — **verified 0 leaks** |

Markup matches your snippet exactly: container div first, then the async loader with
`data-cfasync="false"`, explicit `https://`.

---

## Live verification

Every desk checked on the real domain, cache-busted:

| Desk | Band | | Desk | Band |
|---|---|---|---|---|
| Home | ✅ | | Fitness | ✅ |
| Tech | ✅ | | Home & DIY | ✅ |
| Sport | ✅ | | Money | ✅ |
| Entertainment | ✅ | | Writers | ✅ |
| Film page (`goldeneye`) | ✅ | | Writing | ✅ |

**Must stay clean — confirmed:**

| Page | Ads |
|---|---|
| `/jobs/` (noindex stub) | none ✅ |
| `/guides/` (noindex stub) | none ✅ |
| `/learn/academic-writing/` (noindex stub) | none ✅ |

---

## I narrowed the guard instead of deleting it

`validate-site-quality.js:72` banned any Adsterra-family string outright:

```js
if(/…|profitableratecpmnetwork|highrevenueformat|…|adsterra/i.test(s))
  fail(`disallowed advertising endpoint remains …`);
```

Rather than remove it, it is now **config-driven**. When `site.config.json` carries both
`adsterra.key` and `adsterra.host`, exactly that one loader is sanctioned. **Clear the key
and the exception disappears by itself.**

It is also **stronger than before.** A name blocklist could never catch an unknown ad host,
so the test now also fails on *any* surviving `/invoke.js` loader whatever its host.

Tested **8/8**:

| Case | Result |
|---|---|
| Sanctioned native band | passes ✅ |
| Marker only | passes ✅ |
| Monetag | **blocked** ✅ |
| PropellerAds | **blocked** ✅ |
| Social bar | **blocked** ✅ |
| Classic 300×250 banner | **blocked** ✅ |
| Unknown-host `invoke.js` | **blocked** ✅ (new) |
| Ordinary YouTube embed | passes ✅ |

---

## Why the other three formats are refused

I implemented the Native Banner only. The rest are actively refused by the code:

**Popunder** — intrusive, and AdSense's site behavior policy bars pages carrying pop-ups.
**Social Bar** — same reason. You previously said *"forget the social bar"* — it never displayed.
**Classic 300×250** (`highrevenueformat`) — its `invoke.js` calls `document.write()`, which
**wipes the entire page** when it runs after load. Your own history records it as *"permanent
empty Advertisement boxes (ads never load)"* and a *"WHITE box (unfilled)"*.

---

## One thing I could not verify from here

**Whether a creative actually fills.** The loader returns 0 bytes to any non-browser request
by design, so the only real test is your eyes on the live site. Your history says the bottom
native unit worked before — *"the first unit to pass the owner's own visible-rendering
definition"* — so this is expected to render.

**Check it yourself:** open `thebryme.com`, press **F12 → Network**, filter for `invoke.js`,
scroll to the bottom. If the request returns bytes, it's filling.

---

## Height: deliberately not reserved

A native banner's height varies with how many cards Adsterra returns. A guessed reservation
would shift the page *anyway*, and become a visible hole when unfilled that then collapses —
a **second** shift. Because the slot sits below the entire article, any growth happens outside
the viewport and costs no measurable CLS. `overflow:hidden` is load-bearing: it stops a wide
creative adding a horizontal scrollbar on phones.

---

## To turn it off

Set `adsterra.key` and `adsterra.host` to `""` in `site.config.json`, rebuild, and run
`python3 scripts/inject-ads.py --revert`. The validator's exception disappears on its own.

---

## The AdSense trade, stated plainly

This **reverses item 10** of the readiness scorecard ("No third-party ad networks"), which
recorded Adsterra as *removed 20 Sep*. You made that call knowingly and I've recorded it here
rather than buried it.

**What protects the application:**
- One unit, bottom of page, static and in-flow. Not a pop-up, not an interstitial.
- Zero ads on thin/noindex pages.
- Never resembles a job card or CTA.
- Google explicitly permits other networks alongside AdSense.

**What still carries risk:**
1. **Adsterra serves dating and gambling advertisers.** AdSense treats *other ads on your page
   as part of your content*, and they must follow content guidelines. **Go to your Adsterra
   dashboard and block Adult / Dating / Gambling categories.** This is the single highest-value
   thing you can do right now, and it takes two minutes.
2. **Never enable Popunder or Social Bar.** Those are a direct policy breach, not a risk.
3. Your consent setup is Google's CMP, which **does not cover Adsterra**. Nigeria traffic is
   low-exposure, but it's a real gap worth knowing about.

---

## Recovering the workspace

The workspace truncates between turns (it dropped to ~4,800 of 13,768 files twice during this
session, losing `.git`). Recovery is always:

```bash
cd /home/user && rm -rf nextclip
git clone --depth 1 https://<TOKEN>@github.com/ojeology/nextclip.git nextclip
cd nextclip && npm run build
```

Everything is committed and pushed. Nothing is held only in the workspace.
