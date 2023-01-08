import telebot
from config import token

HELP = """
/help /h - список доступных команд
/todo /add [date] [task] - добавить задачу(task) на дату(date)
/show_all /sa - показать все задачи
/show [date] - показать список задач на дату(date) или все(all)
"""

today = "сегодня"
tomorrow = "завтра"

tasks = {
    today: [],
    tomorrow: []
    }

bot = telebot.TeleBot(token)

"""************************************************"""
"""************************************************"""

def date_converter(date):
    if date == "today":
        date = today
    elif date == "tomorrow":
        date = tomorrow
    return date

def add_task(date, task, message):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    bot.send_message(message.chat.id, "Задача добавлена")

def show_tasks_for_date(date, message):
    date = date_converter(date)
    if date in tasks and tasks[date]:
        text = f"{date.upper()}:\n"
        for string in tasks[date]:
            text += f"[] {string}\n"
    else:
        text = "Задач на указанную дату нет"
    bot.send_message(message.chat.id, text)

def show_all_tasks(message):
    for date, task in tasks.items():
        text = f"{date.upper()}:\n"
        for string in task:
            text += f"[] {string}\n"
        bot.send_message(message.chat.id, text)

def is_command_show_all(text):
    if (text == "all" or text == "sa" or text == "все"
        or text == "всё" or text == "всех"):
        return True
    return False

"""************************************************"""
"""************************************************"""

@bot.message_handler(commands=["help", "h"])
def help(message):
    bot.send_message(message.chat.id, HELP)
    print(message.chat.id)                        #  ВРЕМЕННО

@bot.message_handler(commands=["todo", "add"])
def todo(message):
    try:
        command = message.text.split(maxsplit=2)
        date = command[1].lower()
        date = date_converter(date)
        task = command[2]
        add_task(date, task, message)
    except:
        bot.send_message(message.chat.id, "Введите дату и задачу: ")

@bot.message_handler(commands=["show_all", "sa"])
def show_all(message):
    show_all_tasks(message)

@bot.message_handler(commands=["show"])
def show(message):
    try:
        date = message.text.split()[1].lower()
        show_tasks_for_date(date, message)
    except:
        bot.send_message(message.chat.id, "Введите дату: ")

@bot.message_handler(content_types=["text"])
def text_without_command(message):
    command = message.text.split(maxsplit=1)
    if len(command) == 1:
        date = command[0].lower()
        if is_command_show_all(date):
            show_all_tasks(message)
        else:
            show_tasks_for_date(date, message)
    else:
        date = command[0].lower()
        date = date_converter(date)
        task = command[1]
        add_task(date, task, message)

bot.polling(none_stop=True)
















