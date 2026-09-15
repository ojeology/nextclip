# -*- coding: utf-8 -*-
"""BRYME Tech — 10/10 research brief, batch 2 (Tier 1 #6: Windows storage).

Verification receipts (2026-09-15):
- WinSxS guidance: Microsoft Learn — component store is never manually deleted;
  supported cleanup is DISM /Online /Cleanup-Image /StartComponentCleanup
  (with /ResetBase documented as blocking uninstall of superseded updates).
- hiberfil.sys: powercfg.exe /hibernate off is the documented removal path;
  it disables hibernation (and hybrid sleep/Fast Startup dependence stated).
- pagefile.sys and C:\\Windows\\Installer: documented as managed-by-Windows /
  required for repair and uninstall — never manual deletion targets.
- Windows.old and Windows Update Cleanup: removed via Disk Cleanup's
  "Clean up system files" / Settings > Storage > Temporary files — supported
  routes, with the rollback caveat stated.
- Storage Sense: documented as system-drive focused; Downloads handling is a
  setting the user must review (personal files can live there).
- No percentage savings claims, no invented file sizes. Sizes named in the
  piece (pagefile/hiberfil "several gigabytes") are ranges, attributed to
  depending-on-RAM arithmetic, not to a vendor figure.
"""

TROUBLESHOOTING_1010_B2 = [

    ("windows-storage-full", "windows", "troubleshooting",
     "Windows storage full? What you can safely delete — in the right order",
     "The diagnostic order that finds gigabytes without breaking anything: map first, supported tools second, the four never-touch folders last — and what to do when cleanup isn't enough.",
     """<p><b>The symptom:</b> the C: drive is full or nearly full, Windows is complaining, and every guide you find offers the same recycled list of folders to delete. The order here is the difference between reclaiming gigabytes and breaking an uninstall you'll need in six months. Rule zero: <em>map before deleting</em> — Settings &gt; System &gt; Storage shows what is actually eating the drive, categorised, before you touch anything.</p>

<h2>Step 1: the safe, supported cleanups (do these first)</h2>
<p><b>Temporary files, the supported way.</b> Settings &gt; System &gt; Storage &gt; Temporary files lists what Windows itself considers removable — update leftovers, delivery-optimisation files, thumbnails, error logs. Review the checkboxes (Downloads can appear here; it can hold personal files — untick it unless you mean it) and let the system do the deleting. The classical route, Disk Cleanup with <b>Clean up system files</b>, reaches the same places and adds <b>Windows Update Cleanup</b> and <b>Previous Windows installation(s)</b> — the supported way to remove the old version after an upgrade.</p>
<p><b>Windows.old, with its caveat.</b> After a feature update, the previous installation sits in C:\\Windows.old for a rollback window. Deleting it through the tools above is safe <em>once you're sure</em> the new version works and you've pulled any personal files out of it — but it also means you cannot go back. That's a decision, not a default.</p>
<p><b>Storage Sense for the future.</b> Settings &gt; System &gt; Storage &gt; Storage Sense automates the temp-file and Recycle Bin housekeeping on a schedule. It manages the system drive; check its settings once so its Downloads handling matches how you actually use that folder. This is prevention, not rescue — <a href="/tech/free-up-storage-android/">the phone-side version of the same discipline</a> works identically.</p>

<h2>Step 2: the space no cleanup tool reaches (still supported)</h2>
<p><b>The hibernation file.</b> hiberfil.sys is roughly the size of your RAM and lives at the drive root, hidden. If you never hibernate, an administrator Command Prompt removes it: <code>powercfg.exe /hibernate off</code>. Know the trade: this also disables Fast Startup's hibernation dependency, so boot times can lengthen slightly. Reversible with <code>/hibernate on</code>.</p>
<p><b>The component store.</b> C:\\Windows\\WinSxS grows with every update and <strong>must never be deleted manually</strong> — it is the store Windows uses to service, repair and uninstall itself. The supported cleanup is an administrator Command Prompt: <code>Dism.exe /online /Cleanup-Image /StartComponentCleanup</code>. Run <code>/AnalyzeComponentStore</code> first if you want to see whether cleanup is even worthwhile. The deeper <code>/ResetBase</code> variant reclaims more but removes the ability to uninstall superseded updates — another decision, not a default.</p>
<p><b>System restore points.</b> Shadow copies can hold many gigabytes. Reducing them is supported (System Properties &gt; System Protection &gt; Configure) but every point you remove is a rollback option you no longer have — <a href="/tech/windows-update-problems/">the thing you want when an update misbehaves</a>.</p>

<h2>Step 3: the honest look at your own files</h2>
<p>The Storage map's biggest category is often just you: Downloads never emptied, video projects, old installers, game libraries. A full <em>user</em> drive isn't a Windows problem — moving large personal files to another drive (or verified cloud storage) beats re-cleaning caches every month. Verify the copy before deleting the original; <a href="/tech/cloud-vs-local-backup/">backup and sync are not the same thing</a>, and cloud sync is not a backup of files you then delete.</p>
<p><b>App caches.</b> Browser caches and GPU shader caches (NVIDIA's DXCache and friends) are safe to clear — they rebuild. The supported route for apps is the app's own settings; for everything else, uninstall programs you don't use through Settings &gt; Apps, which is what keeps their services and registry entries from being orphaned.</p>

<h2>The never-touch list (no matter what a forum says)</h2>
<p><b>C:\\Windows\\WinSxS</b> (DISM only, above). <b>pagefile.sys</b> — virtual memory; resize it through Advanced system settings if you must, never delete it. <b>C:\\Windows\\System32</b> — it is Windows. <b>C:\\Windows\\Installer</b> — cached installers that repairs, updates and uninstalls need; deleting them trades space today for broken uninstalls later. And <b>Program Files</b> folders — uninstall properly so the leftovers come with them. If a "cleanup utility" offers to touch any of these, close it: the built-in tools plus DISM already cover every category that is safe to cover.</p>

<h2>When cleanup isn't enough — the real diagnosis</h2>
<p>If the drive fills again within days of a thorough cleanup, something is actively growing. Three usual suspects: update retry loops (check <a href="/tech/windows-update-problems/">update failure diagnosis</a> — failed updates re-download), a runaway log or cache from one app (the Storage map's per-app view shows the culprit), or WSL/docker virtual disks, which grow to their configured maximum and live as single huge files. Full-drive symptoms can also masquerade as slowness — <a href="/tech/why-is-my-computer-slow/">the slow-computer diagnostic</a> overlaps here, because Windows behaves badly under roughly 10% free space on the system drive.</p>

<h2>When to stop and get help</h2>
<p>Stop and take a backup image before going further if: the drive filled suddenly overnight (possible malfunctioning software — or ransomware's pre-encryption behaviour, which is a security incident, not a cleaning task), files you didn't delete are missing, or the Storage map's numbers don't come close to the used space (a sign of a filesystem problem a cleanup cannot fix). At that point the tool you need is a backup, then a professional — not a bigger delete key. General guidance, not a diagnosis of your specific machine.</p>

<p><b>Official documentation (checked 15 September 2026):</b> Microsoft Learn — "Storage Sense" and "Free up drive space" (support.microsoft.com), "Clean up the WinSxS folder" and "DISM component cleanup" (learn.microsoft.com), "PowerCfg command-line options" for hibernation.</p>"""),
]
