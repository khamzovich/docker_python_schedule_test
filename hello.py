import telebot  # для работы с телеграм ботом
import pandas as pd
import numpy as np

# from itertools import chain
# import re
# from google.oauth2 import service_account

# mongo
# import paramiko
# from paramiko import SSHClient
# from sshtunnel import SSHTunnelForwarder
# from pymongo import MongoClient

# from user_agents import parse

from datetime import datetime
import pytz

IST = pytz.timezone('Europe/Moscow')

# datetime_ist = datetime.now(IST)
x = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')

telegram_token = '5157057758:AAEBmWYKKnBmnGiJxWGthmrPyXsqGi5sc5c'
user_id = 200428870

bot = telebot.TeleBot(telegram_token)
bot.send_message(user_id, f'{df.shape} - {x}')

print(x)