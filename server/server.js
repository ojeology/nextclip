"use strict";
/* BRYME focused work-publication server: explicit public surface, no bots or mutation. */
const http=require("http"),fs=require("fs"),path=require("path");
const indexing=require("./indexing-api");
const ROOT=path.resolve(__dirname,"..");
const PORT=Number(process.env.PORT||8787),HOST=process.env.HOST||"0.0.0.0";
const MIME={".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"application/javascript; charset=utf-8",".json":"application/json; charset=utf-8",".xml":"application/xml; charset=utf-8",".txt":"text/plain; charset=utf-8",".svg":"image/svg+xml",".png":"image/png",".jpg":"image/jpeg",".jpeg":"image/jpeg",".webp":"image/webp",".ico":"image/x-icon",".woff2":"font/woff2"};
const SECURITY_HEADERS={
 "x-content-type-options":"nosniff","x-frame-options":"SAMEORIGIN","referrer-policy":"strict-origin-when-cross-origin",
 "permissions-policy":"camera=(), microphone=(), geolocation=(), payment=(), usb=()",
 "cross-origin-opener-policy":"same-origin","strict-transport-security":"max-age=31536000; includeSubDomains",
 "content-security-policy":"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'self'; form-action 'self' https:; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self'; upgrade-insecure-requests"
};
const PUBLIC_HTML_DIRS=new Set(["about","author","contact","copyright","corrections","disclaimer","editorial-policy","guides","privacy","terms","tested","writing","learn","tools","glossary","templates","checklists","problems","search","find","start","verification","compare","regional","intelligence","tracker","today","writing-opportunities","essays","read"]);
const PUBLIC_ROOT_FILES=new Set(["index.html","404.html","410.html","robots.txt","sitemap.xml","news-sitemap.xml","feed.xml","favicon.ico","manifest.webmanifest","sw.js","google2ec8f794263d784f.html","yandex_78fdd841f95fa2e1.html","1740cdb82c02b9af13911b38c853e85d2f708322fa0c2c55.txt"]);
const PUBLIC_ASSET_EXT=new Set([".css",".js",".jpg",".jpeg",".png",".svg",".webp",".gif",".ico",".woff2"]);
const MEDIA_FAMILIES=new Set(["sports","movie","movies","series","anime","article","articles","entertainment","genre","genres","year","years","trailers","trending","channels","topic","topics","now","legacy"]);
function loadRedirects(){const out=new Map();try{for(const line of fs.readFileSync(path.join(ROOT,"_redirects"),"utf8").split(/\r?\n/)){const clean=line.trim();if(!clean||clean.startsWith("#"))continue;const [from,to,status]=clean.split(/\s+/);if(status==="301"&&from&&to)out.set(from,to)}}catch{}return out}
const EXACT_REDIRECTS=loadRedirects();
function headers(extra={}){return {...SECURITY_HEADERS,...extra}}
function send(res,status,body,type="text/plain; charset=utf-8",method="GET"){const b=Buffer.isBuffer(body)?body:Buffer.from(String(body));res.writeHead(status,headers({"content-type":type,"content-length":String(b.length),"cache-control":status===200?"public, max-age=300":"no-store"}));if(method==="HEAD")return res.end();res.end(b)}
function safeFile(rel){
 const clean=String(rel||"").replace(/^\/+/,"").replace(/\\/g,"/");if(!clean||clean.includes("\0"))return null;
 const parts=clean.split("/").filter(Boolean);if(parts.some(x=>x.startsWith(".")||x===".."))return null;
 let allowed=false;if(parts.length===1&&PUBLIC_ROOT_FILES.has(parts[0]))allowed=true;
 else if(parts[0]==="assets"&&PUBLIC_ASSET_EXT.has(path.extname(parts.at(-1)).toLowerCase()))allowed=true;
 else if(PUBLIC_HTML_DIRS.has(parts[0])&&(parts.length===1||!path.extname(parts.at(-1))||path.extname(parts.at(-1)).toLowerCase()===".html"))allowed=true;
 if(!allowed)return null;const abs=path.normalize(path.join(ROOT,clean));if(abs!==ROOT&&!abs.startsWith(ROOT+path.sep))return null;
 try{const stat=fs.statSync(abs);if(stat.isFile())return abs;if(stat.isDirectory()){const index=path.join(abs,"index.html");if(fs.statSync(index).isFile())return index}}catch{}return null;
}
function pageFile(name){try{const p=path.join(ROOT,name);return fs.statSync(p).isFile()?p:null}catch{return null}}
function sendFile(res,file,status,method){const body=fs.readFileSync(file),ext=path.extname(file).toLowerCase();return send(res,status,body,MIME[ext]||"application/octet-stream",method)}
function mediaGone(pathname){const first=pathname.split("/").filter(Boolean)[0]||"";return MEDIA_FAMILIES.has(first)}
const server=http.createServer((req,res)=>{
 let url;try{url=new URL(req.url,"http://localhost")}catch{return send(res,400,"Bad request")}
 const method=req.method||"GET";
 let raw;try{raw=decodeURIComponent(url.pathname)}catch{return send(res,400,"Bad request")}
 raw=raw.replace(/\/{2,}/g,"/");

 // Google Indexing API control endpoints. These must be reachable via POST so
 // they are handled before the read-only method gate below.
 if(raw==="/api/index/status"){return send(res,200,JSON.stringify({ok:true,configured:indexing.enabled(),site:indexing.SITE_URL})+"\n","application/json; charset=utf-8",method)}
 if(raw==="/api/index/notify"){
   if(method!=="POST"){res.writeHead(405,headers({allow:"POST","content-type":"application/json; charset=utf-8"}));return res.end(JSON.stringify({ok:false,error:"method not allowed"})+"\n")}
   const auth=(req.headers.authorization||"").replace(/^Bearer\s+/i,"").trim();
   if(!indexing.PUBLISHER_TOKEN||auth!==indexing.PUBLISHER_TOKEN){res.writeHead(401,headers({"content-type":"application/json; charset=utf-8"}));return res.end(JSON.stringify({ok:false,error:"unauthorized"})+"\n")}
   let body="";req.on("data",c=>{body+=c;if(body.length>65536)req.destroy()});
   req.on("end",async()=>{let payload={};try{payload=JSON.parse(body||"{}")}catch{payload={} }
     const result=await indexing.notify(payload.url||"/", payload.type||"updated");
     const status=result.ok?202:400;
     res.writeHead(status,headers({"content-type":"application/json; charset=utf-8"}));res.end(JSON.stringify(result)+"\n");
   });
   return
 }

 if(!["GET","HEAD"].includes(method)){res.writeHead(405,headers({allow:"GET, HEAD","content-type":"text/plain; charset=utf-8"}));return res.end("Method not allowed")}
 if(raw==="/healthz")return send(res,200,JSON.stringify({ok:true,service:"bryme-work"})+"\n","application/json; charset=utf-8",method);
 if(EXACT_REDIRECTS.has(raw)){res.writeHead(301,headers({location:EXACT_REDIRECTS.get(raw),"cache-control":"public, max-age=86400"}));return res.end()}
 if(mediaGone(raw)){const gone=pageFile("410.html")||pageFile("404.html");return gone?sendFile(res,gone,410,method):send(res,410,"This media route moved out of BRYME.",undefined,method)}
 if(/\/index\.html$/i.test(raw)){const target=raw.replace(/index\.html$/i,"")||"/";res.writeHead(308,headers({location:target+(url.search||""),"cache-control":"public, max-age=86400"}));return res.end()}
 const requested=raw==="/"?"index.html":raw.replace(/^\//,"");const file=safeFile(requested);
 if(file&&raw!=="/"&&!raw.endsWith("/")&&path.basename(file)==="index.html"){res.writeHead(308,headers({location:raw+"/"+(url.search||""),"cache-control":"public, max-age=86400"}));return res.end()}
 if(file)return sendFile(res,file,200,method);
 const missing=pageFile("404.html");return missing?sendFile(res,missing,404,method):send(res,404,"Not found",undefined,method);
});
if(require.main===module)server.listen(PORT,HOST,()=>console.log(`BRYME work publication listening on ${HOST}:${PORT}`));
module.exports={server,PUBLIC_HTML_DIRS,PUBLIC_ROOT_FILES,SECURITY_HEADERS,MEDIA_FAMILIES};
