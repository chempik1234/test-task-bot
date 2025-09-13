from config.channel_config import Channel


class SenderRepositoryBase:
    channel_class = Channel

    async def send(self, channel: channel_class, message_text: str) -> None:
        raise NotImplementedError()
