(function(){var i=document.getElementById('tt-in');if(!i)return;var o=document.getElementById('tt-out');
function words(t){return t.split(/[^A-Za-z0-9]+/).filter(Boolean);}
function cap(w){return w.charAt(0).toUpperCase()+w.slice(1).toLowerCase();}
var fns={upper:function(t){return t.toUpperCase();},lower:function(t){return t.toLowerCase();},
title:function(t){return t.toLowerCase().replace(/(^|\s)(\S)/g,function(m,a,b){return a+b.toUpperCase();});},
sentence:function(t){return t.toLowerCase().replace(/(^\s*[a-z])|([.!?]\s+[a-z])/g,function(m){return m.toUpperCase();});},
camel:function(t){return words(t).map(function(w,j){return j?cap(w):w.toLowerCase();}).join('');},
pascal:function(t){return words(t).map(cap).join('');},
snake:function(t){return words(t).join('_').toLowerCase();},
kebab:function(t){return words(t).join('-').toLowerCase();}};
Object.keys(fns).forEach(function(k){document.getElementById('tt-'+k).addEventListener('click',function(){o.textContent=fns[k](i.value);});});})();
