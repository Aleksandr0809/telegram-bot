from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("BOT_TOKEN")

@app.get("/")
def home():
    return {"status": "bot alive"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = f"AI сигнал: BUY BTC 🚀 (демо)"

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    return {"ok": True}
