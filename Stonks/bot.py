import telebot

token = '1235319864:AAErBd1NgrDwu5QTPoe_9yMEmsjoOjQ9oBY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()

