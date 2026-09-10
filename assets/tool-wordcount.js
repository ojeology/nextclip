(function(){var i=document.getElementById('tt-in');if(!i)return;var o=document.getElementById('tt-out');
function upd(){var t=i.value,w=t.trim()?t.trim().split(/\s+/).length:0,ns=t.replace(/\s/g,'').length;
var se=(t.match(/[.!?]+(\s|$)/g)||[]).length,pa=t.trim()?t.trim().split(/\n\s*\n/).length:0;
var mi=w?Math.max(1,Math.round(w/200)):0;
o.textContent='Words: '+w+'\nCharacters: '+t.length+' (without spaces: '+ns+')\nSentences: ~'+se+'\nParagraphs: '+pa+'\nReading time: ~'+mi+' min';}
i.addEventListener('input',upd);upd();})();
