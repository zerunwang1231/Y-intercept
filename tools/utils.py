# possible trading strategies;
# Moving Volume-Weighted Average Price: cannot be applied since there is no intraday info.
# Bollinger Bands
# Relative Strength Index
# Volume Oscillator (VO)


# if output is positive, ie, fast volume average is larger than the slow one, then it signals a strong trend
# otherwise, it signals a weak trend
def vo(vol):
    short_period = 5
    long_period = 20
    short_vol = []
    long_vol = []
    for i in range(long_period-1, len(vol)):
        window_short = vol[(i-(short_period-1)):(i+1)]
        window_long = vol[(i-(long_period-1)):(i+1)]
        short_vol.append(sum(window_short)/short_period)
        long_vol.append(sum(window_long) / long_period)
    return short_vol-long_vol

