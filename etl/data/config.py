import os
from typing import Any
from dotenv import load_dotenv, dotenv_values

"""
This module is the configuration for the ETL process.
It reads the .env file and sets the variables for the ETL process (local).
The ETL process is responsible for extracting the data from the Robinhood API,
transforming the data into a usable format, and loading the data into a Redis database.
The ETL process is run on a schedule on a cadence.

Attributes:
    BASE (str): The base directory for the ETL process.
    MAIN (str): The main directory for the ETL process.
    robinhood_user (str): The Robinhood username.
    robinhood_pass (str): The Robinhood password.
    robinhood_opt_key (str): The Robinhood options key (API key from RobinHood).
    redis_host (str): The Redis host.
    redis_port (str): The Redis port.
    redis_password (str): The Redis password.
    redis_app_key (str): The Redis app key. (This is the key for the Redis database.)
    log_file (str): The log file for the ETL process.

The .env file should contain the above variables, and the .redis_key file should contain the Redis App Key (redis_app_key).
"""
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
