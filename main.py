#--------------------------------------------------#
# IMPORTS
#--------------------------------------------------#
import asyncio
import os
from dotenv import load_dotenv
import telebot

#--------------------------------------------------#
# CONFIGURATIONS
#--------------------------------------------------#
load_dotenv()
apiKey=os.getenv('api_key')
bot=telebot.TeleBot(apiKey)

#--------------------------------------------------#
# APPLICATION
#--------------------------------------------------#
@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, "Howdy, how are you doing?")

asyncio.run(bot.infinity_polling())