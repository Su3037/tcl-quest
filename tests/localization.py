"""English parity, media and language assets without external dependencies."""
import json,re,struct,unittest,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
HAN=re.compile(r'[\u3400-\u9fff]')
class Localization(unittest.TestCase):
 def test_course_parity(self):
  zh=json.loads((R/'site/curriculum.json').read_text());en=json.loads((R/'site/curriculum.en.json').read_text())
  self.assertEqual(len(en['levels']),20)
  for a,b in zip(zh['levels'],en['levels']):
   with self.subTest(lesson=a['id']):
    for key in ['id','world','boss','xp','minutes','solution','expected']:self.assertEqual(a[key],b[key],key)
    for key in ['title','topic','story','quiz','pitfall','transfer','task']:self.assertTrue(b[key]);self.assertIsNone(HAN.search(b[key]),key)
    for key in ['explain','hints','choices','diagram']:
     self.assertEqual(len(a[key]),len(b[key]))
     for value in b[key]:self.assertIsNone(HAN.search(value),key)
    self.assertEqual(a['answer'],b['answer'])
    for c,d in zip(a['checks'],b['checks']):
     self.assertIsNone(HAN.search(d['label']))
     self.assertEqual({k:v for k,v in c.items() if k!='label'},{k:v for k,v in d.items() if k!='label'})
    path=R/'lessons'/f'{a["id"]:02d}'/'README.en.md';self.assertIn(b['task'],path.read_text())
 def test_story_parity(self):
  zh=json.loads((R/'site/adventures.json').read_text());en=json.loads((R/'site/adventures.en.json').read_text())
  for a,b in zip(zh,en):
   self.assertEqual(a['id'],b['id']);self.assertEqual(len(b['steps']),4)
   for old,new in zip(a['steps'],b['steps']):self.assertEqual(old['line'],new['line']);self.assertIsNone(HAN.search(new['title']+new['text']))
   for old,new in zip(a['variants'],b['variants']):
    for k in ['code','output','props']:self.assertEqual(old[k],new[k])
    self.assertIsNone(HAN.search(new['label']))
 def test_english_media(self):
  for i in range(1,5):
   for suffix in ['mp4','png','vtt','txt']:self.assertTrue((R/'site/media'/f'demo-{i}-en.{suffix}').is_file())
   video=(R/'site/media'/f'demo-{i}-en.mp4').read_bytes();self.assertEqual(video[4:8],b'ftyp');self.assertIn(b'moov',video)
   for suffix in ['vtt','txt']:self.assertIsNone(HAN.search((R/'site/media'/f'demo-{i}-en.{suffix}').read_text()))
  for i in range(1,21):
   svg=ET.fromstring((R/'site/media/scenes'/f'level-{i:02d}-en.svg').read_text())
   for node in svg.iter():
    if node.tag.endswith('text'):self.assertIsNone(HAN.search(node.text or ''),(i,node.text))
 def test_catalog_and_runtime_bundle(self):
  messages=json.loads((R/'site/locales/en.json').read_text());self.assertGreater(len(messages['text']),200)
  for value in messages['text'].values():self.assertIsNone(HAN.search(value))
  source=(R/'site/trace-source.js').read_text().split('self.QUEST_TRACE_TCL = ',1)[1].rstrip('\n;')
  self.assertEqual(json.loads(source),(R/'site/trace.tcl').read_text())
  self.assertIn('id="language"',(R/'site/index.html').read_text())
if __name__=='__main__':unittest.main()
