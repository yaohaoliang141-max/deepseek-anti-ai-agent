# postprocess.py
"""基于规则的后处理，进一步去除 AI 写作痕迹。
主要功能：
- 删除常见 AI 连接词
- 随机拆分/合并句子
- 人为制造语病、错句、标点错位
- 随机插入轻度拼写错误
"""
import random, re

COMMON_CONNECTORS = [
    "因此", "综上所述", "显然", "显而易见", "可以看出", "从而", "总体而言", "换言之", "事实上",
    "总体来看", "由于", "因为", "所以", "然而", "但是", "不过", "此外",
]

def remove_connectors(text: str) -> str:
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, COMMON_CONNECTORS)) + r")\b")
    return pattern.sub("", text)

def random_split_sentences(text: str) -> str:
    sentences = re.split(r"(?<=[。！？])", text)
    new_sentences = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if random.random() < 0.1:
            parts = re.split(r"[，,]", s)
            if len(parts) > 1:
                idx = random.randint(1, len(parts)-1)
                parts.insert(idx, "\n")
                s = "，".join(parts)
        new_sentences.append(s)
    return " ".join(new_sentences)

def random_punctuation_errors(text: str) -> str:
    def repl(m):
        if m.group(0) == "。":
            return random.choice(["。", "，", ""])
        return m.group(0)
    return re.sub(r"[。！？]", repl, text)

def inject_typos(text: str) -> str:
    def typo(word):
        if len(word) < 3:
            return word
        r = random.random()
        if r < 0.05:
            i = random.randint(0, len(word)-2)
            lst = list(word)
            lst[i], lst[i+1] = lst[i+1], lst[i]
            return "".join(lst)
        elif r < 0.08:
            i = random.randint(0, len(word)-1)
            return word[:i] + word[i] + word[i:]
        return word
    return " ".join(typo(w) for w in text.split())

def postprocess_text(text: str) -> str:
    text = remove_connectors(text)
    text = random_split_sentences(text)
    text = random_punctuation_errors(text)
    text = inject_typos(text)
    return re.sub(r"\s+", " ", text).strip()
