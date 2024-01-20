#import telebot
from aiogram import Bot, Dispatcher, executor, types

botTG = Bot('6544058138:AAHaHzcL0e1ltl98CRTD2zNAOSCPWT0wE14')
dp = Dispatcher(botTG)


@dp.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('hello', reply_markup=markup)
    

@dp.callback_query_handler() 
async def callback(call):
    await call.message.anwer(call.data)
    
executor.start_polling(dp)




#bot = telebot.TeleBot('6544058138:AAHaHzcL0e1ltl98CRTD2zNAOSCPWT0wE14')

        
#bot.polling(none_stop=True)