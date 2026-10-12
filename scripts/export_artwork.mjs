// Export the same original vectors for both languages in GitHub Markdown.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const source=fs.readFileSync(path.join(root,'site/adventure-art.js'),'utf8');
const {CAST,character,sceneSVG,setArtTranslator}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const core=fs.readFileSync(path.join(root,'site/locale-core.js'),'utf8');
const {translateText}=await import('data:text/javascript;base64,'+Buffer.from(core).toString('base64'));
const messages=JSON.parse(fs.readFileSync(path.join(root,'site/locales/en.json'),'utf8'));
const sceneDir=path.join(root,'site/media/scenes');fs.mkdirSync(sceneDir,{recursive:true});
for(const lang of ['zh','en']){
 const suffix=lang==='en'?'-en':'',tr=lang==='en'?s=>translateText(s,messages):s=>s;
 setArtTranslator(tr);
 const stories=JSON.parse(fs.readFileSync(path.join(root,`site/adventures${lang==='en'?'.en':''}.json`),'utf8'));
 for(const story of stories)fs.writeFileSync(path.join(sceneDir,`level-${String(story.id).padStart(2,'0')}${suffix}.svg`),sceneSVG(story.id,Math.floor((story.id-1)/5),story.variants[0].props,3,'ready',false)+'\n');
 const cards=CAST.map((c,i)=>`<g transform="translate(${30+i*214} 77)"><rect width="196" height="207" rx="18" fill="#fffdf4" stroke="#d7dfc8"/><g transform="translate(45 6) scale(.9)">${character(c.kind)}</g><text x="98" y="153" text-anchor="middle" fill="#355448" font-size="23" font-weight="600">${tr(c.name)}</text><text x="98" y="181" text-anchor="middle" fill="#718168" font-size="${lang==='en'?10:12}">${tr(c.role)}</text></g>`).join('');
 const title=lang==='en'?'Tcl Quest · Your Chip Island companions':'Tcl Quest · 你的芯片岛伙伴';
 const label=lang==='en'?'Chip Island companions: Chip, Hoot, Sprout, Rivet and Lolo':'芯片岛冒险的五位伙伴：芯芯、咕咕、芽芽、铆铆、洛洛';
 const sheet=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 310" role="img" aria-label="${label}"><rect width="1100" height="310" rx="20" fill="#f0f3e5"/><g font-family="PingFang SC,Microsoft YaHei,sans-serif"><text x="30" y="45" fill="#355448" font-size="26" font-weight="600">${title}</text>${cards}</g></svg>\n`;
 fs.writeFileSync(path.join(root,`site/media/party${suffix}.svg`),sheet);
}
console.log('Exported 40 lesson illustrations and two character sheets');
