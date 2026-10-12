/* One Worker per run: fresh Tcl interpreter and virtual filesystem. */
importScripts('vendor/require.js');
require.config({baseUrl:new URL('.',self.location.href).href,paths:{tcl:'vendor'}});
require(['tcl/wacl'],function(wacl){
  wacl.onReady(function(interp){
    const M=interp.Module;
    const evaluate=M.cwrap('Tcl_Eval','number',['number','string']);
    const result=M.cwrap('Tcl_GetStringResult','string',['number']);
    evaluate(interp.interp,'encoding system utf-8\nfconfigure stdout -encoding utf-8 -translation lf\nfconfigure stderr -encoding utf-8 -translation lf');
    let output=[];
    interp.stdout=interp.stderr=s=>output.push(String(s).replace(/\r$/,''));
    self.postMessage({type:'ready'});
    self.onmessage=function(e){
      try{
        output=[];
        const code=evaluate(interp.interp,e.data.code);
        const value=result(interp.interp);
        const userOutput=output.join('\n');
        const tests=[];
        if(code===0){
          for(const check of e.data.checks){
            const script=check.script||`expr {${check.expr}}`;
            const status=evaluate(interp.interp,script);
            const v=result(interp.interp);
            tests.push({label:check.label,ok:status===0&&v==='1',error:status!==0?v:undefined});
          }
        }
        self.postMessage({type:'result',output:userOutput,result:value,error:code!==0?value:null,tests});
      }catch(err){self.postMessage({type:'failure',message:String(err)});}
    };
  });
},function(err){self.postMessage({type:'failure',message:'无法加载 Tcl 引擎：'+err});});
