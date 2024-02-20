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

api_key = _config["api"]["api_key"]

# Let's get the Robinhood credentials from the .env file
load_dotenv(os.path.join(MAIN, '.env'))
load_dotenv(os.path.join(MAIN, '.api_key'))

robinhood_user = os.getenv('ROBINHOOD_USER')
robinhood_pass = os.getenv('ROBINHOOD_PASS')
btc_app_robinhood_api_key = os.getenv('BTC_APP_ROBINHOOD_API_KEY')
robinhood_opt_key = os.getenv('ROBINHOOD_OPT_KEY')

google_user = os.getenv('GOOGLE_USER')
google_pass = os.getenv('GOOGLE_PASS')

# Let's get the Alpha Vantage API key from the .env file
_app = _tomlcfg["tool"]["poetry"]["name"]
_version = _tomlcfg["tool"]["poetry"]["version"]
_description = _tomlcfg["tool"]["poetry"]["description"]
_authors = _tomlcfg["tool"]["poetry"]["authors"]
