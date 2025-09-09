# part of it was made by donBarbos https://github.com/donBarbos/telegram-bot-template
import asyncio
import sched
import time

import schedule
import structlog

from bot_functions.publish import publish_random_vacancy
from handlers import routers_list
from commands import router as commands_router
from init.bot import app, dp, bot
from init.config.init_config import channels_config

# from middlewares.check_user_middleware import CheckUserMiddleware
from start_bot import start_bot

logger = structlog.get_logger('main')


async def on_startup() -> None:
    logger.info("bot startup beginning")

    for channel in channels_config.all_channels():
        for time_of_day in channel.publish_hours:
            schedule.every().day.at(time_of_day).do(publish_random_vacancy, None, channel)
        logger.info("set publishing of a channel", publish_hours=channel.publish_hours)

    dp.include_routers(commands_router, *routers_list)

    # dp.message.outer_middleware(CheckUserMiddleware())
    # dp.callback_query.outer_middleware(CheckUserMiddleware())

    logger.info("bot startup configured")


async def on_shutdown() -> None:
    logger.info("bot shutdown")
    await bot.delete_webhook()
    await bot.session.close()


async def start():
    # global postgres_conn, users_service, category_service, reloader_service

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    logger.info("starting bot")

    # postgres_conn.set_dependency(init_postgres_conn())
    # vacancy_service.set_dependency(init_vacancy_service(postgres_conn))

    await start_bot(bot, dp, app)


if __name__ == "__main__":
    asyncio.run(start())
