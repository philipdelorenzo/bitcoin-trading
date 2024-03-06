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

app = FastAPI()
app.include_router(testing.router)

@app.get("/", response_class=RedirectResponse)
def home():
    logger.info("Redirecting to /health")
    return RedirectResponse(url="/health")

@app.get("/health")
def health():
    logger.info(f"Health check {status.HTTP_200_OK}")
    _data = {"status": status.HTTP_200_OK}
    _response = json.dumps(_data, indent=4, default=str)
    return Response(content=_response, media_type="application/json")

