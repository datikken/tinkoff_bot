from talib import RSI
import numpy as np

#low value buy when 31 from bottom
#high value sell when 69 from top
def get_rsi_index(candles):
    close = []
    for candle in candles:
        close.append(float(candle.close.units))

    return RSI(
        np.array(close),
        timeperiod=14
    )
