import json
from fastapi import Response
from fastapi import FastAPI, HTTPException, status, Security, Depends 
from fastapi.security import APIKeyHeader, APIKeyQuery
from fastapi.security import OAuth2PasswordBearer

from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO

# Config data
from btc_app import _app, _version, _description, _authors

app = FastAPI()

@app.get("/")
def read_root():
    _data = {"status": status.HTTP_200_OK}
    _response = json.dumps(_data, indent=4, default=str)
    return Response(_response)

@app.get("/public")
def public():
    """A public endpoint that does not require any authentication."""
    _data = {
        "status": status.HTTP_200_OK,
        "app": {
            "name": _app,
            "description": _description,
            "authors": _authors,
            "version": _version,
            },
        }
    _response = json.dumps(_data, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/crypto_portfolio", dependencies=[Depends(api_key_auth)])
def get_crypto_portfolio():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio
    _response = json.dumps(_crypto_portfolio_data, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/invested_tickers", dependencies=[Depends(api_key_auth)])
def get_crypto_tickers():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _ticker_symbols = []
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio

    for item in _crypto_portfolio_data:
        _ticker_symbols.append(item["currency"]["code"]) if item["currency"]["code"] not in _ticker_symbols and item["currency"]["code"] is not None else None

    _response = json.dumps(_ticker_symbols, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/quotes", dependencies=[Depends(api_key_auth)])
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

@app.get("/robinhood/markets", dependencies=[Depends(api_key_auth)])
def get_markets():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _markets = _robinhood_crypto_data.get_markets()
    _response = json.dumps(_markets, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/account_profile", dependencies=[Depends(api_key_auth)])
def get_account_profile():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.account_profile
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/investment_profile", dependencies=[Depends(api_key_auth)])
def get_investment_profile():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.investment_profile
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/phoenix_account", dependencies=[Depends(api_key_auth)])
def get_phoenix_account():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.phoenix_account
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(_response)
