# imports
import os
import telebot
from dotenv import load_dotenv

# configurations
load_dotenv()
apiKey = os.getenv('api_key')
bot=telebot.TeleBot(apiKey)

# bot app
@bot.message_handler(commands=['start'])
def welcome_message(message):
    username = message.chat.username
    bot.send_message(message.chat.id, 'Hello, {}, my name is Samuel, Doghor, How may I help you?'.format(username))

# run
bot.infinity_polling()