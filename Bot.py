help = """
add - добавить задачу в список;
end - закончить выполнение программы;
help - показать команды;
random - добавление случайной задачи на сегодня;
show - показать список дел.
"""
random_task = "cook"
tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]


run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(help)
    elif command == "show":
        date = input("Введите дату: ")
        if date in tasks:
            for task in tasks[date]:
                print("- ", task)
        else:
            print("Этот день свободен")
    elif command =="add":
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        add_todo(date, task)
        print("Задача добавлена")
    elif command == "random":
        add_todo("today", task)
        print("На сегодня есть одна случайная задача!")
    elif command == "end":
        break
    else:
        print("Неизвестная команда")
print("Завершение работы")




