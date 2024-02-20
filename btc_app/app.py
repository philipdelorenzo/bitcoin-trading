import json
from pprint import pprint

from fastapi import Response
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse

from btc_app.api.routers import rh_crypto, rh_profile, rh_markets

# Config data
from btc_app import _app, _version, _description, _authors

app = FastAPI(prefix="/robinhood")
app.include_router(rh_profile.router)
app.include_router(rh_crypto.router)
app.include_router(rh_markets.router)

@app.get("/", response_class=RedirectResponse)
def home():
    return RedirectResponse(url="/health")

@app.get("/health")
def health():
    _data = {"status": status.HTTP_200_OK}
    _response = json.dumps(_data, indent=4, default=str)
    #return Response(_response) # This is pprinted in the browser
    return Response(content=_response, media_type="application/json")

@app.get("/about")
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
    return Response(content=_response, media_type="application/json")
