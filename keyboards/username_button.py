# imports
from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def Username():
    markup = ReplyKeyboardMarkup()
    markup.width = 2
    markup.resize_keyboard = True
    btn1 = KeyboardButton("Name")

    markup.add(btn1)
    return markup