
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --------- CONFIG ----------
TICKER = "AAPL"   # Apple stock
START = "2024-01-01"
END = "2024-12-31"
SHORT_WINDOW = 20
LONG_WINDOW = 50
# ---------------------------

def download_data():
    data = yf.download(TICKER, start=START, end=END)
    data['SMA20'] = data['Close'].rolling(window=SHORT_WINDOW).mean()
    data['SMA50'] = data['Close'].rolling(window=LONG_WINDOW).mean()
    return data

def backtest(data):
    # Generate signals
    data['Signal'] = 0
    data.loc[data['SMA20'] > data['SMA50'], 'Signal'] = 1
    data.loc[data['SMA20'] < data['SMA50'], 'Signal'] = -1

    # Calculate returns
    data['Market_Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Market_Returns'] * data['Signal'].shift(1)
    return data

def plot_results(data):
    import matplotlib
    matplotlib.use("Agg")  # backend non interactif
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12,6))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA20'], label='SMA20')
    plt.plot(data['SMA50'], label='SMA50')
    plt.legend()
    plt.title(f"Trading Strategy Demo on {TICKER}")
    plt.savefig("strategy_plot.png")

if __name__ == "__main__":
    df = download_data()
    df = backtest(df)
    plot_results(df)
    print("Total Strategy Return:", (df['Strategy_Returns']+1).prod())
