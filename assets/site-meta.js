/* Generated from site.config.json — do not hand-edit. */
(function(){
  var siteUrl="https://ojeology.github.io/nextclip", name="NEXTCLIP", description="A movie discovery guide for trailers, cast, stories and what to watch next.";
  function meta(key, value, property){ var selector=property?'meta[property="'+key+'"]':'meta[name="'+key+'"]'; var el=document.querySelector(selector); if(!el){ el=document.createElement('meta'); el.setAttribute(property?'property':'name',key); document.head.appendChild(el); } el.setAttribute('content',value); }
  var canonical=document.querySelector('link[rel="canonical"]'); if(!canonical){ canonical=document.createElement('link'); canonical.rel='canonical'; document.head.appendChild(canonical); } canonical.href=siteUrl+'/';
  meta('og:url',siteUrl+'/',true); meta('og:site_name',name,true); meta('twitter:card','summary_large_image');
  if(!document.title || document.title==='NEXTCLIP') document.title=name+' — Movie discovery';
  meta('description', description);
}());
