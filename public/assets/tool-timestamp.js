(function(){var s=document.getElementById('tt-stamp');if(!s)return;var o=document.getElementById('tt-out'),m=document.getElementById('tt-msg'),d=document.getElementById('tt-date');
function msg(t,c){m.textContent=t;m.className='tt-msg '+(c||'');}
function doConv(){var v=parseInt(s.value.trim(),10);if(isNaN(v)){msg('Enter a number (seconds or milliseconds).','err');return;}
var ms=v>1e11?v:v*1000,dt=new Date(ms);if(isNaN(dt.getTime())){msg('That number is out of range.','err');return;}
o.textContent='Local: '+dt.toLocaleString()+'\nUTC: '+dt.toUTCString()+'\n('+(v>1e11?'milliseconds':'seconds')+' detected)';msg('Converted.','ok');}
document.getElementById('tt-now').addEventListener('click',function(){s.value=Math.floor(Date.now()/1000);doConv();});
document.getElementById('tt-conv').addEventListener('click',doConv);
document.getElementById('tt-dconv').addEventListener('click',function(){if(!d.value){msg('Pick a date and time first.','err');return;}
var t=new Date(d.value).getTime();if(isNaN(t)){msg('Could not read that date.','err');return;}
o.textContent='Unix seconds: '+Math.floor(t/1000)+'\nUnix milliseconds: '+t;msg('Converted.','ok');});})();
