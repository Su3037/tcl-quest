"""Exercise every scene/variant/beat and reject malformed SVG or invalid coordinates."""
import json,subprocess,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Artwork(unittest.TestCase):
 def test_every_scene_frame_is_valid_svg(self):
  code="""
import fs from 'node:fs';
const source=fs.readFileSync('site/adventure-art.js','utf8');
const {sceneSVG}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const stories=JSON.parse(fs.readFileSync('site/adventures.json','utf8'));
const frames=[];
for(const s of stories)for(const v of s.variants)for(let beat=0;beat<4;beat++)
 frames.push({id:s.id,label:v.label,beat,svg:sceneSVG(s.id,Math.floor((s.id-1)/5),v.props,beat)});
frames.push({id:8,label:'third of five live items',beat:3,svg:sceneSVG(8,1,{runtime:true,items:[1,2,3,4,5],taken:3,previousTaken:2,walk:true,total:6},3)});
frames.push({id:20,label:'large slack values',beat:3,svg:sceneSVG(20,3,{rows:[['p1',1e300],['p2',-1e300]],violations:1,worst:'-1e300'},3)});
console.log(JSON.stringify(frames));
"""
  r=subprocess.run(['node','--input-type=module','-e',code],cwd=ROOT,text=True,capture_output=True,timeout=15)
  self.assertEqual(r.returncode,0,r.stderr)
  frames=json.loads(r.stdout);self.assertEqual(len(frames),242)
  for f in frames:
   with self.subTest(level=f['id'],input=f['label'],beat=f['beat']):
    svg=ET.fromstring(f['svg']);self.assertEqual(svg.get('role'),'img')
    self.assertIn('芯芯',svg.get('aria-label',''))
    if f['label']=='third of five live items':
     texts=[n.text for n in svg.iter() if n.tag.endswith('text')]
     self.assertIn('+3',texts);self.assertNotIn('+5',texts)
    self.assertNotIn('Infinity',f['svg']);self.assertNotIn('NaN',f['svg']);self.assertNotIn('undefined',f['svg'].replace('undefined</text>','</text>'))
if __name__=='__main__':unittest.main()
