import numpy as np
import pandas as pd


def calculate_returns(prices: pd.Series) -> pd.Series:
    """Calculate percentage returns from a price series."""
    return prices.pct_change()


def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    """Calculate the maximum drawdown of an equity curve."""
    running_max = equity_curve.cummax()
    drawdown = equity_curve / running_max - 1
    return drawdown.min()


def calculate_win_rate(returns: pd.Series) -> float:
    """Calculate the share of positive returns."""
    valid_returns = returns.dropna()

    if len(valid_returns) == 0:
        return np.nan

    return (valid_returns > 0).mean()


def calculate_sharpe_like(
    returns: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Calculate a simplified annualized Sharpe-like metric.

    This does not include a risk-free rate and should not be interpreted
    as a full Sharpe ratio.
    """
    valid_returns = returns.dropna()

    if len(valid_returns) == 0 or valid_returns.std() == 0:
        return np.nan

    return np.sqrt(periods_per_year) * valid_returns.mean() / valid_returns.std()
