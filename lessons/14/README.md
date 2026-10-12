# 14 · 识破错误陷阱

打不开的宝箱不该让整场冒险终止。学会处理失败。

目标：catch · error · 错误信息。约 10 分钟，首次通关 +100 XP。

catch 执行一段脚本，并把结果或错误文字存入指定变量。返回 0 表示正常完成；普通错误返回 1。

用 error 主动报告不符合规则的输入。错误是程序给你的线索。catch 还有 return、break 等其他完成码，本关只处理普通错误与成功。

## 图解

```text
检查输入
   ↓
有效 → 计算
   ↓
无效 → 解释原因
```

## 先看示例

```tcl
if {[catch {open missing.txt r} message]} {
    puts "Could not open file"
}
puts "Still running"
```

## 你的任务

实现 safeDivide {a b}：b 为 0 时返回 undefined，否则做浮点除法。输出 5/2 的 2.5 和 5/0 的 undefined。

预期输出：

```text
2.5
undefined
```

运行 `tclsh lessons/14/starter.tcl`。检查：`python3 scripts/check.py 14 lessons/14/starter.tcl`。

<details><summary>给我一点提示</summary>

在除法之前用 if {$b == 0} 判断。

expr 中的 double($a) 让整数输入也能保留小数。

</details>

## 常见坑

安全除法可以先检查输入，不必等程序报错再处理。

## 理解检查

catch 返回 0 通常说明什么？

1. 脚本正常完成
2. 发生普通错误
3. 文件大小为 0

<details><summary>查看解释</summary>

正确选项：脚本正常完成。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

额外实验：catch {error "Bad key"} msg 后输出 $msg。
