# 17 · 从报告中寻找线索

设计报告里藏着一个 slack 数字，把它取出来。

目标：regexp · 捕获组。约 10 分钟，首次通关 +100 XP。

正则表达式 regexp 是寻找文字规律的工具。([0-9]+) 表示捕获一串数字；括号圈住的部分可以存入变量。

slack 可以理解为时间余量：负数通常意味着这个检查没有满足时间要求。本关只识别教学格式 slack: 数字，不代替真实工具的报告解析。

## 图解

```text
报告 slack: -0.25
   ↓
regexp 识别模式
   ↓
value = -0.25
```

## 先看示例

```tcl
set line "slack: -0.25"
if {[regexp {slack: (-?[0-9]+\.[0-9]+)} $line whole value]} {
    puts $value
}
```

## 你的任务

实现 slackValue {line}，识别格式 slack: 后的整数或小数（可带负号），返回数值文字；不匹配返回 NA。输出 -0.25。

预期输出：

```text
-0.25
```

运行 `tclsh lessons/17/starter.tcl`。检查：`python3 scripts/check.py 17 lessons/17/starter.tcl`。

<details><summary>给我一点提示</summary>

-? 表示可选负号，(\.[0-9]+)? 表示可选小数部分。

模式两端用 ^ 和 $，整行匹配；数值保存在 value。

</details>

## 常见坑

正则里的点默认表示任意字符；匹配小数点要用反斜杠转义。

## 理解检查

slack 为负数，在本教学场景中意味着？

1. 时间要求未满足
2. 文件不存在
3. 芯片已经损坏

<details><summary>查看解释</summary>

正确选项：时间要求未满足。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

扩展规则让 slack: 后也可以有多个空格，提示使用 [[:space:]]+。
