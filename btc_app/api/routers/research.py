import json
import redis
import datetime

from fastapi import APIRouter, Depends, Response
from btc_app.api.auth import api_key_auth
from btc_app import transaction_log_file
from btc_app.rh_src.robinhood import RH_CRYPTO
from btc_app.api.trade_logic.crypto import cash_to_dispatch
from btc_app import redis_host, redis_port

r = redis.Redis(host=redis_host, port=redis_port, db=0)

router = APIRouter(
    prefix="/research",
    tags=["research"],
    dependencies=[Depends(api_key_auth)],
)

@router.get("/headlines", dependencies=[Depends(api_key_auth)])
def get_headlines():
    """Gets the headlines from the sources specified in the codebase."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _data = r.get("headlines")
    if type(_data) == bytes:
        _data = _data.decode('utf-8')

    _response = json.dumps(_data, indent=4, default=str)
    return Response(content=_response, media_type="application/json")
