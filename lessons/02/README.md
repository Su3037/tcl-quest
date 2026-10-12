# 02 · 给背包贴标签

出发前，把金币放进一个有名字的背包格子。

目标：set · $变量。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 2 关场景](../../site/media/scenes/level-02.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

变量像贴了标签的格子。set coins 8 把数字 8 放到 coins 格子里。set 既可以存入，也可以在只给名字时取出。

$coins 的意思是“拿出 coins 里面的东西”。设置时写名字 coins，使用值时常写 $coins。

## 图解

```text
标签 coins
   ↓
格子里是 12
   ↓
$coins → 12
```

## 先看示例

```tcl
set coins 8
puts $coins
set coins 12
puts "Coins: $coins"
```

## 你的任务

建立变量 hero，值为 Ada；建立变量 coins，值为 12。输出 Ada has 12 coins。

预期输出：

```text
Ada has 12 coins
```

运行 `tclsh lessons/02/starter.tcl`。检查：`python3 scripts/check.py 2 lessons/02/starter.tcl`。

<details><summary>给我一点提示</summary>

修改 set coins 后面的数字。

输出时，$hero 和 $coins 会被替换成变量的值。

</details>

## 常见坑

set $coins 12 会把 coins 的值当作另一个变量的名字。

## 理解检查

哪一句把 12 放入 coins？

1. set coins 12
2. set $coins 12
3. coins = 12

<details><summary>查看解释</summary>

正确选项：set coins 12。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

试着覆盖 coins 的值，观察变量不是永久不变的。
