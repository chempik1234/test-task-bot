# part of it was made by donBarbos https://github.com/donBarbos/telegram-bot-template
import asyncio
from datetime import datetime

import schedule
import structlog

from bot_functions.publish import publish_random_vacancy
from handlers import routers_list
from commands import router as commands_router
from init.bot import app, dp, bot
from init.config.init_config import channels_config
from init.services.init_1 import sender_service, init_sender_service

from middlewares.check_user_middleware import CheckUserMiddleware
from start_bot import start_bot

logger = structlog.get_logger('main')


async def run_background_sending():
    send = lambda ch: asyncio.create_task(publish_random_vacancy(None, ch))

    for channel in channels_config.all_channels():
        if not channel.publish_hours:
            continue

        for time_of_day in channel.publish_hours:
            schedule.every().day.at(time_of_day).do(send, channel)
        logger.info("set publishing of a channel", publish_hours=channel.publish_hours, channel=channel)

    while True:
        # logger.debug("pending background sending")
        schedule.run_pending()
        await asyncio.sleep(10)


async def on_startup() -> None:
    logger.info("bot startup beginning")

    asyncio.create_task(run_background_sending())

    dp.include_routers(commands_router, *routers_list)

    dp.message.outer_middleware(CheckUserMiddleware())
    dp.callback_query.outer_middleware(CheckUserMiddleware())

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
    # sender_service.set_dependency(init_sender_service(bot))

    await start_bot(bot, dp, app)


if __name__ == "__main__":
    asyncio.run(start())
