from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import logging

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_URL = "https://t.me/kittuu_updates"
SUPPORT_GROUP_URL = "https://t.me/+2Bu0_JhMY7BkMmY1"
BOT_USERNAME = "toxicxedit_guardian_bot"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/toxicxedit_guardian_bot?startgroup=true")],
        [
            InlineKeyboardButton("📢 Updates", url="https://t.me/kittuu_updates"),
            InlineKeyboardButton("💬 Support", url="https://t.me/+2Bu0_JhMY7BkMmY1")
        ]
    ]
    text = (
        "🤖 <b>Edit Guardian Bot</b> 🤖\n\n"
        "👋 <b>Hello!</b>\n\n"
        "✨ I'm already protecting this group! 🛡️\n"
        "✅ <b>Status:</b> <i>Active & Monitoring</i>\n\n"
        "🔒 <b>Your Group is Now Secured!</b> 🚀"
    )
    await update.message.reply_html(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True
    )

async def edited_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.edited_message
    if not message:
        return
    user = message.from_user
    chat = message.chat
    try:
        await message.delete()
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🚀 Solution", url=https://t.me/+2Bu0_JhMY7BkMmY1)]]
        )
        warn_text = (
            f"⚠️ <b>{user.first_name}</b>, your message was deleted because it contained an edited message."
        )
        await chat.send_message(
            warn_text,
            parse_mode="HTML",
            reply_markup=button
        )
    except Exception as e:
        logger.error(f"Error deleting message: {e}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, edited_message_handler))
    logger.info("Bot started successfully...")
    application.run_polling
