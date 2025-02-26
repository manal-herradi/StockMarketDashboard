import plotly.graph_objs as go  # Import Plotly for interactive charting
from plotly.subplots import make_subplots  # Import subplots module for multiple plots
import pandas as pd  # Import pandas for data manipulation

def create_stock_chart(df: pd.DataFrame, ticker: str, sma_window: int = 20):
    """
    Creates an interactive stock price chart with a moving average.
    
    :param df: DataFrame containing historical stock data
    :param ticker: Stock ticker symbol (e.g., 'AAPL')
    :param sma_window: Number of periods for the Simple Moving Average (SMA)
    :return: Plotly figure object
    """

    # Create a line plot for the closing price
    trace_close = go.Scatter(
        x=df['Date'], y=df['Close'], mode='lines', name='Close Price'
    )

    # Create a line plot for the moving average
    trace_sma = go.Scatter(
        x=df['Date'], y=df[f"SMA_{sma_window}"], mode='lines', name=f'SMA {sma_window}'
    )

    # Create a figure and add the two traces (close price & moving average)
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(trace_close, row=1, col=1)
    fig.add_trace(trace_sma, row=1, col=1)

    # Customize the chart layout
    fig.update_layout(
        title=f'{ticker} Stock Price and {sma_window}-Day SMA',  # Set chart title
        xaxis_title='Date',  # Label for the x-axis
        yaxis_title='Price (USD)',  # Label for the y-axis
        template='plotly_dark'  # Apply a dark theme for better visibility
    )

    return fig  # Return the figure object

if __name__ == "__main__":
    from data_fetch import get_stock_data  # Import function to fetch stock data
    from analysis import add_moving_average  # Import function to compute moving average

    # Define stock ticker symbol
    ticker = "AAPL"

    # Fetch historical stock data
    df = get_stock_data(ticker)

    # Calculate and add a 20-day simple moving average (SMA)
    df = add_moving_average(df, window=20)

    # Generate the stock price chart with SMA
    fig = create_stock_chart(df, ticker, sma_window=20)

    # Display the chart
    fig.show()
