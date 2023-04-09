from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('5255444441:AAFX2xVwHC5yG4TB9fGEN7bn2H6Fi8YDoO8')


async def send_to_channel(msg = ''):
    await bot.send_message(-1001924459497, msg)
    await bot.close_session()
