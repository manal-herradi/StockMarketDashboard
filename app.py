import streamlit as st  # Import Streamlit for building the web application interface
import pandas as pd  # Import pandas for data manipulation
from data_fetch import get_stock_data  # Import function to fetch stock data
from analysis import add_moving_average  # Import function to calculate moving average
from visualization import create_stock_chart  # Import function to generate stock price chart

# Set up the Streamlit page configuration
st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")  # Sidebar section title

# Input field for stock ticker symbol (default: AAPL)
ticker = st.sidebar.text_input("Ticker", value="AAPL")

# Dropdown menu for selecting time period of historical data
period = st.sidebar.selectbox(
    "Period", options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=3
)

# Dropdown menu for selecting the interval between data points
interval = st.sidebar.selectbox(
    "Interval", options=["1d", "1wk", "1mo"], index=0
)

# Slider to choose the moving average window (default: 20 days)
sma_window = st.sidebar.slider(
    "Moving Average Window", min_value=5, max_value=60, value=20, step=5
)

# Display header for stock data
st.header(f"{ticker} Stock Data")

# Show loading message while fetching data
data_load_state = st.text('Loading data...')
df = get_stock_data(ticker, period=period, interval=interval)  # Fetch stock data
df = add_moving_average(df, window=sma_window)  # Calculate moving average
data_load_state.text('Loading data...done!')  # Update loading message

# Checkbox to show raw stock data if selected
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df.tail())  # Display last few rows of data

# Display stock price chart
st.subheader("Stock Price Chart")
fig = create_stock_chart(df, ticker, sma_window=sma_window)  # Create chart
st.plotly_chart(fig, use_container_width=True)  # Display chart in Streamlit
