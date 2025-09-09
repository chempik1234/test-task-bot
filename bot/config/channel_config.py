import itertools
from collections import defaultdict
from typing import List, Dict, Any, TypeVar, Generic

Surface = str

T = TypeVar('T')


class Rule:
    field: str
    filter: Any

    def __init__(self, field: str, filter: Any):
        self.field = field
        self.filter = filter

    def check(self, value: str) -> bool:
        """
        check if a record satisfies given rule
        :param value: value to check
        :return: bool value of whether the record satisfies given rule or not
        """
        raise NotImplementedError()

    def to_kwarg(self):
        raise NotImplementedError()


class OneOfListRule(Rule, Generic[T]):
    field: T
    filter: List[T]

    def __init__(self, field: T, filter: List[T]):
        super().__init__(field, filter)

    def check(self, value: str) -> bool:
        return value in self.filter

    def to_kwarg(self):
        return f"{self.field}__in", self.filter


class Channel:
    id: int
    rules: List[Rule]
    publish_hours = List[str]
    name: str

    def __init__(self, name: str, rules: List[Rule], publish_hours: List[str]):
        self.name = name
        self.rules = rules
        self.publish_hours = publish_hours

    def rules_as_kwargs(self):
        result = {}
        for rule in self.rules:
            key, value = rule.to_kwarg()
            result[key] = value
        return result


class TelegramChannel(Channel):
    link: str
    chat_id: int

    def __init__(self, name: str, link: str, chat_id: int, rules: List[Rule], publish_hours: List[str]):
        super().__init__(name, rules, publish_hours)
        self.link = link
        self.chat_id = chat_id


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

    return ChannelsConfig(telegram=telegram_channels)
