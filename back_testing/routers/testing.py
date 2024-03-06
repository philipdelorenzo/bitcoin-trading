import json
import redis
import datetime

from fastapi import APIRouter, Depends, Response
from back_testing.config.auth import api_key_auth
from back_testing.config import redis_host, redis_port, log_file

r = redis.Redis(host=redis_host, port=redis_port, db=0)

router = APIRouter(
    prefix="/testing",
    tags=["testing"],
    dependencies=[Depends(api_key_auth)],
)

@router.post("/testing", dependencies=[Depends(api_key_auth)])
def set_testing(stock: str):
    """Tests the trading patters for a given stock."""
    r = redis.Redis(host=redis_host, port=redis_port, db=0)
    _data = r.get("testing")
    if type(_data) == bytes:
        _data = _data.decode('utf-8')

    _response = json.dumps(_data, indent=4, default=str)
    return Response(content=_response, media_type="application/json")
