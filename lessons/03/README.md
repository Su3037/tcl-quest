# 03 · 穿过括号迷宫

[English](README.en.md) · [课程首页](../../README.md)

迷宫里有三种门：有的替换内容，有的保留原样，有的先执行里面的指令。

目标：" " · { } · [ ]。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 3 关场景](../../site/media/scenes/level-03.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

双引号允许 $变量 和 [命令] 替换。花括号通常保留内容原样，适合保存脚本或表达式。方括号先执行里面的命令，再用结果替换整对方括号。

例如 set n 3 后，puts "$n" 输出 3，而 puts {$n} 输出字面文字 $n。花括号并非永远不执行：if、expr 等命令拿到它们的内容后，会按各自规则处理。

## 图解

```text
"$hero" → Ada
   ↓
{$hero} → $hero
   ↓
[string toupper hi] → HI
```

## 先看示例

```tcl
set n 3
puts "value=$n"
puts {value=$n}
puts [string toupper hi]
```

## 你的任务

设置 hero 为 Ada。第一行输出 Hello Ada，第二行原样输出 Hello $hero，第三行输出 ADA。

预期输出：

```text
Hello Ada
Hello $hero
ADA
```

运行 `tclsh lessons/03/starter.tcl`。检查：`python3 scripts/check.py 3 lessons/03/starter.tcl`。

<details><summary>给我一点提示</summary>

花括号会保留 $hero 的原样文字。

用 [string toupper $hero] 先取得大写结果。

</details>

## 常见坑

Tcl 的括号有语义，不是可以随意互换的装饰。

## 理解检查

puts {$hero} 会输出什么？

1. $hero 这段文字
2. hero 的值
3. 什么也没有

<details><summary>查看解释</summary>

正确选项：$hero 这段文字。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

写出一句同时包含普通文字、变量和命令替换的欢迎语。
