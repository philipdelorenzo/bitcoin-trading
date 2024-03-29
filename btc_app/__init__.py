import os
import tomllib
import configparser
from dotenv import load_dotenv, dotenv_values

# Read the config file
BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, ".."))
_config = configparser.ConfigParser()
_config.read(os.path.join(MAIN, 'config.ini'))

with open(os.path.join(MAIN, 'pyproject.toml'), "rb") as f:
    _tomlcfg = tomllib.load(f)

# Let's get the Robinhood credentials from the .env file
_apifile = os.path.join(MAIN, '.api_key')
_redisfile = os.path.join(MAIN, '.redis_key')
_envfile = os.path.join(MAIN, '.env')

if not os.path.exists(_apifile):
    raise FileNotFoundError(f"The .api_key file - {_apifile} does not exist.")
if not os.path.exists(_redisfile):
    raise FileNotFoundError(f"The .redis_key file - {_redisfile} does not exist.")
if not os.path.exists(_envfile):
    raise FileNotFoundError(f"The .env file - {_envfile} does not exist.")

load_dotenv(os.path.join(MAIN, '.env'))
load_dotenv(os.path.join(MAIN, '.api_key'))
load_dotenv(os.path.join(MAIN, '.redis_key'))

robinhood_user = os.getenv('ROBINHOOD_USER')
robinhood_pass = os.getenv('ROBINHOOD_PASS')
btc_app_robinhood_api_key = os.getenv('BTC_APP_ROBINHOOD_API_KEY')
robinhood_opt_key = os.getenv('ROBINHOOD_OPT_KEY') # This is the key for Robinhood, set in .env

# Let's get the Redis credentials from the .env file
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")
redis_app_key = os.getenv('REDIS_APP_KEY') # This is the key for Redis, set in .redis_key file

google_user = os.getenv('GOOGLE_USER')
google_pass = os.getenv('GOOGLE_PASS')

# Let's get the Alpha Vantage API key from the .env file
_app = _tomlcfg["tool"]["poetry"]["name"]
_version = _tomlcfg["tool"]["poetry"]["version"]
_description = _tomlcfg["tool"]["poetry"]["description"]
_authors = _tomlcfg["tool"]["poetry"]["authors"]

# Logging
log_file = os.path.join("/btc_app_data", "btc_app.log")
transaction_log_file = os.path.join("/btc_app_data", "btc_transaction_records.log")