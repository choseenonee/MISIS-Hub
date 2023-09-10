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
main_text = 'Главное меню\n1. Включить Random Coffee\n2. Выключить Random Coffee'
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

class User():
    login: str
    telegram: str

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
        await message.answer('Добро пожаловать в MISIS Hub')
        User.login = requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).json()["login"]
        User.telegram = username
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["1", "2"]
        keyboard.add(*buttons)

        await message.answer(main_text, reply_markup = keyboard)
        await Wait.menu_answer.set()
    else:
        # await message.answer("Пройди регистрацию на нашем сайте (сайт), после этого заново введи команду /start")
        await message.answer('Добро пожаловать!\nЕсли ты уже зарегистрирован на нашем сайте, то введи свой логин\nЕсли ты не зарегистрирован, то скорее сделай это и возвращайся сюда, не забудь снова прописать команду /start. Вот ссылка на наш сайт (ссылка)')
        await Wait.login.set()

@dp.message_handler(state = Wait.login)
async def enter_login(message: types.Message, state: FSMContext):
    datas = {
        'login': message.text
    }
    r = requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).text
    print(r)
    if r != '{"detail":"Not Found"}':

        message.answer('Вы успешно авторизовались')
        User.login = message.text
        User.telegram = message.from_user.username
        print(User.telegram)
        await state.update_data(login = message.text)
        if requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).json()['random_coffee_active'] == True:
            await message.answer('Напишите с какой частотой(раз во сколько дней) ты хочешь получать Random Coffee\nОтправь только число')
            await Wait.random_coffee_days_delta.set()
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Да", "Нет"]
            keyboard.add(*buttons)
            await message.answer('Ты хочешь включить функцию Random Coffee?', reply_markup = keyboard)
            await Wait.random_coffee.set()
    else:
        await message.answer('Такого пользователя не существует')
        return

@dp.message_handler(state = Wait.random_coffee)
async def text(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await state.update_data(login = message.text.lower())
        await message.answer('Напишите с какой частотой(раз во сколько дней) ты хочешь получать Random Coffee\nОтправь только число')
        await Wait.random_coffee_days_delta.set()

    elif message.text == 'Нет':
        await message.answer('До встречи!')
        await state.update_data(login = message.text.lower())
        return
    
    else:
        await message.answer('Выбери из предложенных вариантов')
        return

@dp.message_handler(state = Wait.random_coffee_days_delta)
async def text(message: types.Message, state: FSMContext):
    print('RCDD', message.text)
    print(User.login)
    try:
        if int(message.text) < 0:
            await message.answer('Отправь положительное число')
            return
    except(TypeError, ValueError):
            await message.answer('Отправь положительное число')
            return
    
    await state.update_data(random_coffee_days_delta = int(message.text))
    datas = {
        "login": User.login,
        "telegram": User.telegram,
        "telegram_id": str(message.from_user.id),
        "random_coffee_days_delta": int(message.text)
    }
    print(datas)
    requests.post('http://127.0.0.1:8000/database/add_user_tg', json = datas)
    data = await state.get_data()
    d = list(data.values())
    print(d)

    await message.answer(f"Ты будешь получать Random Coffee раз в {int(message.text)} дней")
    # r = requests.get('http://127.0.0.1:8000/get_matches')
    # print(r.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1", "2"]
    keyboard.add(*buttons)

    await message.answer(main_text, reply_markup = keyboard)
    await Wait.menu_answer.set()

@dp.message_handler(state = Wait.menu_answer)
async def menu_answer(message: types.Message, state: FSMContext):
    if message.text == "1":
        datas = {
            'login': User.login
        }
        if requests.post('http://127.0.0.1:8000/database/get_user_for_tg', json = datas).json()['random_coffee_active'] == True:
            await message.answer('У тебя уже включена данная функция')
            return
        else:
            await enter_login()
    elif message.text == '2':
        return
    else:
        await message.answer('Выбери из предложенных вариантов')
        return

async def task():
    while True:
        print(1)
        r = requests.get('http://127.0.0.1:8000/get_matches').json()
        questions = requests.get('http://127.0.0.1:8000/get_questions').json()
        first = r[0][1]
        second = r[0][0]
        await bot.send_message(second["telegram_id"], f'Вот твой новый собеседник!\n\n@{second["telegram"]}\nИмя: {second["name"]}\nОбщага: {second["dormitory"]}\nОписание: {second["description"]}\n\nДержи темы для разговора\n{questions}')
        await bot.send_message(first["telegram_id"], f'Вот твой новый собеседник!\n\n@{first["telegram"]}\nИмя: {first["name"]}\nОбщага: {first["dormitory"]}\nОписание: {first["description"]}\n\nДержи темы для разговора\n{questions}')
        await asyncio.sleep(60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(task())

    executor.start_polling(dp, skip_updates=True)