#!/usr/bin/env python3
"""Run real Tcl in a temporary working directory; stdout + semantic checks."""
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(level,code):
 if not shutil.which('tclsh'): raise SystemExit('请先安装 Tcl 8.6+，确保 tclsh 在 PATH 中。')
 with tempfile.TemporaryDirectory(prefix='tcl-quest-') as directory:
  p=Path(directory)/'main.tcl';p.write_text(code)
  checks=[]
  for i,c in enumerate(level['checks']):
   script=c.get('script', 'expr {'+c.get('expr','')+'}')
   checks.append(f'set __quest_code [catch {{{script}}} __quest_value]\nputs stderr "QUEST_CHECK_{i}:$__quest_code:$__quest_value"')
  wrapper=Path(directory)/'runner.tcl'
  wrapper.write_text('if {[catch {source main.tcl} __quest_error]} {puts stderr $__quest_error; exit 1}\n'+'\n'.join(checks)+'\n')
  try:r=subprocess.run(['tclsh',str(wrapper)],cwd=directory,capture_output=True,text=True,timeout=5)
  except subprocess.TimeoutExpired:return False,'运行超时（5 秒），请检查循环。'
  problems=[]
  if r.returncode:problems.append('Tcl 错误：'+r.stderr)
  if r.stdout.rstrip('\n')!=level['expected']:problems.append('输出不匹配。期望：\n'+level['expected']+'\n实际：\n'+r.stdout)
  for i,c in enumerate(level['checks']):
   if f'QUEST_CHECK_{i}:0:1' not in r.stderr.splitlines():problems.append('行为检查失败：'+c['label'])
  return not problems,'\n'.join(problems)
def main():
 a=argparse.ArgumentParser();a.add_argument('level',type=int,nargs='?');a.add_argument('file',nargs='?');a.add_argument('--all',action='store_true');args=a.parse_args()
 levels=json.loads((ROOT/'site/curriculum.json').read_text())['levels'];failed=0
 if args.all:
  for l in levels:
   code=(ROOT/'lessons'/f'{l["id"]:02d}'/'solution.tcl').read_text();ok,msg=run(l,code);print(f'{"PASS" if ok else "FAIL"} {l["id"]:02d} {l["title"]}');failed+=not ok
   if msg:print(msg)
   with tempfile.TemporaryDirectory() as d:
    example=subprocess.run(['tclsh',str(ROOT/'lessons'/f'{l["id"]:02d}'/'example.tcl')],cwd=d,text=True,capture_output=True,timeout=5)
    if example.returncode:failed+=1;print('EXAMPLE FAILED:',example.stderr)
 else:
  if not args.level or not args.file:a.error('用法：python3 scripts/check.py 关卡号 文件路径，或 --all')
  if not 1<=args.level<=len(levels):a.error('关卡号为 1–20')
  l=levels[args.level-1];ok,msg=run(l,Path(args.file).read_text());print('PASS · 任务完成' if ok else '还差一点');failed=not ok
  if msg:print(msg)
 raise SystemExit(int(bool(failed)))
if __name__=='__main__':main()
