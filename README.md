# Stock Market Dashboard

## Overview

This project is a Stock Market Dashboard built with Python that retrieves, analyzes, and visualizes historical stock data. It uses libraries such as yfinance for data retrieval, pandas for data manipulation, Plotly for interactive visualization, and Streamlit for the web interface. The dashboard offers an interactive way to explore stock price trends and moving averages.

## Context and Background

A **stock price** is the cost of buying one share of a company. It fluctuates based on **supply and demand**, company performance, and broader economic events. Each trading day, a stock shows:
- **Open Price:** The first price at which the stock trades during the day.
- **High Price:** The maximum price achieved during the day.
- **Low Price:** The minimum price reached during the day.
- **Close Price:** The final price at the end of the trading day.

A **moving average** smooths out price fluctuations by calculating the average **Close Price** over a set period (e.g., 20 days). This helps identify trends—rising averages can indicate an uptrend, while falling averages may suggest a downtrend.

## Project Structure

The project is organized into the following key components:
- **Data Fetching Module:** Retrieves historical stock data using yfinance.
- **Analysis Module:** Processes the data and calculates metrics such as the moving average.
- **Visualization Module:** Creates interactive charts to display the stock's closing price and moving average.
- **Dashboard Application:** An interactive Streamlit app that ties everything together, allowing users to adjust parameters like ticker symbol, period, and moving average window.

## Installation and Setup

### Clone the Repository

Clone the project from GitHub:
```bash
git clone https://github.com/manal-herradi/StockMarketDashboard.git
cd StockMarketDashboard
```

### Setup Virtual Environment

Create and activate a Python virtual environment (recommended):

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Install Dependencies

Install the required packages listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## How to Use It

1. **Fetch and Analyze Data:**
   - The project automatically retrieves historical stock data for a specified ticker, computes the moving average based on your settings, and prepares the data for visualization.

2. **Run the Dashboard:**
   - Launch the interactive dashboard with Streamlit:
     ```bash
     streamlit run app.py
     ```
   - This opens your web browser with the dashboard, where you can:
     - Enter a ticker symbol (e.g., AAPL).
     - Select the desired time period and interval.
     - Adjust the moving average window using the sidebar.
     - View interactive charts and raw data.

3. **Interact with the Dashboard:**
   - Use the sidebar to change input parameters.
   - Check the "Show Raw Data" option to view the underlying data in a table.
   - The dashboard updates the interactive chart accordingly.

## Screenshots

- **Data Visualization:**  
  An interactive chart displaying the stock's closing price and its moving average.  
  ![Data Visualization](https://github.com/manal-herradi/images/blob/main/screenshot_dashboard_home.png)

- **Raw Data Display:**  
  A table view of the raw stock data retrieved for analysis.  
  ![Raw Data](https://github.com/manal-herradi/images/blob/main/screenshot_raw_data.png)

## Conclusion

This project provides a practical introduction to financial data analysis and interactive dashboard development. By combining real-time data retrieval, analysis, and visualization, it offers insights into stock market trends and aids in the understanding of technical analysis.
