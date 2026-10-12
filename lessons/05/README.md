# 05 · BOSS · 修好出发信标

[English](README.en.md) · [课程首页](../../README.md)

信标的名字、能量和原始模板都坏了。把前三种技能组合起来。

目标：组合挑战 · 变量与替换。约 20 分钟，首次通关 +200 XP。

![芯芯与伙伴的第 5 关场景](../../site/media/scenes/level-05.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

这关把输出、变量、计算和引用组合成一个小程序。先准备数据，再计算，最后展示结果，是很多脚本的共同顺序。

不要急着一次写完。先让第一行正确，再增加下一行。编程中的试错像调试积木：每次只改一个地方，更容易找到原因。

## 图解

```text
准备数据
   ↓
计算能量
   ↓
点亮信标
```

## 先看示例

```tcl
set name Beacon
set power [expr {4 * 5}]
puts "$name: $power"
```

## 你的任务

设置 hero=Ada、cells=4、each=5，energy 为两者乘积。输出三行：Ada ready、Energy: 20、$energy（最后一行保留字面变量名）。

预期输出：

```text
Ada ready
Energy: 20
$energy
```

运行 `tclsh lessons/05/starter.tcl`。检查：`python3 scripts/check.py 5 lessons/05/starter.tcl`。

<details><summary>给我一点提示</summary>

第一步是 set energy [expr {$cells * $each}]。

前两行用双引号，最后一行用花括号。

</details>

## 常见坑

把所有内容都包进花括号会阻止你想要的替换。

## 理解检查

程序出错时，哪种方法更容易找到原因？

1. 每次改一处并运行
2. 同时改所有行
3. 把所有括号删掉

<details><summary>查看解释</summary>

正确选项：每次改一处并运行。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

为信标增加一个 doubleEnergy 变量，显示双倍能量。
