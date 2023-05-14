import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['29476744'])
API_HASH = environ['1420405818d0d6af5ef7a91c996a3129']
BOT_TOKEN = environ['5806744878:AAE-vWVObWnx14C3ILNDOp54ZX6OKGiSTKU']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['1374058330'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1001524905582'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001927936509')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://amazonkosam221:Amazon121@cluster0.wfp7fsq.mongodb.net/?retryWrites=true&w=majori>']
DATABASE_NAME = environ['myfilesbot']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Raja Movies/Files Search Bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {RajaMoviesBot} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Contact @thunderstorm01 for any queries')
