import os
from env_variables import set_all

set_all()

SERVER_ID = int(os.environ["DC_SERVER_ID"])
APP_ID = int(os.environ["DC_APP_ID"])
PERMISSIONS = int(os.environ["DC_PERMISSIONS"])
BOT_TOKEN = os.environ["DC_BOT_TOKEN"]
BOT_ID_CHANNEL = int(os.environ["DC_BOT_ID_CHANNEL"])



HOST = "http://68.183.117.103/"