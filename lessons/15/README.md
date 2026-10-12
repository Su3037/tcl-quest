# 15 · BOSS · 修复技能工坊

工坊需要一张计算平均值的技能卡，空背包也不能把它弄坏。

目标：组合挑战 · 通用过程。约 20 分钟，首次通关 +200 XP。

先用 foreach 求和，再除以元素数量。空列表的长度为 0，要先处理，避免除以零。

工程脚本经常需要统计多个数。使用 double 保留平均值的小数部分；过程接收一个列表参数，调用时用花括号把多个数打包。

## 图解

```text
列表 → 求和
   ↓
空列表先返回 0
   ↓
总和 ÷ 数量
```

## 先看示例

```tcl
puts [llength {3 4 8}]
puts [expr {double(15) / 3}]
```

## 你的任务

实现 average {numbers}。空列表返回 0，其他列表返回算术平均值。输出 {2 4 9} 的平均值 5.0。

预期输出：

```text
5.0
```

运行 `tclsh lessons/15/starter.tcl`。检查：`python3 scripts/check.py 15 lessons/15/starter.tcl`。

<details><summary>给我一点提示</summary>

先用 llength 判断空列表。

累计后返回 expr {double($total) / [llength $numbers]}。

</details>

## 常见坑

incr 只适合整数；本关求和用 expr 也能支持小数。

## 理解检查

为什么平均值计算中使用 double？

1. 避免整数除法截断小数
2. 让循环跑两遍
3. 给变量改名

<details><summary>查看解释</summary>

正确选项：避免整数除法截断小数。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

输入 {1.5 2.5}，验证结果是 2.0。
