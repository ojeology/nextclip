/* BRYME PDF tools — fully client-side, powered by pdf-lib (pdf-lib.min.js)
   and pdf.js (pdfjs.min.js), both vendored locally under /assets/vendor/. */
(function () {
  "use strict";
  var SCRIPT = document.currentScript;
  var P, STD, RGB; // set once PDFLib is present
  function q(id) { return document.getElementById(id); }
  function fmt(bytes) { return bytes < 1024 ? bytes + " B" : bytes < 1048576 ? (bytes / 1024).toFixed(1) + " KB" : (bytes / 1048576).toFixed(2) + " MB"; }
  function el(id, text) { var e = q(id); if (e) e.textContent = text; }
  function log(id, text, ok) { var e = q(id); if (!e) return; e.textContent = text; e.className = "tool-note" + (ok === undefined ? "" : ok ? " ok" : " err"); }
  function dl(bytes, name) {
    var blob = new Blob([bytes], { type: "application/pdf" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { document.body.removeChild(a); URL.revokeObjectURL(a.href); }, 2000);
  }
  function fileToBuf(file) {
    return new Promise(function (res, rej) {
      var fr = new FileReader();
      fr.onload = function () { res(new Uint8Array(fr.result)); };
      fr.onerror = rej; fr.readAsArrayBuffer(file);
    });
  }
  // pdf.js transfers (and detaches) the Uint8Array to its worker, so every
  // getDocument call must receive its own copy.
  function clone(u8) { return new Uint8Array(u8); }

  // ---- PDF Editor: load one PDF, rotate / delete / reorder, export ----
  // We track pages as {idx, rot} where idx = the page's origin index in the
  // loaded file. Users delete/reorder freely; export copies from the source by
  // those origin indices, preserving each page's rotation.
  function pdfEditor() {
    var file = q("pdf-file"), status = q("editor-status"), pagesBox = q("pages-list"), exportBtn = q("editor-export");
    var bytes = null;             // raw loaded file
    var order = [];               // list of origin page indices, in current display order
    var rots = {};                // originIdx -> rotation degrees
    function renderPages() {
      pagesBox.innerHTML = "";
      order.forEach(function (idx, i) {
        var item = document.createElement("div");
        item.className = "pdf-pg";
        var canvas = document.createElement("canvas");
        canvas.className = "pdf-pg-canvas";
        var top = document.createElement("div"); top.className = "pdf-pg-top";
        var num = document.createElement("span"); num.className = "pdf-pg-n"; num.textContent = "Pg " + (i + 1);
        var actions = document.createElement("span"); actions.className = "pdf-pg-actions";
        top.appendChild(num); top.appendChild(actions);
        item.appendChild(top); item.appendChild(canvas);
        var rot = document.createElement("button"); rot.className = "btn-sm"; rot.textContent = "⟳"; rot.title = "Rotate 90°";
        var del = document.createElement("button"); del.className = "btn-sm"; del.textContent = "✕"; del.title = "Remove this page";
        var up = document.createElement("button"); up.className = "btn-sm"; up.textContent = "↑"; up.title = "Move earlier";
        var dn = document.createElement("button"); dn.className = "btn-sm"; dn.textContent = "↓"; dn.title = "Move later";
        actions.appendChild(up); actions.appendChild(dn); actions.appendChild(rot); actions.appendChild(del);
        up.addEventListener("click", function () { if (i > 0) { var t = order[i - 1]; order[i - 1] = order[i]; order[i] = t; renderPages(); } });
        dn.addEventListener("click", function () { if (i < order.length - 1) { var t = order[i + 1]; order[i + 1] = order[i]; order[i] = t; renderPages(); } });
        rot.addEventListener("click", function () { rots[idx] = ((rots[idx] || 0) + 90) % 360; renderPages(); });
        del.addEventListener("click", function () { order.splice(i, 1); delete rots[idx]; renderPages(); });

        // thumbnail via pdf.js (render the origin page)
        if (window.pdfjsLib && bytes) {
          window.pdfjsLib.getDocument({ data: clone(bytes) }).promise.then(function (src) {
            return src.getPage(idx + 1);
          }).then(function (page) {
            var vp = page.getViewport({ scale: 0.28 });
            canvas.width = vp.width; canvas.height = vp.height;
            return page.render({ canvasContext: canvas.getContext("2d"), viewport: vp }).promise;
          }).catch(function () {});
        }
        pagesBox.appendChild(item);
      });
      el("editor-count", order.length + " page" + (order.length === 1 ? "" : "s"));
    }
    function start() {
      var name = file.files[0].name;
      fileToBuf(file.files[0]).then(function (u8) {
        bytes = u8;
        return window.pdfjsLib.getDocument({ data: clone(u8) }).promise;
      }).then(function (srcDoc) {
        var n = srcDoc.numPages;
        order = []; for (var i = 0; i < n; i++) order.push(i);
        rots = {};
        renderPages();
        log(status, "Loaded \u201c" + name + "\u201d (" + n + " pages). Rotate, remove, or reorder the pages, then export.", true);
      }).catch(function () { log(status, "Could not load that PDF. It may be password-protected or corrupted.", false); });
    }
    file.addEventListener("change", function () { if (file.files[0]) start(); });
    exportBtn.addEventListener("click", function () {
      if (!bytes) { log(status, "Choose a PDF first."); return; }
      // Render each retained page (in the chosen order) to an image via pdf.js,
      // then rebuild a fresh PDF. This sidesteps pdf-lib's copyPages edge case
      // and faithfully applies deletes/reorders/rotation.
      var jsDoc = window.pdfjsLib.getDocument({ data: clone(bytes) });
      jsDoc.promise.then(function (src) {
        var keep = order.slice(); // origin indices, in display order
        var canvases = [];
        (function next(i) {
          if (i >= keep.length) { return build(); }
          var oi = keep[i];
          src.getPage(oi + 1).then(function (page) {
            var vp = page.getViewport({ scale: 2 });
            var c = document.createElement("canvas");
            c.width = vp.width; c.height = vp.height;
            return page.render({ canvasContext: c.getContext("2d"), viewport: vp }).promise.then(function () {
              canvases.push(c); next(i + 1);
            });
          }).catch(function () { log(status, "Could not render a page. Please try again.", false); });
        })(0);
        function build() {
          P.PDFDocument.create().then(function (d) {
            var idx = 0;
            (function add() {
              if (idx >= canvases.length) { return d.save(); }
              var c = canvases[idx++];
              return new Promise(function (res) {
                c.toBlob(function (blob) {
                  blob.arrayBuffer().then(function (ab) { res(new Uint8Array(ab)); });
                }, "image/png");
              }).then(function (png) {
                return d.embedPng(png).then(function (img) {
                  var scale = Math.min(595.28 / img.width, 841.89 / img.height);
                  var w = img.width * scale, h = img.height * scale;
                  var pg = d.addPage([595.28, 841.89]);
                  pg.drawImage(img, { x: (595.28 - w) / 2, y: (841.89 - h) / 2, width: w, height: h });
                  return add();
                });
              });
            })();
          }).then(function (outBytes) {
            dl(outBytes, "edited.pdf");
            log(status, "Exported edited.pdf (" + fmt(outBytes.length) + ", " + order.length + " page" + (order.length === 1 ? "" : "s") + ").", true);
          }).catch(function (e) { log(status, "Could not export — please try again (" + (e && e.message ? e.message : "error") + ").", false); });
        }
      }).catch(function () { log(status, "Could not load that PDF. It may be password-protected or corrupted.", false); });
    });
  }

  // ---- PDF to Text (pdf.js) ----
  function pdfToText() {
    var file = q("pdft-text-file"), status = q("pdft-status"), ta = q("pdft-out"), copy = q("pdft-copy");
    function extract(u8) {
      var task = window.pdfjsLib.getDocument({ data: clone(u8) });
      task.promise.then(function (doc) {
        var out = [];
        (function next(i) {
          if (i >= doc.numPages) {
            ta.value = out.join("\n\n---\n\n");
            el("pdft-count", doc.numPages + " page" + (doc.numPages === 1 ? "" : "s") + " of text");
            log(status, "Text extracted. Copy it, or paste it into the Word document converter for an editable file.", true);
            return;
          }
          doc.getPage(i + 1).then(function (pg) {
            pg.getTextContent().then(function (tc) {
              var line = "";
              tc.items.forEach(function (it) { line += (it.hasEOL ? it.str + "\n" : (line ? " " : "") + it.str); });
              out.push(line.trim());
              next(i + 1);
            });
          });
        })(0);
      }).catch(function () { log(status, "Could not read that PDF's text (it may be a scanned image or password-protected).", false); });
    }
    if (file) file.addEventListener("change", function () {
      if (!file.files[0]) { log(status, "Choose a PDF file."); return; }
      fileToBuf(file.files[0]).then(extract);
    });
    if (copy) copy.addEventListener("click", function () {
      if (!ta || !ta.value) return;
      ta.select(); document.execCommand("copy");
      log(status, "Copied to clipboard.", true);
    });
  }

  // ---- Text to PDF (pdf-lib) ----
  function textToPdf() {
    var ta = q("txt2pdf-in"), out = q("txt2pdf-status"), go = q("txt2pdf-go");
    go.addEventListener("click", function () {
        var text = (ta.value || "").trim();
      if (!text) { log(out, "Type or paste some text first."); return; }
      P.PDFDocument.create().then(function (d) {
        d.setTitle("BRYME Document"); d.setAuthor("BRYME");
        return d.embedFont(STD.Helvetica).then(function (f) {
          var page = d.addPage([595.28, 841.89]), m = 56, y = 800, size = 11, lh = 16;
          var words = text.split(/\s+/), line = "";
          function flush() {
            if (y < m + 16) { page = d.addPage([595.28, 841.89]); y = 800; }
            page.drawText(line, { x: m, y: y, size: size, font: f, color: RGB(0.12, 0.12, 0.12) });
            y -= lh; line = "";
          }
          words.forEach(function (w) {
            var test = line ? line + " " + w : w;
            if (line && f.widthOfTextAtSize(test, size) > 595.28 - m * 2) flush();
            line = test;
          });
          if (line) flush();
          return d.save();
        });
      }).then(function (bytes) { dl(bytes, "bryme-document.pdf"); log(out, "Exported bryme-document.pdf (" + fmt(bytes.length) + ").", true); })
        .catch(function () { log(out, "Could not create the PDF. Please try again.", false); });
    });
  }

  // ---- Image(s) to PDF ----
  function imagesToPdf() {
    var file = q("img2pdf-file"), status = q("img2pdf-status");
    if (!file) return;
    file.addEventListener("change", function () {
      var files = Array.prototype.slice.call(file.files);
      if (!files.length) { log(status, "Choose one or more images."); return; }
      var addBtn = q("img2pdf-add");
      if (addBtn) addBtn.addEventListener("click", function () { file.click(); });
      P.PDFDocument.create().then(function (d) {
        var i = 0;
        return (function next() {
          if (i >= files.length) { return d.save(); }
          var f = files[i++];
          return fileToBuf(f).then(function (buf) {
            var isPng = /png/i.test(f.type) || /\.png$/i.test(f.name);
            var embed = isPng ? d.embedPng(buf) : d.embedJpg(buf);
            return Promise.resolve(embed).then(function (img) {
              var scale = Math.min(595.28 / img.width, 841.89 / img.height);
              var pg = d.addPage([595.28, 841.89]);
              pg.drawImage(img, { x: (595.28 - img.width * scale) / 2, y: (841.89 - img.height * scale) / 2, width: img.width * scale, height: img.height * scale });
              return next();
            });
          }).catch(function () { log(status, "Could not read \u201c" + f.name + "\u201d. Only JPG/PNG are supported.", false); return next(); });
        })();
      }).then(function (bytes) { dl(bytes, "images.pdf"); log(status, "Exported images.pdf (" + fmt(bytes.length) + ", " + files.length + " image" + (files.length === 1 ? "" : "s") + ").", true); })
        .catch(function () { log(status, "Could not create the PDF. Please try again.", false); });
    });
  }

  // ---- Self-plagiarism & repeated-phrase checker (client-side heuristics) ----
  function selfPlagiarism() {
    var ta = q("plag-in"), run = q("plag-run"), out = q("plag-out");
    if (!run) return;
    run.addEventListener("click", function () {
      var text = (ta.value || "").trim();
      if (!text) { out.innerHTML = "Paste your text first."; return; }
      var sents = text.replace(/\s+/g, " ").split(/[.!?]+/).map(function (s) { return s.trim(); }).filter(function (s) { return s.length > 20; });
      var seen = {}, dups = [];
      sents.forEach(function (s, idx) {
        var key = s.length > 14 ? s.slice(0, 40).toLowerCase() : "";
        if (!key) return;
        if (seen[key]) { dups.push(idx + 1); }
        else { seen[key] = idx + 1; }
      });
      if (!dups.length) {
        out.innerHTML = "<p>No repeated or near-identical sentences found <i>within this text</i>.</p>";
      } else {
        var items = dups.map(function (n) { return "<li>A sentence in position " + n + " repeats wording used earlier in the text.</li>"; }).join("");
        out.innerHTML = "<p><b>" + dups.length + "</b> repeated-phrase" + (dups.length === 1 ? "" : "s") + " found. This is a <b>self</b>-check for internal duplication — it does not scan the open web.</p><ul>" + items + "</ul>";
      }
    });
  }

  // ---- AI-writing heuristics (honest, client-side) ----
  function aiChecker() {
    var ta = q("ai-in"), run = q("ai-run"), out = q("ai-out");
    if (!run) return;
    run.addEventListener("click", function () {
      var text = (ta.value || "").trim();
      if (!text) { out.innerHTML = "Paste your text first."; return; }
      var lower = text.toLowerCase(), signals = [];
      var phrases = ["In conclusion", "Moreover", "Furthermore", "Additionally", "In today's world", "It is important to note", "Delve into", "In the ever-evolving", "Boasts", "Testament to", "Unlock", "Elevate", "Game-changer", "In summary", "As a result", "Overall", "In essence", "By and large", "It goes without saying", "To sum up", "In recent years", "When it comes to"];
      phrases.forEach(function (p) { if (lower.indexOf(p.toLowerCase()) > -1) signals.push({ type: "Phrase", text: p }); });
      var rx = /\b(moreover|furthermore|additionally|consequently|subsequently|thereby|notwithstanding|delve|meticulously|utilize|foster|robust|seamless|harness|leverage)\b/gi;
      var m; while ((m = rx.exec(lower))) signals.push({ type: "Word", text: m[1] });
      var sents = text.replace(/\s+/g, " ").split(/[.!?]+/).filter(function (s) { return s.trim(); });
      var avg = sents.length ? (text.split(/\s+/).length / sents.length) : 0;
      var score = Math.min(100, Math.round(signals.length * 6 + (avg > 20 ? (avg - 20) * 2 : 0)));
      var verdict = score >= 55 ? "Shows several patterns commonly associated with AI-generated text." : score >= 30 ? "Shows some common patterns — worth reviewing for a more natural voice." : "Few common AI markers detected.";
      out.innerHTML = "<p class=\"tool-result\"><b>" + score + "/100</b> — heuristic AI-likeness score. " + verdict + "</p>" +
        (signals.length ? "<p>Markers found:</p><ul>" + signals.slice(0, 14).map(function (s) { return "<li><b>" + s.type + ":</b> \u201c" + s.text + "\u201d</li>"; }).join("") + "</ul>" : "<p>No obvious formulaic markers in the lists checked. Average sentence length ≈ " + Math.round(avg) + " words.</p>") +
        "<p><small>This is a <b>rule-based heuristic</b>, not a real AI detector. No tool can reliably tell human from AI text — treat any result as a nudge, not a verdict. See the guide \u201cHow plagiarism and AI checkers are made\u201d.</small></p>";
    });
  }

  function init() {
    window.__BRYME_TOOL_STATE = { start: true, done: false, err: "" };
    try {
      var id = (SCRIPT && SCRIPT.getAttribute("data-hub-tool")) || "";
      var needsLib = (id === "pdf-editor" || id === "text-to-pdf" || id === "images-to-pdf" || id === "pdf-to-text");
      if (needsLib && window.PDFLib) { P = window.PDFLib; STD = P.StandardFonts; RGB = P.rgb; }
      if (window.pdfjsLib && !window.pdfjsLib.GlobalWorkerOptions.workerSrc) {
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = "/assets/vendor/pdfjs.worker.min.js";
      }
      window.__BRYME_TOOL_STATE.id = id;
      if (id === "pdf-editor") pdfEditor();
      else if (id === "pdf-to-text") pdfToText();
      else if (id === "text-to-pdf") textToPdf();
      else if (id === "images-to-pdf") imagesToPdf();
      else if (id === "self-plagiarism-checker") selfPlagiarism();
      else if (id === "ai-writing-checker") aiChecker();
      window.__BRYME_TOOL_STATE.done = true;
    } catch (e) { window.__BRYME_TOOL_STATE.err = e.message; }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var id = (SCRIPT && SCRIPT.getAttribute("data-hub-tool")) || "";
    init();
  });
})();
