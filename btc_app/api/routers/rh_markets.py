import json
import datetime

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app import transaction_log_file
from btc_app.rh_src.robinhood import RH_CRYPTO

# Setup logging
import logging
from pythonjsonlogger import jsonlogger
from logging.handlers import RotatingFileHandler

_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=_format)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter()
fh = RotatingFileHandler(
    transaction_log_file, maxBytes=(1048576*5), backupCount=10
)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

router = APIRouter(
    prefix="/markets",
    tags=["markets"],
    dependencies=[Depends(api_key_auth)],
)

@router.post("/calculate", dependencies=[Depends(api_key_auth)])
async def calculate_market_data(
        symbol: str,
        purchased_price: float,
        current_price: float,
        percentage_change: float
    ) -> str:
    """Returns whether a buy, sell, or hold signal should be triggered."""
    data = {
        "symbol": symbol,
        "purchased_price": purchased_price,
        "current_price": current_price,
        "percentage_change": percentage_change
    }
    logger.info({"timestamp": datetime.datetime.now(), "data": data, "symbol": symbol, "message": f"Calculating market data for symbol: {symbol}"})
    return "Complete!"
