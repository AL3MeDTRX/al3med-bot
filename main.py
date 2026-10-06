import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8531426087:AAGlRdaTNSTW5YNLStWjHR24pXAOr1Ce1iI"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🛍️ المنتجات", "📞 تواصل"], ["ℹ️ عن المتجر"]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("أهلا فيك بمتجر AL3MeD Market! 🛒\nاختار من القائمة:", reply_markup=markup)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text
    if "المنتجات" in t:
        await update.message.reply_text("🔥 عنا لابتوبات، موبايلات، اكسسوارات.. قريباً قائمة كاملة!")
    elif "تواصل" in t:
        await update.message.reply_text("📞 تواصل: @AL3MeDTRX")
    else:
        await update.message.reply_text("ℹ️ متجر AL3MeD Market - ديرعطية")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()
