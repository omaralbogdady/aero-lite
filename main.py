from flask import Flask, request
import os
import requests
from model_router import generate_reply

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DEFAULT_MODEL = "phi"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    # Model switching
    if text.startswith("/model"):
        parts = text.split()
        if len(parts) == 2:
            model = parts[1]
            from config import MODELS
            if model in MODELS:
                global DEFAULT_MODEL
                DEFAULT_MODEL = model
                send_message(chat_id, f"Switched to model: {model}")
            else:
                send_message(chat_id, f"Available models: {', '.join(MODELS.keys())}")
        return "ok"

    prompt = f"You are Aero, a helpful assistant.\nUser: {text}\nAssistant:"
    reply = generate_reply(DEFAULT_MODEL, prompt)

    send_message(chat_id, reply)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
