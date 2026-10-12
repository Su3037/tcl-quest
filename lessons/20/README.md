# 20 · 终极 BOSS · 时序报告侦探

[English](README.en.md) · [课程首页](../../README.md)

芯片城的时序报告送到了。找出违规路径数和最差时间余量，提交你的结案报告。

目标：毕业项目 · 统计与验证。约 20 分钟，首次通关 +200 XP。

![芯芯与伙伴的第 20 关场景](../../site/media/scenes/level-20.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

报告用列表模拟，每条记录是 {路径名 slack}。slack <0 算违规；最小的 slack 是最差余量。程序输出字典，便于别的脚本继续使用。

先处理空输入，再把最差值设为第一条记录的 slack。不要随便从 0 开始取最小值：如果所有 slack 都为正，最差余量也应该为正。

## 图解

```text
报告记录列表
   ↓
计数 slack < 0 · 取最小 slack
   ↓
字典 violations / worst
```

## 先看示例

```tcl
set rows {{p1 0.12} {p2 -0.25} {p3 -0.05}}
foreach row $rows {
    lassign $row path slack
    puts "$path -> $slack ns"
}
```

## 你的任务

实现 analyze {rows}，返回包含 violations 和 worst 的字典。空列表返回 violations=0、worst=NA。示例输出 Violations: 2 和 Worst: -0.25 ns。

预期输出：

```text
Violations: 2
Worst: -0.25 ns
```

运行 `tclsh lessons/20/starter.tcl`。检查：`python3 scripts/check.py 20 lessons/20/starter.tcl`。

<details><summary>给我一点提示</summary>

空输入先返回。非空时 worst 从第一条记录读取。

foreach 中分别判断 slack<0 和 slack<worst，最后用 dict create 返回。

</details>

## 常见坑

这是简化的教学数据格式；真实报告包含多种检查和单位，需按工具文档解析。

## 理解检查

所有 slack 都是正数时，worst 应该是什么？

1. 其中最小的正数
2. 一定是 0
3. 一定是 NA

<details><summary>查看解释</summary>

正确选项：其中最小的正数。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

升级毕业作品：从文本文件读取记录，忽略空行，检查坏数据并输出 CSV。
