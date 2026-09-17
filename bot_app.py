import os

from dotenv import load_dotenv
from telegram.ext import Application, CallbackQueryHandler, CommandHandler

from handlers.jokes import another_joke, category_selected, show_categories
from handlers.start import start


load_dotenv()


def build_application(*, use_updater: bool = True) -> Application:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    builder = Application.builder().token(token)
    if not use_updater:
        builder = builder.updater(None)
    application = builder.build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        CallbackQueryHandler(category_selected, pattern=r"^category:")
    )
    application.add_handler(CallbackQueryHandler(another_joke, pattern=r"^joke:"))
    application.add_handler(
        CallbackQueryHandler(show_categories, pattern=r"^categories$")
    )
    return application
