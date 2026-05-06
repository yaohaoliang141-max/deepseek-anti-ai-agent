# DeepSeek 去除 AI 痕迹 Agent

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
