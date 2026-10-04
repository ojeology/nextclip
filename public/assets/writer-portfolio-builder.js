(() => {
  "use strict";

  const form = document.getElementById("wpb-form");
  if (!form) return;

  const preview = document.getElementById("wpb-preview");
  const samplesHost = document.getElementById("wpb-samples");
  const status = document.getElementById("wpb-status");
  const linkWarning = document.getElementById("wpb-link-warning");
  const nameInput = document.getElementById("wpb-name");
  const downloadButton = document.getElementById("wpb-download");
  const resetButton = document.getElementById("wpb-reset");
  const addButton = document.getElementById("wpb-add-sample");
  if (!preview || !samplesHost || !status || !nameInput || !downloadButton || !resetButton || !addButton) return;

  const MAX_SAMPLES = 12;
  const escapeHTML = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[char]);

  function safeWebURL(value) {
    const raw = String(value ?? "").trim();
    if (!raw) return "";
    if (/^[a-z][a-z\d+.-]*:/i.test(raw) && !/^https?:\/\//i.test(raw)) return "";
    const candidate = /^https?:\/\//i.test(raw) ? raw : `https://${raw}`;
    try {
      const url = new URL(candidate);
      if (!["http:", "https:"].includes(url.protocol) || !url.hostname || url.username || url.password) return "";
      return url.href;
    } catch (_) {
      return "";
    }
  }

  function fieldValue(id) {
    const field = document.getElementById(id);
    return field ? field.value.trim() : "";
  }

  function readPortfolio() {
    const invalidLinks = [];
    const email = fieldValue("wpb-email");
    const websiteInput = fieldValue("wpb-website");
    const profileInput = fieldValue("wpb-profile");
    const website = safeWebURL(websiteInput);
    const profile = safeWebURL(profileInput);
    if (websiteInput && !website) invalidLinks.push("website");
    if (profileInput && !profile) invalidLinks.push("profile");

    const samples = [...samplesHost.querySelectorAll("[data-wpb-sample]")].map((row) => {
      const title = row.querySelector('[data-wpb-field="title"]')?.value.trim() || "";
      const publication = row.querySelector('[data-wpb-field="publication"]')?.value.trim() || "";
      const urlInput = row.querySelector('[data-wpb-field="url"]')?.value.trim() || "";
      const summary = row.querySelector('[data-wpb-field="summary"]')?.value.trim() || "";
      const url = safeWebURL(urlInput);
      if (urlInput && !url) invalidLinks.push("sample");
      if (title || publication || urlInput || summary) {
        return { title, publication, url, summary };
      }
      return null;
    }).filter(Boolean);

    return {
      name: fieldValue("wpb-name"),
      tagline: fieldValue("wpb-tagline"),
      location: fieldValue("wpb-location"),
      bio: fieldValue("wpb-bio"),
      focus: fieldValue("wpb-focus").split(/[\n,]/).map((item) => item.trim()).filter(Boolean).slice(0, 12),
      samples,
      email,
      website,
      profile,
      invalidLinks
    };
  }

  function renderPortfolio(data, previewMode = false) {
    const name = data.name || (previewMode ? "Your name" : "Writer");
    const nameHeading = previewMode ? "h3" : "h1";
    const sectionHeading = previewMode ? "h4" : "h2";
    const sampleHeading = previewMode ? "h5" : "h3";
    const tagline = data.tagline || (previewMode ? "Add a one-line description of what you write." : "");
    const bio = data.bio || (previewMode ? "Add a concise bio to show an editor who you are and what you cover." : "");
    const focusHTML = data.focus.length
      ? `<ul class="wpb-tags" aria-label="Writing areas">${data.focus.map((item) => `<li>${escapeHTML(item)}</li>`).join("")}</ul>`
      : (previewMode ? '<p class="wpb-placeholder">Your writing areas can appear here.</p>' : "");
    const sampleHTML = data.samples.length
      ? `<section class="wpb-work"><${sectionHeading}>Selected work</${sectionHeading}><div class="wpb-sample-grid">${data.samples.map((sample) => {
          const title = sample.title || sample.publication || "Writing sample";
          const titleHTML = sample.url
            ? `<a href="${escapeHTML(sample.url)}" target="_blank" rel="noopener noreferrer">${escapeHTML(title)} <span aria-hidden="true">↗</span></a>`
            : escapeHTML(title);
          const publicationHTML = sample.publication && sample.title
            ? `<p class="wpb-publication">${escapeHTML(sample.publication)}</p>` : "";
          const summaryHTML = sample.summary ? `<p>${escapeHTML(sample.summary)}</p>` : "";
          return `<article class="wpb-sample-card"><${sampleHeading}>${titleHTML}</${sampleHeading}>${publicationHTML}${summaryHTML}</article>`;
        }).join("")}</div></section>`
      : (previewMode ? '<p class="wpb-placeholder">Add a published clip, a public sample, or a link to your work to show it here.</p>' : "");

    const contactLinks = [];
    if (data.email) {
      const emailHref = `mailto:${encodeURIComponent(data.email)}`;
      contactLinks.push(`<a href="${escapeHTML(emailHref)}">Email me</a>`);
    }
    if (data.website) contactLinks.push(`<a href="${escapeHTML(data.website)}" target="_blank" rel="noopener noreferrer">Website <span aria-hidden="true">↗</span></a>`);
    if (data.profile) contactLinks.push(`<a href="${escapeHTML(data.profile)}" target="_blank" rel="noopener noreferrer">More about me <span aria-hidden="true">↗</span></a>`);
    const contactHTML = contactLinks.length
      ? `<footer class="wpb-contact"><${sectionHeading}>Get in touch</${sectionHeading}><nav aria-label="Contact and profile links">${contactLinks.join("")}</nav></footer>`
      : (previewMode ? '<footer class="wpb-placeholder">Add an email or public profile if you want editors to contact you.</footer>' : "");

    return `<article class="wpb-portfolio"><header class="wpb-header"><p class="wpb-eyebrow">WRITING PORTFOLIO</p><${nameHeading}>${escapeHTML(name)}</${nameHeading}>${tagline ? `<p class="wpb-tagline">${escapeHTML(tagline)}</p>` : ""}${data.location ? `<p class="wpb-location">${escapeHTML(data.location)}</p>` : ""}${bio ? `<p class="wpb-bio">${escapeHTML(bio)}</p>` : ""}${focusHTML}</header>${sampleHTML}${contactHTML}</article>`;
  }

  const PORTFOLIO_CSS = `
    :root{color-scheme:light;--ink:#1b2822;--muted:#5a6a61;--line:#dbe3dc;--paper:#fff;--wash:#f3f6f2;--green:#235842;--accent:#d7f0df}
    *{box-sizing:border-box}
    body{margin:0;background:var(--wash);color:var(--ink);font:16px/1.65 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
    .wpb-portfolio{max-width:920px;margin:clamp(18px,5vw,64px) auto;padding:clamp(22px,5vw,56px);background:var(--paper);border:1px solid var(--line);border-radius:18px;box-shadow:0 18px 56px rgba(22,49,35,.08)}
    .wpb-header{padding:0 0 30px;border-bottom:1px solid var(--line)}
    .wpb-eyebrow{margin:0 0 12px;color:var(--green);font-size:12px;font-weight:800;letter-spacing:.16em}
    .wpb-header h1{margin:0;font-family:Georgia,"Times New Roman",serif;font-size:clamp(36px,7vw,64px);line-height:1.04;letter-spacing:-.035em;overflow-wrap:anywhere}
    .wpb-tagline{margin:14px 0 0;font-size:clamp(18px,2.5vw,24px);font-weight:650;line-height:1.35}
    .wpb-location{margin:8px 0 0;color:var(--muted);font-size:14px}
    .wpb-bio{max-width:68ch;margin:20px 0 0;font-size:17px}
    .wpb-tags{display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:18px 0 0;list-style:none}
    .wpb-tags li{padding:5px 11px;border:1px solid #b9d3c1;border-radius:999px;background:#f4faf5;color:#28543b;font-size:13px;font-weight:650}
    .wpb-work{padding:28px 0 8px}
    .wpb-work h2,.wpb-contact h2{margin:0 0 14px;font-family:Georgia,"Times New Roman",serif;font-size:26px;line-height:1.2}
    .wpb-sample-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px}
    .wpb-sample-card{padding:16px 18px;border:1px solid var(--line);border-radius:12px;background:#fbfcfa;overflow-wrap:anywhere}
    .wpb-sample-card h3{margin:0;font-size:17px;line-height:1.4}
    .wpb-sample-card a,.wpb-contact a{color:var(--green);text-decoration-thickness:1px;text-underline-offset:3px}
    .wpb-publication{margin:6px 0 0;color:var(--muted);font-size:13px;font-weight:650}
    .wpb-sample-card p:not(.wpb-publication){margin:10px 0 0;color:#435249;font-size:14px}
    .wpb-contact{margin-top:24px;padding-top:22px;border-top:1px solid var(--line)}
    .wpb-contact nav{display:flex;flex-wrap:wrap;gap:10px 22px}
    .wpb-contact a{font-weight:700}
    .wpb-placeholder{color:#718078;font-style:italic}
    @media print{body{background:#fff}.wpb-portfolio{max-width:none;margin:0;padding:0;border:0;border-radius:0;box-shadow:none}a{color:inherit}}
  `;

  function makeDocument(data) {
    const description = (data.bio || data.tagline || `Writing portfolio for ${data.name}`).slice(0, 160);
    return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="${escapeHTML(description)}">
<title>${escapeHTML(data.name)} — writing portfolio</title>
<style>${PORTFOLIO_CSS}</style>
</head>
<body>
${renderPortfolio(data, false)}
</body>
</html>`;
  }

  function updateRows() {
    const rows = [...samplesHost.querySelectorAll("[data-wpb-sample]")];
    rows.forEach((row, index) => {
      const legend = row.querySelector("legend");
      const remove = row.querySelector("[data-remove-sample]");
      if (legend) legend.textContent = `Sample ${index + 1}`;
      if (remove) remove.disabled = rows.length <= 1;
    });
    addButton.disabled = rows.length >= MAX_SAMPLES;
    addButton.textContent = rows.length >= MAX_SAMPLES ? `Maximum ${MAX_SAMPLES} samples` : "+ Add another sample";
  }

  function addSampleRow() {
    const row = document.createElement("fieldset");
    row.className = "wpb-sample";
    row.dataset.wpbSample = "";
    row.innerHTML = `<legend>Sample</legend>
      <label>Title <input type="text" data-wpb-field="title" maxlength="100" placeholder="Title of the piece"></label>
      <label>Publication / client <input type="text" data-wpb-field="publication" maxlength="100" placeholder="Where it appeared (optional)"></label>
      <label>Public link <input type="url" data-wpb-field="url" maxlength="500" placeholder="https://example.com/your-piece" inputmode="url"></label>
      <label>One-line note <textarea data-wpb-field="summary" rows="2" maxlength="400" placeholder="What this sample demonstrates (optional)"></textarea></label>
      <button class="btn secondary" type="button" data-remove-sample>Remove this sample</button>`;
    samplesHost.appendChild(row);
    updateRows();
    row.querySelector('[data-wpb-field="title"]')?.focus();
  }

  function refresh() {
    const data = readPortfolio();
    preview.innerHTML = renderPortfolio(data, true);
    if (linkWarning) {
      linkWarning.hidden = data.invalidLinks.length === 0;
      linkWarning.textContent = data.invalidLinks.length
        ? "One or more links could not be checked. Only valid http or https links will be clickable in your portfolio."
        : "";
    }
  }

  form.addEventListener("input", refresh);
  form.addEventListener("change", refresh);
  form.addEventListener("click", (event) => {
    const remove = event.target.closest("[data-remove-sample]");
    if (!remove || remove.disabled) return;
    remove.closest("[data-wpb-sample]")?.remove();
    updateRows();
    refresh();
  });

  addButton.addEventListener("click", addSampleRow);

  resetButton.addEventListener("click", () => {
    form.reset();
    [...samplesHost.querySelectorAll("[data-wpb-sample]")].slice(1).forEach((row) => row.remove());
    updateRows();
    refresh();
    status.textContent = "Form cleared. Nothing was stored.";
    nameInput.focus();
  });

  downloadButton.addEventListener("click", () => {
    const data = readPortfolio();
    if (!data.name) {
      status.textContent = "Add your name or professional byline before downloading.";
      nameInput.focus();
      return;
    }
    const blob = new Blob([makeDocument(data)], { type: "text/html;charset=utf-8" });
    const objectURL = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const slug = data.name.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "writer";
    link.href = objectURL;
    link.download = `${slug}-writing-portfolio.html`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(objectURL), 1000);
    status.textContent = data.invalidLinks.length
      ? "Portfolio downloaded. Check the links that were left unlinked, then edit and download again. Your details stayed in this browser."
      : "Portfolio downloaded as a standalone HTML file. Your details stayed in this browser.";
  });

  updateRows();
  refresh();
})();
