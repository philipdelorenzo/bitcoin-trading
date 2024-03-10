# Machine Learning Scanner Package

This module retrieves data from Yahoo, Robinhood, etc. It applies this data to
scan stocks for possible tickers to trade.

## Scanner Locate Module
::: scanner.locate
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'back_testing'))
