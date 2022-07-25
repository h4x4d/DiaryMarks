from aiogram import Bot
from aiogram.types import ParseMode

from db import config

bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
