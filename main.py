import telebot
from config import token

HELP = """
/help - список доступных команд
/todo /add [date] [task] - добавить задачу(task) на дату(date)
/show_all - показать все задачи
/show [date] - показать список задач на дату(date)
"""

today = "сегодня"
tomorrow = "завтра"

tasks = {
    today: [],
    tomorrow: []
    }
bot = telebot.TeleBot(token)

def date_converter(date):
    if date == "today":
        date = today
    elif date == "tomorrow":
        date = tomorrow
    return date

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["todo", "add"])
def todo(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    date = date_converter(date)
    task = command[2]
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    bot.send_message(message.chat.id, "Задача добавлена")

@bot.message_handler(commands=["show_all"])
def show_all(message):
    for date, task in tasks.items():
        text = f"{date.upper()}:\n"
        for string in task:
            text += f"[] {string}\n"
        bot.send_message(message.chat.id, text)
    print(tasks)                            #  ВРЕМЕННО

@bot.message_handler(commands=["show"])
def show(message):
    date = message.text.split()[1].lower()
    date = date_converter(date)
    if date in tasks and tasks[date]:
        text = f"{date.upper()}:\n"
        for string in tasks[date]:
            text += f"[] {string}\n"
    else:
        text = "Задач на указанную дату нет"
    bot.send_message(message.chat.id, text)
    

bot.polling(none_stop=True)
















