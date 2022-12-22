import statistics
import numpy as np
# possible trading strategies;
# Moving Volume-Weighted Average Price: cannot be applied since there is no intraday info.
# Bollinger Bands
# Relative Strength Index
# Volume Oscillator (VO)


# if output is positive, ie, fast volume average is larger than the slow one, then it signals a strong trend
# otherwise, it signals a weak trend
# set fast period to be 5 days, long period to be 20 days
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
    return np.arr(short_vol-long_vol)

# Bollinger Band; set the time period to be 20 days
def bb(price):
    window_size = 20
    m = 2 # set scale to be 2
    ma = []
    sd = []
    for i in range(window_size-1, len(price)):
        window = price[(i-(window_size-1)):(i+1)]
        ma.append((sum(window) / window_size))
        sd.append(statistics.stdev(window))
    # upper line
    bolu = np.arr(ma)+m*np.arr(sd)
    bold = np.arr(ma)-m*np.arr(sd)
    return bolu, bold
