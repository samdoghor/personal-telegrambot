# imports
import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import apiKey

# configurations
bot=AsyncTeleBot(apiKey)

# bot app
@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, "Howdy, how are you doing?")

# run
asyncio.run(bot.infinity_polling())