(function(){var i=document.getElementById('tt-in');if(!i)return;var o=document.getElementById('tt-out'),m=document.getElementById('tt-msg');
function msg(t,c){m.textContent=t;m.className='tt-msg '+(c||'');}
document.getElementById('tt-format').addEventListener('click',function(){try{var v=JSON.parse(i.value);o.textContent=JSON.stringify(v,null,2);msg('Valid JSON. Formatted.','ok');}catch(e){msg('Invalid JSON: '+e.message,'err');}});
document.getElementById('tt-minify').addEventListener('click',function(){try{var v=JSON.parse(i.value);o.textContent=JSON.stringify(v);msg('Valid JSON. Minified.','ok');}catch(e){msg('Invalid JSON: '+e.message,'err');}});
document.getElementById('tt-clear').addEventListener('click',function(){i.value='';o.textContent='';msg('');});})();
