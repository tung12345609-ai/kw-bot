from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8878252315:AAETPZHyr0xMV4KrO9gWXsN4yHh8KxEVTWo"

async def hellobot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ten = update.effective_user.first_name
    await update.message.reply_text(
        f"Xin chào {ten}, tôi là bot Quân Đoàn KW, bạn cần sự trợ giúp gì không?"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("hellobot", hellobot))

print("Bot đang chạy...")
app.run_polling()