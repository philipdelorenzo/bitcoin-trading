import json
from pprint import pprint

from fastapi import Response
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse

from btc_app.api.routers import rh_crypto, rh_profile, rh_markets

# Config data
from btc_app import _app, _version, _description, _authors
from btc_app import log_file

# Setup logging
import logging
from logging.handlers import RotatingFileHandler
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = RotatingFileHandler(
    log_file, maxBytes=(1048576*5), backupCount=10
)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

# Add basic data to the logfile so we know the app is running
logger.info(f"App: {_app} | Version: {_version} | Description: {_description} | Authors: {_authors}")

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
    return Response(content=_response, media_type="application/json")

@app.get("/about")
def about():
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
