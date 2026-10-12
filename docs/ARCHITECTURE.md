# 实现说明

## 数据与页面

`build_curriculum.py` 是课程内容的编辑入口。它生成 `site/curriculum.json` 和 `lessons/01` 到 `lessons/20` 的讲义、起始代码、示例与答案。修改课程后需运行生成器并检查输出。

`site/` 为可直接静态部署的目录。`app.js` 使用 hash 路由，资源使用相对路径，适用于 GitHub 项目 Pages 的 `/tcl-quest/` 子路径，不需要打包工具或外部 CDN。

地图插画是内联 SVG；图解用 HTML 和可访问文字表达。CSS 在窄屏使用单列阅读和双列地图。视频为本地 MP4，附 VTT 和纯文本稿。

## Tcl 执行

每次执行创建一个 `runner.js` Worker。通过 RequireJS 加载本地 Wacl，引擎提供真正的 Tcl 8.6 系列解释器。直接调用导出的 `Tcl_Eval` 和 `Tcl_GetStringResult`，避免 Wacl 旧版 JS 包装器把用户脚本再次拼入花括号。

stdout/stderr 捕获后规范化末尾 CR；输出测试忽略末尾换行。过程题额外执行行为检查，包括新参数、边界、空输入和小数。检查运行在同一临时解释器中，完成后 Worker 终止。

加载超时 25 秒，执行超时 5 秒，均由主页面计时后 terminate；页面不会被 Tcl 无限循环阻塞。停止按钮可以提前终止。虚拟文件和解释器状态不跨次运行保留。

本地自动检查使用真实 tclsh 在临时工作目录运行；`tests/wasm.mjs` 在 Node VM 中提供仅映射本地文件的 importScripts/XHR 适配器，直接测试相同的二进制和 Worker 代码。它不借助浏览器，也不联网。

## 进度和局限

localStorage 键为 `tcl-quest-progress-v1`，保存完成关卡、代码草稿和答对的理解题；经验值从完成关卡推导，不重复奖励。导入校验版本、关卡范围、字段类型和文件大小。

没有账号系统、服务端数据库、远程排名或遥测。代码不会被本项目的服务端接收；Wacl 本身带有额外扩展，不将浏览器 Worker 描述为能防御所有恶意脚本的安全边界。教学页面应按自学工具使用，不承载敏感数据。

## 已知范围

- 网页需要现代浏览器的 ES modules、Worker、WebAssembly、dialog 支持。
- 文件为虚拟内存文件；不提供桌面 Tk 窗口、操作系统 exec 或商业 EDA。
- 单次运行不可交互输入；请把输入写为变量或过程参数。
- 引擎为上游 2017 年预编译包；本项目固定资源和哈希、保留授权，更新时必须重新验证所有关卡。
- 所有关卡开放，答案可见；检查用于学习反馈，不用于考试防作弊。


## 执行事件与语言版本

Worker 现在使用 `trace.tcl` 的 Tcl execution observer 推送真实参数、返回值、变量和 stdout 事件。`runtime-story.js` 将事件映射为关卡状态，`live-runtime.js` 在编辑器下方回放。评分检查前停用观察。详见 [RUNTIME.md](RUNTIME.md)。

`curriculum.en.json` 和 `adventures.en.json` 来自人工编写的英文源文件。`i18n.js` 与 `locale-core.js` 翻译界面和可访问性标签，保留原生代码/输出。中英文各自提供四段视频、字幕、文字稿和每关静态插图。进度不按语言拆分。
