import random
import json
import telebot

token = '5645737999:AAFguhZtbvmcqosgDV4zO_-Bhu26mI3dG38'

# мы создаем переменную bot, в которой будут содержаться те функции, которые нам нужны для обработки и ответа на
# сообщение
bot = telebot.TeleBot(token)

HELP = """
/add - добавить задачу в список;
/end - закончить выполнение программы;
/help - вывести список доступных команд;
/random - добавить случайную задачу на сегодня;
/show - показать список дел.
"""

with open("Help.json", "w")as f:
    json.dump(HELP, f, indent=4)

with open("Help.json")as f:
    HELP = json.load(f)

tasks = {}

random_tasks = ["sport", "grocery", "playing piano", "study"]


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " на " + date + " добавлена!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "cегодня"
    task = random.choice(random_tasks)
    add_todo(date, task)
    text = "На сегодня появилась задача " + task + "!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show_commands(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"  # \n - перевод строки
    else:
        text = "День свободен"
    bot.send_message(message.chat.id, text)


# функция polling начинает отправку запросов в телеграм с заданным токеном и спрашивает, нет ли для него сообщений.
# Если сообщение есть, то вызывается обработка. Long polling - процесс постоянного обращения к серверам
bot.polling(none_stop=True)

# contrl^C - остановка бота
