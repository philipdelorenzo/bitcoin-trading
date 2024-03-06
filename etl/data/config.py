import os
from typing import Any
from dotenv import load_dotenv, dotenv_values

# Read the config file
BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, ".."))

if not os.path.isfile(os.path.join(MAIN, ".env")):
    raise FileNotFoundError("No .env file found")

load_dotenv(os.path.join(MAIN, ".env"))
load_dotenv(os.path.join(MAIN, ".redis_key"))
robinhood_user = os.getenv("ROBINHOOD_USER")
robinhood_pass = os.getenv("ROBINHOOD_PASS")
robinhood_opt_key = os.getenv("ROBINHOOD_OPT_KEY")
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")

# Logging Data
log_file = os.path.join("/btc_app_data", "etl.log")
