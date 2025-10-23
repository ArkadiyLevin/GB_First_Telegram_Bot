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


@dp.message(F.text == "Инфо")
async def info(message: types.Message):
    await message.answer(
        "📘 *Информация о боте*\n\n"
        "   Этот бот создан по мотивам фильма _«Бегущий по лезвию 2049»_.\n"
        "В центре истории — тест Войта-Кампфа, разработанный для выявления репликантов — "
        "искусственно созданных существ, внешне неотличимых от людей.\n\n"
        "   Тест проверяет эмоциональные реакции, способность к сочувствию и спонтанным чувствам. "
        "Репликанты, как правило, не умеют по-настоящему сопереживать — и это выдает их.\n\n"
        "   Этот бот — игровая интерпретация теста. Здесь ты можешь пройти проверку и узнать, "
        "кто ты — человек или репликант.\n\n"
        "   Создан в качестве творческого проекта и личного эксперимента с искусственным интеллектом.\n\n"
        "👤 Автор: *Райан Гослинг*\n"
        "_По мотивам вселенной Blade Runner._",
        parse_mode="Markdown"
    )


@dp.message(Command(commands=['stop']))
async def start(message: types.Message):
    await message.answer(f'До свидания, {message.from_user.full_name}!')


# Запускает бесконечный цикл
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
