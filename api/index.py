import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Header, HTTPException, Request
from telegram import Update

from bot_app import build_application


application = build_application(use_updater=False)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await application.initialize()
    yield
    await application.shutdown()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str | None = Header(default=None),
):
    expected_secret = os.getenv("TELEGRAM_WEBHOOK_SECRET")
    if expected_secret and x_telegram_bot_api_secret_token != expected_secret:
        raise HTTPException(status_code=403, detail="Invalid webhook secret")

    update = Update.de_json(await request.json(), application.bot)
    await application.process_update(update)
    return {"ok": True}
