import os
import time as tm
import datetime as dt

# SETTINGS

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
