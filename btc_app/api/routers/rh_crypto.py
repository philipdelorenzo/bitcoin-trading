import json
from fastapi import Response
from fastapi import Depends, APIRouter

from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO

router = APIRouter(
    prefix="/crypto",
    tags=["crypto"],
    dependencies=[Depends(api_key_auth)],
)

@router.get("/portfolio", dependencies=[Depends(api_key_auth)])
def get_crypto_portfolio():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio
    _response = json.dumps(_crypto_portfolio_data, indent=4, default=str)
    return Response(_response)

@router.get("/invested_symbols", dependencies=[Depends(api_key_auth)])
def get_crypto_tickers():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _ticker_symbols = []
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio

    for item in _crypto_portfolio_data:
        _ticker_symbols.append(item["currency"]["code"]) if item["currency"]["code"] not in _ticker_symbols and item["currency"]["code"] is not None else None

    _response = json.dumps(_ticker_symbols, indent=4, default=str)
    return Response(_response)

@router.get("/quotes", dependencies=[Depends(api_key_auth)])
def get_crypto_quotes():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _ticker_symbols = []
    _quotes = {}
    _robinhood_crypto_data = RH_CRYPTO()
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio

    for item in _crypto_portfolio_data:
        _ticker_symbols.append(item["currency"]["code"]) if item["currency"]["code"] not in _ticker_symbols and item["currency"]["code"] is not None else None

    for ticker in _ticker_symbols:
        _quotes[ticker] = _robinhood_crypto_data.get_crypto_quote(ticker, info=None)

    _response = json.dumps(_quotes, indent=4, default=str)
    return Response(_response)
