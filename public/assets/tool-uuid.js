(function(){var out=document.getElementById('tt-out');if(!out)return;var m=document.getElementById('tt-msg'),n=document.getElementById('tt-count');
function gen(){var b=new Uint8Array(16);crypto.getRandomValues(b);b[6]=(b[6]&15)|64;b[8]=(b[8]&63)|128;
var h=[].map.call(b,function(x){var s=x.toString(16);return s.length<2?'0'+s:s;}).join('');
return h.slice(0,8)+'-'+h.slice(8,12)+'-'+h.slice(12,16)+'-'+h.slice(16,20)+'-'+h.slice(20);}
document.getElementById('tt-gen').addEventListener('click',function(){var k=parseInt(n.value,10)||1,l=[];for(var j=0;j<k;j++)l.push(gen());out.textContent=l.join('\n');m.textContent=k+' UUID'+(k>1?'s':'')+' generated (version 4, random).';m.className='tt-msg ok';});
document.getElementById('tt-copy').addEventListener('click',function(){if(!out.textContent)return;navigator.clipboard.writeText(out.textContent).then(function(){m.textContent='Copied to clipboard.';m.className='tt-msg ok';},function(){m.textContent='Copy failed - select the text manually.';m.className='tt-msg err';});});})();
