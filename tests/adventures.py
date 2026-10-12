"""Check storyboard sources and real Tcl results, including the intentional error."""
import json,os,shutil,subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Adventures(unittest.TestCase):
 def test_every_runnable_input(self):
  stories=json.loads((ROOT/'site/adventures.json').read_text())
  levels=json.loads((ROOT/'site/curriculum.json').read_text())['levels']
  tcl=os.environ.get('TCLSH') or shutil.which('tclsh')
  self.assertTrue(tcl,'Install Tcl 8.6+ to verify the storyboards')
  self.assertEqual([s['id'] for s in stories],list(range(1,21)))
  for l,s in zip(levels,stories):
   self.assertEqual(len(s['steps']),4);self.assertEqual(len(s['variants']),3)
   self.assertEqual(s['variants'][0]['code'],l['solution'])
   self.assertEqual(s['variants'][0]['output'],l['expected'])
   for v in s['variants']:
    with self.subTest(level=s['id'],input=v['label']):
     for beat in s['steps']:self.assertLess(beat['line'],len(v['code'].splitlines()))
     with tempfile.TemporaryDirectory() as tmp:
      script=Path(tmp)/'story.tcl';script.write_text('encoding system utf-8\n'+v['code']+'\n')
      r=subprocess.run([tcl,str(script)],cwd=tmp,text=True,capture_output=True,timeout=5)
     if v['props'].get('error'):
      self.assertNotEqual(r.returncode,0);self.assertIn(v['props']['error'],r.stderr)
     else:
      self.assertEqual(r.returncode,0,r.stderr)
      self.assertEqual(r.stdout.rstrip('\n'),v['output'])
if __name__=='__main__':unittest.main()
