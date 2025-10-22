import asyncio
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
dp = Dispatcher()


# Декоратор
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)


@dp.message(Command(commands=['stop']))
async def start(message: types.Message):
    await message.answer(f'До свидания, {message.from_user.full_name}!')


@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f'Твое число - , {number}!')


@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')


# Запускает бесконечный цикл
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
