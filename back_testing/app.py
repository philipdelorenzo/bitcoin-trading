import json
import redis
from pprint import pprint

from fastapi import Response
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, JSONResponse

from back_testing.routers import testing

# Config data
from back_testing.config import log_file
from back_testing.config import redis_host, redis_port

# Setup logging
from . import logger

# Setup logging
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from . import exception_handlers as eh
from . import middleware

app = FastAPI()
app.middleware("http")(middleware.log_request_middleware)
app.add_exception_handler(RequestValidationError, eh.request_validation_exception_handler)
app.add_exception_handler(HTTPException, eh.http_exception_handler)
app.add_exception_handler(Exception, eh.unhandled_exception_handler)

app.include_router(testing.router)

@app.get("/", response_class=RedirectResponse)
def home():
    logger.info("Redirecting to /health")
    return RedirectResponse(url="/health")

@app.get("/health")
def health():
    _data = {"status": status.HTTP_200_OK}
    _response = json.dumps(_data, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

