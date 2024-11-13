import asyncio
from aiogram import F, Router, Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token='')
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    print('Привет! Я бот помогающий твоему здоровью.')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('Calories'))
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calorie_norm = int(data['weight']) * 10 + int(data['growth']) * 6.25 - int(data['age']) * 5 + 5
    await message.answer(f'Ваша норма калорий: {calorie_norm}')
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
