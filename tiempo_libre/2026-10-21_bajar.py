import sys, os, json
from huggingface_hub import hf_hub_download
repos = {
 "gpt2": "openai-community/gpt2",
 "pythia": "EleutherAI/pythia-160m",
 "smollm2": "HuggingFaceTB/SmolLM2-360M",
 "qwen2.5": "Qwen/Qwen2.5-0.5B",
 "qwen3": "Qwen/Qwen3-0.6B-Base",
 "deepseek-v3": "deepseek-ai/DeepSeek-V3",
 "gpt-4o(o200k)": "Xenova/gpt-4o",
 "gpt-4(cl100k)": "Xenova/gpt-4",
 "llama3": "NousResearch/Meta-Llama-3-8B",
 "mistral7b": "mistral-community/Mistral-7B-v0.2",
 "glm4.5": "zai-org/GLM-4.5",
 "minimax": "MiniMaxAI/MiniMax-Text-01",
 "mimo": "XiaomiMiMo/MiMo-7B-Base",
 "kimi-k2": "moonshotai/Kimi-K2-Instruct",
 "gemma3": "google/gemma-3-1b-pt",
 "grok-1": "xai-org/grok-1",
}
out = {}
for k, r in repos.items():
    for fn in ["tokenizer.json", "tokenizer_config.json", "tiktoken.model", "tokenizer.model"]:
        try:
            p = hf_hub_download(r, fn, cache_dir="tok/cache")
            out.setdefault(k, {})[fn] = p
            print("OK ", k, fn)
        except Exception as e:
            print("-- ", k, fn, type(e).__name__, str(e)[:80])
json.dump(out, open("tok/rutas.json","w"), indent=1)
