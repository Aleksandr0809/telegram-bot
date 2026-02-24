from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Токен из Render Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

@app.get("/")
def home():
    return {"status": "bot working"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Ответ бота
        reply = f"AI bot: {text}"

        # Отправка ответа в Telegram
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    return {"ok": True}
