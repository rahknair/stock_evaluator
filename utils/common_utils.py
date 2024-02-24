def extract_current_price(input=None):
    """
    This function will check and give the current price of the stock
    :return: the current price of the stock
    """
    import yfinance as yf

    # Specify the stock symbol (ticker)
    #stock_symbol = "ICICIBANK.NS"
    stock_symbol = input

    # Get stock information
    ticker = yf.Ticker(stock_symbol)
    print(ticker.info)
    current_price = ticker.info["currentPrice"]

    # Print the result
    print(f"Stock: {stock_symbol}")
    print(f"Current Price: Rs.{current_price:.2f}")
    return current_price



