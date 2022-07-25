from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode

from db import config

from beautify import start_alert

from bot_create import bot


def setup():
    import handlers
    from data import db_session

    handlers.errors.setup(dp)
    handlers.user.setup(dp)

    db_session.global_init("db/data.sqlite")


if __name__ == '__main__':

    dp = Dispatcher(bot)
    setup()

    start_alert()

    executor.start_polling(dp)
