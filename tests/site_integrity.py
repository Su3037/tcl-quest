"""Content and local-resource integrity checks without third-party packages."""
import hashlib,json,re,struct,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Site(unittest.TestCase):
 def test_curriculum(self):
  data=json.loads((ROOT/'site/curriculum.json').read_text());levels=data['levels']
  self.assertEqual([l['id'] for l in levels],list(range(1,21)))
  self.assertEqual(len(data['worlds']),4);self.assertEqual(sum(l['xp'] for l in levels),2400)
  self.assertEqual([l['id'] for l in levels if l['boss']],[5,10,15,20])
  for l in levels:
   with self.subTest(level=l['id']):
    self.assertEqual(l['world'],(l['id']-1)//5)
    self.assertGreaterEqual(len(l['explain']),2);self.assertEqual(len(l['hints']),2)
    self.assertLess(l['answer'],len(l['choices']))
    d=ROOT/'lessons'/f'{l["id"]:02d}'
    self.assertTrue((ROOT/'site/media/scenes'/f'level-{l["id"]:02d}.svg').is_file())
    self.assertIn(f'level-{l["id"]:02d}.svg',(d/'README.md').read_text())
    for key in ('solution','starter','example'):self.assertEqual((d/(key+'.tcl')).read_text(),l[key]+'\n')
    self.assertIn(l['task'],(d/'README.md').read_text())
 def test_assets(self):
  for f in ['app.js','adventure.js','adventure-art.js','adventures.json','style.css','curriculum.json','runner.js','icon.svg','vendor/require.js','vendor/wacl.js','vendor/wacl.wasm','vendor/wacl-library.data','vendor/wacl-custom.data']:
   self.assertTrue((ROOT/'site'/f).is_file(),f)
  for i in range(1,5):
   for ext in ('mp4','png','vtt','txt'):self.assertTrue((ROOT/'site/media'/f'demo-{i}.{ext}').is_file())
   b=(ROOT/'site/media'/f'demo-{i}.mp4').read_bytes();self.assertEqual(b[4:8],b'ftyp')
   self.assertIn(b'moov',b);self.assertIn(b'mdat',b)
   self.assertTrue((ROOT/'site/media'/f'demo-{i}.vtt').read_text().startswith('WEBVTT'))
 def test_vendor_hashes(self):
  hashes=json.loads((ROOT/'site/vendor/SHA256.json').read_text())
  for f,digest in hashes.items():self.assertEqual(hashlib.sha256((ROOT/'site/vendor'/f).read_bytes()).hexdigest(),digest,f)
 def test_no_remote_runtime_dependencies(self):
  for file in ['index.html','app.js','adventure.js','adventure-art.js','style.css','runner.js']:
   s=(ROOT/'site'/file).read_text()
   self.assertNotRegex(s,r'(src|href)=[\"\']https?://[^\"\']+\.(?:js|css)')
 def test_publication_guard(self):
  workflow=(ROOT/'.github/workflows/pages.yml').read_text()
  self.assertIn("github.event.repository.visibility == 'public'",workflow)
  self.assertNotIn('push:',workflow)
if __name__=='__main__':unittest.main()
