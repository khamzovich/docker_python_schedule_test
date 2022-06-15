import telegram

from datetime import datetime
import pytz
from settings import TG_TOKEN, USER_ID


def test_report(chat_id, telegram_token, msg):

    bot = telegram.Bot(token=telegram_token)
    
    # send text message
    bot.sendMessage(chat_id=chat_id, text=msg)

IST = pytz.timezone('Europe/Moscow')

# datetime_ist = datetime.now(IST)
message = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')

try:
    test_report(USER_ID, TG_TOKEN, message)
except Exception as e:
    print(e)