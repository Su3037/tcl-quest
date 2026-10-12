# 12 · 记录角色档案

用名字取属性，比记住“第几个格子”更直观。

目标：dict · array。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 12 关场景](../../site/media/scenes/level-12.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

字典 dict 用键和值记录信息，像“hp 对应 80，name 对应 Ada”的档案。dict get 取值，dict set 修改，dict exists 检查键是否存在。

Tcl 还有数组 array：set hero(hp) 80。数组是一组变量元素，字典则是一个可以作为参数传递的值。本关练习字典，不把两者混为一谈。

## 图解

```text
字典 hero
   ↓
name → Ada
   ↓
hp → 100
```

## 先看示例

```tcl
set hero [dict create name Ada hp 80]
dict incr hero hp 5
puts [dict get $hero hp]
set bag(key) 1
puts $bag(key)
```

## 你的任务

创建 hero 字典，name=Ada、hp=80；增加 20 点 hp，输出 Ada:100。

预期输出：

```text
Ada:100
```

运行 `tclsh lessons/12/starter.tcl`。检查：`python3 scripts/check.py 12 lessons/12/starter.tcl`。

<details><summary>给我一点提示</summary>

dict incr hero hp 20 修改变量 hero 中的字典。

dict get $hero hp 读取修改后的数值。

</details>

## 常见坑

读取不存在的键会报错，可以先用 dict exists 判断。

## 理解检查

哪一句读取 hero 字典中的 hp？

1. dict get $hero hp
2. set hero(hp)
3. lindex hp hero

<details><summary>查看解释</summary>

正确选项：dict get $hero hp。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

为 hero 添加 level 键，值为 3。
