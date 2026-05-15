# Market Signal Lab

A small Python/Jupyter project for market time-series analysis and simple signal testing.

The goal is to demonstrate practical Python data analysis skills: loading market data, preparing a time series, engineering basic features, testing a simple signal, and interpreting the result critically.

This is not a production trading system, live trading tool, or investment strategy.

## What This Project Demonstrates

- Loading market price data from CSV
- Parsing timestamps and preparing a time-series index
- Calculating returns, rolling mean, and rolling volatility
- Building a simple momentum signal
- Running a simplified backtest
- Calculating cumulative return, max drawdown, win rate, and a Sharpe-like metric
- Visualizing price, volatility, and strategy equity curve
- Discussing limitations instead of pretending the signal is production-ready

## Tech Stack

- Python
- Jupyter Notebook
- pandas
- NumPy
- matplotlib

## Project Structure

```text
market-signal-lab/
  README.md
  requirements.txt
  data/
    sample_prices.csv
  notebooks/
    market_signal_analysis.ipynb
  src/
    metrics.py
    signals.py
```

## How To Run

Create a virtual environment:

```powershell
python -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open and run the notebook:

```text
notebooks/market_signal_analysis.ipynb
```

Run all cells from top to bottom.

## Notebook Overview

The notebook:

- loads sample price data from `data/sample_prices.csv`
- converts timestamps to datetime values
- sorts observations by time
- calculates returns, rolling mean, and rolling volatility
- creates a simple momentum signal
- shifts the signal by one period to avoid look-ahead bias
- calculates strategy returns and an equity curve
- reports basic backtest metrics
- visualizes price, volatility, and equity curve

## Dataset

The included dataset is a small hourly sample market price series.

It is used as an illustrative market time-series proxy. The purpose of the project is to demonstrate analysis workflow and backtest mechanics, not to model a specific energy market or claim a profitable strategy.

## Example Metrics

The notebook calculates:

- cumulative return
- maximum drawdown
- win rate
- Sharpe-like metric

The Sharpe-like metric is simplified and does not include a risk-free rate. It should not be interpreted as a full professional Sharpe ratio.

## Limitations

- Simplified execution model
- No order book, liquidity, slippage, or market impact modeling
- Transaction costs are not included
- Small illustrative dataset
- No out-of-sample validation
- No walk-forward testing
- Signal parameters are not optimized
- Results are sensitive to the sample data
- Not a production trading system
- Not investment advice

## Why This Project Exists

This project is intended as a compact portfolio piece for software developer internship applications at trading, energy trading, and market data companies.

It focuses on clear analysis, simple code, and honest interpretation rather than pretending to be an advanced quantitative trading system.
