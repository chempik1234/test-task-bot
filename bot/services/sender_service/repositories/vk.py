import structlog
import requests

from config.channel_config import VKChannel
from services.sender_service.repositories.base import SenderRepositoryBase
from utils import is_success_http

logger = structlog.get_logger(__name__)


class SenderRepositoryVK(SenderRepositoryBase):
    channel_class = VKChannel

    def __init__(self, *channels: VKChannel):
        self.channels = channels

    async def send(self, channel: channel_class, message_text: str) -> None:
        result = requests.post(
            url=channel.endpoint,
            params={
                "message": message_text,
                "v": channel.version,
                "access_token": channel.access_token,
                "owner_id": channel.peer_id,
            },
        )

        if not is_success_http(result.status_code):
            logger.error("request sent, VK replied with an error", status=result.status_code)
            raise Exception("result status code = {}".format(result.status_code))

        logger.info("sent message in vk", peer_id=channel.peer_id)
