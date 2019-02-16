import pandas as pd

def DailyPct(_px_last):
  tmp = pd.DataFrame(_px_last)
  px_last = tmp/tmp.shift(1) - 1
  px_last.iloc[0,0] = 0.0
  return px_last.iloc[:, 0].tolist()
