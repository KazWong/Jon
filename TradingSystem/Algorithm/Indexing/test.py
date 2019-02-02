import MovingAverage
from MovingAverage import M as MA

t = MovingAverage.M(1)
MovingAverage.da = [2,2,2,2]
print t.data
print t.SMA([1])
print MovingAverage.da

MA(1)
print MA(2).data
print MA(1).DaDa()
