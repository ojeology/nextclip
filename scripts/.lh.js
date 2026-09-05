const net=require("net"),{spawn}=require("child_process");
function fp(){return new Promise((r,j)=>{const s=net.createServer();s.listen(0,"127.0.0.1",()=>{const p=s.address().port;s.close(()=>r(p))});s.on("error",j)})}
(async()=>{const port=await fp();const c=spawn(process.execPath,["server/server.js"],{cwd:process.cwd(),env:{...process.env,PORT:String(port),HOST:"127.0.0.1"},stdio:"ignore"});await new Promise(r=>setTimeout(r,1500));console.log("PORT",port);await c.kill();
})().catch(e=>{console.error(e);process.exit(1)});
