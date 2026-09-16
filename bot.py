import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
)

from handlers.start import start
from handlers.jokes import (
    category_selected,
    another_joke,
    show_categories,
)


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    CallbackQueryHandler(
        category_selected,
        pattern=r"^category:",
    )
)

app.add_handler(
    CallbackQueryHandler(
        another_joke,
        pattern=r"^joke:",
    )
)

app.add_handler(
    CallbackQueryHandler(
        show_categories,
        pattern=r"^categories$",
    )
)


app.run_polling()