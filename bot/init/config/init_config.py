import json
import os

from config import BotConfig, read_channels_config_from_dict

bot_config = BotConfig()

config_file_name = "config.json" if not bot_config.BOT_DEBUG else "debug_config.json"
with open(os.path.join(bot_config.CONFIG_MOUNT_DIR, config_file_name)) as f:
    json_config = json.load(f)

channels_config = read_channels_config_from_dict(json_config)
