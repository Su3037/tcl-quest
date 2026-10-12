#!/usr/bin/env python3
"""Render original silent code demonstrations; outputs come from real Tcl.
Needs Pillow, ffmpeg, and a Chinese font. No recordings or remote assets.
"""
import argparse,json,subprocess,tempfile,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--lang',choices=['zh','en'],default='zh');p.add_argument('--font',default='/System/Library/Fonts/STHeiti Medium.ttc');a=p.parse_args()
font=ImageFont.truetype(a.font,24);small=ImageFont.truetype(a.font,19);titlefont=ImageFont.truetype(a.font,42)
mono_path='/System/Library/Fonts/Menlo.ttc'
if not Path(mono_path).exists():mono_path='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
mono=ImageFont.truetype(mono_path,20)
levels=json.loads((ROOT/'site/curriculum.json').read_text())['levels']
proc=levels[14]['solution'].split('puts [average')[0]
analyze='''proc analyze {rows} {
    set count 0
    set worst [lindex [lindex $rows 0] 1]
    foreach row $rows {
        lassign $row path slack
        if {$slack < 0} {incr count}
        if {$slack < $worst} {set worst $slack}
    }
    return [dict create violations $count worst $worst]
}
set report {{p1 0.12} {p2 -0.25} {p3 -0.05}}
set result [analyze $report]
puts $result'''
videos=[('第一行代码与变量',[
('让电脑说你好','puts 像小喇叭，双引号把一句话包在一起。','puts "Hello, Tcl!"'),
('为背包贴上名字','set 把值放进一个有名字的变量格子里。','set hero Ada\nputs $hero'),
('拿出格子里的内容','$hero 会替换成变量 hero 里保存的 Ada。','set hero Ada\nputs "Hello $hero"'),
('让计算器加入冒险','方括号先执行 expr，再把结果交给 set。','set energy [expr {4 * 5}]\nputs $energy'),
('区别三种括号','双引号允许替换；花括号保留这段原样文字。','set hero Ada\nputs "Hello $hero"\nputs {Hello $hero}'),
('现在去修好信标','暂停视频，预测输出，再到第 5 关自己试一次。',levels[4]['solution'])]),
('列表、条件与循环',[
('背包里有几个格子','list 保持每件物品的边界，red apple 是一件物品。','set bag [list key "red apple" map]\nputs [llength $bag]'),
('找到第二件物品','索引从 0 开始，所以第二件物品的索引是 1。','set bag [list key "red apple" map]\nputs [lindex $bag 1]'),
('一件一件做相同的事','foreach 把列表元素依次放入 item，再执行脚本。','foreach item {key apple map} {\n    puts $item\n}'),
('让守门人做选择','>= 也包含等于，10 枚金币可以通过。','set coins 10\nif {$coins >= 10} {puts Enter} else {puts Wait}'),
('用循环完成求和','total 从 0 开始，每轮把当前数字加进去。','set total 0\nforeach n {2 4 6} {incr total $n}\nputs $total'),
('把两个本领组合起来','只收集达到门槛的角色。改成 >=8 会怎样？','set selected {}\nforeach row {{Ada 7} {Bo 2} {Cy 5}} {\n    lassign $row name hunger\n    if {$hunger >= 5} {lappend selected $name}\n}\nputs $selected')]),
('过程与安全计算',[
('制作一张技能卡','proc 定义配方，参数是输入，return 是返回的结果。','proc double {n} {return [expr {$n * 2}]}\nputs [double 7]'),
('换一个输入也能用','同一个过程，不需要复制代码。','proc double {n} {return [expr {$n * 2}]}\nputs [double 3]\nputs [double -2]'),
('留意整数除法','5/2 得到 2。使用小数或 double，结果才保留小数。','puts [expr {5 / 2}]\nputs [expr {5 / 2.0}]'),
('先保护空输入','空列表先返回 0，避免平均值计算中除以零。',proc+'puts [average {}]'),
('累加，再除以数量','求和得到 15，除以 3，平均值为 5.0。',proc+'puts [average {2 4 9}]'),
('换数据，验证规则','试试 {1 2} 和 {-2 2}，确认过程真的通用。',proc+'puts [average {1 2}]\nputs [average {-2 2}]')]),
('一份报告，一次芯片冒险',[
('认识简化的时序报告','每行是一条路径和 slack；负余量算作违规。','set report {{p1 0.12} {p2 -0.25} {p3 -0.05}}\nforeach row $report {puts $row}'),
('拆开一行数据','lassign 把一行按顺序交给 path 和 slack。','lassign {p2 -0.25} path slack\nputs "Path: $path"\nputs "Slack: $slack ns"'),
('数出没有达标的路径','循环里遇到 slack<0，就给 count 加一。','set count 0\nforeach row {{p1 0.12} {p2 -0.25} {p3 -0.05}} {\n    lassign $row path slack\n    if {$slack < 0} {incr count}\n}\nputs "Violations: $count"'),
('寻找最差余量','worst 从第一条记录开始，依次保留更小的值。','set worst 0.12\nforeach slack {0.12 -0.25 -0.05} {\n    if {$slack < $worst} {set worst $slack}\n}\nputs "Worst: $worst ns"'),
('用字典交付结果','结果可以继续交给别的 Tcl 脚本处理。',analyze),
('毕业前的最后检查','这段动画演示非空输入；第 20 关还要处理空报告。',analyze+'\nputs [dict get $result violations]')])]
if a.lang=='en':
 translated=json.loads((ROOT/'site/locales/media.en.json').read_text())
 videos=[(tr['title'],[(heading,caption,old[2]) for (heading,caption),old in zip(tr['scenes'],original[1])]) for tr,original in zip(translated,videos)]
