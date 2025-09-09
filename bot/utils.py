import os
import uuid
from typing import Any

from init.config import bot_config


def get_logging_extra(user_id: Any = None) -> dict:
    request_id = str(uuid.uuid4())
    result = {"request_id": request_id}
    if user_id is not None:
        result["user_id"] = user_id
    return result


# def split_text_for_telegram(string: str) -> list[str]:
#     return [string[i: i + 4000] for i in range(0, len(string), 4000)]


def get_path_to(path_to_join: str) -> str:
    return os.path.join(bot_config.CONFIG_MOUNT_DIR, path_to_join)
