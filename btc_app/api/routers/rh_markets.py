import json

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app.rh_src.robinhood import RH_CRYPTO

router = APIRouter(
    prefix="/markets",
    tags=["markets"],
    dependencies=[Depends(api_key_auth)],
)

@router.get("/", dependencies=[Depends(api_key_auth)])
def get_markets():
    """Returns the symbols for the stocks in your Robinhood portfolio."""
    _robinhood_crypto_data = RH_CRYPTO()
    _markets = _robinhood_crypto_data.get_markets()
    _response = json.dumps(_markets, indent=4, default=str)
    return Response(_response)
