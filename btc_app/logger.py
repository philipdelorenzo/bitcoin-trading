import logging
import logging_loki

# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(logging.DEBUG))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Setting up Loki Logging Handler
logging_loki.emitter.LokiEmitter.level_tag = "level"

loki_handler = logging_loki.LokiHandler(
    url="http://loki:3100/loki/api/v1/push", 
    tags={"application": "btc_app"},
    auth=("admin", "admin"),
    version="1",
)
loki_handler.setFormatter(formatter)
logger.addHandler(loki_handler)
