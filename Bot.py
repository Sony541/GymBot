help = """
add - добавить задачу в список;
help - показать команды;
show - показать список дел
end - закончить выполнение программы.
"""

tasks = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(help)
    elif command == "show":
        print(tasks)
    elif command =="add":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена")
    elif command == "end":
        break
    else:
        print("Неизвестная команда")
print("Завершение работы")
