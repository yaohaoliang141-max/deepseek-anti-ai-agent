# prompts.py
"""Prompt 构建模块
负责把原始文本包装成让 DeepSeek 生成 "人化" 文本的提示。
"""
import textwrap

def build_prompt(raw_text: str) -> str:
    """返回用于 DeepSeek 的完整提示。

    目标：让模型在保持语义不变的情况下，输出更口语化、带有适度错误的文本。
    """
    instruction = (
        "你是一个语言编辑专家，任务是把下面的文本转换成更像人写的风格，" 
        "去掉常见的 AI 写作痕迹。具体要求如下：\n"
        "1. 删除冗余的修辞、过度正式的表达和常用 AI 连接词（例如：因此、综上所述、显然等）。\n"
        "2. 人为制造适度的语病、错句或标点错误，使文本更自然但仍可读。\n"
        "3. 随机拆分或合并句子，增加段落划分，使结构更碎片化。\n"
        "4. 保持原意不变，尽量不要改变关键信息。\n"
        "请直接返回处理后的文本，不要加任何解释或额外的文字。"
    )
    prompt = f"{instruction}\n\n原文：\n" + textwrap.dedent(raw_text).strip()
    return prompt
