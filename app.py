import logging

from aiogram import executor, types
import handlers
from data.config import *
from loader import dp



async def on_startup(dp):
    logging.info("Bot started")
    await dp.bot.set_my_commands(
    [
        types.BotCommand(command="/start", description="Start bot"),
        types.BotCommand(command="/rate", description="Get currency rates")
    ]
    )
    await dp.bot.send_message(ADMINS[0], "Bot started")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
