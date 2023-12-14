import telebot
from telebot import types
import time
from user import User
from icecream import ic

bot = telebot.TeleBot("API_TOKEN_KEY")

def get_expense(message):
    new_user_data = {'expense': message.text}
    bot.send_message(message.chat.id, f" {new_user_data['expense']}! ")

def get_refill(message):
    new_user_data = {'refill': message.text}
    bot.send_message(message.chat.id, f" {new_user_data['refill']}! ")

def get_categories(message):
    new_user_data = {'categories': message.text}
    bot.send_message(message.chat.id, f" {new_user_data['categories']}! ")

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    bot.send_message(message.chat.id, f'Добрый день, {first_name}!')
    user = User(tg_id=chat_id, firstname=first_name, lastname=last_name, tg_nick=username)
    user_data = user.fetch_user()
    ic(user_data)

@bot.message_handler(commands=['add_expense'])
def add_expense(message):
    bot.send_message(message.chat.id, f'Введите расход:э')
    user_data = {}
    bot.register_next_step_handler(message, lambda msg: get_expense(msg, user_data))

@bot.message_handler(commands=['add_refill'])
def add_refill(message):
    bot.send_message(message.chat.id, f'Введите пополнение:')
    user_data = {}
    bot.register_next_step_handler(message, lambda msg: get_refill(msg, user_data))

@bot.message_handler(commands=['add_categories'])
def add_categories(message):
    bot.send_message(message.chat.id, f'Введите список категорий через запятую:')
    user_data = {}
    bot.register_next_step_handler(message, lambda msg: get_categories(msg, user_data))

while True:
    try:
        bot.polling(none_stop=True, interval=4)
    except:
        print('restart')
        time.sleep(2)