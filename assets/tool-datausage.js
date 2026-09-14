(function(){var b=document.getElementById('tt-est');if(!b)return;
function num(id){return parseFloat((document.getElementById(id)||{}).value);}
function out(){return document.getElementById('tt-out');}
var RATES={sd:0.7,hd:3.0};
b.addEventListener('click',function(){
  var g=num('tt-bundle'),days=num('tt-cycle'),used=num('tt-used'),
      vh=num('tt-video'),q=(document.getElementById('tt-quality')||{}).value||'sd',
      mh=num('tt-music'),sh=num('tt-social');
  if(!(g>0&&g<=2000)){out().textContent='Enter your bundle size in GB (1-2000).';return;}
  if(!(days>0&&days<=120)||!(used>=0&&used<days)){out().textContent='Enter the cycle length and how many days are already used (used must be less than the cycle length).';return;}
  var daily=vh*RATES[q]+mh*0.1+sh*0.15+0.05;
  if(daily<=0.05){out().textContent='With no video, music or social hours entered, the baseline alone is tiny - your bundle lasts the cycle easily.';return;}
  var monthGB=daily*days,left=g-daily*used,daysLeft=days-used,lasts=left/daily;
  var verdict;
  if(lasts>=daysLeft){verdict='Comfortable: at this pace the bundle outlasts the cycle by about '+Math.round(lasts-daysLeft)+' day'+(Math.round(lasts-daysLeft)===1?'':'s')+'.';}
  else if(lasts>=daysLeft*0.7){verdict='Tight: the bundle runs to about day '+Math.round(used+lasts)+' of '+Math.round(days)+' - trim video quality or save the last days.';}
  else{verdict='Won\'t last: the bundle dies around day '+Math.round(used+lasts)+' - about '+Math.round(daysLeft-lasts)+' day'+(Math.round(daysLeft-lasts)===1?'':'s')+' short. The data diet fixes this: see the guide below.';}
  out().textContent='Pace: about '+daily.toFixed(1)+' GB/day ('+Math.round(monthGB)+' GB over the full cycle). '+verdict+' Rates are rough industry averages - your apps may differ.';
});})();