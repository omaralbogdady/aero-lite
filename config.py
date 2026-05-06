MODELS = {
    "phi": {
        "provider": "huggingface",
        "url": "https://api-inference.huggingface.co/microsoft/Phi-3.5-mini-instruct"
    },
    "llama3": {
        "provider": "huggingface",
        "url": "https://api-inference.huggingface.co/meta-llama/Llama-3.1-8B-Instruct"
    },
    "gemma": {
        "provider": "huggingface",
        "url": "https://api-inference.huggingface.co/google/gemma-2-9b-it"
    },
    "groq_llama3": {
        "provider": "groq",
        "url": "https://api.groq.com/openai/v1/chat/completions"
    }
}
