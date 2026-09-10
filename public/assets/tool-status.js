(function(){var q=document.getElementById('tt-q');if(!q)return;var rows=[].slice.call(document.querySelectorAll('#tt-table tbody tr')),m=document.getElementById('tt-msg');
function filt(){var v=q.value.trim(),n=0;
rows.forEach(function(r){var hit=!v||r.getAttribute('data-code').indexOf(v)===0||r.textContent.toLowerCase().indexOf(v.toLowerCase())!==-1;
r.style.display=hit?'':'none';if(hit)n++;});
m.textContent=v?n+' match'+(n===1?'':'es')+' for "'+v+'"':'';m.className='tt-msg';}
document.getElementById('tt-look').addEventListener('click',filt);
q.addEventListener('input',filt);})();
