/* BRYME trailer facades - click to load. Nothing runs until the visitor presses
   the button; then the official YouTube trailer plays in this page (nocookie).
   v2: modestbranding + rel=0 to match the restored NEXTCLIP player behaviour. */
(function () {
  "use strict";
  document.addEventListener("click", function (e) {
    var b = e.target && e.target.closest ? e.target.closest(".trailer-play") : null;
    if (!b || b.getAttribute("data-done")) return;
    var id = b.getAttribute("data-yt");
    var title = b.getAttribute("data-title") || "Official trailer";
    if (!id || !/^[A-Za-z0-9_-]{6,20}$/.test(id)) return;
    b.setAttribute("data-done", "1");
    var f = document.createElement("iframe");
    f.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&modestbranding=1");
    f.setAttribute("title", title);
    f.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture");
    f.setAttribute("allowfullscreen", "");
    f.setAttribute("referrerpolicy", "strict-origin-when-cross-origin");
    b.parentNode.appendChild(f);
    b.remove();
  }, false);
})();
