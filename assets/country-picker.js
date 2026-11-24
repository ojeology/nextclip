/* ================================================================
   The country picker — assets/country-picker.js
   ----------------------------------------------------------------
   "The country selection looks stupid. It should be something where
   you select your flag or type your country name." (owner,
   2026-11-24)

   It was a native <select> with 110 options grouped by continent.
   This replaces the interface, not the control: the <select> stays in
   the page, one pixel wide, still holding every option and every
   count. Reading it rather than duplicating it means the picker can
   never disagree with the filter that actually runs, and the existing
   harness that sets #f-country directly keeps working.

   Behaviour: type to filter, arrow keys to move, Enter to choose,
   Esc to close, click outside to dismiss. Flags are derived from the
   ISO code in the option value, so a new country needs no new asset.
   ================================================================ */
(function () {
  "use strict";

  var POPULAR = ["NG", "GB", "US", "CA", "AU", "KE", "ZA", "IN", "GH"];

  function flag(iso) {
    if (!/^[A-Za-z]{2}$/.test(iso)) return "\uD83C\uDF0D"; /* globe */
    return String.fromCodePoint.apply(null, iso.toUpperCase().split("").map(function (c) {
      return 0x1f1e6 + c.charCodeAt(0) - 65;
    }));
  }

  function labelOf(text) {
    /* "Nigeria — 12" becomes name "Nigeria", count "12"; so does
       "All countries — 304 publications". The button shows the name only. */
    var m = text.split(/\s+[—–-]\s+(\d+)\b/);
    return { name: (m[0] || text).trim(), count: (m[1] || "").trim() };
  }

  function init(root) {
    var sel = root.querySelector("select");
    var btn = root.querySelector(".cpick-btn");
    var pop = root.querySelector("[data-cpick-pop]");
    var q = root.querySelector(".cpick-q");
    var list = root.querySelector(".cpick-list");
    var none = root.querySelector(".cpick-none");
    var flagEl = btn.querySelector(".cpick-flag");
    var valEl = btn.querySelector(".cpick-val");
    if (!sel || !btn || !pop || !q || !list) return;

    /* ---- build the list once, from the select's own options ---- */
    var groups = [];
    var every = [];
    Array.prototype.forEach.call(sel.children, function (node) {
      if (node.tagName === "OPTGROUP") {
        groups.push({ label: node.label, items: Array.prototype.map.call(node.children, read) });
      } else if (node.tagName === "OPTION") {
        groups.push({ label: "", items: [read(node)] });
      }
    });
    function read(o) {
      var l = labelOf(o.textContent);
      var item = {
        value: o.value, name: l.name, count: l.count,
        text: (l.name + " " + l.count + " " + o.value).toLowerCase(),
        el: null
      };
      every.push(item);
      return item;
    }

    var popular = POPULAR.map(function (iso) {
      return every.filter(function (it) { return it.value === iso; })[0];
    }).filter(Boolean);

    function render(needle) {
      var n = (needle || "").trim().toLowerCase();
      list.innerHTML = "";
      none.hidden = true;
      var hits = 0;

      function addGroup(label, items) {
        var kept = items.filter(function (it) { return !n || it.text.indexOf(n) !== -1; });
        if (!kept.length) return;
        hits += kept.length;
        if (label) {
          var h = document.createElement("li");
          h.className = "cpick-group";
          h.setAttribute("role", "presentation");
          h.textContent = label;
          list.appendChild(h);
        }
        kept.forEach(function (it) {
          var li = document.createElement("li");
          li.setAttribute("role", "option");
          li.tabIndex = -1;
          li.dataset.value = it.value;
          li.innerHTML =
            '<span class="cpick-flag" aria-hidden="true">' + flag(it.value) + "</span>" +
            '<span class="cpick-name"></span>' +
            (it.count ? '<span class="cpick-n">' + it.count + "</span>" : "");
          li.querySelector(".cpick-name").textContent = it.name;
          if (it.value === sel.value) li.setAttribute("aria-selected", "true");
          li.addEventListener("mousedown", function (e) { e.preventDefault(); choose(it.value); });
          list.appendChild(li);
          it.el = li;
        });
      }

      if (!n && popular.length) addGroup("Popular", popular);
      groups.forEach(function (g) { addGroup(g.label, g.items); });
      none.hidden = hits !== 0;
    }

    function syncButton() {
      var opt = sel.options[sel.selectedIndex];
      var l = opt ? labelOf(opt.textContent) : { name: "All countries" };
      flagEl.textContent = flag(sel.value);
      valEl.textContent = l.name;
    }

    function open() {
      pop.hidden = false;
      btn.setAttribute("aria-expanded", "true");
      q.value = "";
      render("");
      q.focus();
    }

    function close() {
      pop.hidden = true;
      btn.setAttribute("aria-expanded", "false");
    }

    function choose(value) {
      if (sel.value !== value) {
        sel.value = value;
        /* Let the rest of the page react exactly as it always did. */
        sel.dispatchEvent(new Event("change", { bubbles: true }));
        sel.dispatchEvent(new Event("input", { bubbles: true }));
      }
      syncButton();
      close();
      btn.focus();
    }

    btn.addEventListener("click", function () {
      pop.hidden ? open() : close();
    });
    q.addEventListener("input", function () { render(q.value); });

    /* keyboard: down/up walk the visible options, Enter takes one */
    function move(step) {
      var opts = Array.prototype.slice.call(list.querySelectorAll('[role="option"]'));
      if (!opts.length) return;
      var i = opts.indexOf(document.activeElement);
      var next = opts[Math.max(0, Math.min(opts.length - 1, i === -1 ? (step > 0 ? 0 : opts.length - 1) : i + step))];
      if (next) next.focus();
    }
    root.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(); btn.focus(); return; }
      if (pop.hidden) {
        if (e.key === "ArrowDown" || e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); }
        return;
      }
      if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
      else if (e.key === "Enter") {
        var active = document.activeElement;
        if (active && active.getAttribute("role") === "option") {
          e.preventDefault();
          choose(active.dataset.value);
        }
      }
    });
    list.addEventListener("click", function (e) {
      var li = e.target.closest('[role="option"]');
      if (li) choose(li.dataset.value);
    });
    document.addEventListener("click", function (e) {
      if (!root.contains(e.target)) close();
    });

    /* The page can change the select behind our back - a URL parameter, a
       reset button, the test harness. Follow it rather than drift from it. */
    sel.addEventListener("change", syncButton);
    syncButton();
  }

  var roots = document.querySelectorAll("[data-cpick]");
  if (!roots.length) return;
  /* The stylesheet shows the native select by default and swaps in the button
     only once this script is running - so a reader with JavaScript off keeps a
     control that works instead of a dead one. */
  document.documentElement.classList.add("cpick-ready");
  Array.prototype.forEach.call(roots, init);
})();
