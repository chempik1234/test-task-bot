from db.utils import get_asyncpg_url
from init.config import bot_config

postgres_url = get_asyncpg_url(
    bot_config.POSTGRES_USER,
    bot_config.POSTGRES_PASSWORD,
    bot_config.POSTGRES_HOST,
    bot_config.POSTGRES_PORT,
    bot_config.POSTGRES_DB,
)
# postgres_url_alembic = (postgres_url.replace("+asyncpg", "").
#                         replace(f"@{bot_config.POSTGRES_HOST}", "@localhost"))
