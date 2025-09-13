from typing import List

import structlog

from services.sender_service.repositories.base import SenderRepositoryBase

logger = structlog.get_logger(__name__)


class SenderService:
    def __init__(self, *sender_repositories: SenderRepositoryBase):
        self.sender_repositories = sender_repositories

    async def send(self, channel, message_text: str) -> None:
        for repo in self.sender_repositories:
            if isinstance(channel, repo.channel_class):
                logger.info("found channel to send message to", channel=channel.__class__.__name__)
                await repo.send(channel, message_text)
                return
        logger.error("not found channel to send message to",
                     channel=channel.__class__.__name__,
                     available_channels=[i.channel_class for i in self.sender_repositories])
        raise Exception(f"no sender repo found for channel type {channel.__class__}")