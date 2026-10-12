# 原创演示视频

`site/media/` 内含四段 1280×720、60 秒、H.264 MP4。每段由 6 个 10 秒代码演示步骤组成，输出由真实 tclsh 生成；中文字幕直接画在画面中，另有 VTT 字幕和逐步文字稿。视频没有配音，也不是实际桌面录屏。

重新生成：

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-media.txt
python3 scripts/render_videos.py --font /你的中文字体路径.ttf
```

还需安装 ffmpeg 和 Tcl。macOS 脚本默认用系统 STHeiti 字体；Linux 可以安装 Noto Sans CJK 并传入字体文件路径。代码区使用 Menlo，Linux 回退到 DejaVu Sans Mono。字体只用于本地渲染，不作为字体文件随仓库分发。

要调整讲解，修改 `render_videos.py` 中的场景文本；第 3、4 段会使用课程的数据或算法。重生成后用 `ffprobe` 检查时长、分辨率，并逐段播放检查字幕和代码可读性。


## 英文版本

运行 `python3 scripts/render_videos.py --lang en` 生成 `demo-1-en` 到 `demo-4-en` 的 MP4、封面、VTT 和文字稿。英文画面说明来自 `site/locales/media.en.json`，实际代码和输出沿用同一套 Tcl 演示；画面标题、结果区和字幕均为英文。英文界面自动选择这些成品，中文成品继续保留。
