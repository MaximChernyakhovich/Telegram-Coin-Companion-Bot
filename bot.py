import telebot
from telebot import types
from user import User
from operations import Operations
from icecream import ic
import time

class BotHandler:
    def __init__(self, api_token_key):
        self.bot = telebot.TeleBot(api_token_key)
        self.user_instance = None
        self.operations_instance = None

    def start(self, message):
        chat_id = message.chat.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        self.bot.send_message(message.chat.id, f'Добрый день, {first_name}!')
        self.user_instance = User(tg_id=chat_id, firstname=first_name, lastname=last_name, tg_nick=username)
        user_data = self.user_instance.fetch_user()
        ic(user_data)

    def get_expense(self, message, user_data):
        user_data['expense'] = message.text
        self.bot.send_message(message.chat.id, f" {user_data['expense']}! ")

    def get_refill(self, message, user_data):
        user_data['refill'] = message.text
        self.bot.send_message(message.chat.id, f" {user_data['refill']}! ")

    def get_categories(self, message, user_data):
        user_data['categories'] = message.text
        self.bot.send_message(message.chat.id, f" {user_data['categories']}! ")

    def add_expense(self, message):
        self.bot.send_message(message.chat.id, 'Введите расход:')
        user_data = {}
        self.bot.register_next_step_handler(message, lambda msg: self.get_expense(msg, user_data))

    def add_refill(self, message):
        self.bot.send_message(message.chat.id, 'Введите пополнение:')
        user_data = {}
        self.bot.register_next_step_handler(message, lambda msg: self.get_refill(msg, user_data))

    def add_categories(self, message):
        self.bot.send_message(message.chat.id, 'Введите список категорий через запятую:')
        user_data = {}
        self.bot.register_next_step_handler(message, lambda msg: self.get_categories(msg, user_data))

    def polling(self):
        while True:
            try:
                self.bot.polling(none_stop=True, interval=4)
            except:
                print('restart')
                time.sleep(2)


api_token_key = "TELEGRAM_API_KEY"
bot_handler = BotHandler(api_token_key)

@bot_handler.bot.message_handler(commands=['start'])
def start(message):
    bot_handler.start(message)

@bot_handler.bot.message_handler(commands=['add_expense'])
def add_expense(message):
    bot_handler.add_expense(message)

@bot_handler.bot.message_handler(commands=['add_refill'])
def add_refill(message):
    bot_handler.add_refill(message)

@bot_handler.bot.message_handler(commands=['add_categories'])
def add_categories(message):
    bot_handler.add_categories(message)

bot_handler.polling()