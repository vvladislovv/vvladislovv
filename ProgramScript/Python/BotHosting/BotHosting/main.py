from telebot import TeleBot

TOKEN = 'your token'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def Start(message):
    bot.send_message(message.from_user.id, 'Hello!')     

@bot.message_handler(commands=['Text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)     


bot.polling(none_stop=True, interval=0)