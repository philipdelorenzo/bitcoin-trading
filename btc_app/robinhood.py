import os
import robin_stocks.robinhood as r
from dotenv import load_dotenv, dotenv_values

BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, '..'))
load_dotenv(os.path.join(MAIN, '.env'))

def login():
    username = os.getenv('ROBINHOOD_USER')
    password = os.getenv('ROBINHOOD_PASS')
    r.login(username, password)