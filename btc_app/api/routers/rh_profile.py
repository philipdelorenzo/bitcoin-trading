import json

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
    dependencies=[Depends(api_key_auth)],
)

@router.get("/account", dependencies=[Depends(api_key_auth)])
def get_account_profile():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.account_profile
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

@router.get("/investment", dependencies=[Depends(api_key_auth)])
def get_investment_profile():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.investment_profile
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

@router.get("/phoenix", dependencies=[Depends(api_key_auth)])
def get_phoenix_account():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.phoenix_account
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

@router.get("/holdings", dependencies=[Depends(api_key_auth)])
def get_holdings():
    """Returns the current holdings and their information."""
    _robinhood_crypto_data = RH_CRYPTO()
    _profile = _robinhood_crypto_data.holdings
    _response = json.dumps(_profile, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

