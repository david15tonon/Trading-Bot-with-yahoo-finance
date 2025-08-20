
# 📄 Python Trading Bot with Yahoo Finance Demo

## Overview
This project is a **Python-based trading bot prototype** designed as a proof of concept (POC) for algorithmic trading applications.  
It retrieves stock market data, applies a **Moving Average Crossover strategy**, generates buy/sell signals, and evaluates the performance of the strategy compared to the market.

The goal is to demonstrate the ability to work with financial data, implement trading logic, and build scalable components for a trading platform.

---

## Features
- 📈 **Data Retrieval**: Fetches historical stock data using the `yfinance` library.  
- ⚡ **Trading Strategy**: Implements a **Simple Moving Average (SMA) Crossover** strategy (20-day SMA vs 50-day SMA).  
- 🛠️ **Backtesting Engine**: Simulates trades and calculates cumulative returns.  
- 📊 **Visualization**: Displays stock price with SMA indicators.  
- ✅ **Easy to Extend**: Can be integrated with broker APIs (e.g., Alpaca, Tradovate) for live trading.  

---

## Requirements
Make sure you have Python **3.8+** installed.  

Install the required dependencies:  
```bash
pip install yfinance pandas matplotlib
````

---

## Usage

1. Clone or download this project.
2. Run the script:

   ```bash
   python trading_bot_demo.py
   ```
3. The bot will:

   * Download Apple’s stock data (2024 by default).
   * Apply SMA crossover strategy.
   * Plot stock price with SMA lines.
   * Print total strategy return in the terminal.

---

## Example Output

**Graph:**

* Blue line: Stock closing price
* Orange line: 20-day SMA
* Green line: 50-day SMA

Crossovers indicate buy/sell signals.

**Console output example:**

```
Total Strategy Return: 1.153
```

(This means the strategy yielded a \~15.3% return over the selected period.)

---

## File Structure

```
trading_demo/
│
├── trading_bot_demo.py    # Main trading script
├── README.md              # Documentation
```

---

## Strategy Explanation

The strategy used is **Moving Average Crossover**:

* **Buy Signal:** When the short-term SMA (20 days) crosses above the long-term SMA (50 days).
* **Sell Signal:** When the short-term SMA crosses below the long-term SMA.

This is a classical technical analysis strategy used by many traders to capture trend changes.

---

## Next Steps (Possible Extensions)

* 🔌 Connect to live trading APIs (e.g., Alpaca, Interactive Brokers, Tradovate).
* 🤖 Add advanced strategies (RSI, Bollinger Bands, MACD).
* 📡 Enable real-time streaming data handling.
* 💾 Store trade logs and results in a database.