suffix='-en' if a.lang=='en' else ''
media=ROOT/'site/media';media.mkdir(exist_ok=True)
def wrap(draw,txt,f,maxw):
 lines=[];line=''
 for c in txt:
  if draw.textlength(line+c,font=f)>maxw:lines.append(line);line=c
  else:line+=c
 lines.append(line);return lines
for v,(title,scenes) in enumerate(videos,1):
 transcript=[title,'Original silent demo · 10 seconds per scene · Output from real Tcl' if a.lang=='en' else '原创无配音代码演示 · 每段 10 秒 · 输出来自真实 Tcl'];vtt=['WEBVTT','']
 with tempfile.TemporaryDirectory(prefix='tcl-video-') as tmp:
  for i,(heading,caption,code) in enumerate(scenes):
   run=subprocess.run(['tclsh'],input=code,text=True,capture_output=True,timeout=5)
   if run.stderr:raise RuntimeError(run.stderr)
   out=run.stdout.rstrip('\n')
   im=Image.new('RGB',(1280,720),'#f5f4ec');d=ImageDraw.Draw(im)
   d.rounded_rectangle((38,34,90,85),12,fill='#294c3c');d.text((50,39),'t_',font=font,fill='#c3ef9f')
   d.text((108,45),('Tcl Quest / Chip Island' if a.lang=='en' else 'Tcl Quest / 芯片岛冒险'),font=font,fill='#294c3c');d.text((1060,47),f'WORLD 0{v}',font=small,fill='#66785b')
   d.text((45,112),heading,font=titlefont,fill='#243b32')
   d.rounded_rectangle((45,184,815,596),16,fill='#23362e');d.text((66,202),'quest.tcl   /   REAL TCL OUTPUT',font=mono,fill='#afc69e')
   for j,line in enumerate(code.splitlines()):
    d.text((66,246+j*24),f'{j+1:02d}',font=small,fill='#728a74');d.text((104,246+j*24),line,font=mono,fill='#e1efcf')
   d.rounded_rectangle((837,184,1235,596),16,fill='#e5ecda');d.text((860,205),('Output' if a.lang=='en' else '运行结果'),font=font,fill='#294c3c')
   for j,line in enumerate(out.splitlines()):
    for k,piece in enumerate(textwrap.wrap(line,25) or ['']):d.text((860,255+(j+k)*34),piece,font=mono,fill='#365d35')
   caplines=wrap(d,caption,font,1170)
   for j,line in enumerate(caplines):d.text((50,618+j*31),line,font=font,fill='#334d3e')
   d.rounded_rectangle((45,697,1235,703),3,fill='#d3ddc7');d.rounded_rectangle((45,697,int(45+1190*(i+1)/6),703),3,fill='#7a9e55')
   path=Path(tmp)/f'{i}.png';im.save(path)
   if i==0:im.save(media/f'demo-{v}{suffix}.png')
   begin=f'00:{i*10:02d}.000';end=f'00:{(i+1)*10:02d}.000' if i<5 else '01:00.000'
   vtt.extend([f'{begin} --> {end}',caption,''])
   transcript.extend(['',f'[{i*10:02d}–{(i+1)*10:02d} {"seconds" if a.lang=="en" else "秒"}] {heading}',caption,'',code,'',('Output:' if a.lang=='en' else '输出：'),out])
  listing=Path(tmp)/'frames.txt';listing.write_text(''.join(f"file '{i}.png'\nduration 10\n" for i in range(6))+"file '5.png'\n")
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(listing),'-t','60','-r','10','-c:v','libx264','-preset','fast','-crf','25','-pix_fmt','yuv420p','-movflags','+faststart',str(media/f'demo-{v}{suffix}.mp4')],check=True)
 (media/f'demo-{v}{suffix}.vtt').write_text('\n'.join(vtt));(media/f'demo-{v}{suffix}.txt').write_text('\n'.join(transcript)+'\n')
 print(f'Rendered demo-{v}.mp4',flush=True)
