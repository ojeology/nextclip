/* BRYME Match Comic — multi-match engine. data-comic on #mc-hero picks the match.
   Images + single caption track the AUDIO progress. One caption at a time. */
(function(){
  var AUDIO_DIR="/assets/audio/comic/";
  var MATCHES={
    "hull-united":{
      dir:"/assets/img/sports/comics/hull-united-mw1/",
      home:{ab:"HUL",sw:"sw-amber",clr:"#f5a300"},away:{ab:"UTD",sw:"sw-red",clr:"#e23b3b"},
      chapters:[
        {imgs:["01.jpg","19.jpg"],audio:"hu-ch01.mp3",tag:"Homecoming",min:"PRE-MATCH",h:0,a:0,st:"build",title:"9 years done — Tigers return!",
         cap:[["🎙️ Commentator","Nine years for relegation jail don end! Hull enter Premier League like person wey collect alert! MKM dey burst!","c"],["Hull fan","Omo! I don wait nine years for this night. My heart dey beat!","f"]]},
        {imgs:["13.jpg","20.jpg","02.jpg","14.jpg","15.jpg"],audio:"hu-ch02.mp3",tag:"1' · Kick-off",min:"1'",h:0,a:0,st:"live",title:"Whistle blow — Hull press!",
         cap:[["🎙️ Commentator","Teams dey tunnel, eye dey red! Whistle blow — Hull press like say dem no get brake!","c"],["Hull player","We no go give dem breathing space! Press, press, press!","h"],["United player","These boys dey run like say dem drink fuel! Calm down na!","u"]]},
        {imgs:["03.jpg","21.jpg"],audio:"hu-ch03.mp3",tag:"12' · Save",min:"12'",h:0,a:0,st:"live",title:"Tzolakis catch am like rent!",
         cap:[["🎙️ Commentator","Tzolakis catch ball like landlord wey come collect house rent! E be like say he get three hands!","c"],["Tzolakis","Welcome to Hull, my brother. Carry your ball go front!","h"]]},
        {imgs:["04.jpg","05.jpg","06.jpg","22.jpg"],audio:"hu-ch04.mp3",tag:"17' · GOAL",min:"17'",h:1,a:0,st:"live",title:"Corner → header → AJAYI goal!",
         cap:[["🎙️ Commentator","Corner kick — setup dey load! McBurnie head am… saved! But Ajayi pounce on the rebound — GOOOAL!","c"],["Ajayi","Scatter the net! Dem think say we come here to play!","h"],["United defender","Wait, wetin just happen? We wey suppose control game?","u"]]},
        {imgs:["07.jpg","24.jpg"],audio:"hu-ch05.mp3",tag:"1–0 · Scene",min:"17'",h:1,a:0,st:"live",title:"MKM don turn mad house!",
         cap:[["🎙️ Commentator","MKM Stadium don turn mad house! Nine years of waiting, e don pay!","c"],["Ajayi","I don wait my whole career for this kind night. E choke!","h"]]},
        {imgs:["16.jpg","23.jpg","08.jpg"],audio:"hu-ch06.mp3",tag:"34' · Bruno hot",min:"34'",h:1,a:0,st:"live",title:"Bruno dey blame everybody!",
         cap:[["🎙️ Commentator","Bruno don dey hot! He dey blame referee, ball, even the wind! Then Dorgu see yellow!","c"],["Bruno Fernandes","Wetin be this?! Nobody dey mark!","u"],["Referee","Na card be that. No begging, my friend.","r"]]},
        {imgs:["09.jpg","10.jpg","24.jpg"],audio:"hu-ch07.mp3",tag:"38' · GOAL",min:"38'",h:2,a:0,st:"live",title:"Free kick → MENDY header! 2–0!",
         cap:[["🎙️ Commentator","Free kick — danger dey load! Mendy rise like helicopter for set-piece — two nil o!","c"],["Mendy","Fly high! Another set piece chop una clean!","h"],["Bruno Fernandes","How we con leave tall man for free header again?!","u"]]},
        {imgs:["11.jpg","17.jpg"],audio:"hu-ch08.mp3",tag:"60' · Possession",min:"60'",h:2,a:0,st:"live",title:"72% award vs 3 points",
         cap:[["🎙️ Commentator","United get 72% possession award, but Hull fans dey count their 3 points! Wall no dey move!","c"],["United player","Omo, we get 72% possession o! We dey dictate!","u"],["Hull defender","Sorry say possession no dey inside soup. 2-0 remains 2-0!","h"]]},
        {imgs:["18.jpg","25.jpg"],audio:"hu-ch09.mp3",tag:"78' · Double save",min:"78'",h:2,a:0,st:"live",title:"Tzolakis wall no dey break!",
         cap:[["🎙️ Commentator","Tzolakis don do double save o! First the shot, then the rebound! Wall no dey break!","c"],["Tzolakis","Anything wey enter my box, I go commot!","h"],["Sesko","This keeper dey impossible! Wetin man go do?!","u"]]},
        {imgs:["12.jpg","26.jpg"],audio:"hu-ch10.mp3",tag:"Full time",min:"FT",h:2,a:0,st:"ft",title:"Red Devils? Crying Devils!",
         cap:[["🎙️ Commentator","Full time! Red Devils? Crying Devils proper! Tigers are back — and we starving!","c"],["Rashford","We come all this way only to chop premium tears.","u"],["Hull captain","Go tell them say the Tigers are back!","h"]]}
      ]
    },
    "arsenal-coventry":{
      dir:"/assets/img/sports/comics/arsenal-coventry-mw1/",
      home:{ab:"ARS",sw:"sw-red",clr:"#d11"},away:{ab:"COV",sw:"sw-sky",clr:"#5aa9e6"},
      chapters:[
        {imgs:["ac-01.jpg","ac-09.jpg","ac-10.jpg","ac-19.jpg"],audio:"ac-ch01.mp3",tag:"Homecoming",min:"PRE-MATCH",h:0,a:0,st:"build",title:"Champions open the defence!",
         cap:[["🎙️ Commentator","Champions Arsenal open the defence tonight! Twenty-two years of waiting don end — now dem dey guard the crown!","c"],["Arsenal fan","We be champions! Anybody wey enter Emirates go collect!","hm"],["Coventry fan","We just come back o. Make dem no use us do birthday party!","aw"]]},
        {imgs:["ac-02.jpg","ac-11.jpg","ac-20.jpg"],audio:"ac-ch02.mp3",tag:"1' · In control",min:"1'",h:0,a:0,st:"live",title:"Arsenal dey toy with dem!",
         cap:[["🎙️ Commentator","Whistle blow! Arsenal dey move the ball like training — Coventry no even smell am!","c"],["Arsenal midfielder","Calm, calm, make dem chase shadow!","hm"],["Coventry defender","Haaa, the ball dey fly up and down! I don already tire!","aw"]]},
        {imgs:["ac-03.jpg","ac-12.jpg","ac-13.jpg","ac-21.jpg"],audio:"ac-ch03.mp3",tag:"GOAL · 12'",min:"12'",h:1,a:0,st:"live",title:"Opener! Arsenal 1–0!",
         cap:[["🎙️ Commentator","GOOOAL! The ball don enter! Champions don open account — Arsenal one nil!","c"],["Arsenal fan","E choke! First one don enter!","hm"],["Coventry keeper","I suppose catch that one... the boy hit am well!","aw"]]},
        {imgs:["ac-04.jpg","ac-14.jpg","ac-22.jpg"],audio:"ac-ch04.mp3",tag:"25' · Big save",min:"25'",h:1,a:0,st:"live",title:"Coventry try, keeper say no!",
         cap:[["🎙️ Commentator","Coventry try counter! But Arsenal keeper say not today — big save!","c"],["Arsenal keeper","You think say e go enter? No be today!","hm"],["Coventry fan","Ah! We for score that one o!","aw"]]},
        {imgs:["ac-05.jpg","ac-15.jpg","ac-23.jpg"],audio:"ac-ch05.mp3",tag:"GOAL · 40'",min:"40'",h:2,a:0,st:"live",title:"Two nil — defense scatter!",
         cap:[["🎙️ Commentator","Two nil! Another one don enter! Coventry defense dey scatter like pack of cards!","c"],["Arsenal fan","Two! Make we chop more!","hm"],["Coventry defender","Wetin be this?! Dem no dey tire?","aw"]]},
        {imgs:["ac-06.jpg","ac-16.jpg","ac-24.jpg"],audio:"ac-ch06.mp3",tag:"55' · Frustration",min:"55'",h:2,a:0,st:"live",title:"Coventry dey find miracle!",
         cap:[["🎙️ Commentator","Coventry boys dey look themselves — 'we go come back from this one?'","c"],["Coventry fan","Bros, na only 2-0. Miracle dey happen... sometimes!","aw"],["Arsenal fan","Miracle kee you there! Na 3 we dey look for!","hm"]]},
        {imgs:["ac-07.jpg","ac-17.jpg","ac-25.jpg"],audio:"ac-ch07.mp3",tag:"GOAL · 75'",min:"75'",h:3,a:0,st:"live",title:"Three nil — rout confirmed!",
         cap:[["🎙️ Commentator","THREE NIL! Rout confirmed! Champions dey show say last season no be luck!","c"],["Arsenal fan","Three! Statement of intent! The crown dey stay!","hm"],["Coventry fan","Abeg, referee blow make we go house!","aw"]]},
        {imgs:["ac-08.jpg","ac-18.jpg","ac-26.jpg"],audio:"ac-ch08.mp3",tag:"Full time",min:"FT",h:3,a:0,st:"ft",title:"Clean sheet — defence starts well!",
         cap:[["🎙️ Commentator","Full time! Arsenal three, Coventry nil — clean sheet, three points, defence don start well!","c"],["Arsenal fan","Champions! Same again next week!","hm"],["Coventry fan","Long season dey front... we go re-group!","aw"]]}
      ]
    }
  };
  var PILL={build:"BUILD-UP",live:"LIVE",ht:"HALF TIME",ft:"FULL TIME"};
  var CAP_DUR=4200;
  function init(){
    var root=document.getElementById("mc-hero"); if(!root) return;
    var slug=root.getAttribute("data-comic")||"hull-united";
    var M=MATCHES[slug]||MATCHES["hull-united"];
    var DIR=M.dir, S=M.chapters, home=M.home, away=M.away;
    root.className="mc";
    root.style.setProperty("--home-c",home.clr);
    root.style.setProperty("--away-c",away.clr);
    root.innerHTML=
      '<div class="mc-deck">'+
        '<div class="mc-bars" aria-hidden="true"></div>'+
        '<div class="mc-track"></div>'+
        '<div class="mc-hud"><span class="mc-pill" id="mcpill"></span><span class="mc-score" id="mcscore"></span></div>'+
        '<div class="mc-mark"><b>BRYME</b><span>@bryme</span></div>'+
        '<div class="mc-cap-slot"><div class="mc-cap-card" id="mccap"></div></div>'+
      '</div>'+
      '<div class="mc-head"><span class="mc-tag" id="mctag"></span><h2 id="mctitle"></h2></div>'+
      '<div class="mc-ctrl">'+
        '<button class="mc-nav mc-prev" aria-label="Previous">‹ Prev</button>'+
        '<div class="mc-dots"></div>'+
        '<button class="mc-play" aria-pressed="true">⏸ Pause</button>'+
        '<button class="mc-sound" aria-pressed="false">🔇 Sound</button>'+
        '<button class="mc-nav mc-next" aria-label="Next">Next ›</button>'+
        '<span class="mc-cnt" id="mccnt"></span>'+
      '</div>'+
      '<div class="mc-md">'+
        '<span class="mc-md-i on"><span class="mc-md-n">● Matchday 1</span><span class="mc-md-s">BRYME Match Comic · playing now</span></span>'+
        '<a class="mc-md-i soon" href="/sports/premier-league/"><span class="lock">🔒</span><span class="mc-md-n">Matchday 2</span><span class="mc-md-s">Comic drops after full time</span></a>'+
        '<a class="mc-md-i soon" href="/sports/premier-league/"><span class="lock">🔒</span><span class="mc-md-n">Matchday 3</span><span class="mc-md-s">Coming soon</span></a>'+
      '</div>';
    var track=root.querySelector(".mc-track"),dotsEl=root.querySelector(".mc-dots"),barsEl=root.querySelector(".mc-bars"),
        pill=root.querySelector("#mcpill"),score=root.querySelector("#mcscore"),tag=root.querySelector("#mctag"),
        title=root.querySelector("#mctitle"),cntEl=root.querySelector("#mccnt"),playBtn=root.querySelector(".mc-play"),
        soundBtn=root.querySelector(".mc-sound"),deck=root.querySelector(".mc-deck"),capCard=root.querySelector("#mccap"),len=S.length;
    track.innerHTML=S.map(function(s,i){
      var layers=s.imgs.map(function(g,k){return '<img class="mc-layer'+(k===0?' on':'')+'" src="'+DIR+g+'" alt="Original BRYME comic frame: '+s.title+'" loading="'+(i||k?'lazy':'eager')+'">';}).join("");
      return '<div class="mc-card">'+layers+'</div>';
    }).join("");
    dotsEl.innerHTML=S.map(function(s,i){return '<button type="button" aria-label="Chapter '+(i+1)+'"></button>';}).join("");
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
    var capTimer=null;
    function showCap(c){ if(capTimer)clearTimeout(capTimer); capCard.classList.remove("in");
      capTimer=setTimeout(function(){ capCard.className="mc-cap-card "+c[2]; capCard.innerHTML='<i>'+c[0]+'</i><b>'+c[1]+'</b>'; void capCard.offsetWidth; capCard.classList.add("in"); },160); }

    var idx=0,playing=true,hover=false,elapsed=0,last=0,curLayer=-1,curCap=-1;
    function durFor(i){return S[i].cap.length*CAP_DUR+1200;}
    function updateHud(){
      var s=S[idx],st=s.st;
      pill.className="mc-pill "+(st==="live"?"live":st==="ft"?"ft":"");
      pill.innerHTML=(st==="live"?'<span class="d"></span>':'')+PILL[st];
      score.innerHTML='<span class="t"><span class="sw '+home.sw+'"></span>'+home.ab+'</span>'+s.h+'–'+s.a+'<span class="t"><span class="sw '+away.sw+'"></span>'+away.ab+'</span><span class="min">'+s.min+'</span>';
      tag.textContent=s.tag;title.textContent=s.title;
    }
    function show(n,dir){
      var old=idx;idx=((n%len)+len)%len;var c=cards[idx];
      stopAudio();
      if(old!==idx){var o=cards[old];o.classList.remove("on");o.classList.add(dir==="next"?"left":"right");}
      c.style.transition="none";c.classList.remove("on","left","right");c.classList.add(dir==="next"?"right":"left");
      void c.offsetWidth;c.style.transition="";c.classList.remove("right","left");c.classList.add("on");
      setLayer(c,0);curLayer=0;curCap=-1;capCard.classList.remove("in");
      dots.forEach(function(d,i){d.classList.toggle("on",i===idx);});
      cntEl.textContent=(idx+1)+" / "+len;updateHud();elapsed=0;last=performance.now();
      loadAudio(idx); if(!muted) playAudio();
    }
    function loop(now){var dt=now-last;last=now;
      if(playing&&!hover&&(muted||!audioOK)){elapsed+=dt;if(elapsed>=durFor(idx))show(idx+1,"next");}
      var ch=S[idx];
      var prog=(!muted&&audioOK&&audio.duration)?(audio.currentTime/audio.duration):Math.min(0.999999,elapsed/durFor(idx));
      prog=Math.max(0,Math.min(0.999999,prog));
      if(ch.imgs.length>1){var li=Math.floor(prog*ch.imgs.length)%ch.imgs.length; if(li!==curLayer){setLayer(cards[idx],li);curLayer=li;}}
      var ci=Math.floor(prog*ch.cap.length)%ch.cap.length;
      if(ci!==curCap){showCap(ch.cap[ci]);curCap=ci;}
      for(var i=0;i<len;i++){bars[i].style.width=(i<idx?100:i===idx?Math.min(100,prog*100):0)+"%";}
      requestAnimationFrame(loop);
    }
    function pause(){if(!playing)return;playing=false;stopAudio();
      playBtn.setAttribute("aria-pressed","false");playBtn.textContent="▶ Play";}
    function resume(){if(playing)return;playing=true;playBtn.setAttribute("aria-pressed","true");playBtn.textContent="⏸ Pause";
      last=performance.now();if(!muted)playAudio();}
    function toggleSound(){
      muted=!muted;soundBtn.setAttribute("aria-pressed",String(!muted));
      soundBtn.textContent=muted?"🔇 Sound":"🔊 Sound on";
      if(muted){stopAudio();}
      else{elapsed=0;last=performance.now();curCap=-1;curLayer=-1;playAudio();}
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
    cards[0].classList.add("on");dots[0].classList.add("on");idx=0;curLayer=0;curCap=-1;
    cntEl.textContent="1 / "+len;updateHud();loadAudio(0);
    last=performance.now();requestAnimationFrame(loop);
  }
  if(document.readyState!=="loading")init();
  else document.addEventListener("DOMContentLoaded",init);
})();
