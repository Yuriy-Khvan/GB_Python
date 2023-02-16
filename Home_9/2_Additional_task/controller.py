import telebot
from telebot import types
import spy
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

bot = telebot.TeleBot("5910383561:AAEfsJzRilsWr_tiIn7aSXns0HTB9-xZ9s4")

@bot.message_handler(commands = ["start"])
def start(message):
    spy.log(message)
    bot.send_message(message.chat.id,"/button")
    
@bot.message_handler(commands = ["button"])
def button(message):
    spy.log(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=None)
    but1 = types.KeyboardButton("рациональные")
    but2 = types.KeyboardButton("комплексные")

    markup.add(but1)
    markup.add(but2)
   
    bot.send_message(message.chat.id,"Выбери ниже",reply_markup=markup)

@bot.message_handler(content_types = "text")
def controller(message):
    spy.log(message)
    print(message.text)
    if message.text == "рациональные":
        bot.send_message(message.chat.id,"введи пример через пробелы (например 2 + 3)")
        bot.register_next_step_handler(message,rats)
    if message.text == "комплексные":
        bot.send_message(message.chat.id,"введи пример через пробелы (например 1j + 3j)")
        bot.register_next_step_handler(message,compl)

def rats(message):
    # spy.log(message)
    a = message.text.split()
    if a[1] == '+':
        result = int(a[0]) + int(a[2])
    elif a[1] == '-':
        result = int(a[0]) - int(a[2])
    elif a[1] == '*':
        result = int(a[0]) * int(a[2])
    elif a[1] == '/':
        result = int(a[0]) / int(a[2])
    elif a[1] == '//':
        result = int(a[0]) // int(a[2])
    elif a[1] == '%':
        result = int(a[0]) % int(a[2])
    bot.send_message(message.chat.id,f"{message.text} = {result}")
    button(message)

def compl(message):
    # spy.log(message)
    a = message.text.split()
    if a[1] == '+':
        result = complex(a[0]) + complex(a[2])
    elif a[1] == '-':
        result = complex(a[0]) - complex(a[2])
    elif a[1] == '*':
        result = complex(a[0]) * complex(a[2])
    elif a[1] == '/':
        result = complex(a[0]) / complex(a[2])
    bot.send_message(message.chat.id,f"{message.text} = {result}")
    button(message)

    
bot.infinity_polling()