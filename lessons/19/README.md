# 19 · 搭建教学设计流程

把配置和操作分开，让一套脚本能用于不同设计。

目标：source · 模块 · 流程。约 10 分钟，首次通关 +100 XP。

source 读取另一个 Tcl 文件，并在当前解释器中执行。把可变参数放在配置文件，再 source 它，是常见的脚本组织方式。

真实 EDA 的读入、约束、综合、布局布线与报告命令因工具而异。本关 mockFlow 只生成教学流程描述，不调用商业工具，不生成 GDS。

## 图解

```text
配置文件
   ↓
source 载入
   ↓
读入 → 时钟 → 报告
```

## 先看示例

```tcl
set f [open config.tcl w]
puts $f {set design Tiny}
close $f
source config.tcl
puts "Design: $design"
```

## 你的任务

实现 mockFlow {design period}：周期 <=0 时用 error 报错，否则返回列表 {read:设计名 clock:周期 report:timing}。输出 Tiny、周期 10 的流程。

预期输出：

```text
read:Tiny clock:10 report:timing
```

运行 `tclsh lessons/19/starter.tcl`。检查：`python3 scripts/check.py 19 lessons/19/starter.tcl`。

<details><summary>给我一点提示</summary>

if {$period <= 0} {error "Period must be positive"}。

用 list 而不是拼接字符串，保留包含空格的设计名。

</details>

## 常见坑

这里的 clock:10 只是文字，不是创建真实时钟的 EDA 命令。

## 理解检查

source config.tcl 的作用是什么？

1. 执行这个 Tcl 文件
2. 把它变成视频
3. 自动启动商业 EDA

<details><summary>查看解释</summary>

正确选项：执行这个 Tcl 文件。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

把设计名换成 My Chip，用 llength 验证仍有三个步骤。
