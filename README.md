# DeepSeek 去除 AI 痕迹 Agent

> 一个基于 DeepSeek API 的开源工具，把 AI 生成的文本"人化"，消除常见的 AI 写作痕迹。

---

## ✨ 功能特点

- 自动删除常用 AI 连接词（因此、综上所述、显然等）
- 随机制造语病、标点错误，模拟真人写作
- 随机拆分/合并句子，生成自然段落
- **无需后端服务器**，纯前端运行，打开浏览器即可使用
- 双栏布局（左侧输入，右侧实时显示结果），类似 Markdown‑Nice 编辑器
- 一键复制处理结果

---

## 📦 快速部署（推荐，3 步完成）

### 第一步：下载项目

```bash
git clone https://github.com/yaohaoliang141-max/deepseek-anti-ai-agent.git
cd deepseek-anti-ai-agent
```

或者直接在 GitHub 页面点击 **Code → Download ZIP**，解压后进入文件夹。

### 第二步：获取 DeepSeek API Key

1. 前往 [DeepSeek 开放平台](https://platform.deepseek.com/) 注册账号。
2. 进入 **API Keys** 页面，创建一个新的 API Key，复制备用。

### 第三步：启动工具

**Windows 用户（推荐）：**

双击 `deepseek_ui.bat`，或者在 CMD / PowerShell 中执行：

```cmd
deepseek_ui.bat
```

浏览器会自动打开工具界面，即可开始使用。

**其他系统（Mac / Linux）：**

直接用浏览器打开项目目录下的 `ui.html` 文件：

```bash
open ui.html       # macOS
xdg-open ui.html   # Linux
```

---

## 🖥️ 使用方法

1. 打开工具界面后，在左侧 **API Key** 输入框粘贴你的 DeepSeek API Key。
2. 在左侧 **原始文本** 框中粘贴需要处理的 Markdown 文本。
3. 点击 **一键处理** 按钮，等待处理完成（按钮会显示"处理中…"）。
4. 右侧会实时显示处理后的文本（已自动分段，去除 AI 痕迹）。
5. 点击右侧 **复制** 按钮，结果即可粘贴到任何地方使用。<img width="1915" height="896" alt="屏幕截图 2026-05-06 211216" src="https://github.com/user-attachments/assets/512946a2-6ded-465a-9ece-287d4ee4c896" />


---

## 🗂️ 项目结构

```
deepseek-anti-ai-agent/
├─ ui.html          # 主界面（双栏编辑器，直接浏览器打开）
├─ style.css        # UI 样式（暗色玻璃拟态）
├─ script.js        # 前端逻辑（DeepSeek API 调用 + 本地后处理）
├─ deepseek_ui.bat  # Windows 一键启动脚本
├─ build.bat        # 打包脚本，生成可分发的 zip 包
├─ main.py          # Python CLI 版本（可选）
├─ prompts.py       # Prompt 构造模块
├─ postprocess.py   # 本地后处理规则
├─ requirements.txt # Python 依赖（仅 CLI 版本需要）
└─ README.md        # 本说明文件
```

---

## 🐍 Python CLI 版本（可选）

如果你更喜欢命令行方式，可以使用 Python CLI 版本：

### 安装依赖

```bash
pip install -r requirements.txt
```

### 使用方法

```bash
# 将待处理文本写入 input.txt
python main.py input.txt output.txt
```

---

## 🔒 安全说明

- 本工具**不存储**你的 API Key，密钥仅在浏览器会话中临时使用。
- 项目代码中**无任何硬编码的密钥**，可安全公开使用。
- 所有处理均在**本地浏览器**完成（除 DeepSeek API 调用外），无需额外服务器。

---

## 📝 示例

**原文（AI 风格）：**
```
综上所述，今天的天气很好，因此我决定去公园散步。显然，我喜欢自然，所以我带上了相机。
```

**处理后（人化风格）：**
```
今天的天气很好，我决定去公园散步。喜欢自然嘛，带上了相机。
```

---朱雀ai检测为0<img width="1794" height="886" alt="屏幕截图_6-5-2026_211656_matrix tencent com" src="https://github.com/user-attachments/assets/e2cbddc9-f8b9-4ac8-8258-9aa1c3fe42e3" />


## 📄 License

MIT
