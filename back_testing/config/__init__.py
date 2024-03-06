import os
import time as tm
import datetime as dt

# SETTINGS
import configparser
from dotenv import load_dotenv, dotenv_values

# Read the config file
BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, ".."))
APP = os.path.abspath(os.path.join(MAIN, ".."))

# Let's get the Robinhood credentials from the .env file
_apifile = os.path.join(APP, '.api_key')
_redisfile = os.path.join(APP, '.redis_key')
_envfile = os.path.join(APP, '.env')

if not os.path.exists(_apifile):
    raise FileNotFoundError(f"The .api_key file - {_apifile} does not exist.")
if not os.path.exists(_redisfile):
    raise FileNotFoundError(f"The .redis_key file - {_redisfile} does not exist.")
if not os.path.exists(_envfile):
    raise FileNotFoundError(f"The .env file - {_envfile} does not exist.")

load_dotenv(os.path.join(APP, '.env'))
load_dotenv(os.path.join(APP, '.api_key'))
load_dotenv(os.path.join(APP, '.redis_key'))

btc_app_robinhood_api_key = os.getenv('BTC_APP_ROBINHOOD_API_KEY')

# Window size or the sequence length, 7 (1 week)
N_STEPS = 7

# Lookup steps, 1 is the next day, 3 = after tomorrow
LOOKUP_STEPS = [1, 2, 3]

# Stock ticker, GOOGL
#STOCK = 'BTC-USD'
STOCK = 'BTC-USD'

# Current date
date_now = tm.strftime('%Y-%m-%d')
date_3_years_back = (dt.date.today() - dt.timedelta(days=1104)).strftime('%Y-%m-%d')

log_file = os.path.join("/btc_app_data", "back_testing.log")

# Let's get the Redis credentials from the .env file
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
