import telebot  # для работы с телеграм ботом
import pandas as pd
import numpy as np

from datetime import datetime
import pytz
from settings import TG_TOKEN, USER_ID

IST = pytz.timezone('Europe/Moscow')

# datetime_ist = datetime.now(IST)
x = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')

bot = telebot.TeleBot(TG_TOKEN)
bot.send_message(USER_ID, f'{x}')

print(x)