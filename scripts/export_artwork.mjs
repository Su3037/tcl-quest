// Export the same original vectors for GitHub's Markdown renderer (no animation).
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const source=fs.readFileSync(path.join(root,'site/adventure-art.js'),'utf8');
const {CAST,character,sceneSVG}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const stories=JSON.parse(fs.readFileSync(path.join(root,'site/adventures.json'),'utf8'));
const sceneDir=path.join(root,'site/media/scenes');fs.mkdirSync(sceneDir,{recursive:true});
for(const story of stories)fs.writeFileSync(path.join(sceneDir,`level-${String(story.id).padStart(2,'0')}.svg`),sceneSVG(story.id,Math.floor((story.id-1)/5),story.variants[0].props,3,'ready',false)+'\n');
const cards=CAST.map((c,i)=>`<g transform="translate(${30+i*214} 77)"><rect width="196" height="207" rx="18" fill="#fffdf4" stroke="#d7dfc8"/><g transform="translate(45 6) scale(.9)">${character(c.kind)}</g><text x="98" y="153" text-anchor="middle" fill="#355448" font-size="23" font-weight="600">${c.name}</text><text x="98" y="181" text-anchor="middle" fill="#718168" font-size="12">${c.role}</text></g>`).join('');
const sheet=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 310" role="img" aria-label="芯片岛冒险的五位伙伴：芯芯、咕咕、芽芽、铆铆、洛洛"><rect width="1100" height="310" rx="20" fill="#f0f3e5"/><g font-family="PingFang SC,Microsoft YaHei,sans-serif"><text x="30" y="45" fill="#355448" font-size="26" font-weight="600">Tcl Quest · 你的芯片岛伙伴</text>${cards}</g></svg>\n`;
fs.writeFileSync(path.join(root,'site/media/party.svg'),sheet);
console.log('Exported 20 lesson illustrations and one character sheet');
