/* BRYME Match Comic — header carousel. Transient speech bubbles that match the
   action on screen, slide-left, autoplay, BRYME fingerprint + Matchday nav. Auto-builds into #mc-hero. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var S=[
    {img:"01-return.jpg",tag:"Arrival · Build-up",min:"PRE-MATCH",h:0,a:0,st:"build",
     title:"The Tigers arrive home",copy:"MKM Stadium, 22 Aug 2026. First top-flight home night in nine years.",
     pos:[[10,58],[40,26],[70,18],[62,62]],
     ban:[["Home fan","Nine years. NINE. We waited for this.","f"],["Hull captain","We're home, lads. Now ruin their evening.","h"],["Mascot","Smile for the camera. I'm paid in sandwiches.","n"],["United fan","Lovely stadium. Shame about the result, eh.","u"]]},
    {img:"02-opener.jpg",tag:"Goal · 17'",min:"17'",h:1,a:0,st:"live",
     title:"Ajayi. Rebound. Bedlam.",copy:"McBurnie's effort is saved. The rebound drops. Semi Ajayi says thank you.",
     pos:[[44,30],[10,52],[64,14],[12,18]],
     ban:[["Ajayi","MINE. Thank you. Goodnight.","h"],["McBurnie","Oi! That was MY rebound, Semi!","h"],["Bruno","WHO was marking?! Am I the defender now?!","u"],["Home fan","GOAL! Nine years — worth every one!","f"]]},
    {img:"03-second.jpg",tag:"Goal · 38'",min:"38'",h:2,a:0,st:"live",
     title:"Mendy. Header. Again.",copy:"Slater's free-kick. Mendy climbs above everyone. Two-nil.",
     pos:[[40,28],[64,14],[66,58],[10,16]],
     ban:[["Mendy","Two headers. No fuss. Taxi for the lot of you.","h"],["Bruno","A SET PIECE! Who left the post empty?!","u"],["Maguire","...there was a post? Nobody told me.","u"],["BRYME desk","Two centre-backs, two set pieces. Statues in red.","n"]]},
    {img:"04-halftime.jpg",tag:"Half-time",min:"HT",h:2,a:0,st:"ht",
     title:"Two rooms. Two worlds.",copy:"Same scoreline, very different conversations. Rashford laces up.",
     pos:[[8,28],[42,14],[62,34],[62,62]],
     ban:[["Jakirović","2–0 is a trap, not a trophy. Stay sharp.","h"],["Carrick","Mark the tall ones. The short ones. Everyone.","u"],["Bruno","I blame the wind. The posts. And, honestly, you.","u"],["Rashford","I'll fix it. Boots on. Send me out.","u"]]},
    {img:"05-rashford.jpg",tag:"Under siege · 56'",min:"56'",h:2,a:0,st:"live",
     title:"72% of absolutely nothing",copy:"Rashford's on. United swarm. Hull turn into a wall with gloves.",
     pos:[[8,16],[64,58],[40,54],[64,16]],
     ban:[["United","72% possession! We're DOMINATING!","u"],["Hull defender","Cute. We're WINNING. Look it up.","h"],["Tzolakis","Keep knocking. I've had a nap back here.","h"],["Bruno","PASS! No— HIM. Why's no one where I want?!","u"]]},
    {img:"06-subs.jpg",tag:"Late drama · 90+6'",min:"90+6'",h:2,a:0,st:"live",
     title:"The wall holds. Millar smiles.",copy:"Tzolakis tips one over. Millar gets a yellow at 2–0 and shrugs.",
     pos:[[40,28],[64,14],[10,56],[64,58]],
     ban:[["Tzolakis","Tipped over. Lovely. Next customer.","h"],["Sesko","Six chances. SIX. He's a wall with gloves.","u"],["Millar","A yellow?! At 2–0?! I barely touched him!","h"],["Referee","Still a yellow, son. No loyalty cards at 2–0.","r"]]},
    {img:"07-fulltime.jpg",tag:"Full time",min:"FT",h:2,a:0,st:"ft",
     title:"FULL TIME. Pandemonium.",copy:"The whistle goes. United's 72% possession boards exactly zero points.",
     pos:[[10,18],[64,56],[64,16],[40,60]],
     ban:[["Hull","FULL TIME!!! Somebody pinch me!","h"],["Maguire","I'd like the ground to swallow me now.","u"],["Home fan","72% possession, zero points. Beautiful maths.","f"],["Ajayi","Nobody gave us a chance. Nobody. Beautiful.","h"]]},
    {img:"08-aftermath.jpg",tag:"Welcome back",min:"FT",h:2,a:0,st:"ft",
     title:"Red Devils? More like Crying Devils.",copy:"Ajayi 17. Mendy 38. Nine years away — one unforgettable night home.",
     pos:[[8,16],[64,30],[64,58],[10,60]],
     ban:[["BRYME desk","The Red Devils? Tonight: the CRYING Devils.","n"],["Bruno","*sniff* 72% of the ball, 0% of the joy.","u"],["Maguire","*one tear* ...set pieces.","u"],["Ajayi","Tigers ROAR. Devils dribble. On their faces.","h"]]}
  ];
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  var POS=[[10,30],[60,16],[12,55],[60,60]];      // fallback bubble anchors [left%,top%]
  var STEP=1200, VISIBLE=4600, LEAD=550;           // slower: bubbles appear gradually and linger
  function init(){
    var root=document.getElementById("mc-hero"); if(!root) return;
    root.className="mc";
    root.innerHTML=
      '<div class="mc-bars" aria-hidden="true"></div>'+
      '<div class="mc-deck">'+
        '<div class="mc-track"></div>'+
        '<div class="mc-hud"><span class="mc-pill" id="mcpill"></span><span class="mc-score" id="mcscore"></span></div>'+
        '<div class="mc-mark"><b>BRYME</b><span>@bryme</span></div>'+
        '<button class="mc-arr pv" aria-label="Previous">‹</button>'+
        '<button class="mc-arr nx" aria-label="Next">›</button>'+
      '</div>'+
      '<div class="mc-cap"><span class="mc-tag" id="mctag"></span><h2 id="mctitle"></h2></div>'+
      '<div class="mc-ctrl"><div class="mc-dots"></div><button class="mc-play" aria-pressed="true">⏸ Pause</button><span class="mc-cnt" id="mccnt"></span></div>'+
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
    function scheduleBubbles(c){
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
      cards[idx].querySelectorAll(".mc-bubble").forEach(function(e){e.classList.add("in");});
      playBtn.setAttribute("aria-pressed","false");playBtn.textContent="▶ Play";}
    function resume(){if(playing)return;playing=true;playBtn.setAttribute("aria-pressed","true");playBtn.textContent="⏸ Pause";
      elapsed=0;last=performance.now();scheduleBubbles(cards[idx]);}
    root.querySelector(".mc-arr.nx").addEventListener("click",function(){show(idx+1,"next");});
    root.querySelector(".mc-arr.pv").addEventListener("click",function(){show(idx-1,"prev");});
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
