import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Sizning bot tokeningiz
TOKEN = "9089534105:AAG7HSXPWugc49BZmNq5YRsv6i63y2Swqq8"
bot = telebot.TeleBot(TOKEN)

# Render'dagi mini-ilovangizning havolasi (agar havolangiz boshqacha bo'lsa, o'sha link bilan almashtirasiz)
WEB_APP_URL = "https://ozimiz-uchun.onrender.com"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEB_APP_URL)
    markup.add(InlineKeyboardButton("🛍️ Ilovani ochish", web_app=web_app))
    
    welcome_text = (
        "Assalomu alaykum! \"Oʻzimiz uchun\" qishloq savdo va taksi platformasiga xush kelibsiz! 🏡\n\n"
        "Quyidagi tugmani bosib, e'lonlar va taksi xizmatidan foydalanishingiz mumkin:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

print("Bot ishga tushdi...")
bot.infinity_polling()

