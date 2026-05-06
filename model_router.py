import os
import requests
from config import MODELS

HF_API_KEY = os.getenv("HF_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_huggingface(model_cfg, prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    r = requests.post(model_cfg["url"], headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, list):
        return data[0].get("generated_text", "")
    return str(data)

def call_groq(model_cfg, prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post(model_cfg["url"], headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def generate_reply(model_name, prompt):
    model_cfg = MODELS[model_name]

    if model_cfg["provider"] == "huggingface":
        return call_huggingface(model_cfg, prompt)

    if model_cfg["provider"] == "groq":
        return call_groq(model_cfg, prompt)

    return "Unknown model provider."
