# import pandas as pd
import telegram
from datetime import datetime
import pytz
# from google.oauth2 import service_account
# from github import Github # PyGithub
import os


# telegram_token = os.environ['TG_TOKEN']
# user_id = os.environ['USER_ID']
# g_bq = os.environ['G_BQ']

telegram_token = os.environ.get('TG_TOKEN')
user_id = os.environ.get('USER_ID')


def test_report(chat_id, telegram_token, msg):
    bot = telegram.Bot(token=telegram_token)
    # send text message
    bot.sendMessage(chat_id=chat_id, text=msg)


# credentials = service_account.Credentials.from_service_account_info(g_bq)
# project_id = 'medpoint-gbq'


# query = f"""
#          SELECT
#             COUNT(DISTINCT user_id) AS n_users
#          FROM `medpoint-gbq.analytics_250521411.user_info`
#          """

# # max saved event date
# n_users_df = pd.read_gbq(query,
#                          project_id=project_id,
#                          credentials=credentials,
#                          max_results=10)

# n_users = str(n_users_df.iloc[0, 0])

n_users = ' 54'


IST = pytz.timezone('Europe/Moscow')
message = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S') + n_users

try:
    test_report(user_id, telegram_token, message)
except Exception as e:
    print(e)
