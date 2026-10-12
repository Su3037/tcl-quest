# 07 · 收集物品清单

把钥匙、苹果和地图装进背包，保持每件物品的边界。

目标：list · lindex · llength · lappend。约 10 分钟，首次通关 +100 XP。

列表像一排格子，每个格子放一件物品。list 可以把多个值组成列表；lappend 往末尾加物品。

lindex bag 0 取第一个物品，索引从 0 开始；llength 计算物品数量。带空格的物品用 list 或花括号保持为一个元素。

## 图解

```text
0: key
   ↓
1: red apple
   ↓
2: map
```

## 先看示例

```tcl
set bag [list key "red apple"]
lappend bag map
puts [llength $bag]
puts [lindex $bag 1]
```

## 你的任务

创建 bag，依次装入 key、red apple、map。输出数量 3，再输出第二件物品 red apple。

预期输出：

```text
3
red apple
```

运行 `tclsh lessons/07/starter.tcl`。检查：`python3 scripts/check.py 7 lessons/07/starter.tcl`。

<details><summary>给我一点提示</summary>

list key "red apple" map 会生成三个元素。

第二个元素的索引是 1。

</details>

## 常见坑

set bag "key red apple map" 会把 red 和 apple 作为两个列表元素。

## 理解检查

列表的第一个索引是？

1. 0
2. 1
3. -1

<details><summary>查看解释</summary>

正确选项：0。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

用 lappend 再放入 compass，预测新长度。
