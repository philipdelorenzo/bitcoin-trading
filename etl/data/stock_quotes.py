import yfinance as yahooFinance
import datetime

from pprint import pprint
from halo import Halo

# Run time consuming work here
# You can also change properties for spinner as and when you want

test_stocks = ['ETH-USD', 'BTC']

def quote(stock: str) -> dict:
    with Halo(text=f'Loading {stock} stock data...', spinner='dots'):

        GetStockInformation = yahooFinance.Ticker(stock)
        return GetStockInformation.info

def ten_day_history(stock: str) -> dict:
    now = datetime.datetime.now().date()

    # startDate , as per our convenience we can modify
    startDate = now - datetime.timedelta(days=10)
    
    # endDate , as per our convenience we can modify
    endDate = now

    GetStockInformation = yahooFinance.Ticker(stock)
    
    return GetStockInformation.history(start=startDate,
                                            end=endDate)

def month_history(stock: str) -> dict:
    now = datetime.datetime.now().date()

    # startDate , as per our convenience we can modify
    startDate = now - datetime.timedelta(days=30)
    
    # endDate , as per our convenience we can modify
    endDate = now

    GetStockInformation = yahooFinance.Ticker(stock)
    
    return GetStockInformation.history(start=startDate,
                                            end=endDate)

def year_history(stock: str) -> dict:
    now = datetime.datetime.now().date()

    # startDate , as per our convenience we can modify
    startDate = now - datetime.timedelta(days=365)
    
    # endDate , as per our convenience we can modify
    endDate = now

    GetStockInformation = yahooFinance.Ticker(stock)
    
    return GetStockInformation.history(start=startDate,
                                            end=endDate)

if __name__ == "__main__":
    for stock in test_stocks:
        with Halo(text=f'Loading {stock} stock data...', spinner='dots'):
            # display Company Sector
            #print("Company Sector : ", GetFacebookInformation.info['sector'])
            
            # display Price Earnings Ratio
            #print("Price Earnings Ratio : ", GetFacebookInformation.info['trailingPE'])
            
            # display Company Beta
            #print(" Company Beta : ", GetFacebookInformation.info['beta'])

            #pprint(quote(stock=stock))
            #pprint(month_history(stock=stock))
            pprint(ten_day_history(stock=stock))
