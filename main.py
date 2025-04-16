from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route("/leao-ia", methods=["POST"])
def webhook():
    message = request.get_data(as_text=True)
    if message:
        send_telegram_message(f"📢 Alerta do LEÃO IA 🦁: {message}")

    return "OK", 200

if __name__ == "__main__":
    app.run()
