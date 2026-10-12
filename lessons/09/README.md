# 09 · 文字变形术

路牌文字太乱了。清理空格、统一大小写，再拼成新路牌。

目标：string · split · join。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 9 关场景](../../site/media/scenes/level-09.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

string trim 去掉两端空白，string toupper 转大写，string length 数字符。可以用嵌套方括号把步骤串起来。

split 把字符串按分隔字符拆成列表；join 把列表拼成字符串。split 的第二个参数是一组分隔字符，不是一个完整分隔词。

## 图解

```text
"  chip  "
   ↓
trim → "chip"
   ↓
toupper → "CHIP"
```

## 先看示例

```tcl
set raw "  chip island  "
puts [string toupper [string trim $raw]]
puts [join {A B C} "-"]
```

## 你的任务

写过程 clean {text}：去掉两端空白并转大写。输出 clean "  chip  " 的结果 CHIP。

预期输出：

```text
CHIP
```

运行 `tclsh lessons/09/starter.tcl`。检查：`python3 scripts/check.py 9 lessons/09/starter.tcl`。

<details><summary>给我一点提示</summary>

先 string trim $text。

把 trim 的结果传给 string toupper。

</details>

## 常见坑

llength 计算列表元素数，string length 计算字符串长度。

## 理解检查

哪条命令去掉字符串两端的空格？

1. string trim
2. string length
3. llength

<details><summary>查看解释</summary>

正确选项：string trim。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

把 CHIP 用 string tolower 改回小写，看看命令名字的规律。
