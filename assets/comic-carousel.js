/* BRYME Match Comic — FULL-BLEED cinematic carousel. 6 states, Naija Pidgin banter.
   ONE speech bubble at a time. Arrows below. BRYME fingerprint + Matchday nav. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var S=[
    {img:"02.jpg",tag:"Kick-off",min:"1'",h:0,a:0,st:"live",title:"9 years done — Hull don return!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","9 years for relegation jail, Hull City enter Premier League like person wey collect alert!","c"],
          ["United player","Why these people dey run like say dem drink fuel? Calm down na!","u"],
          ["Hull player","My friend, welcome back to Premier League! No rest for the wicked today!","h"]]},
    {img:"03.jpg",tag:"12' · Save",min:"12'",h:0,a:0,st:"live",title:"Tzolakis catch am like rent!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","United dey find tiki-taka, Hull dey find trouble! Tzolakis catch ball like landlord wey come collect house rent!","c"],
          ["Mbeumo","How this goalkeeper take catch that one?! E be like say he get three hands!","u"],
          ["Tzolakis","Welcome to Hull, my brother. Carry your ball go front!","h"]]},
    {img:"06.jpg",tag:"GOAL · 17'",min:"17'",h:1,a:0,st:"live",title:"AJAYI scatter net! 1–0!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","GOOOAL! Ajayi run enter box like debt collector, scatter net! Hull 1–0 United!","c"],
          ["Ajayi","Scatter the net! Dem think say we come here to play!","h"],
          ["United defender","Wait... wetin just happen? We wey suppose control game?","u"]]},
    {img:"10.jpg",tag:"GOAL · 38'",min:"38'",h:2,a:0,st:"live",title:"MENDY fly! 2–0 o!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Lightning strikes twice! Mendy rise like helicopter for set-piece—2–0 o!","c"],
          ["Mendy","Fly high! Another set piece chop una clean!","h"],
          ["Bruno Fernandes","How we con leave tall man like this for free header again?!","u"]]},
    {img:"11.jpg",tag:"60' · Possession",min:"60'",h:2,a:0,st:"live",title:"72% award vs 3 points",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Man United fans currently holding 72% possession award, while Hull fans are busy counting their 3 points.","c"],
          ["United player","Omo, we get 72% possession o! We dey dictate the pace!","u"],
          ["Hull defender","Eyah. Sorry say possession no dey inside soup. 2–0 still remains 2–0!","h"]]},
    {img:"12.jpg",tag:"Full time",min:"FT",h:2,a:0,st:"ft",title:"Tigers are back — and starving!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Full time! Tigers show Premier League say wetin pass you, make you leave am for owners!","c"],
          ["Rashford","We come all this way... only to chop premium tears.","u"],
          ["Hull captain","Go tell them say the Tigers are back, and we starving!","h"]]}
  ];
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  var POS=[[28,56],[8,62],[54,60]];
  var STEP=3700, VISIBLE=3000, LEAD=500;   // strictly ONE bubble at a time (STEP > VISIBLE)
  function init(){
    var root=document.getElementById("mc-hero"); if(!root) return;
    root.className="mc";
    root.innerHTML=
      '<div class="mc-deck">'+
        '<div class="mc-bars" aria-hidden="true"></div>'+
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
    function durFor(i){return LEAD+(S[i].ban.length-1)*STEP+VISIBLE+1100;}
    function clearTimers(){timers.forEach(clearTimeout);timers=[];}
    function scheduleBubbles(c){            // strictly sequential: one appears, holds, leaves, then the next
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
    cards[0].classList.add("on");dots[0].classList.add("on");idx=0;
    cntEl.textContent="1 / "+len;updateHud();scheduleBubbles(cards[0]);
    last=performance.now();requestAnimationFrame(loop);
  }
  if(document.readyState!=="loading")init();
  else document.addEventListener("DOMContentLoaded",init);
})();
