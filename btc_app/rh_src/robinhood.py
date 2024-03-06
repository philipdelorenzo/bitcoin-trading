import os
import pyotp
import requests
import robin_stocks.robinhood as rh

from typing import Any
from btc_app import robinhood_user, robinhood_pass, robinhood_opt_key

class RH_CRYPTO():
    """This class instantiates all the methods needed to interact with the Robinhood API (crpyto)."""
    def __init__(self):
        """Initializes the class and logs in to Robinhood."""
        self._login() # Log in to Robinhood
        self.my_portfolio = self._get_portfolio_symbols()
        self.crypto_portfolio = self._get_crypto_portfolio()
        self.account_profile = self._get_account_profile()
        self.investment_profile = self._get_investment_profile()
        self.phoenix_account = self._get_phoenix_account()
        self.holdings = self._get_holdings()
    
    def _login(self):
        """Logs in to Robinhood."""
        _username = robinhood_user
        _password = robinhood_pass
        totp  = pyotp.TOTP(robinhood_opt_key).now()

        try:
            rh.login(_username, _password, mfa_code=totp)
        except Exception as e:
            print(f"Error: {e}")
            raise e
  
    def _get_portfolio_symbols(self):
        """
        Returns: the symbol for each stock in your portfolio as a list of strings
        """
        symbols = []
        holdings_data = rh.get_open_stock_positions()
        for item in holdings_data:
            if not item:
                continue
            instrument_data = rh.get_instrument_by_url(item.get("instrument"))
            symbol = instrument_data["symbol"]
            symbols.append(symbol)
        
        return symbols
    
    def get_crypto_symbols(self, symbols: list = []) -> list:
        """Returns the symbols for the stocks in your Robinhood portfolio."""
        symbols = []
        holdings_data = rh.crypto.get_crypto_positions(info=None)
        for item in holdings_data:
            if not item:
                continue

            symbol = item["currency"]["code"]
            symbols.append(symbol) if symbol not in symbols else None
        
        return symbols
    
    def _get_crypto_portfolio(self):
        """Returns the symbols for the stocks in your Robinhood portfolio."""
        return rh.crypto.get_crypto_positions(info=None)
    
    def get_crypto_quote(self, ticker, info=None):
        """Returns the current price of the specified stock."""
        return rh.crypto.get_crypto_quote(ticker, info=None)

    def get_markets(self):
        """Returns the current markets and data associated with them."""
        return rh.markets.get_markets()

    def _get_account_profile(self):
        """Returns the user's account profile information."""
        return rh.profiles.load_account_profile()
    
    def _get_investment_profile(self):
        """Returns the user's investment profile information."""
        return rh.profiles.load_investment_profile()

    def _get_phoenix_account(self):
        """Returns the user's Phoenix account information."""
        return rh.account.load_phoenix_account()
    
    def _get_holdings(self):
        """Returns the user's holdings."""
        return rh.account.build_holdings()
