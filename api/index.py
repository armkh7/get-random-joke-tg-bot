import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Header, HTTPException, Request
from telegram import Update

from bot_app import build_application


bot_application = build_application(use_updater=False)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await bot_application.initialize()
    yield
    await bot_application.shutdown()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str | None = Header(default=None),
):
    expected_secret = os.getenv("TELEGRAM_WEBHOOK_SECRET")
    if expected_secret and x_telegram_bot_api_secret_token != expected_secret:
        raise HTTPException(status_code=403, detail="Invalid webhook secret")

    update = Update.de_json(await request.json(), bot_application.bot)
    await bot_application.process_update(update)
    return {"ok": True}
