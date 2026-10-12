# 13 · 保存冒险日志

离开页面前，把故事写进文件，再读回来。

目标：open · puts · gets · close。约 10 分钟，首次通关 +100 XP。

open 返回文件通道，像一根连接文件的管道。模式 w 会新建或覆盖文件；r 读取；a 追加。puts $f 把文字写进通道。

gets $f 读取一行，close $f 关闭通道。在这里，浏览器使用内存中的虚拟文件；它不会自动写进你电脑的磁盘。每次运行都会获得新环境。

## 图解

```text
open quest.txt w
   ↓
puts → 文件 → close
   ↓
open r → gets → close
```

## 先看示例

```tcl
set f [open diary.txt w]
puts $f "Day 1: Ready"
close $f
set f [open diary.txt r]
puts [gets $f]
close $f
```

## 你的任务

向 quest.txt 写入第一行 Level 13、第二行 Saved。关闭后重新打开，读回两行并输出。

预期输出：

```text
Level 13
Saved
```

运行 `tclsh lessons/13/starter.tcl`。检查：`python3 scripts/check.py 13 lessons/13/starter.tcl`。

<details><summary>给我一点提示</summary>

写入用 puts $f "Level 13"。

关闭写通道后，再 set f [open quest.txt r]。

</details>

## 常见坑

真实电脑上用 w 会覆盖文件，练习时请使用专门的练习文件名。

## 理解检查

模式 w 对已有文件会做什么？

1. 覆盖原内容
2. 只读取
3. 自动备份所有版本

<details><summary>查看解释</summary>

正确选项：覆盖原内容。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

用 a 追加第三行，在本地 Tcl 中再次运行读取脚本。
