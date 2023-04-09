from telebot.async_telebot import AsyncTeleBot
from app.settings import settings


bot = AsyncTeleBot(settings.bot_token)


async def send_to_channel(msg = ''):
    await bot.send_message(-1001924459497, msg)
    await bot.close_session()
