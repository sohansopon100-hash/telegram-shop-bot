from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8908319230:AAEDN3HFX49IjoEGkfHntRCzJUVFKeCbR5U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\nYour Telegram Shop Bot is working."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
