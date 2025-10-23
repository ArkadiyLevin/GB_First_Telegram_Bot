# Импорты и библиотеки
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard

# Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


# Декоратор.   Приветствие и базовая инфа о боте
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}! \nЭтот бот проверит, репликант ты или нет.\nЖми «Начать тест», если готов узнать результат.\nИли «Поговорить» — если просто хочется пообщаться.',
        reply_markup=keyboard)


@dp.message(Command(commands=['stop']))
async def start(message: types.Message):
    await message.answer(f'До свидания, {message.from_user.full_name}!')


@dp.message(Command(commands=['инфо', 'info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Привет, твоё число: {number}!')


@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')

#
# @dp.message(F.text)
# async def msg(message: types.Message):
#
#
# # if 'привет' in message.text.lower():
#     await message.reply('И тебе привет!')
# elif 'как дела' in message.text.lower():
# await message.reply('Нормально, а у тебя?')
# else:
# await message.reply('Не понимаю тебя...')


# Запускает бесконечный цикл
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
