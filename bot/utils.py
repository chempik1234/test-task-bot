import datetime
import json
import uuid
from typing import Any, Dict

from aiogram.types import Message


def str_to_int_nullable(s: str) -> int | None:
    if s == 'None':
        result = None
    elif s.isdigit():
        result = int(s)
    else:
        raise ValueError("invalid nullable int from str: {}".format(s))
    return result


def get_logging_extra(user_id: Any) -> dict:
    request_id = str(uuid.uuid4())
    result = {"request_id": request_id}
    if user_id is not None:
        result["user_id"] = user_id
    return result


def split_text_for_telegram(string: str) -> list[str]:
    return [string[i: i + 4000] for i in range(0, len(string), 4000)]


def render(template: str, context: Dict[str, str]) -> str:
    """
    render template with context

    replace {key} in template with value by 'key' in context
    :param template: raw template string
    :param context: dict with values to insert into template
    :return: rendered template
    """
    return template.format(**context)
