import json
import redis

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO
from btc_app import redis_host, redis_port, log_file

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
    dependencies=[Depends(api_key_auth)],
)

#@router.get("/account", dependencies=[Depends(api_key_auth)])
#def get_account_profile():
#    """Returns the symbols for the stocks in your Robinhood portfolio."""
#    _robinhood_crypto_data = RH_CRYPTO()
#    _profile = _robinhood_crypto_data.account_profile
#    _response = json.dumps(_profile, indent=4, default=str)
#    return Response(content=_response, media_type="application/json")
#
#@router.get("/investment", dependencies=[Depends(api_key_auth)])
#def get_investment_profile():
#    """Returns the symbols for the stocks in your Robinhood portfolio."""
#    _robinhood_crypto_data = RH_CRYPTO()
#    _profile = _robinhood_crypto_data.investment_profile
#    _response = json.dumps(_profile, indent=4, default=str)
#    return Response(content=_response, media_type="application/json")

@router.get("/phoenix", dependencies=[Depends(api_key_auth)])
def get_phoenix_account():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    phoenix_account = r.get('phoenix_account')
    if type(phoenix_account) == bytes:
        phoenix_account = phoenix_account.decode('utf-8')
    return Response(content=phoenix_account, media_type="application/json")

@router.get("/cash", dependencies=[Depends(api_key_auth)])
def get_cash():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    phoenix_account = r.get('phoenix_account')
    if type(phoenix_account) == bytes:
        phoenix_account = phoenix_account.decode('utf-8')

    phoenix_account = json.loads(phoenix_account) # Convert to dict, we need to access the data via keys
    cash = float(phoenix_account['crypto_buying_power']['amount'])
    return Response(content=json.dumps({"cash": cash}), media_type="application/json")

@router.get("/crypto_holdings", dependencies=[Depends(api_key_auth)])
def get_holdings():
    """Returns the current holdings and their information."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _holdings = r.get("crypto_holdings")
    if type(_holdings) == bytes:
        _holdings = _holdings.decode('utf-8')

    return Response(content=_holdings, media_type="application/json")
