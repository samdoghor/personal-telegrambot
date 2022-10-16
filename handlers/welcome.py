# imports
import telebot

from keyboards.username_button import Username
from models.user import User


# welcome
def Welcome(message, bot):
    displayname = message.chat.username
    bot.send_message(
        message.chat.id, 
        '''
Hello, my friend with Telegram username({}).

My name is Samuel, Doghor Destiny. I will like to know your name as well.

Tap on the <b>Name</b> button below to tell me your name.

'''.format(displayname), parse_mode='HTML', reply_markup = Username())

def Re_welcome(message, bot):
    user_id = message.chat.id
    filtering = User.query.filter_by(user_id=user_id).one()
    displayname = filtering.user_name
    bot.send_message(
        message.chat.id, 
        '''
Hello, {}.

Welcome back. How may I help today?

'''.format(displayname), parse_mode='HTML')