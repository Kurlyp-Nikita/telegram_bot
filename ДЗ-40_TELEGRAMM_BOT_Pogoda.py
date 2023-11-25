# 6526265827:AAE67IBOXJ8-xHVbIlrhhRjgFGFL8kvA5BI
# https://t.me/babrians_bot

# API = 'b5acdd7f46dc29237cec9d8e615405b3'


import telebot
from telebot import types
import random
import requests




with open('films.txt', 'r', encoding='utf-8') as file:
    films = file.readlines()
    films = [i.strip() for i in films]

with open('anecdots.txt', 'r', encoding='utf-8') as file:
    anecdots = file.read()
    random_anecdots = anecdots.split('#')

bot = telebot.TeleBot('6600729605:AAG_sVKVe2B8ivd4a9HwjJiZhUs6KT-nLN8')
bot.send_message(1896507321, 'Hello !')
gifka = 'CgACAgIAAxkBAAMlZPRq6P71uSN9Ii3eZLW4SVwuXMoAArESAAIa1VhIXGDaumITcl8wBA'
smile = b'\xf0\x9f\x98\x83'
dog = 'CgACAgQAAxkBAANaZPR4p57or3d2mNBdBd_QDv3emw4AAnUDAAIgcNVR7edAbmZIqmIwBA'
hamster = 'CgACAgQAAxkBAANgZPR51u_wgVH36kJSHbrZr6LcaG8AAooCAAKj4AxTJvYNuqYrn-YwBA'
symbol_1 = b'\xf0\x9f\x98\x8e'
symbol_2 = b'\xf0\x9f\x98\xa2'

line = 'CgACAgQAAxkBAAIEMWT43aHI0WyND9j1XAABlV0E2ZlHxwACXQMAArJSzVPGrBuX4GByQjAE'
hel = 'CgACAgQAAxkBAAIEOmT43x-anz9rxMH7mRmuiykcO1AjAAI0AwACBSN1UIv4HDezs4kbMAQ'

# jungle = 'CgACAgQAAxkBAAIDmWT4yR3Cw_YwPrweetzVapAbNRecAALLAgACIwQMUyzZSRgUJd_qMAQ'
# egypt = 'CgACAgQAAxkBAAIDm2T4yYhI_cIyDMUyrao6PpNHrns0AAIwAwAC2Ns9Uz9o09vaX7AKMAQ'
# underwater_world = 'CgACAgQAAxkBAAIDnWT4ygABw7mtReI3nzjbRiBN0Hp6YgACQAQAAjTo3VLKV0s47fV5HzAE'

location = ''


@bot.message_handler(commands=['start', 'help'])
def key(info):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buton_name = types.KeyboardButton('как тебя зовут?')
    buton_time = types.KeyboardButton('сколько времени?')
    buton_adventures = types.KeyboardButton('приключения')
    buton_films = types.KeyboardButton('фильм')
    buton_anecdots = types.KeyboardButton('анекдот')
    button_weather = types.KeyboardButton('погода на сегодня')
    button_weather_5d = types.KeyboardButton('погода на будни')
    buton_1 = types.KeyboardButton('Привет')
    buton_2 = types.KeyboardButton('кинь кубик')
    buton_dog = types.KeyboardButton('покажи собаку')
    buton_cat = types.KeyboardButton('покажи кота')
    buton_hamster = types.KeyboardButton('покажи хомяка')
    buton_symbol_1 = types.KeyboardButton(')')
    buton_symbol_2 = types.KeyboardButton('(')
    kb.add(buton_1, buton_2, buton_dog, buton_cat, buton_hamster, buton_symbol_1, buton_symbol_2,
           buton_films, buton_anecdots, button_weather, button_weather_5d, buton_name, buton_time, buton_adventures)
    bot.send_message(info.chat.id, 'нажми на кнопку!', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'приключения')
