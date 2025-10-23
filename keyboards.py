from aiogram import types

button1 = types.KeyboardButton(text='Начать тест')
button2 = types.KeyboardButton(text='Поговорить')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Очистить')
button5 = types.KeyboardButton(text='Стоп')

keyboard1 = [
    [button1],
    [button2, button3, button4],
    [button5]
]

keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
