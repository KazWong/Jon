import MovingAverage
import DailyPct
from MovingAverage import M as MA

################################################
'''
t = MovingAverage.M(1)
MovingAverage.da = [2,2,2,2]
print t.data
print t.SMA([1])
print MovingAverage.da

MA(1)
print MA(2).data
print MA(1).DaDa()
'''
################################################
px_last = [100,101,102.01,103,105]
print DailyPct.DailyPct(px_last)
