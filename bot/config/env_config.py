from typing import List

from betterconf import Config
from betterconf.caster import IntCaster, BoolCaster, AbstractCaster, ListCaster
from betterconf.config import Field


class BotConfig(Config):
    API_TOKEN: str = Field("API_TOKEN")
    WEBHOOK_SECRET: str = Field("WEBHOOK_SECRET", default="1234")

    CONFIG_MOUNT_DIR: str = Field("CONFIG_MOUNT_DIR", default="/etc/app")

    # region postgres conf
    POSTGRES_DB: str = Field("POSTGRES_DB")
    POSTGRES_HOST: str = Field("POSTGRES_HOST", default="db")
    POSTGRES_USER: str = Field("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = Field("POSTGRES_PASSWORD")
    POSTGRES_PORT: int = Field("POSTGRES_PORT", default="5432")
    # endregion

    BOT_DEBUG: bool = Field("BOT_DEBUG", default=False, caster=BoolCaster())
    BOT_ADMIN_USER_IDS: List[str] = Field("BOT_ADMIN_USER_IDS", default=[], caster=ListCaster())
    BOT_SECRET_KEY_ON_LOGIN: str = Field("BOT_SECRET_KEY_ON_LOGIN")
    BOT_WEBHOOK_HOST: str = Field("BOT_WEBHOOK_HOST", default="0.0.0.0")
    BOT_WEBHOOK_BASE: str = Field("BOT_WEBHOOK_BASE", default="")
    BOT_WEBHOOK_PORT: int = Field("BOT_WEBHOOK_PORT", default="5000")
    BOT_WEBHOOK_PATH: str = Field("BOT_WEBHOOK_PATH", default="/webhook")

    BOT_USE_WEBHOOK: bool = Field("BOT_USE_WEBHOOK", caster=BoolCaster())

    BOT_INSTANCE_NAME: str = Field("BOT_INSTANCE_NAME")

    @property
    def BOT_WEBHOOK_URL(self):
        return f"https://{self.BOT_WEBHOOK_BASE}{self.BOT_WEBHOOK_PATH}"

    def USE_PROMETHEUS(self):
        return self.BOT_USE_WEBHOOK
