# 执行驱动剧情 / Execution-driven stories

## 中文

右侧“电脑”上方是编辑器和 Tcl 输出，下方是实时剧情窗。点击“运行代码”后，Worker 在真实 Tcl 8.6.6 解释器中执行脚本，通过 Tcl 的 execution trace 观察已经发生的操作。回调发送结构化的参数、返回值和相关变量；stdout 也发送真实输出事件。主线程按可阅读的速度回放这些事件。

例如第 8 关输入：

```tcl
set total 0
foreach n {3 5 9} {incr total $n}
puts $total
```

实际 `incr` 的返回值依次为 3、8、17，剧情窗就按这些值采集和累加。注释、没有调用的过程体、`if {0}` 的循环体都不能凭源码文字触发动作。错误发生前已经执行的步骤仍可回放。程序本身已经执行完毕后，动画可能还在按节奏播放；“下一步”控制的是回放，不是暂停 Tcl 解释器。

20 关分别把对应的操作映射为背包、药水、门、列表格、采集、文字修理、补给、技能卡、字典、文件、保护分支、平均值机、命名空间、正则、对象、流程和报告。输入、返回值和输出来自当前程序，不使用参考解法的固定数值代替。没有识别到本关语义的操作会保留在运行记录和输出中；这不是通用物理游戏引擎或逐行调试器。

原来的四幕教学分镜收进了工作区上方的可展开面板。它讲解所选例子，与实时剧情窗独立。手动播放分镜、运行代码、播放轨迹都不会直接获得 XP；只有原任务的输出与行为检查全部通过后才计分。评分检查运行前关闭观察，不让隐藏检查中的额外调用进入剧情。

支持暂停、继续、单步回放、从头回放与快进。改动草稿会暂停旧轨迹，并提示重新运行，避免把旧画面误认为新代码的结果。离开关卡会清除定时器和观察流；语言切换共享草稿、XP、徽章，保留当前回放位置。程序真正运行的短暂期间禁用语言切换，结束后即可切换。

实现文件：

- `site/trace.tcl`：Tcl 观察回调，使用每次运行独立的命名空间。`scripts/build_trace.py` 生成 Worker 使用的本地 `trace-source.js`。
- `site/runner.js`：安装观察器、桥接事件、执行用户代码、关闭观察、运行评分检查。没有改写或拆分用户程序的语法。
- `site/runtime-story.js`：纯数据模型，只消费执行事件，不通过匹配未执行的源码猜测动作。
- `site/live-runtime.js`：队列、播放控制、运行记录、剧情窗及语言切换时的回放快照。

为保持浏览器流畅，每次最多观察 256 个核心执行事件，变量文字最多 2048 字符，列表最多记录 32 项；画布进一步只画有限数量的项目。达到事件上限会显示提示，Tcl 继续运行并返回完整结果，仍受原来的五秒执行超时约束。这些观察器针对课程涉及的常见命令，不承诺完整支持用户自行安装的 execution/variable trace、解释器内部自省或重命名观察器内部命令。虚拟文件系统仍在每次运行时重建。

英文入口覆盖地图、20 关文字与提示、概念题、NPC、80 幕分镜、图内标签、实时剧情、指南、反馈、记录导出以及四段英文视频和文字稿。语言偏好单独保存，用户代码和 Tcl 原生输出不做翻译。

## English

The computer panel places the Tcl editor and output above **Chip’s Live Story Window**. Running a script installs Tcl execution observers in a fresh Worker. Actual arguments, results, relevant variable values and stdout events feed the story model. The UI replays those events at a readable pace; its pause and next-step buttons control the replay, not the interpreter.

Changing the collection list to `{3 5 9}` therefore produces the real intermediate totals **3 → 8 → 17**. Comments and unexecuted branches cannot trigger those operations. A failed run retains events completed before the failure. The original four-beat teaching guide remains available separately.

Each lesson maps its observed operations to the corresponding illustration. This is a teaching visualization, not a universal animation engine or source-line debugger. Unrecognized operations still have their actual execution record and output. The application does not substitute fixed reference-solution values for your program’s values.

Only **Check mission** can award XP after the original output and behavior assertions pass. Observation is disabled before grading assertions execute, so their extra calls cannot advance the story. Replays and manual teaching demos never award XP by themselves.

For responsiveness, each run records at most 256 core execution events, 2048 characters per observed string and 32 elements per list; the small canvas draws only a subset of larger collections. A visible notice reports the event limit. Tcl still returns its full result and retains the five-second execution timeout. These observers target normal course commands; they are not a guarantee of compatibility with additional user-installed execution/variable traces or manipulation of observer internals.

Language switching shares drafts and progress and preserves the replay cursor. User code and native Tcl output remain verbatim. English material includes all 20 lessons, NPC dialogue, 80 teaching beats, guides, feedback, illustrations, learning records and four fully English demonstration videos with transcripts.

Reference: [Tcl 8.6 execution-trace documentation](https://www.tcl-lang.org/man/tcl8.6/TclCmd/trace.htm).
