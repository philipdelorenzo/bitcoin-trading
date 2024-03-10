# Bitcoin Trading Application Routers

## Trade Logic (Crypto)

::: api.trade_logic.crypto
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'btc_app'))
