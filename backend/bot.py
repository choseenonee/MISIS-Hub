import random
import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests
import asyncio

bot = Bot(token="6393800116:AAGYz3w5mo8jsxekDhAOAbmC4jPOUsuyWmc")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# заготовленные ответы
main_text = '1. Включить Random Coffee\n2. Выключить Random Coffee'
back_text = 'Вернуться назад'

class Datas():
    logins = []
    tgids = []    
# машина состояний для навигации.
class Wait(StatesGroup):
    login = State()
    random_coffee = State()
    random_coffee_days_delta = State()
    menu_answer = State()
    my_anketa_answer = State()
    anketa_reaction = State()

@dp.message_handler(commands="start", state = "*")
async def anketa_start(message: types.Message):
    # Сделать проверку по tg id
    # Если нет id в бд, то авторизовать по email / login. Иначе зарегистрироваться
    # r = requests.get('http://127.0.0.1:8000/database/get_all_users').json()
    # for i in r:
    #     Datas.logins.append(i['login'])
    #     Datas.tgids.append(i['telegram'])

    username = message.from_user.username
    datas = {
        'telegram': username
    }
    # if username in Datas.tgids:
    r = requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).text
    if r != '{"detail":"Not Found"}':
        message.answer('Добро пожаловать в MISIS Hub')

    else:
        # await message.answer("Пройди регистрацию на нашем сайте (сайт), после этого заново введи команду /start")
        await message.answer('Добро пожаловать!\nЕсли ты уже зарегистрирован на нашем сайте, то введи свой логин\nЕсли ты не зарегистрирован, то скорее сделай это и возвращайся сюда, не забудь снова прописать команду /start. Вот ссылка на наш сайт (ссылка)')
        await Wait.login.set()

@dp.message_handler(state = Wait.login)
async def enter_login(message: types.Message, state: FSMContext):
    datas = {
        'telegram': message.text
    }
    r = requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).text
    if r != '{"detail":"Not Found"}':

        message.answer('Вы успешно авторизовались')
        await state.update_data(login = message.text)
        if requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).json()['random_coffee_active'] == True:
            message.answer('Напишите с какой частотой(раз во сколько дней) ты хочешь получать Random Coffee\nОтправь только число')
            await Wait.random_coffee_days_delta.set()
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Да", "Нет"]
            keyboard.add(*buttons)
            message.answer('Ты хочешь включить функцию Random Coffee?', reply_markup = keyboard)
            await Wait.random_coffee.set()
    else:
        message.answer('Такого пользователя не существует')
        return

@dp.message_handler(state = Wait.random_coffee)
async def text(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await state.update_data(login = message.text.lower())
        message.answer('Напишите с какой частотой(раз во сколько дней) ты хочешь получать Random Coffee\nОтправь только число')
        await Wait.random_coffee_days_delta.set()

    elif message.text == 'Нет':
        message.answer('До встречи!')
        await state.update_data(login = message.text.lower())
        return
    
    else:
        message.answer('Выбери из предложенных вариантов')
        return

@dp.message_handler(state = Wait.random_coffee_days_delta)
async def text(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 0:
            await message.answer('Отправь положительное число')
            return
    except(TypeError, ValueError):
            await message.answer('Отправь положительное число')
            return
    
    await state.update_data(random_coffee_days_delta = int(message.text))
    datas = {
        "login": Wait.login,
        "telegram": message.from_user.username,
        "random_coffee_days_delta": int(message.text)
    }
    requests.put('http://127.0.0.1:8000/database/add_user_tg', json = datas)
    data = await state.get_data()
    d = list(data.values())
    print(d)

    await message.answer(f"Ты будешь получать Random Coffee раз в {int(message.text)} дней", chat_id = message.from_user.id)
    r = requests.get('http://127.0.0.1:8000/get_matches')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1", "2"]
    keyboard.add(*buttons)

    await message.answer(main_text, reply_markup = keyboard)
    await Wait.menu_answer.set()

@dp.message_handler(state = Wait.menu_answer)
async def menu_answer(message: types.Message, state: FSMContext):
    if message.text == "1":
        datas = {
            'telegram': message.from_user.username
        }
        if requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).json()['random_coffee_active'] == True:
            message.answer('У тебя уже включена данная функция')
            return
        else:
            await enter_login()
    elif message.text == '2':
        pass
    else:
        message.answer('Выбери из предложенных вариантов')
        return


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)