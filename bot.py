import telebot
from telebot import types
import time
from user import User
from icecream import ic

bot = telebot.TeleBot("API_TOKEN_KEY")

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    bot.send_message(message.chat.id, f'Добрый день, {first_name}!')
    
    user = User(tg_id=chat_id, firstname=first_name, lastname=last_name, tg_nick=username)
    user_data = user.fetch_user()
    print(user_data)

while True:
    try:
        bot.polling(none_stop=True, interval=4)
    except:
        print('restart')
        time.sleep(2)