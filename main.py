import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Render Environment Variable မှ Token ကို ယူမည်
TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", "8443"))
# Render ပေါ်ရှိ သင့် Web Service ရဲ့ URL (ဥပမာ - https://your-app-name.onrender.com)
RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Telegram", callback_data="app_telegram")],
        [InlineKeyboardButton("WeChat", callback_data="app_wechat")],
        [InlineKeyboardButton("WhatsApp", callback_data="app_whatsapp")],
        [InlineKeyboardButton("Viber", callback_data="app_viber")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("ကျေးဇူးပြု၍ သင်လိုအပ်သော Service ကို ရွေးချယ်ပါ။", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "app_telegram":
        text = "Telegram စျေးနှုန်း - 3000ks"
        keyboard = [[InlineKeyboardButton("ဝယ်ယူမည်", callback_data="buy")]]
    elif query.data == "app_wechat":
        text = "WeChat စျေးနှုန်း - 30000ks"
        keyboard = [[InlineKeyboardButton("ဝယ်ယူမည်", callback_data="buy")]]
    elif query.data == "app_whatsapp":
        text = "WhatsApp စျေးနှုန်း - 3000ks"
        keyboard = [[InlineKeyboardButton("ဝယ်ယူမည်", callback_data="buy")]]
    elif query.data == "app_viber":
        text = "Viber စျေးနှုန်း - 2000ks"
        keyboard = [[InlineKeyboardButton("ဝယ်ယူမည်", callback_data="buy")]]
    elif query.data == "buy":
        text = (
            "ငွေလွှဲရန် အချက်အလက်များ:\n\n"
            "Kpay - 09680000080\n"
            "Wave - 09680000080"
        )
        keyboard = []

    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    await query.edit_message_text(text=text, reply_markup=reply_markup)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))

    # Webhook ဖြင့် Render ပေါ်တွင် Run ခြင်း
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
