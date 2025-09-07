import os.path

from init.config import bot_config

with open(os.path.join(bot_config.CONFIG_MOUNT_DIR, "template.txt"), "r") as f:
    TEMPLATE_TEXT = f.read()
