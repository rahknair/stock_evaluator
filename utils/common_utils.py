import yfinance as yf

class CommonUtils:
    """
    This class defines common functions
    """
    def __init__(self):
        """
        Initializing parametrs
        """

    def extract_current_price(self, stock_sym=None):
        """
        This function will check and give the current price of the stock
        :return: the current price of the stock
        """

        # Specify the stock symbol (ticker)
        #stock_symbol = "ICICIBANK.NS"
        stock_symbol = stock_sym

        # Get stock information
        ticker = yf.Ticker(stock_symbol)
        current_price = ticker.info["currentPrice"]
        return current_price