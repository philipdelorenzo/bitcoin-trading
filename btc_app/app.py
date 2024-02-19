import json
from fastapi import Response
from fastapi import FastAPI, HTTPException, status, Security, Depends 
from fastapi.security import APIKeyHeader, APIKeyQuery
from fastapi.security import OAuth2PasswordBearer

from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK!"}

@app.get("/public")
def public():
    """A public endpoint that does not require any authentication."""
    return {"message": "Public Endpoint. No API Key required."}

#@app.get("/protected", dependencies=[Depends(api_key_auth)])
@app.get("/protected", dependencies=[Depends(api_key_auth)])
def protected():
    """A private endpoint that requires a valid API key to be provided."""
    return {"message": "API Key is valid. You can access the private endpoint."}

@app.get("/robinhood/crypto_portfolio", dependencies=[Depends(api_key_auth)])
def get_crypto_portfolio():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio
    _response = json.dumps(_robinhood_crypto_data.crypto_portfolio, indent=4, default=str)
    return Response(_response)

@app.get("/robinhood/crypto_quotes", dependencies=[Depends(api_key_auth)])
def get_crypto_quotes():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _ticker_symbols = []
    _crypto_portfolio_data = _robinhood_crypto_data.crypto_portfolio
    for item in _crypto_portfolio_data:
        _ticker_symbols.append(item["currency"]["code"]) if item["currency"]["code"] not in _ticker_symbols and item["currency"]["code"] is not None else None

    _response = json.dumps(_ticker_symbols, indent=4, default=str)
    return Response(_response)
