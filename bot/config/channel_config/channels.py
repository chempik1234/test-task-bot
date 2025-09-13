from typing import List

from .rule import Rule


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

    def __init__(self, name: str,
                 link: str, chat_id: int,  # TelegramChannel attrs
                 rules: List[Rule], publish_hours: List[str]):
        super().__init__(name, rules, publish_hours)
        self.link = link
        self.chat_id = chat_id


class VKChannel(Channel):
    access_token: str
    version: str
    endpoint: str
    peer_id: str

    def __init__(self, name: str,
                 endpoint: str, access_token: str, version: str, peer_id: str,  # VKChannel attrs
                 rules: List[Rule], publish_hours: List[str]):
        super().__init__(name, rules, publish_hours)
        self.access_token = access_token
        self.version = version
        self.endpoint = endpoint
        self.peer_id = peer_id
