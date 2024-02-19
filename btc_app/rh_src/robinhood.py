import os
import pyotp
import robin_stocks.robinhood as rh

from btc_app import robinhood_user, robinhood_pass, robinhood_opt_key

class RH_CRYPTO():
    """This class instantiates all the methods needed to interact with the Robinhood API (crpyto)."""
    def __init__(self):
        """Initializes the class and logs in to Robinhood."""
        self._login() # Log in to Robinhood
        self.my_portfolio = self._get_portfolio_symbols()
        self.crypto_portfolio = self._get_crypto_portfolio()
    
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
            instrument_data = rh.get_instrument_by_url(item.get('instrument'))
            symbol = instrument_data['symbol']
            symbols.append(symbol)
        
        return symbols
    
    def _get_crypto_portfolio(self):
        """Returns the symbols for the stocks in your Robinhood portfolio."""
        return rh.crypto.get_crypto_positions(info=None)
    
