import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8720594618:AAG8qBE_4WqfZy4GHbwSrdn8254UKQiUzjw"

valid_tokens = {
    "abc123": {"user": "salman", "verified": False}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("👋 Welcome! Koi token nahi diya gaya.")
        return

    token = args[0]
    if token in valid_tokens:
        valid_tokens[token]["verified"] = True
        await update.message.reply_text("✅ Verified! Login successful.")
    else:
        await update.message.reply_text("❌ Invalid or expired link.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
