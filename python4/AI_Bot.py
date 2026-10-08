import os
import logging

from dotenv import load_dotenv
from google import genai
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ============================================================
# ASTRA AI BOT
# Version 1.0
# ============================================================

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")


# ------------------------------------------------------------
# Gemini
# ------------------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)

MODEL = "gemini-3.8-flash"


# ------------------------------------------------------------
# Logging
# ------------------------------------------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("ASTRA")


# ------------------------------------------------------------
# Memory
# ------------------------------------------------------------

user_chats = {}


def get_chat(user_id):

    if user_id not in user_chats:

        user_chats[user_id] = client.chats.create(
            model=MODEL
        )

    return user_chats[user_id]


def clear_chat(user_id):

    if user_id in user_chats:
        del user_chats[user_id]


# ------------------------------------------------------------
# Start
# ------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    name = user.first_name or "دوست من"

    text = f"""
🤖 سلام {name}!

من **ASTRA AI** هستم 🌌

یک دستیار هوش مصنوعی هستم که می‌تونی باهام گفتگو کنی.

💬 هر چیزی می‌خوای بپرس.

دستورات:

/start
شروع ربات

/help
راهنمای ربات

/clear
پاک کردن حافظه گفتگو

/status
وضعیت ربات

🔥 ASTRA AI
"""

    await update.message.reply_text(text)


# ------------------------------------------------------------
# Help
# ------------------------------------------------------------

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = """
🤖 ASTRA AI — Help

💬 برای صحبت با هوش مصنوعی:
فقط پیام خودت را ارسال کن.

دستورات:

/start
شروع ربات

/help
نمایش راهنما

/clear
پاک کردن حافظه مکالمه

/status
نمایش وضعیت ربات

🧠 ASTRA می‌تواند Context مکالمه را حفظ کند.
"""

    await update.message.reply_text(text)


# ------------------------------------------------------------
# Clear
# ------------------------------------------------------------

async def clear_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    clear_chat(user_id)

    await update.message.reply_text(
        "🧹 حافظه مکالمه پاک شد.\n\n"
        "از اینجا یک گفتگوی جدید شروع می‌کنیم."
    )


# ------------------------------------------------------------
# Status
# ------------------------------------------------------------

async def status_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    active = user_id in user_chats

    status = "فعال 🟢" if active else "هنوز شروع نشده ⚪"

    text = f"""
🤖 ASTRA AI STATUS

Model:
{MODEL}

Conversation:
{status}

API:
🟢 Connected

Memory:
{"🟢 Active" if active else "⚪ Empty"}
"""

    await update.message.reply_text(text)


# ------------------------------------------------------------
# AI
# ------------------------------------------------------------

async def ai_response(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.message:
        return

    user_id = update.effective_user.id
    message = update.message.text.strip()

    if not message:
        return

    # Typing indicator
    await update.message.chat.send_action(
        action="typing"
    )

    try:

        chat = get_chat(user_id)

        response = chat.send_message(
            message
        )

        answer = response.text

        if not answer:
            answer = "❌ پاسخی از هوش مصنوعی دریافت نشد."

        # Telegram message limit protection
        max_length = 4000

        if len(answer) <= max_length:

            await update.message.reply_text(
                answer
            )

        else:

            for i in range(
                0,
                len(answer),
                max_length
            ):

                chunk = answer[
                    i:i + max_length
                ]

                await update.message.reply_text(
                    chunk
                )

    except Exception as error:

        logger.exception(
            "Gemini error: %s",
            error
        )

        await update.message.reply_text(
            "❌ متأسفانه هنگام ارتباط با "
            "هوش مصنوعی مشکلی پیش آمد.\n\n"
            "چند لحظه بعد دوباره امتحان کن."
        )


# ------------------------------------------------------------
# Error handler
# ------------------------------------------------------------

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logger.exception(
        "Unhandled error:",
        exc_info=context.error
    )


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    print("=" * 60)
    print("🤖 ASTRA AI BOT")
    print("=" * 60)
    print(f"🧠 Model: {MODEL}")
    print("🚀 Starting bot...")
    print("=" * 60)

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    # Commands
    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    application.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )

    application.add_handler(
        CommandHandler(
            "clear",
            clear_command
        )
    )

    application.add_handler(
        CommandHandler(
            "status",
            status_command
        )
    )

    # Messages
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            ai_response
        )
    )

    # Errors
    application.add_error_handler(
        error_handler
    )

    print("🟢 ASTRA AI is running!")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()