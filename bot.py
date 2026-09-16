import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def get_random_joke():
    response = requests.get(
        "https://icanhazdadjoke.com/",
        headers={
            "Accept": "application/json",
            "User-Agent": "get-random-joke"
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    return data["joke"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! 👋\n\n"
        "I'm Get Random Joke Bot.\n"
        "Use /joke to get a random joke."
    )


async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke_text = get_random_joke()

    await update.message.reply_text(
        f"{joke_text} 😂"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("joke", joke))

app.run_polling()
