import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, Message, \
    InputTextMessageContent, InlineQueryResultArticle

API_TOKEN = os.environ['TELEGRAM_API_KEY']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi! I'm a lunch bot that Incora using.\n\n"
        "If you want to order food please type /set_lunch, "
        "your full name as in the lunch spreadsheet and time "
        "where you want to get a reminder to automatically order "
        "your best lunch to next day ;)\n\n"
        "Do like this: '/set_lunch Yura Dyachuk 22:00'"      
    )

@dp.message_handler(regexp='(^spaceman[s]?$|puss)')
async def cats(message: Message):
    with open('./spaceman.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Your spaceman')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
