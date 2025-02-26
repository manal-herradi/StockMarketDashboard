# Import necessary libraries
import yfinance as yf  # Yahoo Finance API for retrieving stock data
import pandas as pd  # Pandas for handling tabular data

def get_stock_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """
    Retrieve historical stock data.
    
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)
    :param period: Time period for historical data (default is '1y' for one year)
    :param interval: Data interval (default is '1d' for daily data)
    :return: DataFrame containing historical stock data
    """
    
    # Create a Ticker object for the given stock symbol
    stock = yf.Ticker(ticker)
    
    # Fetch the historical stock data for the given period and interval
    df = stock.history(period=period, interval=interval)
    
    # Reset the index to move the date from index to a separate column
    df.reset_index(inplace=True)
    
    return df  # Return the DataFrame containing stock data

if __name__ == "__main__":
    # Test the function by fetching historical stock data for Apple (AAPL)
    data = get_stock_data("AAPL")
    
    # Print the first five rows of the retrieved data
    print(data.head())
