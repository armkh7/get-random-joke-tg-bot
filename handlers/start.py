from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


def get_category_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💻 Programming", callback_data="category:Programming"),
            InlineKeyboardButton("🎲 Misc", callback_data="category:Misc"),
        ],
        [
            InlineKeyboardButton("🌑 Dark", callback_data="category:Dark"),
            InlineKeyboardButton("🎭 Pun", callback_data="category:Pun"),
        ],
        [
            InlineKeyboardButton("👻 Spooky", callback_data="category:Spooky"),
            InlineKeyboardButton("🎄 Christmas", callback_data="category:Christmas"),
        ],
        [
            InlineKeyboardButton("🎯 Any", callback_data="category:Any"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😂 Welcome to Get Random Joke!\n\n"
        "Choose a category:",
        reply_markup=get_category_keyboard(),
    )