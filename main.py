from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# проверка что сервер живой
@app.get("/")
def home():
    return {"status": "bot running"}

# вот ОН — webhook
@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("Update:", data)

    if "message" in data:
        text = data["message"].get("text", "")
        chat_id = data["message"]["chat"]["id"]

        reply = f"AI сигнал получен: {text}"

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": reply}
        )

    return {"ok": True}
