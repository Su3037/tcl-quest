# 私密开发与之后公开

当前阶段只把材料保存到私密 GitHub 仓库，不发布公共 Pages。注意：**私密仓库与私密网站不是同一件事**，不能因为仓库私密就假设 Pages 网站也私密。是否支持私密仓库 Pages 取决于 GitHub 套餐。

## 现在怎样预览

本地运行 `python3 scripts/serve.py`；或使用私密仓库 Codespaces，运行 `python3 scripts/serve.py --host 0.0.0.0`，保持 8765 端口 Private。后者需要 GitHub 账户，并可能使用账户额度。

## 你准备好公开之后

1. 在 GitHub 仓库 Settings → General → Danger Zone → Change repository visibility 中由你手动改为 Public。
2. 在 Settings → Pages → Build and deployment 选择 **GitHub Actions**。
3. 在 Actions 中手动运行 **Publish public GitHub Pages**。
4. 等待部署成功，网站预期地址为 `https://Su3037.github.io/tcl-quest/`。

Pages 工作流仅手动触发，并检查仓库 visibility 为 public；私密阶段会跳过部署。这里没有自动修改仓库可见性的脚本。

公开前读一遍 README、抽查挑战和视频，并确认仓库只含课程材料。若用于正式课程，请记录使用的提交版本。之后更新网页，可再次手动运行 Pages 工作流。

政策依据：[GitHub Pages 官方说明](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)。
