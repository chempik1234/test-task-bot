import itertools
from collections import defaultdict
from typing import List, Dict, Any, TypeVar, Generic

from aiofiles.os import access

from .channels import Channel, TelegramChannel, VKChannel
from .rule import OneOfListRule, Rule

Surface = str


class ChannelsConfig:
    """
    Channels config used like this:

    >>> chan_config = ChannelsConfig(telegram=[
            TelegramChannel(name="some channel", link="a", id=1, rules=[
                Rule(position_category=["pm"])
            ], publish_hours=["09:00", "13:00"]),
        ])
    >>> telegram_channels_list = chan_config.telegram
    >>> telegram_channels_for_pm = chan_config.get_channels_for(surface="telegram", position_category="pm")
    >>> all_channels_list = chan_config.all_channels()
    """

    _channels: Dict[Surface, List[Channel]] = defaultdict(list)

    def __init__(self, **surfaces: List[Channel]):
        for surface, channels in surfaces.items():
            self._set_channel(surface, channels)

    def _set_channel(self, surface: Surface, channels: List[Channel]):
        self._channels[surface] = channels

    def get_channels_for(self, surface: Surface, position_category: str) -> List[Channel]:
        channels_list = self._channels[surface]
        return [chan for chan in channels_list if all(rule.check(position_category) for rule in chan.rules)]

    def all_channels(self) -> List[Channel]:
        return list(itertools.chain(*self._channels.values()))

    def channels_in_surface(self, surface: Surface) -> List[Channel]:
        return self._channels[surface]

    def all_surfaces(self) -> List[Surface]:
        return list(self._channels.keys())

    def get_channel(self, surface: Surface, channel_name: str) -> Channel | None:
        for channel in self._channels[surface]:
            if channel.name == channel_name:
                return channel
        return None


def read_channels_config_from_dict(data: Dict) -> ChannelsConfig:
    telegram_channels_data = data.get("channels", {}).get("telegram", [])

    telegram_channels = [
        TelegramChannel(
            name=i["name"],
            link=i["link"],
            chat_id=i["chat_id"],
            rules=[
                (
                    OneOfListRule(r["field"], r["filter"]) if isinstance(r["filter"], list)
                    else Rule(r["field"], r["filter"])
                )
                for r in i["rules"]
            ],
            publish_hours=i["publish_hours"],
        )
        for i in telegram_channels_data
    ]

    vk_channels_data = data.get("channels", {}).get("vk", [])

    vk_channels = [
        VKChannel(
            name=i["name"],
            endpoint=i["endpoint"],
            version=i["version"],
            peer_id=i["peer_id"],
            access_token=i["access_token"],
            rules=[
                (
                    OneOfListRule(r["field"], r["filter"]) if isinstance(r["filter"], list)
                    else Rule(r["field"], r["filter"])
                )
                for r in i["rules"]
            ],
            publish_hours=i["publish_hours"],
        )
        for i in vk_channels_data
    ]

    return ChannelsConfig(telegram=telegram_channels, vk=vk_channels)
