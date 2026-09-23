(function(){var b=document.getElementById('tt-speed');if(!b)return;
function num(id){var v=parseFloat((document.getElementById(id)||{}).value);return isNaN(v)?0:v;}
function out(){return document.getElementById('tt-out');}
var TIERS=[50,100,150,200,300,500,1000],UPL=[5,10,20,50,100];
function tier(x,list){for(var i=0;i<list.length;i++){if(x<=list[i])return list[i];}return list[list.length-1];}
b.addEventListener('click',function(){
  var f=num('tt-4k')*25,hd=num('tt-hd')*8,cl=num('tt-calls')*4,gm=num('tt-gamers')*5,
      mu=num('tt-music')*1,wf=num('tt-wfh')*10,sm=num('tt-smart')*0.5;
  var sum=f+hd+cl+gm+mu+wf+sm;
  if(sum<=0){out().textContent='Enter at least one activity - even a music stream counts.';return;}
  var need=sum*1.25+15;
  var rec=tier(need,TIERS);
  var upneed=num('tt-calls')*3+num('tt-wfh')*3+5;
  var up=tier(upneed,UPL);
  var lines=[];
  lines.push('Raw demand: about '+Math.round(sum)+' Mbps download across everything at once.');
  lines.push('With 25% headroom and a household base, aim for at least '+rec+' Mbps down');
  lines.push('and about '+up+' Mbps up (video calls and uploads are the usual surprise).');
  if(num('tt-gamers')>0){lines.push('Gaming note: latency (ping) matters more than bandwidth - a smaller plan with low ping beats a big plan with high ping.');}
  if(f>=3){lines.push('That is a lot of simultaneous 4K - consider whether two of those sets are really watched in 4K.');}
  lines.push('Reality check: advertised speeds are best-case; over Wi-Fi expect a good slice less, shared across everyone. If your current plan already beats these numbers, blame the router before the provider.');
  out().textContent=lines.join(' ')+' Nothing you entered left this page.';
});})();
