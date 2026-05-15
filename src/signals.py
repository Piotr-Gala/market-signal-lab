import pandas as pd


def momentum_signal(returns: pd.Series, window: int = 12) -> pd.Series:
    """
    Generate a simple momentum signal.

    Long when rolling return is positive, short when rolling return is negative.
    """
    momentum = returns.rolling(window).sum()

    signal = pd.Series(0, index=returns.index)
    signal[momentum > 0] = 1
    signal[momentum < 0] = -1

    return signal


def mean_reversion_signal(
    z_score: pd.Series,
    entry_threshold: float = 1.0,
) -> pd.Series:
    """
    Generate a simple mean reversion signal.

    Long when price is below its rolling mean, short when it is above.
    """
    signal = pd.Series(0, index=z_score.index)

    signal[z_score < -entry_threshold] = 1
    signal[z_score > entry_threshold] = -1

    return signal
