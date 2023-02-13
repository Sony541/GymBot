help = """
add - добавить задачу в список;
help - показать команды;
show - показать список дел.
"""

tasks = []

command = input("Введите команду: ")
if command == "help":
    print(help)
elif command == "show":
    print(tasks)
elif command =="add":
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена")
else:
    print("Неизвестная команда")