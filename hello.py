import telegram
from datetime import datetime
import pytz
# from github import Github # PyGithub
import os


telegram_token = os.environ['TG_TOKEN']
user_id = os.environ['USER_ID']


def test_report(chat_id, telegram_token, msg):
    bot = telegram.Bot(token=telegram_token)
    # send text message
    bot.sendMessage(chat_id=chat_id, text=msg)


IST = pytz.timezone('Europe/Moscow')
message = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')

try:
    test_report(user_id, telegram_token, message)
except Exception as e:
    print(e)