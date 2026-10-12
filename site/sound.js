/* Unlock one reusable context during a click, before Worker/replay callbacks. */
const melodies={
  enable:[523.25,783.99], run:[392], success:[659.25,783.99],
  error:[220,174.61], reward:[523.25,659.25,783.99,1046.5]
};
export function createSoundPlayer({Context=globalThis.AudioContext||globalThis.webkitAudioContext,onStatus=()=>{}}={}){
  let enabled=false,context=null,master=null,revision=0,pending=null;
  const voices=new Set();
  function status(value){onStatus(value);}
  function stop(){
    if(master)master.gain.value=0;
    for(const voice of voices){try{voice.stop();}catch{}voice.disconnect();}
    voices.clear();
  }
  function unlock(){
    if(!enabled)return Promise.resolve(false);
    if(!Context){status('unsupported');return Promise.resolve(false);}
    try{
      if(!context||context.state==='closed'){
        context=new Context();master=context.createGain();master.gain.value=0;master.connect(context.destination);
        context.onstatechange=()=>{if(enabled&&context.state!=='running')status('blocked');};
      }
      if(context.state==='running'){status('ready');return Promise.resolve(true);}
      if(pending)return pending;
      status('pending');
      // Call resume synchronously in the input handler, not after an await.
      const resume=context.resume();let timeout;
      pending=Promise.race([
        Promise.resolve(resume).then(()=>context.state==='running'),
        new Promise(resolve=>{timeout=setTimeout(()=>resolve(false),1800);})
      ]).catch(()=>false).then(ok=>{if(enabled)status(ok?'ready':'blocked');return ok;}).finally(()=>{clearTimeout(timeout);pending=null;});
      return pending;
    }catch{status('blocked');return Promise.resolve(false);}
  }
  async function play(name){
    if(!enabled||!melodies[name])return false;
    const request=revision;
    if(!await unlock()||!enabled||request!==revision)return false;
    try{
      master.gain.value=.22;
      const start=context.currentTime+.015;
      melodies[name].forEach((frequency,i)=>{
        const oscillator=context.createOscillator(),gain=context.createGain(),at=start+i*.13;
        oscillator.type='triangle';oscillator.frequency.value=frequency;
        gain.gain.setValueAtTime(0,at);gain.gain.linearRampToValueAtTime(.27,at+.012);
        gain.gain.exponentialRampToValueAtTime(.001,at+.18);
        oscillator.connect(gain);gain.connect(master);voices.add(oscillator);
        oscillator.onended=()=>{voices.delete(oscillator);oscillator.disconnect();gain.disconnect();};
        oscillator.start(at);oscillator.stop(at+.19);
      });
      status('ready');return true;
    }catch{stop();status('blocked');return false;}
  }
  function setEnabled(value,{preview=true}={}){
    revision++;enabled=!!value;
    if(!enabled){stop();status('off');return Promise.resolve(false);}
    status('pending');return preview?play('enable'):Promise.resolve(false);
  }
  return {setEnabled,play,unlock,get enabled(){return enabled;}};
}
