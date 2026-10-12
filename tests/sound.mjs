import assert from 'node:assert/strict';
import {createSoundPlayer} from '../site/sound.js';

class FakeContext{
  static instances=[];
  constructor(){this.state='suspended';this.currentTime=5;this.destination={};this.notes=[];this.resumes=0;FakeContext.instances.push(this);}
  createGain(){return {gain:{value:0,setValueAtTime(){},linearRampToValueAtTime(){},exponentialRampToValueAtTime(){}},connect(){},disconnect(){}};}
  createOscillator(){const node={frequency:{},connect(){},disconnect(){},start(at){this.at=at;},stop(at){this.stopped=at??true;}};this.notes.push(node);return node;}
  resume(){this.resumes++;this.state='running';return Promise.resolve();}
}
let status;
const sound=createSoundPlayer({Context:FakeContext,onStatus:value=>status=value});
assert.equal(await sound.play('reward'),false);
assert.equal(FakeContext.instances.length,0,'disabled audio must not create a context');
const preview=sound.setEnabled(true);
assert.equal(FakeContext.instances[0].resumes,1,'resume must be invoked synchronously inside the click handler');
assert.equal(await preview,true);
const context=FakeContext.instances[0];
assert.equal(status,'ready');assert.equal(context.notes.length,2,'enabling previews a chime');
for(const name of ['run','success','error','reward'])assert.equal(await sound.play(name),true);
assert.equal(FakeContext.instances.length,1,'async results and delayed rewards reuse the unlocked context');
assert.equal(context.notes.length,11);
assert.ok(context.notes.every(note=>note.frequency.value>0&&note.stopped>note.at));
await sound.setEnabled(false);
assert.equal(status,'off');assert.ok(context.notes.every(note=>note.stopped===true),'mute cancels all current and queued tones');
assert.equal(await sound.play('run'),false);

const channels=createSoundPlayer({Context:FakeContext});
await channels.setEnabled(true,{preview:false});
assert.equal(await channels.play('collect',{channel:'scene'}),true);
const channelContext=FakeContext.instances.at(-1),collected=[...channelContext.notes];
assert.equal(await channels.play('click',{channel:'ui'}),true);
assert.equal(await channels.play('click',{channel:'ui'}),false,'rapid clicks are bounded');
const click=channelContext.notes.at(-1);
channels.stop('scene');
assert.ok(collected.every(note=>note.stopped===true));
assert.notEqual(click.stopped,true,'pausing scene audio must not cancel UI feedback');
channelContext.currentTime+=.07;
assert.equal(await channels.play('door',{channel:'scene'}),true);
await channels.setEnabled(false);assert.ok(channelContext.notes.every(note=>note.stopped===true));

const countBeforeRestore=FakeContext.instances.length;
const saved=createSoundPlayer({Context:FakeContext});
await saved.setEnabled(true,{preview:false});
assert.equal(FakeContext.instances.length,countBeforeRestore,'restoring preference must not autoplay');
assert.equal(await saved.play('run'),true);
const savedContext=FakeContext.instances.at(-1);savedContext.state='suspended';
assert.equal(await saved.play('success'),true);assert.equal(savedContext.resumes,2,'resume again after suspension');

class DelayedContext extends FakeContext{resume(){this.resumes++;return new Promise(resolve=>{this.release=()=>{this.state='running';resolve();};});}}
const delayed=createSoundPlayer({Context:DelayedContext});
const loading=delayed.setEnabled(true),pendingContext=FakeContext.instances.at(-1);
await delayed.setEnabled(false);pendingContext.release();
assert.equal(await loading,false);assert.equal(pendingContext.notes.length,0,'turning off while resume is pending must stay silent');

const paused=createSoundPlayer({Context:DelayedContext});
await paused.setEnabled(true,{preview:false});
const queued=paused.play('collect',{channel:'scene'}),queuedContext=FakeContext.instances.at(-1);
paused.stop('scene');queuedContext.release();
assert.equal(await queued,false);assert.equal(queuedContext.notes.length,0,'pause cancels scene tones waiting for audio activation');

class RejectedContext extends FakeContext{resume(){return Promise.reject(Error('blocked'));}}
const blocked=createSoundPlayer({Context:RejectedContext,onStatus:value=>status=value});
assert.equal(await blocked.setEnabled(true),false);assert.equal(status,'blocked');
const unsupported=createSoundPlayer({Context:null,onStatus:value=>status=value});
assert.equal(await unsupported.setEnabled(true),false);assert.equal(status,'unsupported');
console.log('Sound: gesture unlock, preview, async playback, mute, persistence, suspension and failures pass.');
