import telebot

token = '5645737999:AAFguhZtbvmcqosgDV4zO_-Bhu26mI3dG38'

# мы создаем переменную bot, в которой будут содержаться те функции, которые нам нужны для обработки и ответа на
# сообщение
bot = telebot.TeleBot(token)

help = """
/add - добавить задачу в список;
/end - закончить выполнение программы;
/help - вывести список доступных команд;
/random - добавить случайную задачу на сегодня;
/show - показать список дел.
"""


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, help)


# функция polling начинает отправку запросов в телеграм с заданным токеном и спрашивает, нет ли для него сообщений.
# Если сообщение есть, то вызывается обработка. Long polling - процесс постоянного обращения к серверам
bot.polling(none_stop=True)

# contrl^C - остановка бота
