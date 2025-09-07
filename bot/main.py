# part of it was made by donBarbos https://github.com/donBarbos/telegram-bot-template
import asyncio

import structlog

from handlers import routers_list
from commands import router as commands_router
from init.bot import app, dp, bot

from middlewares.check_user_middleware import CheckUserMiddleware
from start_bot import start_bot

logger = structlog.get_logger('main')


async def on_startup() -> None:
    logger.info("bot startup beginning")

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

    await start_bot(bot, dp, app)


if __name__ == "__main__":
    asyncio.run(start())
