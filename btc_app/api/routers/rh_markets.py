import json
import datetime

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app import transaction_log_file
from btc_app.rh_src.robinhood import RH_CRYPTO
from btc_app.api.trade_logic.crypto import cash_to_dispatch

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
        cash: float,
        number_of_investments: int,
        purchased_price: float,
        current_price: float,
        percentage_change: float
    ) -> str:
    """Returns whether a buy, sell, or hold signal should be triggered.
    
    Args:
        symbol (str): The stock symbol.
        cash (float): The amount of cash available.
        number_of_investments (int): The number of investments held; Ex: If 3 stocks (coins) are held, then the number_of_investments = 3.
        purchased_price (float): The price the stock was purchased at.
        current_price (float): The current price of the stock.
        percentage_change (float): The percentage change in the stock price.

    Returns:
        str: A message indicating whether a buy, sell, or hold signal should be triggered.
    """
    data = {
        "symbol": symbol,
        "cash": '${:,.2f}'.format(float(cash)),
        "number_of_≈investments": number_of_investments,
        "purchased_price": '${:,.2f}'.format(float(purchased_price)),
        "current_price": '${:,.2f}'.format(float(current_price)),
        "percentage_change": percentage_change
    }

    if percentage_change > 3.5:
        _purchase_amount = cash_to_dispatch(cash=cash, number_of_investments=number_of_investments)
        logger.info({"timestamp": datetime.datetime.now(), "data": data, "symbol": symbol, "message": f"Calculated a sell signal for symbol: {symbol} | Dispatching {_purchase_amount} cash to {symbol}"})
    else:
        logger.info({"timestamp": datetime.datetime.now(), "data": data, "symbol": symbol, "message": f"Calculations will not trigger a sell signal: {symbol}"})
    
    return "Complete!"
