(function(){var i=document.getElementById('tt-in');if(!i)return;var o=document.getElementById('tt-out'),m=document.getElementById('tt-msg');
function msg(t,c){m.textContent=t;m.className='tt-msg '+(c||'');}
function enc(s){var b=new TextEncoder().encode(s),r='';for(var k=0;k<b.length;k++)r+=String.fromCharCode(b[k]);return btoa(r);}
function dec(s){return new TextDecoder().decode(Uint8Array.from(atob(s.trim()),function(c){return c.charCodeAt(0);}));}
document.getElementById('tt-enc').addEventListener('click',function(){try{o.textContent=enc(i.value);msg('Encoded.','ok');}catch(e){msg('Could not encode: '+e.message,'err');}});
document.getElementById('tt-dec').addEventListener('click',function(){try{o.textContent=dec(i.value);msg('Decoded.','ok');}catch(e){msg('Not valid Base64: '+e.message,'err');}});
document.getElementById('tt-clear').addEventListener('click',function(){i.value='';o.textContent='';msg('');});})();
