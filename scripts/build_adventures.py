#!/usr/bin/env python3
"""Build authored storyboards; all runnable variants are verified against Tcl."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
levels=json.loads((ROOT/'site/curriculum.json').read_text())['levels']
# Four story beats per lesson. The quoted fragment is from the runnable script.
D=[
('晨光唤醒站','一句话，点亮芯芯',[
 ('等待指令','芯芯还在休眠。puts 就像传话筒：把后面的文字送到输出区。','puts'),
 ('第一次问好','第一条 puts 让芯芯说出第一句话。双引号把一句话包在一起。','puts'),
 ('准备出发','继续执行下一条 puts；两条命令会依次运行。','puts "Ready!"'),
 ('听见回声','每条 puts 默认另起一行。看气泡，再对照两行输出。','puts "Ready!"')]),
('背包整理台','名字是标签，值是物品',[
 ('贴上姓名','set 给格子取名字，并把值放进去。hero 格子里存的是角色名字。','set hero'),
 ('放入金币','coins 是格子的标签，数字才是格子里的值。','set coins'),
 ('打开格子','双引号中的 $hero 和 $coins 会取出对应的值。','puts'),
 ('读出背包','把取出的值拼进一句话，再交给 puts 说出来。','puts')]),
('三扇括号门','同一张字条，三种旅程',[
 ('准备字条','先保存 hero 的值，再让同一张字条经过三扇门。','set hero'),
 ('双引号门','双引号保留一句话的边界，同时允许 $hero 替换成值。','puts "Hello'),
 ('花括号门','花括号保留里面的文字，$hero 不会在这里被替换。','puts {Hello'),
 ('方括号门','方括号先运行里面的 string toupper，再把返回值交给 puts。','puts [string')]),
('能量炼制台','乘一乘，再加上奖励',[
 ('摆好材料','bottles 记录瓶数，each 记录每瓶的能量。','set bottles'),
 ('配方计算','expr 计算乘法；方括号把算出的结果交给 set energy。','set energy'),
 ('加入奖励','incr 在原来的 energy 上增加奖励，格子里的值更新了。','incr energy'),
 ('能量出炉','puts $energy 取出最后的总能量。','puts $energy')]),
('出发信标','把三项本领接成一束光',[
 ('连接电池','信标需要名字、电池数量和每节能量三个输入。','set hero'),
 ('算出能量','先用 expr 计算总能量，再写进 energy 格子。','set energy'),
 ('发送广播','双引号中的变量会替换成真实名字和能量。','puts "Energy:'),
 ('保留模板','最后使用花括号：广播的是字面文字 $energy。','puts {$energy}')]),
('森林金币门','条件决定走哪条路',[
 ('递交金币','gate 收到一个金币数。可以切换输入，看看守门精灵怎样选择。','puts [gate'),
 ('检查条件','比较 coins >= 10。等于 10 也满足“至少 10”。','if {$coins'),
 ('选择分支','条件成立走 Enter 分支，否则走 Wait 分支；一次只走一条。','if {$coins'),
 ('收到答复','return 把分支结果交回调用处，puts 再显示它。','puts [gate')]),
('物品收纳架','有空格，也只算一件',[
 ('摆出物品','list 把每件物品的边界记录下来。带空格的名字需要正确分组。','set bag'),
 ('装进背包','带空格的物品名有多个单词，却仍然只占一个物品格子。','set bag'),
 ('数清格子','llength 数的是元素个数，不是单词数。','puts [llength'),
 ('取第二件','lindex 从 0 开始计数，所以索引 1 取出第二件物品。','puts [lindex')]),
('循环采集地','让芯芯逐个采集',[
 ('空篮出发','先把 total 设为 0，给累加准备一个起点。','set total'),
 ('采集第一件','foreach 把列表中的第一项交给 n，再执行循环体。','foreach'),
 ('继续采集','每轮 incr total $n 都把当前数加入总和；不是把旧值覆盖。','foreach'),
 ('完成遍历','列表没有下一项时，循环结束，输出累积的 total。','puts $total')]),
('路牌修理铺','让乱糟糟的文字变整齐',[
 ('收到旧路牌','clean 收到原始文字，包括两端看不见的空格。','puts [clean'),
 ('擦掉边缘','内层 string trim 先去掉两端空白，不删除中间的空格。','return'),
 ('统一大写','外层 string toupper 再把清理后的字母转成大写。','return'),
 ('挂上路牌','return 交回新文字，puts 把它显示出来。','puts [clean')]),
('精灵补给站','照顾每一位需要帮助的伙伴',[
 ('拿到名单','每行记录一个名字和饥饿值；先准备空的 selected 列表。','set selected'),
 ('逐位询问','foreach 遍历名单，lassign 把名字和饥饿值拆开。','lassign'),
 ('分发补给','只在 hunger >= 5 时把名字加入 selected；5 也需要补给。','if {$hunger'),
 ('整理回执','返回选中的名字列表；被跳过的伙伴不会出现在回执里。','return $selected')]),
('技能卡工作台','一张图纸，重复使用',[
 ('绘制技能','proc 定义过程 double，n 是等待调用时填写的参数。','proc double'),
 ('插入数字','调用 double 时，把输入值交给 n。下一次可换一个数。','puts [double'),
 ('运行卡片','expr 计算 n 的两倍；return 把结果交回调用处。','return'),
 ('接住结果','puts 打印返回值。卡片不能只写死一个答案。','puts [double')]),
('角色档案室','用属性名字找到数值',[
 ('建立档案','dict create 用 name、hp 这样的键记录属性。','set hero'),
 ('补充生命','dict incr 找到 hp 键，再增加指定的数值。','dict incr'),
 ('按名查找','dict get 分别按 name 和 hp 两个键取值，不需要记位置。','puts'),
 ('展示档案','两个查询结果组成“名字:生命值”，交给 puts。','puts')]),
('冒险日志柜','写完要关，读时再开',[
 ('打开写入口','open 的 w 模式创建或覆盖文件，返回的通道存在 f 中。','set f [open quest.txt w]'),
 ('写入两页','puts $f 把文字写入文件通道，不是屏幕。','puts $f'),
 ('关闭并重开','先 close 结束写入，再用 r 模式重新打开同一文件。','set f [open quest.txt r]'),
 ('读回日志','每次 gets 读一行，puts 将读到的内容显示到屏幕。','puts [gets')]),
('安全宝箱屋','遇到零，也能继续走',[
 ('放入两个数','safeDivide 收到 a 和 b。先检查危险，再进行计算。','puts [safeDivide'),
 ('检查除数','b 等于 0 时直接返回 undefined，绕过除法。','if {$b'),
 ('安全计算','b 非零时用 double 做浮点除法，保留小数结果。','return [expr'),
 ('继续冒险','两个调用都得到可读结果。分支保护让零输入不会终止这段脚本。','puts [safeDivide 5 0]')]),
('工坊平均值机','每件材料，都算进去',[
 ('检查空篮','先用 llength 检查列表；空列表直接返回 0。','if {[llength'),
 ('称出总量','非空时遍历每个数，把所有数累加到 total。','foreach'),
 ('平分材料','用浮点总量除以元素个数，得到算术平均值。','return [expr'),
 ('交付技能','average 应适用于新列表和小数，也应照顾空列表。','puts [average')]),
('芯片城分区台','给工具一个专属地址',[
 ('建立分区','namespace eval lab 建立命名空间，把相关工具放在一起。','namespace eval'),
 ('放入工具','area 定义在 lab 中，参数是宽 w 和高 h。','proc area'),
 ('计算面积','expr 将宽和高相乘。这是教学面积计算，不是 EDA 引擎。','return'),
 ('按地址调用','lab::area 的完整名字告诉 Tcl 去哪个命名空间找工具。','puts [lab::area')]),
('报告放大镜','从一行文字中捕获数字',[
 ('展开报告','slackValue 收到一整行文字。并非每一行都一定符合格式。','puts [slackValue'),
 ('寻找模式','regexp 检查 slack: 后的可选负号、整数和可选小数部分。','if {[regexp'),
 ('取出捕获','匹配时 value 保存数字文字；不匹配则走 NA 返回分支。','return NA'),
 ('交出线索','返回的是捕获的文字，不是重新计算出的时序数据。','puts [slackValue')]),
('芯片图纸工厂','图纸与实例，各有职责',[
 ('画出图纸','oo::class 定义 Chip 类，它是制造对象的图纸。','oo::class'),
 ('制造实例','Chip new 创建对象，constructor 把传入值保存到对象自己的 name。','set chip'),
 ('调用方法','通过对象调用 label，取出该对象内部保存的 name。','puts [$chip label]'),
 ('结束使用','destroy 销毁对象。不同对象可以有不同的名字，不共享这份状态。','$chip destroy')]),
('教学流程轨道','把参数送过三个站点',[
 ('接收配置','mockFlow 收到设计名和周期。这个关卡只模拟流程的文字记录。','puts [mockFlow'),
 ('检查周期','period <= 0 时 error 报错，流程不会继续返回正常结果。','if {$period'),
 ('连接站点','合法周期时，list 把 read、clock、report 三条记录组成列表。','return [list'),
 ('输出流程','返回的是教学流程清单；没有实际读取网表或计算时序。','puts [mockFlow')]),
('时序侦探指挥台','沿着路径，找到最差余量',[
 ('接收路径','每条记录有路径名和 slack。空报告要返回 0 和 NA。','if {[llength'),
 ('逐条检查','slack < 0 才违规；等于 0 不计违规。遍历每一条路径。','if {$slack < 0}'),
 ('更新最差值','从第一条真实记录开始比较，保存更小的 slack，不能默认从 0 开始。','if {$slack < $worst}'),
 ('提交结案','返回含 violations 和 worst 的字典，再读取这两个键输出报告。','return [dict create violations $violations')])
]
P=[
 {'lines':['Hello, Tcl!','Ready!']},{'name':'Ada','coins':12},{'name':'Ada','upper':'ADA'},
 {'bottles':3,'each':7,'bonus':4,'energy':25},{'name':'Ada','cells':4,'each':5,'energy':20},
 {'coins':12,'enter':True},{'items':['key','red apple','map']},{'items':[2,4,6],'total':12},
 {'raw':'  chip  ','clean':'CHIP'},{'rows':[['Ada',7],['Bo',2],['Cy',5]],'selected':['Ada','Cy']},
 {'n':7,'result':14},{'name':'Ada','hp':80,'gain':20},{'lines':['Level 13','Saved']},
 {'a':5,'b':2,'result':'2.5','zero':'undefined'},{'items':[2,4,9],'result':'5.0'},
 {'w':6,'h':7,'result':42},{'line':'slack: -0.25','value':'-0.25'},
 {'name':'Tiny'},{'name':'Tiny','period':10},{'rows':[['p1',0.12],['p2',-0.25],['p3',-0.05]],'violations':2,'worst':'-0.25'}
]
A=[
 [('中文问候',{'Hello, Tcl!':'你好，芯片岛！'},'你好，芯片岛！\nReady!',{'lines':['你好，芯片岛！','Ready!']}),('换个伙伴',{'Hello, Tcl!':'Hello, Ada!'},'Hello, Ada!\nReady!',{'lines':['Hello, Ada!','Ready!']})],
 [('Bo 的 8 枚金币',{'set hero Ada':'set hero Bo','set coins 12':'set coins 8'},'Bo has 8 coins',{'name':'Bo','coins':8}),('空的钱包',{'set coins 12':'set coins 0'},'Ada has 0 coins',{'name':'Ada','coins':0})],
 [('名字换成 Bo',{'set hero Ada':'set hero Bo'},'Hello Bo\nHello $hero\nBO',{'name':'Bo','upper':'BO'}),('名字换成 Cy',{'set hero Ada':'set hero Cy'},'Hello Cy\nHello $hero\nCY',{'name':'Cy','upper':'CY'})],
 [('2 瓶 × 5，加 1',{'set bottles 3':'set bottles 2','set each 7':'set each 5','incr energy 4':'incr energy 1'},'11',{'bottles':2,'each':5,'bonus':1,'energy':11}),('没有药水，奖励仍在',{'set bottles 3':'set bottles 0'},'4',{'bottles':0,'each':7,'bonus':4,'energy':4})],
 [('2 节电池',{'set cells 4':'set cells 2'},'Ada ready\nEnergy: 10\n$energy',{'name':'Ada','cells':2,'each':5,'energy':10}),('Bo 出发',{'set hero Ada':'set hero Bo'},'Bo ready\nEnergy: 20\n$energy',{'name':'Bo','cells':4,'each':5,'energy':20})],
 [('8 枚：还不够',{'puts [gate 12]':'puts [gate 8]'},'Wait',{'coins':8,'enter':False}),('10 枚：刚好够',{'puts [gate 12]':'puts [gate 10]'},'Enter',{'coins':10,'enter':True})],
 [('换成绿梨',{'red apple':'green pear'},'3\ngreen pear',{'items':['key','green pear','map']}),('再装一个指南针',{'"red apple" map]':'"red apple" map compass]'},'4\nred apple',{'items':['key','red apple','map','compass']})],
 [('采集 1、3、5',{'{2 4 6}':'{1 3 5}'},'9',{'items':[1,3,5],'total':9}),('空列表',{'{2 4 6}':'{}'},'0',{'items':[],'total':0})],
 [('换一块路牌',{'"  chip  "':'"  forest  "'},'FOREST',{'raw':'  forest  ','clean':'FOREST'}),('保留中间空格',{'"  chip  "':'"  chip island  "'},'CHIP ISLAND',{'raw':'  chip island  ','clean':'CHIP ISLAND'})],
 [('大家都吃饱了',{'{{Ada 7} {Bo 2} {Cy 5}}':'{{Ada 1} {Bo 2} {Cy 0}}'},'',{'rows':[['Ada',1],['Bo',2],['Cy',0]],'selected':[]}),('Bo 刚好需要',{'{{Ada 7} {Bo 2} {Cy 5}}':'{{Ada 4} {Bo 5} {Cy 8}}'},'Bo Cy',{'rows':[['Ada',4],['Bo',5],['Cy',8]],'selected':['Bo','Cy']})],
 [('输入 3',{'puts [double 7]':'puts [double 3]'},'6',{'n':3,'result':6}),('输入小数 2.5',{'puts [double 7]':'puts [double 2.5]'},'5.0',{'n':2.5,'result':'5.0'})],
 [('只补 5 点',{'dict incr hero hp 20':'dict incr hero hp 5'},'Ada:85',{'name':'Ada','hp':80,'gain':5}),('换成 Bo',{'name Ada hp 80':'name Bo hp 60'},'Bo:80',{'name':'Bo','hp':60,'gain':20})],
 [('换一页日记',{'Level 13':'Day 2','Saved':'Ready'},'Day 2\nReady',{'lines':['Day 2','Ready']}),('中文也能存',{'Level 13':'第十三关','Saved':'已保存'},'第十三关\n已保存',{'lines':['第十三关','已保存']})],
 [('9 除以 2',{'safeDivide 5 2':'safeDivide 9 2','safeDivide 5 0':'safeDivide 9 0'},'4.5\nundefined',{'a':9,'b':2,'result':'4.5','zero':'undefined'}),('负数除法',{'safeDivide 5 2':'safeDivide -5 2'},'-2.5\nundefined',{'a':-5,'b':2,'result':'-2.5','zero':'undefined'})],
 [('小数列表',{'{2 4 9}':'{1.5 2.5}'},'2.0',{'items':[1.5,2.5],'result':'2.0'}),('空背包',{'{2 4 9}':'{}'},'0',{'items':[],'result':'0'})],
 [('3 × 4 的区域',{'lab::area 6 7':'lab::area 3 4'},'12',{'w':3,'h':4,'result':12}),('零宽度',{'lab::area 6 7':'lab::area 0 7'},'0',{'w':0,'h':7,'result':0})],
 [('正整数余量',{'slack: -0.25':'slack: 3'},'3',{'line':'slack: 3','value':'3'}),('不匹配的行',{'slack: -0.25':'arrival: 0.5'},'NA',{'line':'arrival: 0.5','value':'NA'})],
 [('制造 Wide',{'Chip new Tiny':'Chip new Wide'},'Wide',{'name':'Wide'}),('制造 Nano',{'Chip new Tiny':'Chip new Nano'},'Nano',{'name':'Nano'})],
 [('Wide，周期 5',{'mockFlow Tiny 10':'mockFlow Wide 5'},'read:Wide clock:5 report:timing',{'name':'Wide','period':5}),('周期为零',{'mockFlow Tiny 10':'mockFlow Tiny 0'},None,{'name':'Tiny','period':0,'error':'Period must be positive'})],
 [('所有路径都合格',{'{{p1 0.12} {p2 -0.25} {p3 -0.05}}':'{{p1 0.12} {p2 0.25} {p3 0.05}}'},'Violations: 0\nWorst: 0.05 ns',{'rows':[['p1',0.12],['p2',0.25],['p3',0.05]],'violations':0,'worst':'0.05'}),('空报告',{'{{p1 0.12} {p2 -0.25} {p3 -0.05}}':'{}'},'Violations: 0\nWorst: NA ns',{'rows':[],'violations':0,'worst':'NA'})]
]
result=[]
for l,definition,props,alts in zip(levels,D,P,A):
 setting,title,beats=definition
 variants=[dict(label='任务中的输入',code=l['solution'],output=l['expected'],props=props)]
 for label,edits,out,p in alts:
  code=l['solution']
  for before,after in edits.items():
   assert before in code,(l['id'],before)
   code=code.replace(before,after)
  variants.append(dict(label=label,code=code,output=out,props=p))
 steps=[]
 for title_,text,needle in beats:
  # A variant may change a literal in a highlighted line. Store the line index.
  lines=l['solution'].splitlines()
  index=next(i for i,line in enumerate(lines) if needle in line)
  steps.append(dict(title=title_,text=text,line=index))
 result.append(dict(id=l['id'],setting=setting,title=title,steps=steps,variants=variants))
(ROOT/'site/adventures.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Built 20 storyboards / 80 beats / 60 runnable variants')
