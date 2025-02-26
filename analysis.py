# Import necessary library
import pandas as pd  # Pandas is used for handling tabular data

def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Adds a simple moving average (SMA) column to the DataFrame.
    
    :param df: DataFrame containing historical stock data (must include a 'Close' price column)
    :param window: Number of periods over which the moving average is calculated (default is 20)
    :return: DataFrame with an additional column containing the simple moving average
    """
    
    # Calculate the simple moving average using the 'Close' price over the specified window
    df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean()
    
    return df  # Return the updated DataFrame with the new SMA column

if __name__ == "__main__":
    # Import the function to fetch stock data from a separate module
    from data_fetch import get_stock_data  
    
    # Fetch historical stock data for Apple (AAPL)
    df = get_stock_data("AAPL")
    
    # Add a 20-day simple moving average to the data
    df = add_moving_average(df, window=20)
    
    # Print the last five rows of the DataFrame to check the results
    print(df.tail())
