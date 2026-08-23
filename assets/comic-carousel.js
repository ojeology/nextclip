/* BRYME Match Comic — header carousel. 10 cinematic micro-beats.
   ONE speech bubble at a time (Nigerian Pidgin banter). Arrows below the deck.
   BRYME fingerprint + Matchday nav. Auto-builds into #mc-hero. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var S=[
    {img:"01.jpg",tag:"Arrival",min:"PRE-MATCH",h:0,a:0,st:"build",title:"The Tigers land for home",
     pos:[[12,40]],
     ban:[["Home fan","Omo! Nine years! We don come back o!","f"]]},
    {img:"02.jpg",tag:"Kick-off · 1'",min:"1'",h:0,a:0,st:"live",title:"Whistle blow! MKM dey shake",
     pos:[[14,40],[60,38]],
     ban:[["Commentator","Whistle blow! MKM dey shake!","n"],["United fan","Shey na three points we carry come?","u"]]},
    {img:"03.jpg",tag:"12' · Big save",min:"12'",h:0,a:0,st:"live",title:"Tzolakis say no!",
     pos:[[14,40],[60,42]],
     ban:[["Tzolakis","Make dem dey shoot, I dey kampe!","h"],["Mbeumo","How I no score that one?!","u"]]},
    {img:"04.jpg",tag:"16' · Corner",min:"16'",h:0,a:0,st:"live",title:"Corner kick… setup dey load",
     pos:[[14,40],[58,40]],
     ban:[["Slater","Corner kick… everybody enter box!","h"],["BRYME desk","Setup dey load…","n"]]},
    {img:"05.jpg",tag:"17' · Header",min:"17'",h:0,a:0,st:"live",title:"McBurnie head am… saved!",
     pos:[[14,40],[60,42]],
     ban:[["McBurnie","I head am well! Shey e enter?","h"],["Lammens","Saved! No be today!","u"]]},
    {img:"06.jpg",tag:"GOAL · 17'",min:"17'",h:1,a:0,st:"live",title:"AJAYI! Rebound! G-O-A-L!",
     pos:[[40,40],[14,42]],
     ban:[["Ajayi","REBOUND! G-O-A-L! Na me o!","h"],["Home fan","E choke!!! We don score!","f"]]},
    {img:"07.jpg",tag:"1–0",min:"17'",h:1,a:0,st:"live",title:"Nine years wait… e sweet!",
     pos:[[14,40],[60,42]],
     ban:[["Ajayi","Nine years wait… e sweet to score!","h"],["Bruno","Who mark am?! Who do this?!","u"]]},
    {img:"08.jpg",tag:"34' · Yellow",min:"34'",h:1,a:0,st:"live",title:"Dorgu see yellow",
     pos:[[14,40],[60,42]],
     ban:[["Dorgu","Yellow?! I no even touch am well!","u"],["Referee","Na card be that. No begging.","r"]]},
    {img:"09.jpg",tag:"37' · Free kick",min:"37'",h:1,a:0,st:"live",title:"Free kick… danger dey load",
     pos:[[14,40]],
     ban:[["Slater","Free kick… make we wound dem again.","h"]]},
    {img:"10.jpg",tag:"GOAL · 38'",min:"38'",h:2,a:0,st:"live",title:"MENDY! Header! Two-zero!",
     pos:[[40,38],[14,44]],
     ban:[["Mendy","Header! Two-zero! Otilo!","h"],["Maguire","Set pieces go kill me, I swear.","u"]]}
  ];
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  var POS=[[14,40]];
  var STEP=4200, VISIBLE=3200, LEAD=600;   // strictly ONE bubble at a time (STEP > VISIBLE)
  function init(){
    var root=document.getElementById("mc-hero"); if(!root) return;
    root.className="mc";
    root.innerHTML=
      '<div class="mc-bars" aria-hidden="true"></div>'+
      '<div class="mc-deck">'+
        '<div class="mc-track"></div>'+
        '<div class="mc-hud"><span class="mc-pill" id="mcpill"></span><span class="mc-score" id="mcscore"></span></div>'+
        '<div class="mc-mark"><b>BRYME</b><span>@bryme</span></div>'+
      '</div>'+
      '<div class="mc-cap"><span class="mc-tag" id="mctag"></span><h2 id="mctitle"></h2></div>'+
      '<div class="mc-ctrl">'+
        '<button class="mc-nav mc-prev" aria-label="Previous">‹ Prev</button>'+
        '<div class="mc-dots"></div>'+
        '<button class="mc-play" aria-pressed="true">⏸ Pause</button>'+
        '<button class="mc-nav mc-next" aria-label="Next">Next ›</button>'+
        '<span class="mc-cnt" id="mccnt"></span>'+
      '</div>'+
      '<div class="mc-md">'+
        '<span class="mc-md-i on"><span class="mc-md-n">● Matchday 1</span><span class="mc-md-s">Hull 2–0 United · playing now</span></span>'+
        '<a class="mc-md-i soon" href="/sports/premier-league/"><span class="lock">🔒</span><span class="mc-md-n">Matchday 2</span><span class="mc-md-s">Comic drops after full time</span></a>'+
        '<a class="mc-md-i soon" href="/sports/premier-league/"><span class="lock">🔒</span><span class="mc-md-n">Matchday 3</span><span class="mc-md-s">Coming soon</span></a>'+
      '</div>';
    var track=root.querySelector(".mc-track"),dotsEl=root.querySelector(".mc-dots"),barsEl=root.querySelector(".mc-bars"),
        pill=root.querySelector("#mcpill"),score=root.querySelector("#mcscore"),tag=root.querySelector("#mctag"),
        title=root.querySelector("#mctitle"),cntEl=root.querySelector("#mccnt"),playBtn=root.querySelector(".mc-play"),
        deck=root.querySelector(".mc-deck"),len=S.length;
    track.innerHTML=S.map(function(s,i){
      var bubs=s.ban.map(function(b,j){var p=(s.pos&&s.pos[j])||POS[j%POS.length];
        return '<div class="mc-bubble '+b[2]+'" style="left:'+p[0]+'%;top:'+p[1]+'%"><i>'+b[0]+'</i>'+b[1]+'</div>';}).join("");
      return '<div class="mc-card"><img src="'+DIR+s.img+'" alt="Original BRYME comic frame: '+s.title+'" loading="'+(i?"lazy":"eager")+'"><div class="mc-bub">'+bubs+'</div></div>';
    }).join("");
    dotsEl.innerHTML=S.map(function(s,i){return '<button type="button" aria-label="Panel '+(i+1)+'"></button>';}).join("");
    barsEl.innerHTML=S.map(function(){return '<i><span></span></i>';}).join("");
    var cards=[].slice.call(track.children);
    var dots=[].slice.call(dotsEl.children);
    var bars=[].slice.call(barsEl.children).map(function(b){return b.firstChild;});
    dots.forEach(function(b,i){b.addEventListener("click",function(){show(i,i>idx?"next":"prev");});});

    var idx=0,playing=true,hover=false,elapsed=0,last=0,timers=[];
    function durFor(i){return LEAD+(S[i].ban.length-1)*STEP+VISIBLE+1200;}
    function clearTimers(){timers.forEach(clearTimeout);timers=[];}
    function scheduleBubbles(c){            // strictly sequential: one appears, holds, leaves, then next
      clearTimers();
      var bubs=c.querySelectorAll(".mc-bubble");
      bubs.forEach(function(el,i){
        timers.push(setTimeout(function(){el.classList.add("in");},LEAD+i*STEP));
        timers.push(setTimeout(function(){el.classList.remove("in");},LEAD+i*STEP+VISIBLE));
      });
    }
    function updateHud(){
      var s=S[idx],st=s.st;
      pill.className="mc-pill "+(st==="live"?"live":st==="ft"?"ft":"");
      pill.innerHTML=(st==="live"?'<span class="d"></span>':'')+PILL[st];
      score.innerHTML='<span class="t h"><span class="sw"></span>HUL</span>'+s.h+'–'+s.a+'<span class="t u">UTD<span class="sw"></span></span><span class="min">'+s.min+'</span>';
      tag.textContent=s.tag;title.textContent=s.title;
    }
    function show(n,dir){
      var old=idx;idx=((n%len)+len)%len;var c=cards[idx];
      if(old!==idx){var o=cards[old];o.classList.remove("on");o.classList.add(dir==="next"?"left":"right");
        o.querySelectorAll(".mc-bubble").forEach(function(e){e.classList.remove("in");});}
      c.style.transition="none";c.classList.remove("on","left","right");c.classList.add(dir==="next"?"right":"left");
      void c.offsetWidth;c.style.transition="";c.classList.remove("right","left");c.classList.add("on");
      dots.forEach(function(d,i){d.classList.toggle("on",i===idx);});
      cntEl.textContent=(idx+1)+" / "+len;updateHud();elapsed=0;last=performance.now();
      scheduleBubbles(c);
    }
    function loop(now){var dt=now-last;last=now;
      if(playing&&!hover){elapsed+=dt;if(elapsed>=durFor(idx))show(idx+1,"next");}
      for(var i=0;i<len;i++){var w;i<idx?w=100:i===idx?w=Math.min(100,elapsed/durFor(idx)*100):w=0;bars[i].style.width=w+"%";}
      requestAnimationFrame(loop);
    }
    function pause(){if(!playing)return;playing=false;clearTimers();
      // keep the current bubble visible while paused
      var b=cards[idx].querySelectorAll(".mc-bubble");if(b.length)b[b.length-1].classList.add("in");
      playBtn.setAttribute("aria-pressed","false");playBtn.textContent="▶ Play";}
    function resume(){if(playing)return;playing=true;playBtn.setAttribute("aria-pressed","true");playBtn.textContent="⏸ Pause";
      elapsed=0;last=performance.now();scheduleBubbles(cards[idx]);}
    root.querySelector(".mc-next").addEventListener("click",function(){show(idx+1,"next");});
    root.querySelector(".mc-prev").addEventListener("click",function(){show(idx-1,"prev");});
    playBtn.addEventListener("click",function(){playing?pause():resume();});
    deck.addEventListener("mouseenter",function(){hover=true;});
    deck.addEventListener("mouseleave",function(){hover=false;last=performance.now();});
    var sx=null;
    deck.addEventListener("touchstart",function(e){sx=e.touches[0].clientX;},{passive:true});
    deck.addEventListener("touchend",function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>44)show(dx<0?idx+1:idx-1,dx<0?"next":"prev");sx=null;},{passive:true});
    document.addEventListener("keydown",function(e){if(e.key==="ArrowRight")show(idx+1,"next");else if(e.key==="ArrowLeft")show(idx-1,"prev");});
    var m=(location.hash||"").match(/p(\d+)/);
    var start=m&&m[1]?Math.min(Math.max(+m[1]-1,0),len-1):0;
    cards[start].classList.add("on");dots[start].classList.add("on");idx=start;
    cntEl.textContent=(start+1)+" / "+len;updateHud();scheduleBubbles(cards[start]);
    last=performance.now();requestAnimationFrame(loop);
  }
  if(document.readyState!=="loading")init();
  else document.addEventListener("DOMContentLoaded",init);
})();
