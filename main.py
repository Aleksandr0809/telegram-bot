@app.post("/")
async def webhook(req: Request):
    data = await req.json()

    message = data.get("message", {})
    text = message.get("text", "Без текста")

    # ВАЖНО: берём chat_id из Telegram
    chat_id = message.get("chat", {}).get("id")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": f"🤖 Ответ бота:\n{text}"
    })

    return {"ok": True}
