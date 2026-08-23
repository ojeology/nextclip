/* BRYME Match Comic — header carousel logic. Auto-builds into #mc-hero. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var S=[
    {img:"01-return.jpg",tag:"Arrival · Build-up",min:"PRE-MATCH",h:0,a:0,st:"build",
     title:"The Tigers arrive home",copy:"MKM Stadium, 22 Aug 2026. First top-flight home night in nine years. The coach pulls in — and the place erupts.",
     ban:[["Home fan","Nine years. NINE. Don't you dare mess this up.","f"],["Hull","We're home, lads. Breathe it in.","h"],["Hull","First night back. Let's give 'em a show.","h"],["Mascot","Roar for the camera. Good. Now go win.","n"],["United fan","Lovely ground. We'll be taking the points though.","u"]]},
    {img:"02-opener.jpg",tag:"Goal · 17'",min:"17'",h:1,a:0,st:"live",
     title:"Ajayi. Rebound. Bedlam.",copy:"McBurnie's effort is saved. The rebound drops. Semi Ajayi says thank you very much.",
     ban:[["Ajayi","MINE.","h"],["McBurnie","That was MY rebound... I was RIGHT there.","h"],["Lammens","It just hit me. Through a crowd. Help.","u"],["United","We only just got here. Still doing up our laces.","u"],["Home fan","GOAL! I've waited NINE YEARS for that!","f"]]},
    {img:"03-second.jpg",tag:"Goal · 38'",min:"38'",h:2,a:0,st:"live",
     title:"Mendy. Header. Again.",copy:"Slater's free-kick. Mendy climbs above everyone. Two-nil. The set-piece specialists strike twice.",
     ban:[["Mendy","Again? Oh — again. Lovely.","h"],["Bruno","Not ANOTHER set piece. Who's marking?","u"],["Hull","It's the set pieces. Always the set pieces.","h"],["Maguire","...we practiced these. We PRACTICED these.","u"],["BRYME desk","Two centre-backs. Two set pieces. Textbook chaos.","n"]]},
    {img:"04-halftime.jpg",tag:"Half-time",min:"HT",h:2,a:0,st:"ht",
     title:"Two rooms. Two worlds.",copy:"Same scoreline, very different conversations. Carrick erases the board. Rashford laces up.",
     ban:[["Jakirović","2–0 is a trap, not a trophy. Stay switched on.","h"],["Carrick","Somebody... explain the set pieces. Use small words.","u"],["Rashford","I'll fix it. Get me ready. Now.","u"],["Kitman","Same again, lads? Boots, tape, and no conceding.","n"],["United fan","A whole half to fix this. Surely. Surely.","u"]]},
    {img:"05-rashford.jpg",tag:"Under siege · 56'",min:"56'",h:2,a:0,st:"live",
     title:"72% of absolutely nothing",copy:"Rashford's on. United swarm. Hull become a wall with gloves. Tzolakis is, frankly, bored.",
     ban:[["United","We've got the ball! 72%!","u"],["Hull","Cute. We've got the lead.","h"],["Tzolakis","Keep knocking, lads. I'm genuinely bored.","h"],["Bruno","PASS! Move! Somebody do SOMETHING!","u"],["Home fan","Boooo... oh, they still haven't scored. Ha.","f"]]},
    {img:"06-subs.jpg",tag:"Late drama · 90+6'",min:"90+6'",h:2,a:0,st:"live",
     title:"The wall holds. Millar smiles.",copy:"Tzolakis tips one over. Sesko can't believe it. Millar gets a yellow at 2–0 and just shrugs.",
     ban:[["Tzolakis","Over the bar. NEXT.","h"],["Sesko","How are we losing this?! HOW?!","u"],["Millar","A yellow? At 2–0?! I barely breathed on him!","h"],["Referee","Still a yellow. I don't do group discounts.","r"],["Hull sub","Fresh legs. Same wall. Good luck, lads.","h"]]},
    {img:"07-fulltime.jpg",tag:"Full time",min:"FT",h:2,a:0,st:"ft",
     title:"FULL TIME. Pandemonium.",copy:"The whistle goes. Hull hit the deck, the air, each other. United's 72% possession boards exactly zero points.",
     ban:[["Hull","FULL TIME!!! Get in!!!","h"],["Bruno","...","u"],["Home fan","Enjoy your 72% possession, lads. Cheers.","f"],["Maguire","Longest ninety minutes of my life.","u"],["Ajayi","Nobody gave us a chance. Lovely.","h"]]},
    {img:"08-aftermath.jpg",tag:"Welcome back",min:"FT",h:2,a:0,st:"ft",
     title:"The Tigers are back.",copy:"Ajayi 17. Mendy 38. Three yellows, no reds. Nine years away — one unforgettable night home.",
     ban:[["Home fan","Welcome back to the Premier League!","f"],["Home fan","Man United won't forget this one. Neither will we.","f"],["Ajayi","Tigers. ROAR.","h"],["Mendy","Same time next week?","h"],["Carrick","...back to the drawing board. Literally.","u"]]}
  ];
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  function init(){
    var root=document.getElementById("mc-hero"); if(!root) return;
    root.className="mc";
    root.innerHTML=
      '<div class="mc-bars" aria-hidden="true"></div>'+
      '<div class="mc-deck"><button class="mc-arr pv" aria-label="Previous">‹</button>'+
        '<div class="mc-track"></div>'+
        '<button class="mc-arr nx" aria-label="Next">›</button></div>'+
      '<div class="mc-info" aria-live="polite"></div>'+
      '<div class="mc-ctrl"><div class="mc-dots"></div><button class="mc-play" aria-pressed="true">⏸ Pause</button><span class="mc-cnt"></span></div>';
    var track=root.querySelector(".mc-track"),info=root.querySelector(".mc-info"),
        dotsEl=root.querySelector(".mc-dots"),barsEl=root.querySelector(".mc-bars"),
        cntEl=root.querySelector(".mc-cnt"),playBtn=root.querySelector(".mc-play"),
        deck=root.querySelector(".mc-deck"),len=S.length;
    track.innerHTML=S.map(function(s,i){
      return '<div class="mc-card"><img src="'+DIR+s.img+'" alt="Original BRYME comic frame: '+s.title+'" loading="'+(i?"lazy":"eager")+'"></div>';
    }).join("");
    dotsEl.innerHTML=S.map(function(s,i){return '<button type="button" aria-label="Panel '+(i+1)+'"></button>';}).join("");
    barsEl.innerHTML=S.map(function(){return '<i><span></span></i>';}).join("");
    var cards=[].slice.call(track.children);
    var dots=[].slice.call(dotsEl.children);
    var bars=[].slice.call(barsEl.children).map(function(b){return b.firstChild;});
    dots.forEach(function(b,i){b.addEventListener("click",function(){show(i,i>idx?"next":"prev");reset();});});

    function renderInfo(){
      var s=S[idx];
      info.innerHTML=
        '<div class="mc-row1">'+
          '<span class="mc-pill '+(s.st==="live"?"live":s.st==="ft"?"ft":"")+'">'+(s.st==="live"?'<span class="d"></span>':'')+PILL[s.st]+'</span>'+
          '<span class="mc-score"><span class="t h"><span class="sw"></span>HUL</span>'+s.h+'–'+s.a+'<span class="t u">UTD<span class="sw"></span></span><span class="min">'+s.min+'</span></span>'+
          '<span class="mc-tag">'+s.tag+'</span>'+
        '</div>'+
        '<h2 class="mc-title">'+s.title+'</h2>'+
        '<p class="mc-copy">'+s.copy+'</p>'+
        '<div class="mc-ban">'+s.ban.map(function(b){return '<q class="'+b[2]+'"><i>'+b[0]+'</i>'+b[1]+'</q>';}).join("")+'</div>';
    }
    var idx=0,DUR=6500,playing=true,hover=false,elapsed=0,last=0;
    function show(n,dir){
      var old=idx; idx=((n%len)+len)%len; var c=cards[idx];
      if(old!==idx){var o=cards[old];o.classList.remove("on");o.classList.add(dir==="next"?"left":"right");}
      c.style.transition="none";c.classList.remove("on","left","right");c.classList.add(dir==="next"?"right":"left");
      void c.offsetWidth;c.style.transition="";c.classList.remove("right","left");c.classList.add("on");
      dots.forEach(function(d,i){d.classList.toggle("on",i===idx);});
      cntEl.textContent=(idx+1)+" / "+len; renderInfo(); reset();
    }
    function reset(){elapsed=0;last=performance.now();}
    function loop(now){var dt=now-last;last=now;
      if(playing&&!hover){elapsed+=dt;if(elapsed>=DUR)show(idx+1,"next");}
      for(var i=0;i<len;i++){var w;i<idx?w=100:i===idx?w=Math.min(100,elapsed/DUR*100):w=0;bars[i].style.width=w+"%";}
      requestAnimationFrame(loop);
    }
    root.querySelector(".mc-arr.nx").addEventListener("click",function(){show(idx+1,"next");});
    root.querySelector(".mc-arr.pv").addEventListener("click",function(){show(idx-1,"prev");});
    playBtn.addEventListener("click",function(){playing=!playing;playBtn.setAttribute("aria-pressed",String(playing));playBtn.textContent=playing?"⏸ Pause":"▶ Play";});
    deck.addEventListener("mouseenter",function(){hover=true;});
    deck.addEventListener("mouseleave",function(){hover=false;last=performance.now();});
    var sx=null;
    deck.addEventListener("touchstart",function(e){sx=e.touches[0].clientX;},{passive:true});
    deck.addEventListener("touchend",function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>44)show(dx<0?idx+1:idx-1,dx<0?"next":"prev");sx=null;},{passive:true});
    document.addEventListener("keydown",function(e){if(e.key==="ArrowRight")show(idx+1,"next");else if(e.key==="ArrowLeft")show(idx-1,"prev");});
    var m=(location.hash||"").match(/p(\d+)/);
    var start=m&&m[1]?Math.min(Math.max(+m[1]-1,0),len-1):0;
    cards[start].classList.add("on");dots[start].classList.add("on");idx=start;
    cntEl.textContent=(start+1)+" / "+len;renderInfo();
    last=performance.now();requestAnimationFrame(loop);
  }
  if(document.readyState!=="loading")init();
  else document.addEventListener("DOMContentLoaded",init);
})();
