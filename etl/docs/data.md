# Data Package

## Config Module (config)

::: data.config
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'etl'))

## Headlines Module (headlines)

::: data.headlines
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'etl'))

## Robinhood Module (rh)

::: data.rh
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'etl'))

## Stock Quotes Module (stock_quotes)

::: data.stock_quotes
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'etl'))

## Tweets Module (tweets)

::: data.tweets
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'etl'))
