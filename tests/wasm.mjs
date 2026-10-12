import {runtimeActionSound} from '../site/action-sounds.js';
// Verify the exact vendored WASM and Worker adapter in a Node VM.
// XMLHttpRequest and importScripts only map local files; no network access.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const modelModule=fs.readFileSync(new URL('../site/runtime-story.js',import.meta.url),'utf8');
const {createRuntimeModel,advanceRuntime}=await import('data:text/javascript;base64,'+Buffer.from(modelModule).toString('base64'));
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../site');
const data=JSON.parse(fs.readFileSync(path.join(root,'curriculum.json'),'utf8'));
function workerRun(code,checks=[],observe=false){return new Promise((resolve,reject)=>{
 const events=[];let traceLimit=false;const timer=setTimeout(()=>reject(Error('Runtime timeout')),15000);
 class LocalXHR{open(method,url){this.url=url;}send(){setTimeout(()=>{try{const file=path.join(root,new URL(this.url,'https://local.test/').pathname);const b=fs.readFileSync(file);this.status=200;this.responseURL=this.url;this.response=this.responseType==='arraybuffer'?b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength):b.toString();this.onload?.({});}catch(err){this.onerror?.(err);reject(err);}},0);}}
 const context={console:process.env.DEBUG?console:{log(){},warn(){},error(){}},URL,WebAssembly,Uint8Array,Int8Array,Uint16Array,Int16Array,Int32Array,Uint32Array,Float32Array,Float64Array,ArrayBuffer,TextDecoder,TextEncoder,XMLHttpRequest:LocalXHR,setTimeout:(...args)=>setTimeout(...args).unref(),clearTimeout,setInterval:(...args)=>setInterval(...args).unref(),clearInterval,location:{href:'https://local.test/runner.js',pathname:'/runner.js'},postMessage(msg){if(msg.type==='ready'){setTimeout(()=>context.onmessage({data:{code,checks,trace:observe}}),0);}else if(msg.type==='trace-limit'){traceLimit=true;}else if(msg.type==='trace'){events.push(msg.event);}else if(msg.type==='stdout'){events.push({kind:'stdout',text:msg.text});}else if(msg.type==='failure'){clearTimeout(timer);reject(Error(msg.message));}else if(msg.type==='result'){clearTimeout(timer);resolve({...msg,events,traceLimit});}}};
 context.self=context;context.importScripts=(url)=>{const file=path.join(root,new URL(url,'https://local.test/').pathname);vm.runInContext(fs.readFileSync(file,'utf8'),sandbox,{filename:file});};const sandbox=vm.createContext(context);
 try{vm.runInContext(fs.readFileSync(path.join(root,'runner.js'),'utf8'),sandbox,{filename:'runner.js',timeout:10000});}catch(e){clearTimeout(timer);reject(e);}
});}
let failures=0;
for(const l of data.levels){const r=await workerRun(l.solution,l.checks,true);const ok=!r.error&&r.output.replace(/\n+$/,'')===l.expected&&r.tests.every(t=>t.ok);console.log(`${ok?'PASS':'FAIL'} WASM ${String(l.id).padStart(2,'0')} ${l.title}`);if(!ok){console.log(r);failures++;}}
const adventures=JSON.parse(fs.readFileSync(path.join(root,'adventures.json'),'utf8'));
let variants=0;
for(const story of adventures){
 for(const v of story.variants){
  const r=await workerRun(v.code,[],true);
  const model=createRuntimeModel(story.id);for(const event of r.events)advanceRuntime(model,event);
  for(const [key,value] of Object.entries(v.props)){
   if(key==='error')continue;
   const actual=model.props[key];
   const same=typeof value==='number'?Number(actual)===value:JSON.stringify(actual)===JSON.stringify(value);
   if(!same){console.error('FAIL observed scene data',story.id,v.label,key,actual,'expected',value);failures++;}
  }
  const ok=v.props.error?r.error?.includes(v.props.error):!r.error&&r.output.replace(/\n+$/,'')===v.output;
  if(!ok){console.error('FAIL storyboard',story.id,v.label,r);failures++;}variants++;
 }
}
console.log(`Verified ${variants} illustrated inputs in the real browser WASM runtime`);
const loop=await workerRun('set total 0\nforeach n {2 4 6} {incr total $n}\nputs $total',[],true);
const counts=loop.events.filter(e=>e.kind==='incr').map(e=>e.result);
const audioModel=createRuntimeModel(8),collectCues=[];
for(const event of loop.events){const before=structuredClone(audioModel.props),step=audioModel.step;advanceRuntime(audioModel,event);const cue=runtimeActionSound(8,before,audioModel.props,event,step,audioModel.step);if(cue)collectCues.push(cue);}
if(JSON.stringify(collectCues)!=='["collect","collect","collect"]')throw Error('Scene sounds did not match actual WASM collection steps: '+JSON.stringify(collectCues));

