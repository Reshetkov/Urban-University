import asyncio
from itertools import product

from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton, FSInputFile)

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from crud_functions import get_all_products, add_user, is_included

products = get_all_products()

bot = Bot(token='')
dp = Dispatcher()

buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить'), KeyboardButton(text='Регистрация')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
     InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
], resize_keyboard=True, input_field_placeholder='Выберите опцию:')

inline_buttons_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product1', callback_data='product_buying_1'),
     InlineKeyboardButton(text='Product2', callback_data='product_buying_2'),
     InlineKeyboardButton(text='Product3', callback_data='product_buying_3'),
     InlineKeyboardButton(text='Product4', callback_data='product_buying_4')]
], resize_keyboard=True, input_field_placeholder='Выберите опцию:')


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=buttons)


@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    for i in range(1, 5):
        await message.answer(
            f'Название: {products[i - 1][1]} | Описание: {products[i - 1][2]} | Цена: {products[i - 1][3]}')
        vitamins = FSInputFile(f"D:/PythonProject/Vitamins{i}.jpg")
        await message.answer_photo(photo=vitamins)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_buttons_buy)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_buttons)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.callback_query(F.data == 'formulas')
async def set_age(callback: CallbackQuery):
    await callback.answer('Вы выбрали Формулы расчёта')
    await callback.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query(F.data == 'product_buying_1')
async def send_confirm_message(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query(F.data == 'product_buying_2')
async def send_confirm_message(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query(F.data == 'product_buying_3')
async def send_confirm_message(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query(F.data == 'product_buying_4')
async def send_confirm_message(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы успешно приобрели продукт!')


@dp.message(F.text == 'Регистрация')
async def sing_up(message: Message, state: FSMContext):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    is_on_the_list = is_included(message.text)
    if is_on_the_list:
        await message.answer('Пользователь существует, введите другое имя')
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(username=data['username'], email=data['email'], age=data['age'])
    await state.clear()


@dp.callback_query(F.data == 'calories')
async def set_age(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Вы выбрали Рассчитать норму калорий')
    await callback.message.answer('Введите свой возраст:')
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
