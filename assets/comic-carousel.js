/* BRYME Match Comic — FULL-BLEED cinematic carousel, 18 beats, Naija Pidgin banter.
   Multi-image beats: the picture cross-fades DURING each narration (images > audio).
   ONE bubble at a time. BRYME fingerprint + Matchday nav. Auto-builds into #mc-hero. */
(function(){
  var DIR="/assets/img/sports/comics/hull-united-mw1/";
  var AUDIO_DIR="/assets/audio/comic/";
  var S=[
    {imgs:["01.jpg","19.jpg"],audio:"hu-01.mp3",tag:"Arrival",min:"PRE-MATCH",h:0,a:0,st:"build",title:"9 years done — Tigers return!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","After 9 years for relegation wilderness, the Tigers don return home! MKM Stadium dey burst!","c"],
          ["Hull fan","Omo! I don wait nine years for this night. My heart dey beat!","f"],
          ["United fan","Na wah. These people too dey hyped. Calm down na!","u"]]},
    {imgs:["13.jpg","20.jpg"],audio:"hu-n1.mp3",tag:"Tunnel",min:"PRE-MATCH",h:0,a:0,st:"build",title:"Eye dey red — nine years of hunger!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Teams dey tunnel now! Eye dey red, chest dey beat — nine years of hunger!","c"],
          ["Hull captain","Today, we show dem say Tigers no dey fear anybody!","h"],
          ["United captain","Make we just calm down, play our ball. No shake.","u"]]},
    {imgs:["02.jpg"],audio:"hu-02.mp3",tag:"Kick-off",min:"1'",h:0,a:0,st:"live",title:"Hull enter like alert!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Whistle blow! Hull City enter Premier League like person wey collect alert!","c"],
          ["United player","Why these people dey run like say dem drink fuel? Calm down na!","u"],
          ["Hull player","My friend, welcome back to Premier League! No rest for the wicked today!","h"]]},
    {imgs:["14.jpg"],audio:"hu-n2.mp3",tag:"5' · High press",min:"5'",h:0,a:0,st:"live",title:"Hull press like no brake!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Hull press like say dem no get brake! Tackle dey fly up and down!","c"],
          ["Hull player","We no go give dem breathing space! Press, press, press!","h"],
          ["United player","These boys dey run like say dem drink substance! Haaa!","u"]]},
    {imgs:["15.jpg"],audio:"hu-n3.mp3",tag:"10' · Near miss",min:"10'",h:0,a:0,st:"live",title:"McBurnie nearly nod am!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Coyle whip dangerous cross! McBurnie nearly nod am inside — inches wide!","c"],
          ["McBurnie","Ah! I suppose score that one! The grass cheat me!","h"],
          ["Coyle","No worry, more dey come. We go chop one soon.","h"]]},
    {imgs:["03.jpg","21.jpg"],audio:"hu-03.mp3",tag:"12' · Save",min:"12'",h:0,a:0,st:"live",title:"Tzolakis catch am like rent!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","United dey find tiki-taka, Hull dey find trouble! Tzolakis catch ball like landlord wey come collect house rent!","c"],
          ["Mbeumo","How this goalkeeper take catch that one?! E be like say he get three hands!","u"],
          ["Tzolakis","Welcome to Hull, my brother. Carry your ball go front!","h"]]},
    {imgs:["04.jpg"],audio:"hu-c1.mp3",tag:"16' · Corner",min:"16'",h:0,a:0,st:"live",title:"Corner kick — setup dey load",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Corner kick to Hull! Setup dey load — everybody enter the box!","c"],
          ["Slater","Make I put am for the near post, make somebody finish am!","h"],
          ["United defender","Mark everybody tight! No space!","u"]]},
    {imgs:["05.jpg"],audio:"hu-c2.mp3",tag:"17' · Header",min:"17'",h:0,a:0,st:"live",title:"McBurnie head am… saved!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","McBurnie rise, head am well! But Lammens parry commot — saved!","c"],
          ["McBurnie","I head am correct! Shey e enter? No?! Omo!","h"],
          ["Lammens","No be today! I don save am!","u"]]},
    {imgs:["06.jpg","22.jpg"],audio:"hu-04.mp3",tag:"GOAL · 17'",min:"17'",h:1,a:0,st:"live",title:"AJAYI scatter net! 1–0!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","GOOOAL! Ajayi run enter box like debt collector, scatter net! Hull 1–0 United!","c"],
          ["Ajayi","Scatter the net! Dem think say we come here to play!","h"],
          ["United defender","Wait... wetin just happen? We wey suppose control game?","u"]]},
    {imgs:["07.jpg"],audio:"hu-05.mp3",tag:"1–0 · Scene",min:"17'",h:1,a:0,st:"live",title:"MKM don turn mad house!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","MKM Stadium don turn mad house! Nine years of waiting, e don pay!","c"],
          ["Ajayi","I don wait my whole career for this kind night. E choke!","h"],
          ["Home fan","I don tire to shout but I no go stop. Tigers!","f"]]},
    {imgs:["16.jpg","23.jpg"],audio:"hu-n4.mp3",tag:"20' · Bruno hot",min:"20'",h:1,a:0,st:"live",title:"Bruno dey blame everybody!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Bruno don dey hot! He dey shout, dey point, dey blame referee, ball, even the wind!","c"],
          ["Bruno Fernandes","Wetin be this?! Nobody dey mark! Everybody dey look!","u"],
          ["United teammate","Baba, calm down, na only one nil. We go come back.","u"]]},
    {imgs:["08.jpg"],audio:"hu-c3.mp3",tag:"34' · Yellow",min:"34'",h:1,a:0,st:"live",title:"Dorgu see yellow!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Dorgu see yellow! The boy dey complain say he no even touch am!","c"],
          ["Dorgu","Yellow?! Ref, I no even touch am well! Abeg!","u"],
          ["Referee","Na card be that. No begging, my friend.","r"]]},
    {imgs:["09.jpg"],audio:"hu-c4.mp3",tag:"37' · Free kick",min:"37'",h:1,a:0,st:"live",title:"Danger dey load!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Free kick to Hull for dangerous area o! Danger dey load!","c"],
          ["Slater","Make I whip am inside, make tall man do the rest!","h"],
          ["Bruno Fernandes","Wall, jump! Everybody jump!","u"]]},
    {imgs:["10.jpg","24.jpg"],audio:"hu-06.mp3",tag:"GOAL · 38'",min:"38'",h:2,a:0,st:"live",title:"MENDY fly! 2–0 o!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Lightning strikes twice! Mendy rise like helicopter for set-piece—2–0 o!","c"],
          ["Mendy","Fly high! Another set piece chop una clean!","h"],
          ["Bruno Fernandes","How we con leave tall man like this for free header again?!","u"]]},
    {imgs:["11.jpg"],audio:"hu-07.mp3",tag:"60' · Possession",min:"60'",h:2,a:0,st:"live",title:"72% award vs 3 points",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Man United fans currently holding 72% possession award, while Hull fans are busy counting their 3 points.","c"],
          ["United player","Omo, we get 72% possession o! We dey dictate the pace!","u"],
          ["Hull defender","Eyah. Sorry say possession no dey inside soup. 2–0 still remains 2–0!","h"]]},
    {imgs:["17.jpg"],audio:"hu-n5.mp3",tag:"67' · Changes",min:"67'",h:2,a:0,st:"live",title:"Fresh legs, desperation set in!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Carrick dey ring the changes! Fresh legs dey enter, desperation don set in!","c"],
          ["Rashford","My time don reach. Make I enter go change this thing!","u"],
          ["Hull defender","Make dem bring who dem want, wall no dey move.","h"]]},
    {imgs:["18.jpg","25.jpg"],audio:"hu-n6.mp3",tag:"78' · Double save",min:"78'",h:2,a:0,st:"live",title:"Tzolakis wall no dey break!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Tzolakis don do double save o! First the shot, then the rebound! Wall no dey break!","c"],
          ["Tzolakis","Anything wey enter my box, I go commot. Na me dey here!","h"],
          ["Sesko","This keeper dey impossible! Wetin man go do?!","u"]]},
    {imgs:["12.jpg","26.jpg"],audio:"hu-08.mp3",tag:"Full time",min:"FT",h:2,a:0,st:"ft",title:"Tigers are back — and starving!",
     pos:[[28,56],[8,62],[54,60]],
     ban:[["🎙️ Commentator","Full time! Tigers show Premier League say wetin pass you, make you leave am for owners!","c"],
          ["Rashford","We come all this way... only to chop premium tears.","u"],
          ["Hull captain","Go tell them say the Tigers are back, and we starving!","h"]]}
  ];
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  var POS=[[28,56],[8,62],[54,60]];
  var STEP=3700, VISIBLE=3000, LEAD=500;
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
        '<button class="mc-sound" aria-pressed="false">🔇 Sound</button>'+
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
        soundBtn=root.querySelector(".mc-sound"),deck=root.querySelector(".mc-deck"),len=S.length;
    track.innerHTML=S.map(function(s,i){
      var bubs=s.ban.map(function(b,j){var p=(s.pos&&s.pos[j])||POS[j%POS.length];
        return '<div class="mc-bubble '+b[2]+'" style="left:'+p[0]+'%;top:'+p[1]+'%"><i>'+b[0]+'</i>'+b[1]+'</div>';}).join("");
      var layers=s.imgs.map(function(g,k){return '<img class="mc-layer'+(k===0?' on':'')+'" src="'+DIR+g+'" alt="Original BRYME comic frame: '+s.title+'" loading="'+(i||k?'lazy':'eager')+'">';}).join("");
      return '<div class="mc-card">'+layers+'<div class="mc-bub">'+bubs+'</div></div>';
    }).join("");
    dotsEl.innerHTML=S.map(function(s,i){return '<button type="button" aria-label="Panel '+(i+1)+'"></button>';}).join("");
    barsEl.innerHTML=S.map(function(){return '<i><span></span></i>';}).join("");
    var cards=[].slice.call(track.children);
    var dots=[].slice.call(dotsEl.children);
    var bars=[].slice.call(barsEl.children).map(function(b){return b.firstChild;});
    dots.forEach(function(b,i){b.addEventListener("click",function(){show(i,i>idx?"next":"prev");});});

    var audio=document.createElement("audio"); audio.preload="auto"; audio.setAttribute("aria-hidden","true"); root.appendChild(audio);
    var muted=true, audioOK=true;
    audio.addEventListener("ended",function(){ if(playing&&!hover&&!muted&&audioOK) show(idx+1,"next"); });
    audio.addEventListener("error",function(){ audioOK=false; });
    function loadAudio(i){ var s=S[i]; if(s.audio){ audioOK=true; audio.src=AUDIO_DIR+s.audio; audio.load(); } }
    function playAudio(){ if(!muted&&S[idx].audio){ audio.currentTime=0; var p=audio.play(); if(p&&p.catch)p.catch(function(){audioOK=false;}); } }
    function stopAudio(){ try{audio.pause();}catch(e){} }
    function setLayer(card,li){ var ls=card.querySelectorAll(".mc-layer"); ls.forEach(function(l,k){l.classList.toggle("on",k===li);}); }

    var idx=0,playing=true,hover=false,elapsed=0,last=0,curLayer=0,timers=[];
    function durFor(i){return LEAD+(S[i].ban.length-1)*STEP+VISIBLE+1100;}
    function clearTimers(){timers.forEach(clearTimeout);timers=[];}
    function scheduleBubbles(c){
      clearTimers();
      var bubs=c.querySelectorAll(".mc-bubble");
      bubs.forEach(function(el,i){
        timers.push(setTimeout(function(){el.classList.add("in");},LEAD+i*STEP));
        var isLast=(i===bubs.length-1);
        if(muted||!isLast){ timers.push(setTimeout(function(){el.classList.remove("in");},LEAD+i*STEP+VISIBLE)); }
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
      stopAudio();
      if(old!==idx){var o=cards[old];o.classList.remove("on");o.classList.add(dir==="next"?"left":"right");
        o.querySelectorAll(".mc-bubble").forEach(function(e){e.classList.remove("in");});}
      c.style.transition="none";c.classList.remove("on","left","right");c.classList.add(dir==="next"?"right":"left");
      void c.offsetWidth;c.style.transition="";c.classList.remove("right","left");c.classList.add("on");
      setLayer(c,0);curLayer=0;
      dots.forEach(function(d,i){d.classList.toggle("on",i===idx);});
      cntEl.textContent=(idx+1)+" / "+len;updateHud();elapsed=0;last=performance.now();
      loadAudio(idx); if(!muted) playAudio();
      scheduleBubbles(c);
    }
    function loop(now){var dt=now-last;last=now;
      if(playing&&!hover&&(muted||!audioOK)){elapsed+=dt;if(elapsed>=durFor(idx))show(idx+1,"next");}
      var s=S[idx];
      var prog=(!muted&&audioOK&&audio.duration)?(audio.currentTime/audio.duration):(elapsed/durFor(idx));
      prog=Math.max(0,Math.min(0.999999,prog));
      if(s.imgs.length>1){var li=Math.floor(prog*s.imgs.length)%s.imgs.length; if(li!==curLayer){setLayer(cards[idx],li);curLayer=li;}}
      for(var i=0;i<len;i++){var w;
        if(i<idx)w=100;
        else if(i===idx){
          if(!muted&&audioOK&&audio.duration)w=Math.min(100,prog*100);
          else w=Math.min(100,prog*100);
        } else w=0;
        bars[i].style.width=w+"%";}
      requestAnimationFrame(loop);
    }
    function pause(){if(!playing)return;playing=false;stopAudio();
      var b=cards[idx].querySelectorAll(".mc-bubble");if(b.length)b[b.length-1].classList.add("in");
      playBtn.setAttribute("aria-pressed","false");playBtn.textContent="▶ Play";}
    function resume(){if(playing)return;playing=true;playBtn.setAttribute("aria-pressed","true");playBtn.textContent="⏸ Pause";
      elapsed=0;last=performance.now();if(!muted)playAudio();scheduleBubbles(cards[idx]);}
    function toggleSound(){
      muted=!muted;soundBtn.setAttribute("aria-pressed",String(!muted));
      soundBtn.textContent=muted?"🔇 Sound":"🔊 Sound on";
      if(muted){stopAudio();scheduleBubbles(cards[idx]);}
      else{elapsed=0;last=performance.now();playAudio();scheduleBubbles(cards[idx]);}
    }
    root.querySelector(".mc-next").addEventListener("click",function(){show(idx+1,"next");});
    root.querySelector(".mc-prev").addEventListener("click",function(){show(idx-1,"prev");});
    playBtn.addEventListener("click",function(){playing?pause():resume();});
    soundBtn.addEventListener("click",toggleSound);
    deck.addEventListener("mouseenter",function(){hover=true;});
    deck.addEventListener("mouseleave",function(){hover=false;last=performance.now();});
    var sx=null;
    deck.addEventListener("touchstart",function(e){sx=e.touches[0].clientX;},{passive:true});
    deck.addEventListener("touchend",function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>44)show(dx<0?idx+1:idx-1,dx<0?"next":"prev");sx=null;},{passive:true});
    document.addEventListener("keydown",function(e){if(e.key==="ArrowRight")show(idx+1,"next");else if(e.key==="ArrowLeft")show(idx-1,"prev");});
    cards[0].classList.add("on");dots[0].classList.add("on");idx=0;curLayer=0;
    cntEl.textContent="1 / "+len;updateHud();loadAudio(0);scheduleBubbles(cards[0]);
    last=performance.now();requestAnimationFrame(loop);
  }
  if(document.readyState!=="loading")init();
  else document.addEventListener("DOMContentLoaded",init);
})();
