import logging
from aiogram import Bot, Dispatcher, executor, types
import Markups as nav

APITOKENBOT = "6383927916:AAHj_LpeLkud1puWQkotFJpOD4UwAd37-5Y"
CHANLEID = "@asdfasdfw3e253452345234"
NOTSUB_MESSAGE = "Для использование бота, подпишись на канал."


logging.basicConfig(level=logging.INFO)

bot = Bot(token=APITOKENBOT)
dep = Dispatcher(bot)


@dep.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if check_sub_Channle(await bot.get_chat_member(chat_id=CHANLEID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=nav.profileKeyboard)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSbuMenu)
        

def check_sub_Channle(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dep.message_handler()
async def bot_message(message: types.Message):
            if message.chat.type == 'private':
                if check_sub_Channle(await bot.get_chat_member(chat_id=CHANLEID, user_id=message.from_user.id)):
                    if message.text == "Profile":
                        await bot.send_message(message.from_user.id, "сообщение")
                        
                    else:
                        await bot.send_message(message.from_user.id, "сообщение2")
                else:
                    await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSbuMenu)
                


@dep.callback_query_handler(text="subchannledone")
async def subchannledone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_Channle(await bot.get_chat_member(chat_id=CHANLEID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет!", reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSbuMenu)
         
                    
if __name__ == "__main__":
    executor.start_polling(dep)