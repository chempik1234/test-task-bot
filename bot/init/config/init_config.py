import json
import os

from config import BotConfig, read_channels_config_from_dict

bot_config = BotConfig()

with open(os.path.join(bot_config.CONFIG_MOUNT_DIR, "config.json")) as f:
    json_config = json.load(f)

channels_config = read_channels_config_from_dict(json_config)
