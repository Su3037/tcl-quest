# 10 · BOSS · 给精灵分配补给

三只精灵饥饿值各不相同，机器人要分出谁需要补给。

目标：组合挑战 · 列表与条件。约 20 分钟，首次通关 +200 XP。

![芯芯与伙伴的第 10 关场景](../../site/media/scenes/level-10.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

用列表保存多条记录，再用 foreach 一条条处理。每条记录仍然可以是列表，lassign 能按位置把一条记录拆进多个变量。

把变化的输入放进过程参数，便于测试。此处 supply 接收记录列表；同一套规则应该适用于新的角色，而不仅是眼前样例。

## 图解

```text
读取 {名字 饥饿值}
   ↓
饥饿 ≥ 5？
   ↓
把名字加入 selected
```

## 先看示例

```tcl
foreach row {{Ada 4} {Bo 8}} {
    lassign $row name hunger
    puts "$name: $hunger"
}
```

## 你的任务

实现 supply {rows}：每行是 {名字 饥饿值}。饥饿值 >=5 的名字加入列表并返回。输出示例中需要补给的名字 Ada Cy。

预期输出：

```text
Ada Cy
```

运行 `tclsh lessons/10/starter.tcl`。检查：`python3 scripts/check.py 10 lessons/10/starter.tcl`。

<details><summary>给我一点提示</summary>

使用 if {$hunger >= 5}。

条件成立时 lappend selected $name。

</details>

## 常见坑

返回列表时不要提前 join，否则有空格的名字会丢失元素边界。

## 理解检查

为什么测试新的角色名字？

1. 确认程序真的按规则处理输入
2. 为了增加代码长度
3. Tcl 只能接受三个名字

<details><summary>查看解释</summary>

正确选项：确认程序真的按规则处理输入。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

把条件改成 >=8，观察哪些精灵不再需要补给。
