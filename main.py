from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==== AI ответ (простая версия) ====
def ai_reply(text):
    # пока простой AI-ответ
    if "сигнал" in text.lower():
        return "📊 AI сигнал: BTC LONG\nTP: +3%\nSL: -1%"
    return "🤖 AI бот онлайн. Напиши: сигнал"

# ==== Home ====
@app.get("/")
def home():
    return {"status": "AI bot running"}

# ==== Webhook от Telegram ====
@app.post("/")
async def webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = ai_reply(text)

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}
