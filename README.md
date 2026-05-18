# Market Signal Lab

A small Python/Jupyter project for market time-series analysis and simple signal testing.

The goal is to demonstrate practical Python data analysis skills: loading market data, preparing a time series, engineering basic features, testing a simple signal, and interpreting the result critically.

This is not a production trading system, live trading tool, or investment strategy.

## Market Data Trilogy

This repository is part of a small three-project portfolio focused on market data ingestion, monitoring, analysis, and signal evaluation:

- [Market Feed Monitor](https://github.com/Piotr-Gala/market-feed-monitor) — ASP.NET Core + React dashboard for market data ingestion, PostgreSQL snapshots, feed health monitoring, and alerts.
- [Market Signal Lab](https://github.com/Piotr-Gala/market-signal-lab) — Python/Jupyter project for time-series analysis, feature engineering, simple signal testing, and backtest metrics.
- [Market Snapshot Tool](https://github.com/Piotr-Gala/market-snapshot-tool) — Java CLI tool for fetching market data and calculating return and realized volatility snapshots.

## What This Project Demonstrates

- Loading market price data from CSV
- Parsing timestamps and preparing a time-series index
- Calculating returns, rolling mean, and rolling volatility
- Building a simple momentum signal
- Avoiding look-ahead bias by shifting the signal before calculating strategy returns
- Running a simplified backtest
- Calculating cumulative return, max drawdown, win rate, and a Sharpe-like metric
- Visualizing price, volatility, and strategy equity curve
- Discussing limitations instead of pretending the signal is production-ready
- Comparing simple momentum and mean reversion market patterns

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
    volatile_sample_prices.csv
  notebooks/
    market_signal_analysis.ipynb
    market_signal_analysis_volatile_sample.ipynb
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

Open and run one of the notebooks:

```text
notebooks/market_signal_analysis.ipynb
notebooks/market_signal_analysis_volatile_sample.ipynb
```

Run all cells from top to bottom.

## Notebooks

This project includes two notebooks with the same analysis workflow applied to different sample datasets:

- `market_signal_analysis.ipynb` uses a smoother trending sample dataset.
- `market_signal_analysis_volatile_sample.ipynb` uses a more volatile synthetic sample and compares momentum with mean reversion behavior.

The second notebook is included to show how the same signal testing workflow behaves under a less smooth market path.

## Notebook Overview

Each notebook:

- loads sample price data from CSV
- converts timestamps to datetime values
- sorts observations by time
- calculates returns, rolling mean, and rolling volatility
- creates a simple momentum signal
- shifts the signal by one period to avoid look-ahead bias
- calculates strategy returns and an equity curve
- reports basic backtest metrics
- visualizes price, volatility, and equity curve
- compares momentum and mean reversion results on the volatile sample

## Dataset

The included datasets are small hourly sample market price series:

- `sample_prices.csv` is a smoother illustrative price path.
- `volatile_sample_prices.csv` is a synthetic volatile sample designed to produce more visible changes in volatility, position, equity curve, and drawdown.

They are used as illustrative market time-series proxies. The purpose of the project is to demonstrate analysis workflow and backtest mechanics, not to model a specific market or claim a profitable strategy.

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
- Small illustrative datasets
- No out-of-sample validation
- No walk-forward testing
- Signal parameters are not optimized
- Results are sensitive to the selected sample data
- Not a production trading system
- Not investment advice

## Why This Project Exists

This project is intended as a compact portfolio piece for software developer internship applications at trading, energy trading, and market data companies.

It focuses on clear analysis, simple code, and honest interpretation rather than pretending to be an advanced quantitative trading system.
