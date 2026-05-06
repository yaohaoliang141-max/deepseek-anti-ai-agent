// script.js
// 前端逻辑：调用 DeepSeek API、后处理、结果展示 & 复制

const apiKeyInput = document.getElementById('apiKey');
const rawTextInput = document.getElementById('rawText');
const processBtn   = document.getElementById('processBtn');
// const outputBox    = document.getElementById('outputBox'); // 已删除，不再使用
const resultText   = document.getElementById('resultText');
const copyBtn      = document.getElementById('copyBtn');

/* ---------- 本地后处理规则（与 postprocess.py 同步） ---------- */
const COMMON_CONNECTORS = [
    "因此","综上所述","显然","显而易见","可以看出","从而","总体而言","换言之","事实上",
    "总体来看","由于","因为","所以","然而","但是","不过","此外"
];
function removeConnectors(text){
    const pattern = new RegExp(`\\b(${COMMON_CONNECTORS.map(c=>c.replace(/[.*+?^${}()|[\\]\\]/g,'\\$&')).join('|')})\\b`,'g');
    return text.replace(pattern, "");
}
function randomSplit(text){
    const sentences = text.split(/(?<=[。！？])/);
    return sentences.map(s=>{
        s = s.trim();
        if(s && Math.random()<0.1){
            const parts = s.split(/[，,]/);
            if(parts.length>1){
                const idx = Math.floor(Math.random()*(parts.length-1))+1;
                parts.splice(idx,0,"\n");
                s = parts.join("，");
            }
        }
        return s;
    }).join(" ");
}
function punctErrors(txt){
    return txt.replace(/[。！？]/g,m=>["。","，",""][Math.floor(Math.random()*3)]);
}
function injectTypos(txt){
    return txt.split(/\s+/).map(w=>{
        if(w.length<3) return w;
        const r=Math.random();
        if(r<0.05){
            const i=Math.floor(Math.random()*(w.length-1));
            return w.slice(0,i)+w[i+1]+w[i]+w.slice(i+2);
        }else if(r<0.08){
            const i=Math.floor(Math.random()*w.length);
            return w.slice(0,i)+w[i]+w[i]+w.slice(i);
        }
        return w;
    }).join(" ");
}
function postprocess(text){
    let t = removeConnectors(text);
    t = randomSplit(t);
    t = punctErrors(t);
    t = injectTypos(t);
    // 添加段落分隔：在句号、感叹号、问号后插入双换行
    t = t.replace(/[。！？]/g, m => m + "\n\n");
    return t.replace(/\s+/g, " ").trim();
}

/* ---------- 调用 DeepSeek ---------- */
async function callDeepSeek(apiKey, prompt){
    const url = "https://api.deepseek.com/v1/chat/completions";
    const payload = {
        model: "deepseek-chat",
        messages: [{role: "user", content: prompt}],
        temperature: 0.7,
        max_tokens: 2048
    };
    const resp = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${apiKey}`
        },
        body: JSON.stringify(payload)
    });
    if(!resp.ok){
        const txt = await resp.text();
        throw new Error(`HTTP ${resp.status}: ${txt}`);
    }
    const data = await resp.json();
    return data.choices[0].message.content.trim();
}

/* ---------- UI 交互 ---------- */
processBtn.addEventListener('click', async()=>{
    const apiKey = apiKeyInput.value.trim();
    const raw    = rawTextInput.value.trim();
    if(!apiKey){ alert('请填写 DeepSeek API Key'); return; }
    if(!raw){ alert('请填写待处理文本'); return; }
    processBtn.disabled = true;
    processBtn.textContent = '处理中…';
    try{
        const instruction = `你是一个语言编辑专家，任务是把下面的文本转换成更像人写的风格，去掉常见的 AI 写作痕迹。要求：\n1. 删除冗余修辞、过度正式的表达和常用 AI 连接词（例如：因此、综上所述、显然等）。\n2. 人为制造适度的语病、错句或标点错误，使文本更自然但仍可读。\n3. 随机拆分或合并句子，增加段落划分，使结构更碎片化。\n4. 保持原意不变，尽量不要改变关键信息。\n请直接返回处理后的文本，不要加任何解释。`;
        const prompt = `${instruction}\n\n原文：\n${raw}`;
        const aiResult = await callDeepSeek(apiKey, prompt);
        const finalResult = postprocess(aiResult);
        resultText.textContent = finalResult;
        // outputBox 已删除，直接显示结果即可
    }catch(e){
        alert('调用 DeepSeek 失败：' + e.message);
    }finally{
        processBtn.disabled = false;
        processBtn.textContent = '一键处理';
    }
});

copyBtn.addEventListener('click',()=>{
    const range = document.createRange();
    range.selectNodeContents(resultText);
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand('copy');
    sel.removeAllRanges();
    copyBtn.textContent = '已复制';
    setTimeout(()=>{ copyBtn.textContent = '复制'; },1500);
});
