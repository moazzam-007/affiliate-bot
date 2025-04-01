from os import environ as env
from dotenv import load_dotenv
class Telegram:
    API_ID = int(env.get("API_ID"))
    API_HASH = env.get("API_HASH")
    BOT_TOKEN = env.get("BOT_TOKEN")
    PHONE_NUMBER = env.get("PHONE_NUMBER")
    MAIN_CHAT_ID = int(env.get("MAIN_CHAT_ID"))
    STRING_SESSION = env.get("STRING_SESSION")
    CHANNELS = [int(chat_id) for chat_id in env.get("CHANNELS").split(',')]
    FILTER_AMAZON_TAGS = [chat_id for chat_id in env.get("FILTER_AMAZON_TAGS").split(',')]
    YOUR_AMAZON_TAG = env.get('YOUR_AMAZON_TAG')
    EXTRAPE_SESSION_SECRET = env.get('EXTRAPE_SESSION_SECRET')
    LOG_GROUP_ID = int(env.get("LOG_GROUP_ID"))
