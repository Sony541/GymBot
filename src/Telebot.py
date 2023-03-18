import json
import random
import telebot

from Config import token
from Database import read_help_from_file, read_tasks_from_file, add_exercise

bot = telebot.TeleBot(token)

HELP = read_help_from_file()
TASKS = read_tasks_from_file()

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for row in TASKS:
        keyboard.row(
            telebot.types.InlineKeyboardButton(row, callback_data=f"add-{row}")
        )

    bot.send_message(message.chat.id, "Select the exercise:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('add-'):
        get_add_callback(query)
    if data.startswith('write-'):
        get_write_callback(query)

def get_add_callback(query):
    bot.answer_callback_query(query.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    task_name = query.data.replace('add-', "")
    mult = TASKS[task_name] # Multiplier per task
    for i in range(1, 10):
        base = mult * i
        keyboard.row(
            telebot.types.InlineKeyboardButton(base, callback_data=f"write-{task_name}-{base}"),
            telebot.types.InlineKeyboardButton(base + 1*mult, callback_data=f"write-{task_name}-{base+1*mult}"),
            telebot.types.InlineKeyboardButton(base + 2*mult, callback_data=f"write-{task_name}-{base+2*mult}")
        )

    bot.send_message(query.message.chat.id, "Select the weight/count:", reply_markup=keyboard)

def get_write_callback(query):
    _, task, weight = query.data.split("-", maxsplit=2)
    add_exercise(task, weight)
    bot.send_message(query.message.chat.id, query.data)

bot.polling(none_stop=True)
