from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

from init.config.init_config import bot_config

bot = Bot(token=bot_config.API_TOKEN, default=DefaultBotProperties(parse_mode='Markdown'))
app = web.Application()


def create_dp() -> Dispatcher:
    return Dispatcher(storage=MemoryStorage())


dp = create_dp()
