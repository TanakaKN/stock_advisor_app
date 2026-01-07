import yfinance as yf
import pandas as pd


def load_stock_data(
    ticker: str,
    period: str = "2y",
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Fetch historical stock price data.

    Args:
        ticker (str): Stock ticker symbol (e.g. 'AAPL')
        period (str): Data period (default: last 2 years)
        interval (str): Data interval (default: daily)

    Returns:
        pd.DataFrame: Cleaned historical stock data
    """

    if not isinstance(ticker, str) or len(ticker.strip()) == 0:
        raise ValueError("Ticker symbol must be a non-empty string.")

    ticker = ticker.upper().strip()

    try:
        data = yf.download(
            ticker,
            period=period,
            interval=interval,
            progress=False
        )
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data for {ticker}: {e}")

    if data.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'.")

    # Keep only required columns
    data = data[["Close"]].copy()

    # Drop missing values
    data.dropna(inplace=True)

    if len(data) < 60:
        raise ValueError(
            f"Not enough historical data for {ticker}. "
            f"At least 60 data points required."
        )

    return data
