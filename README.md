# DeepSeek 去除 AI 痕迹 Agent

## 简介
本项目是一个开源 **Agent**，基于 DeepSeek LLM，旨在把 AI 生成的文本“人化”，去除常见的 AI 写作痕迹。核心做法包括：
- 删除常用 AI 连接词
- 随机制造语病、错句、拼写错误
- 随机拆分/合并句子，生成段落

## 项目结构
```
deepseek-anti-ai-agent/
├─ main.py          # CLI 入口
├─ prompts.py       # Prompt 构造
├─ postprocess.py   # 本地后处理规则
├─ requirements.txt # Python 依赖
├─ ui.html          # 前端 UI（双栏 Markdown‑Nice）
├─ style.css        # UI 样式（暗色玻璃拟态）
├─ script.js        # 前端逻辑（DeepSeek 调用 + 后处理）
├─ deepseek_ui.bat  # 一键打开 UI
├─ build.bat        # 打包脚本，生成 release/*.zip
├─ .gitignore       # Git 忽略
└─ README.md        # 本说明文件
```

## 安装（仅 Python 依赖）
```bash
pip install -r requirements.txt
```
> 前端 UI 直接在浏览器运行，无需额外依赖。

## 本地运行 UI（推荐）
1. 双击 `deepseek_ui.bat`（或在 CMD 中运行 `deepseek_ui.bat`），浏览器自动打开 `ui.html`。
2. 在左侧输入 DeepSeek **API Key** 与待处理的 **Markdown 文本**。
3. 点击 **一键处理**，右侧实时显示已去除 AI 痕迹、自动分段的文本，点击 **复制** 按钮复制结果。

## 打包发布
```bash
# 生成 zip 包，输出至 release/ 目录
build.bat
```
生成的 `release/deepseek-anti-ai-agent.zip` 包含所有前端资源，可直接在其他机器上使用。

## 推送更新到 GitHub
```bash
git add README.md build.bat
git commit -m "Update README with detailed deployment and usage"
git push
```
若未添加远程仓库，请先执行：
```bash
git remote add origin https://github.com/yaohaoliang141-max/deepseek-anti-ai-agent.git
```

## 示例
```text
原文：
今天的天气很好，我决定去公园散步。因为我喜欢自然，所以我带上了相机。

处理后：
今天的天氣很好，我決定去公園散步。因為我喜歡自然, 所以我帶上了相機.
```

## License
MIT

## 简介
本项目是一个开源 **Agent**，基于 DeepSeek LLM，旨在把 AI 生成的文本“人化”，去除常见的 AI 写作痕迹。主要手段包括：
- 人为制造语病、错句、段落拆分
- 删除冗余修辞、常用连接词
- 随机拼写错误、标点错位

## 项目结构
```
deepseek-anti-ai-agent/
├─ main.py          # CLI 入口
├─ prompts.py       # 生成 Prompt 的模块
├─ postprocess.py   # 基于规则的后处理
├─ requirements.txt # Python 依赖列表
├─ ui.html          # 前端 UI（双栏 Markdown‑Nice）
├─ style.css        # UI 样式（暗色玻璃拟态）
├─ script.js        # 前端逻辑（DeepSeek 调用 + 本地后处理）
├─ deepseek_ui.bat  # 一键打开 UI 的批处理脚本
├─ build.bat        # 打包脚本，生成 release/*.zip
├─ .gitignore       # Git 忽略规则
└─ README.md        # 本说明文件
```

## 安装（仅 Python 依赖）
```bash
pip install -r requirements.txt
```
> 前端 UI 直接在浏览器运行，无需额外依赖。

## 本地运行 UI（推荐）
1. 双击 `deepseek_ui.bat`（或在 CMD 中运行 `deepseek_ui.bat`），浏览器会自动打开 `ui.html`。
2. 在页面左侧填写 **DeepSeek API Key** 与待处理的 **Markdown 文本**，点击 **一键处理**。
3. 右侧实时显示已去除 AI 痕迹、自动分段的文本，点击 **复制** 按钮即可复制结果。

## 打包发布
> 打包后得到的 `deepseek-anti-ai-agent.zip` 可直接在其他机器上使用，无需额外配置。
```bash
# 生成 zip 包（会放在 release/ 目录）
build.bat
```
生成的文件 `release/deepseek-anti-ai-agent.zip` 包含所有前端必要资源。

## 推送更新到 GitHub（如已关联远程）
```bash
# 添加、提交、推送最新修改
git add README.md build.bat
git commit -m "Update README with detailed deployment and usage steps"
git push
```
> 若尚未关联远程，请先执行 `git remote add origin https://github.com/yaohaoliang141-max/deepseek-anti-ai-agent.git`。

## 示例
```text
原文：
今天的天气很好，我决定去公园散步。因为我喜欢自然，所以我带上了相机。

处理后：
今天的天氣很好，我決定去公園散步。因為我喜歡自然, 所以我帶上了相機.
```

## License
MIT

## 简介
本项目是一个开源 **Agent**，基于 DeepSeek LLM，旨在把 AI 生成的文本“人化”，去除常见的 AI 写作痕迹。主要手段包括：
- 人为制造语病、错句、段落拆分
- 删除冗余修辞、常用连接词
- 随机拼写错误、标点错位

## 项目结构
```
deepseek-anti-ai-agent/
├─ main.py          # CLI 入口
├─ prompts.py       # 生成 Prompt 的模块
├─ postprocess.py   # 基于规则的后处理
├─ requirements.txt # 依赖列表
└─ README.md        # 本说明文件
```

## 安装
```bash
pip install -r requirements.txt
```

## 使用方法
```bash
# 将待处理文本写入 input.txt
python main.py input.txt output.txt
```

## 示例
```text
原文：
今天的天气很好，我决定去公园散步。因为我喜欢自然，所以我带上了相机。

处理后：
今天的天氣很好，我決定去公園散步。因為我喜歡自然, 所以我帶上了相機.
```

## License
MIT
