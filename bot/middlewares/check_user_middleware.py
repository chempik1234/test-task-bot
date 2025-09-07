import inspect

import structlog

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from init.config.init_config import bot_config

logger = structlog.get_logger(name="check_user_middleware")


class CheckUserMiddleware(BaseMiddleware):
    async def __call__(self, handler: Message | CallbackQuery, event, data):
        user_id, passed, created_new_user = None, True, False
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id

        if user_id:
            if not str(user_id) in bot_config.BOT_ADMIN_USERS:
                return

        result = await handler(event, data)
        return result
