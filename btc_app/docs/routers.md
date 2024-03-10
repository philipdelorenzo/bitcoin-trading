# Bitcoin Trading Application Routers

## Research Router Module

::: api.routers.research
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'btc_app'))

## Robinhood Crypto Router Module

::: api.routers.rh_crypto
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'btc_app'))

## Robinhood Markets Router Module

::: api.routers.rh_markets
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'btc_app'))

## Robinhood Profile Router Module

::: api.routers.rh_profile
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'btc_app'))
