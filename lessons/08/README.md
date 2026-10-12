# 08 · 循环采集机器人

机器人可以重复采集，不需要你复制十条指令。

目标：foreach · for · while。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 8 关场景](../../site/media/scenes/level-08.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

foreach 逐个拿出列表里的元素并执行脚本。foreach item $bag {...} 就像“对背包里的每件物品都做这些事”。

for 适合计数：初始化、继续条件、步进、循环体四部分。while 只给继续条件，要在循环体内更新状态，否则可能一直运行。

## 图解

```text
total = 0
   ↓
依次加 2、4、6
   ↓
total = 12
```

## 先看示例

```tcl
foreach fruit {apple pear} {puts $fruit}
for {set i 1} {$i <= 3} {incr i} {puts $i}
```

## 你的任务

遍历 2、4、6，把总和存进 total，输出 12。请用 foreach 和累加。

预期输出：

```text
12
```

运行 `tclsh lessons/08/starter.tcl`。检查：`python3 scripts/check.py 8 lessons/08/starter.tcl`。

<details><summary>给我一点提示</summary>

incr total $n 会增加当前数值。

每轮分别加 2、4、6，最后输出 total。

</details>

## 常见坑

在无限循环中，页面会在超时后停止本次运行。

## 理解检查

while 循环最容易忘记什么？

1. 更新用于判断的状态
2. 写 puts 英文大写
3. 加一个网页链接

<details><summary>查看解释</summary>

正确选项：更新用于判断的状态。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

换成 {1 2 3 4 5}，预测总和 15。
