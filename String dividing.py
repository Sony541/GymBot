command = "/add 31 feb текст задачи"

# Для строк есть специальная функция split()
splitted_command = command.split(maxsplit=2)
print(splitted_command)

date = splitted_command[1]
task = splitted_command[2]
print(date, task)