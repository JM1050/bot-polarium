import telebot

# Token do seu bot do Telegram
TOKEN = "7640314696:AAHzRO4Q-j8HbYMXbiyddLS9og2q24JwfKY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! O bot está funcionando corretamente!")

bot.polling()
