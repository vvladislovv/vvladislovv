from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo
API = '6385882709:AAF8Ize-zgdjUHvcEBi1FayfrIMQczBcfRs'

bot = Bot(API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def Start(Msg: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть сайт страницу', web_app=WebAppInfo(url='https://google.com')))
    await Msg.answer('Привет, мой друг!', reply_markup=markup)
executor.start_polling(dp)