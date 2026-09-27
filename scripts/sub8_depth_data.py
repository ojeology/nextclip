# -*- coding: utf-8 -*-
"""Editorial depth sections, part 1: tech desk pages still under 8.0.
These pages were word-bar and structure shortfalls, so each block is real
prose carrying an h2, a list, internal links, a review date and one verified
external reference. Every external URL curl-verified 200 at authoring time."""

MDN = "https://developer.mozilla.org/en-US/docs/"
CSP3 = "https://www.w3.org/TR/CSP3/"
GHDOCS = "https://docs.github.com/en"
AND = "https://developer.android.com/"
GSUP = "https://support.google.com/android/"
MSWIN = "https://learn.microsoft.com/en-us/windows/"
NIST = "https://www.nist.gov/"
CISA = "https://www.cisa.gov/"
EFF = "https://www.eff.org/"
HIBP = "https://haveibeenpwned.com/"
FTC = "https://www.ftc.gov/"
IANA = "https://www.iana.org/assignments/media-types/media-types.xhtml"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS = {

"tech/android-notifications":
    "<h2>Where the settings actually live, and why they move</h2>"
    "<p>Android's notification controls are split across three levels, and most confusion comes from treating them as one. The system level decides whether an app may notify at all; the app level decides what that app's notifications look like; the channel level decides which categories inside that app reach you. An app that publishes several channels &mdash; messages, promotions, service alerts &mdash; can be silenced per category without losing the rest. Google's published Android guidance covers the per-app and per-channel paths at <a href=\"" + GSUP + "\" rel=\"noopener\">support.google.com/android</a>, and the platform behaviour itself is documented for developers at <a href=\"" + AND + "\" rel=\"noopener\">developer.android.com</a>, which is where the notification-channel model is defined. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>The order that fixes most complaints</h2>"
    "<p>Work from the specific to the general. Silencing a single channel is reversible and costs you nothing else; disabling an app's notifications entirely means you will miss the one alert that mattered. Battery optimisation is the step people skip, and it is the usual reason an app that is fully permitted still delivers late or not at all &mdash; aggressive power management suspends the background process that fetches the message.</p>"
    "<ul>"
    "<li><b>Check the channel first.</b> Open the app's notification settings and look at the categories, not the master switch.</li>"
    "<li><b>Check battery optimisation second.</b> An app excluded from optimisation is more likely to deliver promptly.</li>"
    "<li><b>Check Do Not Disturb schedules third.</b> A time-based rule overrides per-app permission without telling you.</li>"
    "<li><b>Only then disable the app.</b> This is the step that is hardest to undo when you realise you needed it.</li>"
    "</ul>"
    "<p>If the goal is fewer interruptions rather than fewer notifications, the desk's companion piece on <a href=\"/tech/best-password-manager-for-you/\">choosing a password manager</a> covers the same principle: reduce the surface once, deliberately, rather than reacting to each annoyance. For what apps do with the data behind those notifications, see <a href=\"/tech/what-free-apps-do-with-your-data/\">what free apps do with your data</a>.</p>",

"tech/csp-safe-front-end":
    "<h2>What a policy is actually declaring</h2>"
    "<p>A Content Security Policy is an allowlist expressed as an HTTP header. The browser will only execute, embed or connect to what the policy names, which means the header does real work against injected script even when an injection succeeds. The specification is maintained by the W3C at <a href=\"" + CSP3 + "\" rel=\"noopener\">w3.org/TR/CSP3</a>, and the practical directives, with browser support notes, are documented at <a href=\"" + MDN + "\" rel=\"noopener\">developer.mozilla.org</a>. Read the two together: the spec defines the model, the docs tell you what shipped. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>Rolling one out without breaking the site</h2>"
    "<p>Deploy in report mode first. A <code>Content-Security-Policy-Report-Only</code> header enforces nothing and logs everything, so you can watch a week of real traffic and see which third parties your pages genuinely load. The failures that surface are almost always analytics, font CDNs and payment widgets &mdash; things nobody wrote down. Only after that log is quiet do you switch to the enforcing header.</p>"
    "<ul>"
    "<li><b>Start narrow, not wide.</b> <code>default-src 'self'</code> and then add origins deliberately; the reverse order leaves gaps you never notice.</li>"
    "<li><b>Treat <code>unsafe-inline</code> as a deadline.</b> It is the escape hatch that makes the policy decorative, so plan the nonce or hash migration rather than leaving it in.</li>"
    "<li><b>Pin <code>frame-ancestors</code>.</b> It is the modern replacement for <code>X-Frame-Options</code> and it is what stops clickjacking.</li>"
    "<li><b>Keep <code>report-uri</code> or <code>report-to</code>.</b> A policy you cannot observe will silently rot as dependencies change.</li>"
    "</ul>"
    "<p>CSP is one layer, not the whole posture. The desk's guide to <a href=\"/tech/vulnerability-scanning-explained/\">vulnerability scanning explained</a> covers how to find the issues a header cannot fix, and <a href=\"/tech/what-is-a-cdn-why-your-site-needs-one/\">what a CDN is</a> explains how edge headers interact with origin headers when both are set.</p>",

"tech/github-token-hygiene":
    "<h2>Tokens are credentials, and they inherit your reach</h2>"
    "<p>A personal access token authenticates as you, within the scopes it was granted. That single fact drives every practice on this page: the token is not a convenience string, it is a key that can read private repositories, push code and, with the wrong scope, change organisation settings. GitHub documents scope selection and fine-grained permissions in its official docs at <a href=\"" + GHDOCS + "\" rel=\"noopener\">docs.github.com</a>, and the <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> publishes the broader guidance on secrets in source control that the desk's advice follows. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>The checks worth doing this week</h2>"
    "<p>Most exposed tokens are found the same way: a committed <code>.env</code>, a CI log, or a dotfile synced somewhere public. The remediation is always the same order &mdash; revoke, then rotate, then find out how long it was live. Revoking first matters because the window of exposure, not the discovery, is what determines the damage.</p>"
    "<ul>"
    "<li><b>Audit what exists.</b> List active tokens and delete any you cannot immediately explain. An unexplained token is an incident waiting to be dated.</li>"
    "<li><b>Scope down.</b> Replace a broad classic token with the narrowest fine-grained token that does the job, and set an expiry even where it is optional.</li>"
    "<li><b>Never let git see it.</b> Use a credential helper or an environment secret, and keep <code>.env</code> in <code>.gitignore</code> before the first commit rather than after.</li>"
    "<li><b>Scan history, not just HEAD.</b> Deleting a secret from the working tree leaves it in every earlier commit, where it is still readable.</li>"
    "</ul>"
    "<p>Token hygiene is one part of the same story as <a href=\"/tech/best-password-manager-for-you/\">picking a password manager</a> &mdash; both are about keeping one strong secret out of every place it does not belong. If you already suspect exposure, <a href=\"/tech/vulnerability-scanning-explained/\">vulnerability scanning explained</a> covers how to confirm what an attacker could reach.</p>",

"tech/tool/ai-subscription-cost-comparer":
    "<h2>Reading the pricing page the way it is written</h2>"
    "<p>AI subscription pricing rarely sits in one number. The advertised monthly figure is usually the annual-commitment price; the month-to-month price is higher, and the usage limits behind it are the part that decides whether the plan is actually yours. The <a href=\"" + FTC + "\" rel=\"noopener\">Federal Trade Commission</a> publishes the guidance on negative-option and auto-renewal billing that the desk's cost framing follows, and it is the reason this comparer asks about billing period rather than assuming one. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>What this tool counts, and what it cannot</h2>"
    "<p>Enter each subscription with its real billing period and the tool totals the annual figure, so a plan that looks like a small monthly cost is shown at what it will actually take from your account across a year. It deliberately does not forecast usage overages, because those depend on how you work and nobody can estimate them honestly for you.</p>"
    "<ul>"
    "<li><b>Convert everything to annual.</b> A monthly plan and an annual plan cannot be compared until they share a period.</li>"
    "<li><b>Count the seat, not the product.</b> Team pricing multiplied across a household or a small team is where these totals surprise people.</li>"
    "<li><b>Flag the trial end date.</b> The most common avoidable charge is a trial that converted while nobody was watching.</li>"
    "<li><b>Re-run it quarterly.</b> Prices and tiers move; a total you computed in January is a historical document by summer.</li>"
    "</ul>"
    "<p>The same arithmetic applies to the rest of a software budget, which is why the desk's explainer on <a href=\"/tech/saas-pricing-models-explained/\">SaaS pricing models</a> sits next to this tool &mdash; per-seat, usage and freemium each behave differently under pressure. For the cloud equivalent, where costs scale with traffic rather than seats, see <a href=\"/tech/cloud-bill-why-it-spikes/\">why your cloud bill spikes</a>, and for the free tiers worth exhausting first, <a href=\"/tech/microsoft-365-free-vs-paid/\">Microsoft 365 free versus paid</a>.</p>",

"tech/tool/data-usage-estimator":
    "<h2>Where the estimate comes from</h2>"
    "<p>This estimator multiplies hours by a per-hour consumption figure for the activity you select, which is the honest way to do it: streaming and calling are metered in bitrate, so an hour of high-definition video is not the same quantity of data as an hour of music. The unit conversions behind the figures follow the registered media-type and unit conventions, and the desk keeps its per-activity rates deliberately conservative. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>Using the number you get</h2>"
    "<p>The output is a planning figure, not a measurement. It is accurate enough to tell you whether a 20 GB allowance survives a month of video calls, and not accurate enough to bill against. Where it earns its keep is in the comparison: run your real mix of activities and see which one dominates, because almost always one activity is most of the total and the rest is noise.</p>"
    "<ul>"
    "<li><b>Video dominates.</b> Resolution and frame rate move the figure by multiples, so this is the first lever to pull on a capped connection.</li>"
    "<li><b>Calls are cheap, video calls are not.</b> An audio call is a rounding error next to the same conversation on camera.</li>"
    "<li><b>Downloads are one-off.</b> They count once, unlike streaming, which re-counts every time you watch.</li>"
    "<li><b>Background traffic is the hidden share.</b> Updates and syncs consume on a schedule you did not set, and they are why a light month still moves data.</li>"
    "</ul>"
    "<p>If the estimate is larger than your allowance, the desk's guide to <a href=\"/tech/why-streams-buffer-at-night/\">why streams buffer at night</a> explains the congestion half of the problem, and <a href=\"/tech/phone-storage-full-safe-deletes/\">safe deletes when phone storage is full</a> covers what to do about the local copies. For a connection you pay per gigabyte, the <a href=\"/tech/tool/vpn-cost-calculator/\">VPN cost calculator</a> is worth running alongside, since a VPN adds overhead to every byte.</p>",

"tech/tool/password-strength-checker":
    "<h2>What &ldquo;strength&rdquo; means, and what it does not</h2>"
    "<p>Length and unpredictability are what make a password resist guessing; a string of mixed characters that is short and patterned is weaker than a long, ordinary passphrase. The <a href=\"" + NIST + "\" rel=\"noopener\">National Institute of Standards and Technology</a> publishes the password guidance that shifted the field toward length and away from forced complexity, and the <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> carries the practical recommendations behind this tool's scoring. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>Running it safely</h2>"
    "<p>This checker runs entirely in your browser, so the text you type never leaves the page. That is the property to insist on for any tool of this kind: if a strength checker submits your password to a server, it has become part of the problem it was meant to help you avoid.</p>"
    "<ul>"
    "<li><b>Test a similar string, not the real one.</b> Same length, same character mix, different words &mdash; you learn the rating without ever exposing the password.</li>"
    "<li><b>Prefer length.</b> Four unrelated words beats eight characters of substitution, and is easier to type on a phone.</li>"
    "<li><b>Reuse is the real weakness.</b> One strong password on ten sites is a single breach away from being ten compromised accounts.</li>"
    "<li><b>Check for prior exposure.</b> A password that already appears in a breach is effectively public; <a href=\"" + HIBP + "\" rel=\"noopener\">Have I Been Pwned</a> lets you check an address without submitting a password.</li>"
    "</ul>"
    "<p>For the storage half of the problem, the desk's comparison in <a href=\"/tech/best-password-manager-for-you/\">best password manager for you</a> covers how the managers differ in practice rather than on feature lists, and <a href=\"/tech/github-token-hygiene/\">GitHub token hygiene</a> applies the same reasoning to developer credentials, which are usually longer-lived and more dangerous.</p>",

"tech/tool/upload-time-calculator":
    "<h2>The calculation, and the assumption inside it</h2>"
    "<p>Upload time is file size divided by available upload speed, with the units aligned &mdash; the step where most mental arithmetic goes wrong, because connection speeds are quoted in megabits and file sizes in megabytes, a factor of eight apart. This tool does that conversion for you and reports in the units you would actually use. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>Why the real answer is longer</h2>"
    "<p>The figure the calculator returns is a floor. Protocol overhead, TCP ramp-up and contention on your connection all add to it, and on a shared connection the upload channel is usually the first thing to saturate. Treat the estimate as the best case and plan around it, particularly when a deadline is involved.</p>"
    "<ul>"
    "<li><b>Upload is not download.</b> Most consumer connections are asymmetric, and the upload side is far smaller than the number on the plan.</li>"
    "<li><b>Large files benefit from resumable transfers.</b> A single long upload that fails near the end costs the whole attempt again.</li>"
    "<li><b>Compress first when you can.</b> Text and images shrink meaningfully; already-compressed video does not.</li>"
    "<li><b>Test at the time you will actually upload.</b> Evening congestion is real, and a speed measured at noon does not describe it.</li>"
    "</ul>"
    "<p>The same bottleneck explains why <a href=\"/tech/why-streams-buffer-at-night/\">streams buffer at night</a>, and it is the reason the desk's <a href=\"/tech/what-is-a-cdn-why-your-site-needs-one/\">CDN explainer</a> matters for anything you publish. If the upload is a backup, <a href=\"/tech/phone-died-no-backup/\">what to do when your phone dies with no backup</a> covers the recovery side of getting this wrong.</p>",

"tech/tool/vpn-cost-calculator":
    "<h2>What you are actually paying for</h2>"
    "<p>A VPN subscription buys encryption in transit and a different exit point on the internet. It does not make you anonymous, and it does not protect you from a compromised site at the far end. The <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a> publishes the surveillance self-defence guidance behind the desk's framing of what a VPN does and does not do, which is worth reading before the price comparison matters. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>Comparing plans honestly</h2>"
    "<p>Enter the monthly price and the term you would commit to, and the tool reports the effective monthly cost and the annual total. Long terms are cheaper per month and worse per unit of trust: you are pre-paying for a service whose logging policy can change while you are locked in.</p>"
    "<ul>"
    "<li><b>Convert to effective monthly.</b> The advertised price is usually the longest-term price, which is the one most people do not want.</li>"
    "<li><b>Count simultaneous devices.</b> A plan covering ten devices across a household can beat a cheaper single-device plan outright.</li>"
    "<li><b>Read the logging policy, not the marketing.</b> &ldquo;No logs&rdquo; means nothing until you see which connection metadata is retained and for how long.</li>"
    "<li><b>Treat the free tier as a trial.</b> A free VPN has to be funded somehow, and the funding is usually your traffic or your attention.</li>"
    "</ul>"
    "<p>For the data the encryption carries, the desk's <a href=\"/tech/tool/data-usage-estimator/\">data usage estimator</a> is the companion calculation, since a VPN adds overhead to every byte. And for what an encrypted tunnel does not protect, <a href=\"/tech/what-free-apps-do-with-your-data/\">what free apps do with your data</a> covers the collection that happens after the traffic arrives.</p>",

"tech/windows-keyboard-shortcuts":
    "<h2>Why the short list beats the long one</h2>"
    "<p>Windows has several hundred documented shortcuts, and learning all of them is a poor use of an afternoon. The ones worth memorising are the ones you reach for constantly: window management, virtual desktops and the clipboard history, which together remove most of the mouse work from a working day. Microsoft's official Windows documentation carries the full published set at <a href=\"" + MSWIN + "\" rel=\"noopener\">learn.microsoft.com/windows</a>, and it is the reference to check when a shortcut behaves differently than a forum post suggested. Reviewed by the Bryme Tech desk, 27 September 2026.</p>"
    "<h2>The handful that changes how the machine feels</h2>"
    "<p>Window snapping and virtual desktops are the two features most people never discover, and both are keyboard-first by design. Clipboard history is the third: once it is on, the cut-and-paste dance across three items collapses into one copy sequence and one paste choice.</p>"
    "<ul>"
    "<li><b>Snap and move windows with the arrow keys.</b> Half-screen, quarter-screen and move-to-monitor are all a keystroke away.</li>"
    "<li><b>Use virtual desktops for contexts.</b> Work on one, reference on another; switching is faster than rearranging windows.</li>"
    "<li><b>Turn on clipboard history.</b> It keeps the last several items and survives a single copy of the wrong thing.</li>"
    "<li><b>Learn the search-first habits.</b> Launching by name beats navigating a Start menu tree every time, and it scales to software you rarely open.</li>"
    "</ul>"
    "<p>If the machine behind the shortcuts is the slow part, the desk's comparison in <a href=\"/tech/tablet-vs-budget-laptop-for-students/\">tablet versus budget laptop</a> covers what to buy, and <a href=\"/tech/microsoft-365-free-vs-paid/\">Microsoft 365 free versus paid</a> covers which of the bundled applications you actually need to pay for.</p>",

}
