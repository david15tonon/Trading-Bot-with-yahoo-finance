# 📄 Python Trading Bot with yahoo finance Demo

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
