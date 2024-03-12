import json
import redis
from pprint import pprint

from fastapi import Response
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse

from btc_app.api.routers import rh_crypto, rh_profile, rh_markets, research

# Config data
from btc_app import _app, _version, _description, _authors
from btc_app import redis_host, redis_port, log_file

from btc_app.logger import logger

# Setup logging
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from btc_app.exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from btc_app.middleware import log_request_middleware

# Add basic data to the logfile so we know the app is running
logger.info(f"App: {_app} | Version: {_version} | Description: {_description} | Authors: {_authors}")

app = FastAPI(prefix="/robinhood")
app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(rh_profile.router)
app.include_router(rh_crypto.router)
app.include_router(rh_markets.router)
app.include_router(research.router)

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

@app.get("/test")
def test():
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
