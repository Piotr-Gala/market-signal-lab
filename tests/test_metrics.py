import numpy as np
import pandas as pd

from src.metrics import (
    calculate_returns,
    calculate_max_drawdown,
    calculate_win_rate,
    calculate_sharpe_like,
)


def test_calculate_returns():
    prices = pd.Series([100, 110, 121])

    returns = calculate_returns(prices)

    expected = pd.Series([np.nan, 0.10, 0.10])
    pd.testing.assert_series_equal(returns, expected)


def test_calculate_max_drawdown():
    equity_curve = pd.Series([1.0, 1.2, 0.9, 1.1])

    max_drawdown = calculate_max_drawdown(equity_curve)

    assert max_drawdown == -0.25


def test_calculate_win_rate():
    returns = pd.Series([0.1, -0.2, 0.0, 0.3, np.nan])

    win_rate = calculate_win_rate(returns)

    assert win_rate == 0.5

def test_calculate_win_rate_empty_series():
    returns = pd.Series([np.nan, np.nan])

    win_rate = calculate_win_rate(returns)

    assert np.isnan(win_rate)


def test_calculate_sharpe_like():
    returns = pd.Series([0.01, 0.02, -0.01, 0.03])

    sharpe_like = calculate_sharpe_like(returns, periods_per_year=4)

    expected = np.sqrt(4) * returns.mean() / returns.std()

    assert sharpe_like == expected


def test_calculate_sharpe_like_zero_std():
    returns = pd.Series([0.01, 0.01, 0.01])

    sharpe_like = calculate_sharpe_like(returns)

    assert np.isnan(sharpe_like)