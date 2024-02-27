import json
import redis
import time
import logging
from logging.handlers import RotatingFileHandler

from data.rh import RH_CRYPTO
from data.config import redis_host, redis_port, redis_password
from data.config import log_file

# Connect to Robinhood
rhood = RH_CRYPTO()

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = RotatingFileHandler(
    log_file, maxBytes=(1048576*5), backupCount=10
)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

# Let's get the data from Robinhood and save it to Redis
def pull_rhood_values(data: dict = {}) -> dict:
    """Updates the data dictionary with the latest values from Robinhood."""
    data.update({"crypto_portfolio": rhood.crypto_portfolio})
    data.update({"phoenix_account": rhood.get_phoenix_account()})
    data.update({"crypto_symbols": rhood.get_crypto_symbols()})
    data.update({"crypto_holdings": rhood.get_holdings()})
    data.update({"current_coins": rhood.get_coin_quantities()})
    data.update({"order_history": rhood.get_order_history()})
    
    # Let's set the empty quotes dictionary and populate it with the latest quotes
    data["quotes"] = {}
    for ticker in rhood.get_crypto_symbols():
        data["quotes"].update({ticker: rhood.get_crypto_quote(ticker=ticker)})

    return data

while True:
    data = pull_rhood_values() # This gets the values from Robinhood and updates the data dictionary
    for k, v in data.items():
        r.set(k, json.dumps(v)) # Save the data to Redis

    logger.info(f"Data saved to Redis - {data.keys()}")
    
    print("Sleeping for 5 minutes...")
    time.sleep(600)
