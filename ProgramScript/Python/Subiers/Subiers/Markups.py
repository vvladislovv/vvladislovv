from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton('Profile')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile)


btbURLChannel = InlineKeyboardButton(text="Подписаться", url='https://t.me/asdfasdfw3e253452345234')
bntSubCheck = InlineKeyboardButton(text="Подписался", callback_data="subchannledone")

checkSbuMenu = InlineKeyboardMarkup(row_width=1)
checkSbuMenu.insert(bntSubCheck)
checkSbuMenu.insert(btbURLChannel)