def adventures(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_jungle = types.KeyboardButton('джунгли')
    button_egypt = types.KeyboardButton('египет')
    button_underwater_world = types.KeyboardButton('подводный мир')
    kb.add(button_jungle, button_egypt, button_underwater_world)
    bot.send_message(message.chat.id, 'Куда пойдем?', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'джунгли')
def jungle(message):
    global location
    location = 'j'
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    forward = types.KeyboardButton('вперёд')
    left = types.KeyboardButton('на лево')
    right = types.KeyboardButton('на право')
    kb.add(forward, left, right)
    bot.send_message(message.chat.id, 'Выбирай направление!', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'египет')
def egypt(message):
    global location
    location = 'e'
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    forward = types.KeyboardButton('вперёд')
    left = types.KeyboardButton('на лево')
    right = types.KeyboardButton('на право')
    kb.add(forward, left, right)
    bot.send_message(message.chat.id, 'Выбирай направление!', reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == 'подводный мир')
def underwater_world(message):
    global location
    location = 'u'
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    forward = types.KeyboardButton('вперёд')
    left = types.KeyboardButton('на лево')
    right = types.KeyboardButton('на право')
    kb.add(forward, left, right)
    bot.send_message(message.chat.id, 'Выбирай направление!', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def message(info):
    print(info)
    name = info.from_user.first_name
    info.text = info.text.lower()
    code = info.text.encode('utf-8')

    print(code)

    if 'привет' in info.text:
        bot.send_message(info.chat.id, 'hello ' + name)
    elif 'как тебя зовут?' in info.text:
        bot.send_message(info.chat.id, 'Меня зовут Den !')
    elif 'сколько времени?' in info.text:
        bot.send_message(info.chat.id, 'Посмотри в телефоне ну или на компьюторе')
    elif 'как дела?' in info.text:
        bot.send_message(info.chat.id, 'У меня всё хорошо, у вас как?')
    elif 'у меня тоже всё хорошо!' in info.text:
        bot.send_message(info.chat.id, 'И это отлично!')
    elif 'пришли гифку' in info.text:
        bot.send_animation(info.chat.id, gifka)
    elif 'пришли смайлик' in info.text:
        bot.send_message(info.chat.id, smile)
    elif 'кинь кубик' in info.text:
        cube = random.randint(1, 6)
        bot.send_message(info.chat.id, f'выпало число {cube}')
    elif 'покажи собаку' in info.text:
        bot.send_animation(info.chat.id, dog)
    elif 'покажи кота' in info.text:
        bot.send_animation(info.chat.id, 'CgACAgQAAxkBAAIJtWT87f0Pf7HPPopqKRFJKsJh6DziAAKFAwAC5cqUUFpaMulasYCHMAQ')
    elif 'покажи хомяка' in info.text:
        bot.send_animation(info.chat.id, hamster)
    elif ')' in info.text:
        bot.send_message(info.chat.id, symbol_1)
    elif '(' in info.text:
        bot.send_message(info.chat.id, symbol_2)
    elif 'фильм' in info.text:
        bot.send_message(info.chat.id, random.choice(films))
    elif 'анекдот' in info.text:
        bot.send_message(info.chat.id, random.choice(random_anecdots))

    elif 'погода на сегодня' in info.text:

        url = 'https://api.openweathermap.org/data/2.5/weather'
        key = 'b5acdd7f46dc29237cec9d8e615405b3'

        params = {
            'id': 500096,
            'appid': key,
            'lang': 'ru',
            'units': 'metric'
        }

        result = requests.get(url, params=params, timeout=20)
        data = result.json()

        k1 = data["name"]
        k2 = data["main"]["temp"]
        k3 = data["wind"]["speed"]
        k4 = data["weather"][0]["description"]

        bot.send_message(info.chat.id, f'Вот тебе погода на сегодня: в {k1}, Температура: {round(k2, 0)}°C {k4}, Ветер: {k3} м/с')

    elif 'погода на будни' in info.text:

        url = 'https://api.openweathermap.org/data/2.5/forecast'
        key = 'b5acdd7f46dc29237cec9d8e615405b3'

        params = {
            'id': 500096,
            'appid': key,
            'lang': 'ru',
            'units': 'metric'
        }

        result = requests.get(url, params=params, timeout=10)
        data = result.json()

        for one in data['list']:
            if '15:00' in one['dt_txt']:
                bot.send_message(info.chat.id, f'{one["dt_txt"]}, {one["main"]["temp"]}°C, {one["weather"][0]["description"]}')

    elif 'пока' in info.text:
        bot.send_message(info.chat.id, 'by ma brother!')
    elif location == 'j':
        if info.text == 'вперёд':
            bot.send_animation(info.chat.id, 'CgACAgQAAxkBAAIJBmT86rcFZE7l1BP49p_miI_Jsyg1AALLAgACIwQMUyzZSRgUJd_qMAQ')
            bot.send_message(info.chat.id, 'Ура вы пришли в Джунгли!')
        elif info.text == 'на лево':
            bot.send_animation(info.chat.id, line)
        elif info.text == 'на право':
            bot.send_animation(info.chat.id, hel)
    elif location == 'e':
        if info.text == 'вперёд':
            bot.send_animation(info.chat.id, line)
        elif info.text == 'на лево':
            bot.send_animation(info.chat.id, 'CgACAgQAAxkBAAIDm2T4yYhI_cIyDMUyrao6PpNHrns0AAIwAwAC2Ns9Uz9o09vaX7AKMAQ')
            bot.send_message(info.chat.id, 'Ура вы пришли в Египет!')
        elif info.text == 'на право':
            bot.send_animation(info.chat.id, hel)
    elif location == 'u':
        if info.text == 'вперёд':
            bot.send_animation(info.chat.id, 'CgACAgQAAxkBAAII_2T86iM3YxmOzzMnhl5zarjD7J2qAAJABAACNOjdUspXSzjt9XkfMAQ')
            bot.send_message(info.chat.id, 'Ура вы пришли в Подводный мир!')
        elif info.text == 'на лево':
            bot.send_animation(info.chat.id, hel)
        elif info.text == 'на право':
            bot.send_animation(info.chat.id, line)
    else:
        bot.send_message(info.chat.id, 'пишешь не то')

@bot.message_handler(content_types=['animation'])
def masseg(info):
    print(info.document.file_id)
    bot.send_message(info.chat.id, 'гифка')


@bot.message_handler(content_types=['photo'])
def masseg(info):
    print(info.photo[0].file_id)
    bot.send_message(info.chat.id, 'картинка')


bot.polling(none_stop=True)
