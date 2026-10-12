import assert from 'node:assert/strict';
import {runtimeActionSound,storyActionSound} from '../site/action-sounds.js';
import {createRuntimeModel,advanceRuntime} from '../site/runtime-story.js';

const model=createRuntimeModel(8),heard=[];
function display(event){const before=structuredClone(model.props),step=model.step;advanceRuntime(model,event);const cue=runtimeActionSound(8,before,model.props,event,step,model.step);if(cue)heard.push(cue);}
display({kind:'set',code:0,args:['set','total','0'],result:'0',vars:{total:'0'}});
display({kind:'foreach',phase:'enter',code:0,argLists:{2:['3','5','9']},vars:{total:'0'}});
for(const [n,total] of [[3,3],[5,8],[9,17]])display({kind:'incr',code:0,args:['incr','total',String(n)],result:String(total),vars:{total:String(total)}});
display({kind:'foreach',phase:'leave',code:0,vars:{total:'17'}});
display({kind:'stdout',text:'17'});
assert.deepEqual(heard,['collect','collect','collect'],'exactly one cue per real accumulation; no repeated cue from stdout');
assert.equal(runtimeActionSound(6,{enter:false},{enter:true},{kind:'call',code:0},0,2),'door');
assert.equal(runtimeActionSound(6,{enter:false},{enter:false},{kind:'call',code:0},0,2),'denied');
assert.equal(runtimeActionSound(6,{enter:true},{enter:true},{kind:'stdout'},2,3),null);
assert.equal(runtimeActionSound(7,{items:[]},{items:['map']},{kind:'list',code:0},0,1),'item');
assert.equal(runtimeActionSound(2,{coins:0},{coins:12},{kind:'set',code:1},0,1),null,'failed operations must not sound successful');
assert.equal(runtimeActionSound(8,{taken:0},{taken:1,walk:true},{kind:'foreach',phase:'enter',code:0},0,1),null);
assert.equal(runtimeActionSound(18,{},{},{kind:'object-deleted',args:['chip']},2,3),'vanish');
assert.equal(storyActionSound(6,2,{enter:true}),'door');assert.equal(storyActionSound(6,2,{enter:false}),'denied');
for(let id=1;id<=20;id++){assert.equal(storyActionSound(id,0),null);for(let step=1;step<=3;step++)assert.ok(storyActionSound(id,step),`lesson ${id}, beat ${step}`);}
console.log('Action cues: real collection changes, gates, items, failures, destruction and all 60 teaching transitions pass.');
