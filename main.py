help = "help"
todo = "todo"
show_all = "show all"
show = "show"
exit = "exit"

today = "сегодня"
tomorrow = "завтра"

HELP = f"""
{help} - показать список доступных команд
{todo} - добавить задачу в список дел
{show_all} - показать весь список задач
{show} - показать список задач на конкретную дату
{exit} - завершение работы
"""

tasks = {
    today: ["отжиматься", "приседать"],
    tomorrow: ["бегать", "прыгать"],
    "31.12": ["отдыхать"]
    }

def date_converter(date):
    if date == "today":
        return today
    elif date == "tomorrow":
        return tomorrow
    return date

while True:
    command = input("Введите команду: ")

    if command == help:
        print(HELP)
    elif command == show_all:
        for date, task in tasks.items():
            print(f"{date}: ", end="")
            print(*task, sep=", ")
    elif command == show:
        date = input("Введите дату: ").lower()
        date = date_converter(date)
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print("Такой даты нет.")
    elif command == todo:
        date = input("Введите срок выполнения: ").lower()
        task = input("Введите задачу: ")
        date = date_converter(date)
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]
        print("Задача добавлена.")
    elif command == exit:
        print("Программа завершена.")
        break
    else:
        print("Неизвестная команда.")
        print(HELP)

