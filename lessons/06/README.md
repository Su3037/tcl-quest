# 06 · 守门人的选择

城门要求至少 10 枚金币。用条件告诉守门人该怎么做。

目标：if · 比较。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 6 关场景](../../site/media/scenes/level-06.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

if 就是“如果”。条件成立，执行第一段脚本；不成立，执行 else 后的脚本。比较数字可以用 >=、<、==。

比较文字推荐用 eq 和 ne。例如 if {$name eq "Ada"}。Tcl 的 if 条件和脚本通常都用花括号包住。

## 图解

```text
金币数 ≥ 10？
   ↓
是 → Enter
   ↓
否 → Wait
```

## 先看示例

```tcl
set coins 8
if {$coins >= 10} {
    puts "Enter"
} else {
    puts "Collect more"
}
```

## 你的任务

写过程 gate {coins}，金币至少 10 时返回 Enter，否则返回 Wait。输出 gate 12 的结果。

预期输出：

```text
Enter
```

运行 `tclsh lessons/06/starter.tcl`。检查：`python3 scripts/check.py 6 lessons/06/starter.tcl`。

<details><summary>给我一点提示</summary>

proc 是一张可以重复使用的指令卡，本关先照着结构填写，第 11 关再深入。

if {$coins >= 10} {return Enter} else {return Wait}

</details>

## 常见坑

别漏掉边界值 10。数字相等比较用 ==，赋值用 set。

## 理解检查

至少 10 枚金币对应哪个条件？

1. $coins >= 10
2. $coins > 10
3. $coins < 10

<details><summary>查看解释</summary>

正确选项：$coins >= 10。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

把门槛改成 20，并测试 19、20、21。
