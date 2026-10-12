# 11 · 制作可重复的技能卡

把招呼语装成技能卡，换个名字也能使用。

目标：proc · 参数 · return。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 11 关场景](../../site/media/scenes/level-11.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

proc 定义过程，像一张带输入格子的配方。proc greet {name} {...} 定义 greet，name 是输入参数。调用 greet Ada 时，name 得到 Ada。

过程内部的普通变量通常是局部变量。return 把计算结果交给调用者，puts 把内容显示出来；两者作用不同。参数还可以有默认值。

## 图解

```text
输入 n = 7
   ↓
过程 double
   ↓
返回 14
```

## 先看示例

```tcl
proc greet {name {place Island}} {
    return "Hello $name at $place"
}
puts [greet Ada]
puts [greet Bo Forest]
```

## 你的任务

实现 double {n} 返回输入的两倍。输出 double 7 的结果 14。

预期输出：

```text
14
```

运行 `tclsh lessons/11/starter.tcl`。检查：`python3 scripts/check.py 11 lessons/11/starter.tcl`。

<details><summary>给我一点提示</summary>

计算使用 expr。

return [expr {$n * 2}] 将结果返回。

</details>

## 常见坑

只在过程里 puts 结果，通常不能让外面的 expr 使用那个结果。

## 理解检查

调用者要拿到计算结果，应使用？

1. return
2. puts
3. #

<details><summary>查看解释</summary>

正确选项：return。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

增加一个 times {n factor} 过程，让倍率也成为参数。
