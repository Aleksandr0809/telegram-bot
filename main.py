from fastapi import FastAPI, Request
import requests
import os
import openai

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY


# Проверка сервера
@app.get("/")
def home():
    return {"status": "bot running"}


# 🔥 ВОТ ЭТОГО У ТЕБЯ НЕ БЫЛО
@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    try:
        text = data["message"]["text"]
        chat_id = data["message"]["chat"]["id"]

        # AI ответ
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": text}]
        )

        answer = response.choices[0].message.content

        send_message(chat_id, answer)

    except Exception as e:
        print("ERROR:", e)

    return {"ok": True}


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })
