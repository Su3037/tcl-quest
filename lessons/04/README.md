# 04 · 炼制能量药水

药水配方需要计算总能量。让电脑帮你做算术。

目标：expr · incr。约 10 分钟，首次通关 +100 XP。

expr 是计算器。expr {3 + 4} 返回 7；把它放进方括号，就能把结果存进变量。常用符号有 +、-、*、/ 和 %。

推荐用花括号包表达式，如 expr {$a + $b}，由 expr 负责变量替换。incr coins 3 会给 coins 加 3。整数除法 5/2 得到 2，5/2.0 才得到 2.5。

## 图解

```text
3 瓶 × 7 点
   ↓
21 点 + 4 点奖励
   ↓
energy = 25
```

## 先看示例

```tcl
set base 6
set power [expr {$base * 3}]
incr power 2
puts $power
puts [expr {5 / 2.0}]
```

## 你的任务

3 瓶药水，每瓶 7 点能量，另加 4 点奖励。把总数存入 energy，并输出 25。

预期输出：

```text
25
```

运行 `tclsh lessons/04/starter.tcl`。检查：`python3 scripts/check.py 4 lessons/04/starter.tcl`。

<details><summary>给我一点提示</summary>

先计算 $bottles * $each。

先 set energy [expr {...}]，再 incr energy 4。

</details>

## 常见坑

puts 3+4 只会输出文字 3+4；puts 不做算术。

## 理解检查

expr {5 / 2} 的结果是？

1. 2
2. 2.5
3. 报错

<details><summary>查看解释</summary>

正确选项：2。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

把瓶数改成 10，预测结果后再运行。
