/* BRYME Match Comic — header carousel logic. Auto-builds into #mc-hero. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var S=[
    {img:"01-return.jpg",tag:"Arrival · Build-up",min:"PRE-MATCH",h:0,a:0,st:"build",
     title:"The Tigers arrive home",copy:"MKM Stadium, 22 Aug 2026. First top-flight home night in nine years. The coach pulls in — and the place loses its mind.",
     ban:[["Home fan","Nine years. NINE. Even my GRAN made it and she's 90.","f"],["Hull","We're home, lads. Breathe it in. Then ruin someone's evening.","h"],["Mascot","Roar for the camera. Good. I'm paid in sandwiches.","n"],["United fan","Lovely stadium. Shame about the result we're about to hand you.","u"],["Steward","Don't pitch-inv— oh, they're already crying. It's been four minutes.","n"]]},
    {img:"02-opener.jpg",tag:"Goal · 17'",min:"17'",h:1,a:0,st:"live",
     title:"Ajayi. Rebound. Bedlam.",copy:"McBurnie's effort is saved. The rebound drops. Semi Ajayi says thank you very much.",
     ban:[["Ajayi","MINE. Thank you. Goodnight.","h"],["McBurnie","That was MY rebound... I was LITERALLY right there, Semi!","h"],["Ajayi","Were you? Didn't see you. Ball did, though. Shame.","h"],["Bruno","WHO was marking?! Am I defending now?! AM I?!","u"],["Home fan","GOAL! I've waited nine years — worth every single one!","f"]]},
    {img:"03-second.jpg",tag:"Goal · 38'",min:"38'",h:2,a:0,st:"live",
     title:"Mendy. Header. Again.",copy:"Slater's free-kick. Mendy climbs above everyone. Two-nil. The set-piece specialists strike twice.",
     ban:[["Mendy","Again? Oh — again. Two goals, no fuss. Taxi for the defence.","h"],["Bruno","A SET PIECE. Another one! Who's on the post?!","u"],["Maguire","...there was a post? Nobody told me about a post.","u"],["Bruno","Harry. HARRY. You're six-foot-four. JUMP.","u"],["BRYME desk","Two centre-backs, two set pieces. Statues in red.","n"]]},
    {img:"04-halftime.jpg",tag:"Half-time",min:"HT",h:2,a:0,st:"ht",
     title:"Two rooms. Two worlds.",copy:"Same scoreline, very different conversations. Carrick erases the board. Rashford laces up.",
     ban:[["Jakirović","2–0 is a trap, not a trophy. Don't you DARE blow it.","h"],["Carrick","So... we mark the tall ones. And the short ones. And basically everyone.","u"],["Bruno","I blame the wind. And the posts. And — honestly? — you.","u"],["Rashford","I'll fix it. Boots on. Send me out alone if I have to.","u"],["Kitman","Same again, lads? Tape, boots, and NO more conceding.","n"]]},
    {img:"05-rashford.jpg",tag:"Under siege · 56'",min:"56'",h:2,a:0,st:"live",
     title:"72% of absolutely nothing",copy:"Rashford's on. United swarm. Hull turn into a wall with gloves. Tzolakis has, frankly, had a little nap.",
     ban:[["United","72% possession! We're DOMINATING!","u"],["Hull","Cute. We're WINNING. Different word — look it up.","h"],["Tzolakis","Keep knocking. I've genuinely had a nap back here.","h"],["Bruno","PASS! No — HIM. Not him. WHY is nobody where I want them?!","u"],["Home fan","Boooo— oh, they've still not scored. Every. Single. Time.","f"]]},
    {img:"06-subs.jpg",tag:"Late drama · 90+6'",min:"90+6'",h:2,a:0,st:"live",
     title:"The wall holds. Millar smiles.",copy:"Tzolakis tips one over. Sesko can't believe it. Millar gets a yellow at 2–0 and just shrugs.",
     ban:[["Tzolakis","Tipped over. Lovely. Next customer.","h"],["Sesko","Six chances. SIX. The man's a wall. With gloves. And an attitude.","u"],["Millar","A yellow?! At 2–0?! I barely breathed near him!","h"],["Referee","Still a yellow, son. No loyalty cards at 2–0.","r"],["Bruno","This is fine. This is FINE. (it is not fine)","u"]]},
    {img:"07-fulltime.jpg",tag:"Full time",min:"FT",h:2,a:0,st:"ft",
     title:"FULL TIME. Pandemonium.",copy:"The whistle goes. Hull hit the deck, the air, each other. United's 72% possession boards exactly zero points.",
     ban:[["Hull","FULL TIME!!! Somebody pinch me!","h"],["Bruno","...","u"],["Maguire","I'd like the ground to swallow me now. Cheers.","u"],["Home fan","72% possession, zero points. My new favourite maths.","f"],["Ajayi","Nobody gave us a chance. Absolutely nobody. Beautiful.","h"]]},
    {img:"08-aftermath.jpg",tag:"Welcome back",min:"FT",h:2,a:0,st:"ft",
     title:"Red Devils? More like Crying Devils.",copy:"Ajayi 17. Mendy 38. Three yellows, no reds. Nine years away — one unforgettable night home. And the Devils are in bits.",
     ban:[["BRYME desk","The Red Devils? Tonight they're the Crying Devils — heads down, ties loosened, dreams deleted.","n"],["Bruno","*sniff* we had 72% of the ball and 0% of the joy.","u"],["Maguire","*a single tear rolls* ...set pieces.","u"],["Home fan","Welcome back to the Premier League! Same again next week?","f"],["Ajayi","Tigers ROAR. Devils dribble. On their faces.","h"]]}
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
