# 16 · 进入芯片城

生活中的自动化学会了。下一步，把技能带到芯片设计现场。

目标：namespace · EDA 命令。约 10 分钟，首次通关 +100 XP。

![芯芯与伙伴的第 16 关场景](../../site/media/scenes/level-16.svg)

网页中可播放四幕剧情、切换输入，与 NPC 一起观察代码。打开方式见[仓库首页](../../README.md#现在就打开互动页面)。

VLSI 指超大规模集成电路；EDA 是帮助设计芯片的软件。Tcl 常被用来控制这些工具，但工具增加的命令并不是 Tcl 自带命令。

namespace 像给技能卡分文件夹，减少同名冲突。下面的 lab::area 是我们自建的教学命令，只算矩形面积，不执行真正的芯片设计。

## 图解

```text
Tcl 核心语法
   ↓
工具扩展命令
   ↓
EDA 设计流程
```

## 先看示例

```tcl
namespace eval lab {
    proc area {w h} {return [expr {$w * $h}]}
}
puts [lab::area 3 4]
```

## 你的任务

在 namespace lab 内实现 area {w h}，返回宽乘高。输出 lab::area 6 7 的结果 42。

预期输出：

```text
42
```

运行 `tclsh lessons/16/starter.tcl`。检查：`python3 scripts/check.py 16 lessons/16/starter.tcl`。

<details><summary>给我一点提示</summary>

命名空间里的过程仍然用 proc 定义。

调用时用 lab::area，过程里返回 expr {$w * $h}。

</details>

## 常见坑

普通 tclsh 中直接运行 create_clock 通常会报 unknown command。

## 理解检查

create_clock 是 Tcl 核心自带命令吗？

1. 不是，通常由 EDA 工具提供
2. 是，所有 tclsh 都能运行
3. 它是浏览器命令

<details><summary>查看解释</summary>

正确选项：不是，通常由 EDA 工具提供。回到上面的概念，再用示例验证一次。

</details>

## 再试一步

在本地执行 info commands lab::*，看看命名空间中的命令。