if(JSON.stringify(counts)!=='["2","6","12"]')throw Error('Actual loop milestones were not captured: '+JSON.stringify(loop.events));
const literal=await workerRun('puts 12',[],true);const literalModel=createRuntimeModel(8);for(const e of literal.events)advanceRuntime(literalModel,e);if(literalModel.props.total!=='?')throw Error('Printed output invented an accumulator variable');
const dead=await workerRun('# incr total 99\nset total 0\nif {0} {incr total 99}\nputs $total',[],true);
if(dead.events.some(e=>e.kind==='incr'))throw Error('Unexecuted code advanced the story');
const partial=await workerRun('set coins 8\nputs $missing',[],true);
if(!partial.error||!partial.events.some(e=>e.kind==='set'&&e.vars.coins==='8'))throw Error('Partial trace was lost on error');
console.log('Execution traces: loop totals, dead-code rejection, partial failures PASS');
const unopened=await workerRun('proc unopened {} {incr total 999}\nset total 0\nputs $total',[],true);
if(unopened.events.some(e=>e.kind==='incr'))throw Error('An uncalled procedure advanced the story');
const forRun=await workerRun('set total 0\nfor {set i 1} {$i <= 3} {incr i} {incr total $i}\nputs $total',[],true);
const forModel=createRuntimeModel(8);for(const e of forRun.events)advanceRuntime(forModel,e);
if(forModel.props.total!==6||forModel.props.taken!==3)throw Error('For-loop accumulation was not observed');
const readHook='set reads 0\nproc bump args {incr ::reads}\nset coins 8\ntrace add variable coins read bump\nputs $coins\nputs $reads';
const withHook=await workerRun(readHook,[],true),withoutHook=await workerRun(readHook);
if(withHook.output!==withoutHook.output)throw Error('Variable inspection triggered a read hook');
const limited=await workerRun('set total 0\nfor {set i 0} {$i < 1000} {incr i} {incr total}\nputs $total',[],true);
if(limited.output!=='1000'||!limited.traceLimit||limited.events.filter(e=>e.kind!=='stdout').length>256)throw Error('Trace limit lost output or failed to report truncation');
const graded=await workerRun(data.levels[10].solution,data.levels[10].checks,true);
if(graded.events.filter(e=>e.kind==='call'&&e.args[0]==='double').some(e=>e.args[1]!=='7'))throw Error('Grading assertions leaked into the story');
console.log('Bounded long loops, for loops, variable hooks, and grading isolation PASS');

const broken=await workerRun('puts $missing');if(!broken.error?.includes('no such variable'))throw Error('Variable error was not reported');
const malformed=await workerRun('puts {broken');if(!malformed.error?.includes('missing close-brace'))throw Error('Syntax error was not reported');
const unicode=await workerRun('puts "你好，芯片岛！"');if(unicode.output!=='你好，芯片岛！')throw Error('Chinese output failed');
const fresh=await workerRun('info exists hero');if(fresh.result!=='0')throw Error('Variables leaked between runs');
const wrong=await workerRun('proc double {n} {return 14}\nputs [double 7]',data.levels[10].checks);if(wrong.tests.every(t=>t.ok))throw Error('Hard-coded solution passed');
const version=await workerRun('info patchlevel');console.log('Runtime Tcl:',version.result);console.log('Error reporting, UTF-8, isolation, hard-coded-answer rejection: PASS');
process.exitCode=failures?1:0;
