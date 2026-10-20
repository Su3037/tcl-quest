# 公开网站与更新

游戏入口：**https://su3037.github.io/tcl-quest/**

源码仓库：**https://github.com/Su3037/tcl-quest**

## 托管与运行位置

GitHub Pages 提供 `site/` 内的静态网页、插图、视频和 Tcl WebAssembly 引擎。每位访问者的代码在自己的浏览器 Worker 中运行，文件操作使用浏览器内存中的虚拟文件系统。网站不连接作者的 Mac，不需要作者保持电脑开机，也没有使用作者计算资源的后端。

草稿、XP、徽章和语言偏好保存在访问者当前浏览器。不同设备或不同网址之间不会自动同步；可在新手指南导出、导入学习进度。本地预览 `http://127.0.0.1:8765/` 与公开网址是不同来源，迁移时使用导出、导入功能。

## 发布配置与更新

仓库设为 Public，Settings → Pages → Build and deployment 的 Source 选择 **GitHub Actions**。`.github/workflows/pages.yml` 将 `site/` 上传并部署到 Pages，仅在仓库为 public 时执行。

向 `main` 推送 `site/` 或 Pages 工作流的更新后，会自动发布。也可在 Actions → **Publish public GitHub Pages** → **Run workflow** 手动发布。部署在 GitHub 云端完成；本地 `scripts/serve.py` 仅用于开发预览。

修改课程后，先按 README 的生成命令和检查命令更新生成文件，再提交推送。可在 Actions 查看部署结果；若用于正式课程，请记录所用提交版本。

## 访问问题排查

访客只需打开 **https://su3037.github.io/tcl-quest/**，不需要下载仓库、注册 GitHub、安装 Tcl 或启动服务器。

| 看到的情况 | 如何排查 |
| --- | --- |
| 网址是 `127.0.0.1`、`localhost` 或 `file://` | 这是本机预览或下载的文件，请改用上面的公开网址。 |
| 打开了 GitHub 文件列表 | 这是源码仓库，点击 README 中的“打开网页版游戏”。 |
| “无法连接”、超时或 DNS 错误 | 请求可能没有到达 GitHub Pages。核对网址，在系统浏览器及其他网络中试一次；仅凭这种现象不能判定是应用故障。 |
| 一直显示加载提示，或“课程暂时没加载出来” | 刷新重试；在最新版 Chrome、Edge、Firefox 或 Safari 中打开。反馈时附上错误详情、网址、浏览器和网络环境。 |
| 页面能打开，但运行提示引擎加载超时 | Tcl 引擎需要从同一个网站下载约 1.9 MB 的 WASM 文件及数据文件。刷新后再运行，或更换网络；无需部署本地服务。 |

微信等应用内打开失败时，可以复制完整公开网址到系统浏览器尝试。这只是排查方法，不代表所有应用内浏览器都不支持。网络能否连接 GitHub Pages 取决于访问者所用网络，本站无法保证所有地区和网络都可达。

## 本地预览

运行 `python3 scripts/serve.py`。使用 Codespaces 时运行 `python3 scripts/serve.py --host 0.0.0.0`，并保持开发端口 Private；这不影响公开 Pages 网站。

依据：[GitHub Pages 官方说明](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)。

## English

Play at **https://su3037.github.io/tcl-quest/**. GitHub Pages serves the static files. Tcl executes in each visitor’s browser Worker with an in-memory filesystem; it does not connect to or use the author’s Mac. The author’s computer can be shut down.

Drafts, XP, badges and language preferences stay in the visitor’s browser. Export/import progress to transfer it between devices or from the local preview to the public URL.

Changes to `site/` or the Pages workflow on `main` deploy automatically, provided the repository is public. Manual deployment is also available under Actions → **Publish public GitHub Pages** → **Run workflow**. Select **GitHub Actions** as the publishing source in Settings → Pages.
