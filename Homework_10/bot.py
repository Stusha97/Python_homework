import telebot 
from calculator import *
from consts import TOKEN
from log import *
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def welcome_handler (message):
    bot.send_message(message.chat.id,f'Привет,{message.from_user.first_name}!\n Это бот-калькулятор\n Для рациональных чисел введи команду: /calc\n Для комплексных чисел введи: /complex')

@bot.message_handler(commands=['calc'])
def welcome_handler (message):
    text = "Введите выражение в строку через пробел, например 2 + 3"
    bot.reply_to (message,text)
    bot.register_next_step_handler(message,calculate)

@bot.message_handler(commands=['complex'])
def welcome_handler (message):
    text = "Введите выражение в строку через пробел, например 2 + 3j - 5 + 7j"
    bot.reply_to (message,text)
    bot.register_next_step_handler(message,calc_complex)

def calculate(message):
    expression = message.text
    some_list = expression.split(' ')
    a = int(some_list[0])
    operation = some_list[1]
    b = int(some_list[2])

    if operation == "+":
        result = summary(a,b)
    elif operation == "-":
        result = difference(a,b)
    elif operation == "/":
        result = division(a,b)
    elif operation == "*":
        result = mult(a,b)
    elif not result:
        bot.send_message(message.from_user.id, "Произошла ошибка")
        return 
    write(expression,result)
    bot.send_message(message.chat.id,str(result))


def calc_complex(message):
    expression = message.text
    some_list = expression.split(' ')
    a1 = some_list[0]
    a2 = ''.join(some_list[1:3])[:-1]
    b1 = some_list[4]
    b2 = ''.join(some_list[5:])[:-1]
    operation = some_list[3]
    a = complex (int(a1),int(a2))
    b = complex (int(b1),int(b2))

    if operation == "+":
        result = summary(a,b)
    elif operation == "-":
        result = difference(a,b)
    elif operation == "/":
        result = division(a,b)
    elif operation == "*":
        result = mult(a,b)
    elif not result:
        bot.send_message(message.from_user.id, "Произошла ошибка")
        return 
    write(expression,result)
    bot.send_message(message.chat.id,str(result))
