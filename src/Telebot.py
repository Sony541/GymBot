import json
import random
import telebot

from Config import TOKEN
from Database import read_help_from_file, read_tasks_from_file, add_exercise, load_exercise, log

bot = telebot.TeleBot(TOKEN)

HELP = read_help_from_file()
TASKS = read_tasks_from_file()

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['get'])
def get_command(message):
    make_tasks_keyboard(message, "get")

@bot.message_handler(commands=['add'])
def add_command(message):
    make_tasks_keyboard(message, "add")

def make_tasks_keyboard(message, kb_type):
    keyboard = telebot.types.InlineKeyboardMarkup()

    if TASKS is None:
        bot.send_message(message.chat.id, "The task list is empty. Use /create command to create new tasks")
        return
    
    for row in TASKS:
        keyboard.row(
            telebot.types.InlineKeyboardButton(row, callback_data=f"{kb_type}-{row}")
        )
    bot.send_message(message.chat.id, "Select the exercise:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('add-'):
        get_add_callback(query)
    if data.startswith('write-'):
        get_write_callback(query)
    if data.startswith('get-'):
        get_get_callback(query)

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
    add_exercise(task, weight, query.from_user.id)
    bot.send_message(query.message.chat.id, query.data)

def get_get_callback(query):
    _, task = query.data.split("-", maxsplit=1)
    log(str(query))
    bot.send_message(query.message.chat.id, load_exercise(task, query.from_user.id))

bot.polling(none_stop=True)
