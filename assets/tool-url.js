(function(){var i=document.getElementById('tt-in');if(!i)return;var o=document.getElementById('tt-out'),m=document.getElementById('tt-msg'),c=document.getElementById('tt-component');
function msg(t,c2){m.textContent=t;m.className='tt-msg '+(c2||'');}
document.getElementById('tt-enc').addEventListener('click',function(){try{o.textContent=c.checked?encodeURIComponent(i.value):encodeURI(i.value);msg('Encoded ('+(c.checked?'component':'full URL')+' mode).','ok');}catch(e){msg('Could not encode: '+e.message,'err');}});
document.getElementById('tt-dec').addEventListener('click',function(){try{o.textContent=c.checked?decodeURIComponent(i.value):decodeURI(i.value);msg('Decoded.','ok');}catch(e){msg('Could not decode - malformed % sequence? ('+e.message+')','err');}});
document.getElementById('tt-clear').addEventListener('click',function(){i.value='';o.textContent='';msg('');});})();
