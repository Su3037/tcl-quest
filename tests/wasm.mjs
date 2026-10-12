// Verify the exact vendored WASM and Worker adapter in a Node VM.
// XMLHttpRequest and importScripts only map local files; no network access.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../site');
const data=JSON.parse(fs.readFileSync(path.join(root,'curriculum.json'),'utf8'));
function workerRun(code,checks=[]){return new Promise((resolve,reject)=>{
 const timer=setTimeout(()=>reject(Error('Runtime timeout')),15000);
 class LocalXHR{open(method,url){this.url=url;}send(){setTimeout(()=>{try{const file=path.join(root,new URL(this.url,'https://local.test/').pathname);const b=fs.readFileSync(file);this.status=200;this.responseURL=this.url;this.response=this.responseType==='arraybuffer'?b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength):b.toString();this.onload?.({});}catch(err){this.onerror?.(err);reject(err);}},0);}}
 const context={console:process.env.DEBUG?console:{log(){},warn(){},error(){}},URL,WebAssembly,Uint8Array,Int8Array,Uint16Array,Int16Array,Int32Array,Uint32Array,Float32Array,Float64Array,ArrayBuffer,TextDecoder,TextEncoder,XMLHttpRequest:LocalXHR,setTimeout:(...args)=>setTimeout(...args).unref(),clearTimeout,setInterval:(...args)=>setInterval(...args).unref(),clearInterval,location:{href:'https://local.test/runner.js',pathname:'/runner.js'},postMessage(msg){if(msg.type==='ready'){setTimeout(()=>context.onmessage({data:{code,checks}}),0);}else if(msg.type==='failure'){clearTimeout(timer);reject(Error(msg.message));}else if(msg.type==='result'){clearTimeout(timer);resolve(msg);}}};
 context.self=context;context.importScripts=(url)=>{const file=path.join(root,new URL(url,'https://local.test/').pathname);vm.runInContext(fs.readFileSync(file,'utf8'),sandbox,{filename:file});};const sandbox=vm.createContext(context);
 try{vm.runInContext(fs.readFileSync(path.join(root,'runner.js'),'utf8'),sandbox,{filename:'runner.js',timeout:10000});}catch(e){clearTimeout(timer);reject(e);}
});}
let failures=0;
for(const l of data.levels){const r=await workerRun(l.solution,l.checks);const ok=!r.error&&r.output.replace(/\n+$/,'')===l.expected&&r.tests.every(t=>t.ok);console.log(`${ok?'PASS':'FAIL'} WASM ${String(l.id).padStart(2,'0')} ${l.title}`);if(!ok){console.log(r);failures++;}}
const adventures=JSON.parse(fs.readFileSync(path.join(root,'adventures.json'),'utf8'));
let variants=0;
for(const story of adventures){
 for(const v of story.variants){
  const r=await workerRun(v.code);
  const ok=v.props.error?r.error?.includes(v.props.error):!r.error&&r.output.replace(/\n+$/,'')===v.output;
  if(!ok){console.error('FAIL storyboard',story.id,v.label,r);failures++;}variants++;
 }
}
console.log(`Verified ${variants} illustrated inputs in the real browser WASM runtime`);
const broken=await workerRun('puts $missing');if(!broken.error?.includes('no such variable'))throw Error('Variable error was not reported');
const malformed=await workerRun('puts {broken');if(!malformed.error?.includes('missing close-brace'))throw Error('Syntax error was not reported');
const unicode=await workerRun('puts "你好，芯片岛！"');if(unicode.output!=='你好，芯片岛！')throw Error('Chinese output failed');
const fresh=await workerRun('info exists hero');if(fresh.result!=='0')throw Error('Variables leaked between runs');
const wrong=await workerRun('proc double {n} {return 14}\nputs [double 7]',data.levels[10].checks);if(wrong.tests.every(t=>t.ok))throw Error('Hard-coded solution passed');
const version=await workerRun('info patchlevel');console.log('Runtime Tcl:',version.result);console.log('Error reporting, UTF-8, isolation, hard-coded-answer rejection: PASS');
process.exitCode=failures?1:0;
