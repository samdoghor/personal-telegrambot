# imports
import telebot
from flask import Flask

import config
from handlers.welcome import Re_welcome, Welcome
from models import User, db_setup

# configurations
bot = telebot.TeleBot(config.apiKey)
app = Flask(__name__)

# db.init_app(app)
db_setup(app)

# flask
@app.route('/')
def index():
    return "<p> Bot is running successfully </p>"

# bot
@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id, "Hello")
    username = message.chat.username
    user_name = User.query.filter_by(user_name=username).one()
    
    if user_name is not None:
        Re_welcome(message)
    else:
        Welcome(message)

# run
bot.infinity_polling()

# if __name__ == '__main__':
#   app.run()