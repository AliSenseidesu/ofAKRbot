import telebot

TOKEN = "8038569727:AAGG6ZDo-tngNLCELKQgPa0GvW0MqAyaX0Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎬 دانلود انیمه", "📰 اخبار")

    bot.send_message(message.chat.id, "یکی رو انتخاب کن:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == "🎬 دانلود انیمه":
        bot.send_message(message.chat.id, "لینک دانلود: AKR40.wordpress.com")

    elif message.text == "📰 اخبار":
        bot.send_message(message.chat.id, "آخرین اخبار انیمه...")

    else:
        bot.send_message(message.chat.id, "گزینه نامعتبره")

bot.polling()