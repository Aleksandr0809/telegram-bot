from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.get("/")
def home():
    return {"status": "bot working"}

@app.post("/")
async def webhook(req: Request):
    data = await req.json()
    text = data.get("text", "Signal received")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": f"📡 Сигнал:\n{text}"
    })

    return {"ok": True}
