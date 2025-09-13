import structlog

from config.channel_config import TelegramChannel
from services.sender_service.repositories.base import SenderRepositoryBase

logger = structlog.get_logger(__name__)


class SenderRepositoryTelegram(SenderRepositoryBase):
    channel_class = TelegramChannel

    def __init__(self, bot):
        self.bot = bot

    async def send(self, channel: channel_class, message_text: str) -> None:
        try:
            await self.bot.send_message(
                chat_id=channel.chat_id,
                text=message_text,
                disable_web_page_preview=True,
            )
            logger.info("sent message in telegram", chat_id=channel.chat_id)
        except Exception as e:
            logger.error("failed to send message in telegram", chat_id=channel.chat_id, exc_info=e)
            raise e
