import pandas as pd

from src.signals import momentum_signal, mean_reversion_signal


def test_momentum_signal():
    returns = pd.Series([0.01, 0.02, -0.01, -0.03, 0.04])

    signal = momentum_signal(returns, window=2)

    expected = pd.Series([0, 1, 1, -1, 1])
    pd.testing.assert_series_equal(signal, expected)


def test_mean_reversion_signal():
    z_score = pd.Series([-1.5, -0.5, 0.0, 0.8, 1.2])

    signal = mean_reversion_signal(z_score, entry_threshold=1.0)

    expected = pd.Series([1, 0, 0, 0, -1])
    pd.testing.assert_series_equal(signal, expected)