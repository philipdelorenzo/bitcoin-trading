import os
import configparser
from dotenv import load_dotenv, dotenv_values

# Read the config file
BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, ".."))
_config = configparser.ConfigParser()
_config.read(os.path.join(MAIN, 'config.ini'))

api_key = _config["api"]["api_key"]

# Let's get the Robinhood credentials from the .env file
load_dotenv(os.path.join(MAIN, '.env'))
robinhood_user = os.getenv('ROBINHOOD_USER')
robinhood_pass = os.getenv('ROBINHOOD_PASS')
robinhood_opt_key = os.getenv('ROBINHOOD_OPT_KEY')

google_user = os.getenv('GOOGLE_USER')
google_pass = os.getenv('GOOGLE_PASS')
