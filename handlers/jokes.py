from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.joke_api import get_random_joke
from handlers.start import get_category_keyboard


def get_joke_keyboard(category: str):
    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 Another joke",
                callback_data=f"joke:{category}",
            )
        ],
        [
            InlineKeyboardButton(
                "📂 Change category",
                callback_data="categories",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def category_selected(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    category = query.data.split(":")[1]

    await send_joke(query, category)


async def another_joke(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    category = query.data.split(":")[1]

    await send_joke(query, category)


async def show_categories(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        text="😂 Choose a joke category:",
        reply_markup=get_category_keyboard(),
    )


async def send_joke(query, category: str):
    try:
        joke = get_random_joke(category)

        await query.edit_message_text(
            text=f"😂 {joke}",
            reply_markup=get_joke_keyboard(category),
        )

    except Exception:
        await query.edit_message_text(
            text="Sorry, I couldn't get a joke right now. Please try again."
        )