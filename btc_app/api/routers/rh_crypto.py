import json
import redis
import logging
from logging.handlers import RotatingFileHandler

from fastapi import Response
from fastapi import Depends, APIRouter

from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO
from btc_app import redis_host, redis_port, log_file

r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Set up logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = RotatingFileHandler(
    log_file, maxBytes=(1048576*5), backupCount=10
)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

router = APIRouter(
    prefix="/crypto",
    tags=["crypto"],
    dependencies=[Depends(api_key_auth)],
)

#@router.get("/portfolio", dependencies=[Depends(api_key_auth)])
#def get_crypto_portfolio():
#    """Returns the symbols for the stocks in your Robinhood portfolio."""
#    _robinhood_crypto_data = RH_CRYPTO()
#    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio
#    _response = json.dumps(_crypto_portfolio_data, indent=4, default=str)
#    return Response(content=_response, media_type="application/json")
#

@router.get("/crypto_symbols", dependencies=[Depends(api_key_auth)])
def crypto_symbols():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    # Connect to Redis
    _crypto_symbols = r.get('crypto_symbols')
    if type(_crypto_symbols) == bytes:
        _crypto_symbols = _crypto_symbols.decode('utf-8')

    return Response(content=_crypto_symbols, media_type="application/json")

@router.get("/quotes", dependencies=[Depends(api_key_auth)])
def get_crypto_quotes():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _quotes = build_quote()
    return Response(content=_quotes, media_type="application/json")

@router.get("/current_coins", dependencies=[Depends(api_key_auth)])
def get_current_coins():
    """Returns the symbols for the coins in your Robinhood portfolio, with quantities.
    
    Example:
    {
        "BTC": 0.0001,
        "ETH": 0.0002,
        "LTC": 0.0003
    }
    """
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _current_coins = r.get('current_coins')

    if type(_current_coins) == bytes:
        _current_coins = _current_coins.decode('utf-8')

    return Response(content=_current_coins, media_type="application/json")

@router.get("/order_history", dependencies=[Depends(api_key_auth)])
def get_order_history():
    """Returns order history of crypto purchases."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _order_history = r.get('order_history')

    if type(_order_history) == bytes:
        _order_history = _order_history.decode('utf-8')

    return Response(content=_order_history, media_type="application/json")

@router.get("buy", dependencies=[Depends(api_key_auth)])
def buy():
    pass

@router.get("sell", dependencies=[Depends(api_key_auth)])
def sell():
    pass

##### Non accessible functions #####
def build_quote() -> dict:
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _quotes = r.get('quotes')
    return _quotes
