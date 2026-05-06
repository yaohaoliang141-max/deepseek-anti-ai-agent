#!/usr/bin/env python3
"""deepseek-anti-ai-agent 主入口
使用方式: python main.py <input.txt> <output.txt>
"""
import sys, os, json, requests
from pathlib import Path
# 确保脚本所在目录在模块搜索路径中，避免 import 错误
sys.path.append(os.path.dirname(__file__))
from prompts import build_prompt
from postprocess import postprocess_text

API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    print("[错误] 请设置环境变量 DEEPSEEK_API_KEY 为你的 DeepSeek API Key")
    sys.exit(1)

def call_deepseek(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2048,
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()

def main():
    if len(sys.argv) != 3:
        print("用法: python main.py <input.txt> <output.txt>")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not input_path.is_file():
        print(f"[错误] 输入文件不存在: {input_path}")
        sys.exit(1)
    raw_text = input_path.read_text(encoding="utf-8")
    prompt = build_prompt(raw_text)
    try:
        ai_result = call_deepseek(prompt)
    except Exception as e:
        print(f"[错误] 调用 DeepSeek 失败: {e}")
        sys.exit(1)
    final_text = postprocess_text(ai_result)
    output_path.write_text(final_text, encoding="utf-8")
    print(f"已写入结果到 {output_path}")

if __name__ == "__main__":
    main()
