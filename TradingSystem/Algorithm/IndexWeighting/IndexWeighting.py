import sys
sys.path.append('../')

from AlgoTemplate.AlgoTemplate import Algorithm

class IndexWeighting(Algorithm):
  def __int__(self):
    self.data = 1
  def Out(self):
    return 222

def trading_system(returns) :
  score = []
  capital = [100]
  cap_daily_p = [0]*returns.size
  
  dmi_plus = returns['DMI_PLUS']
  dmi_minus = returns['DMI_MINUS']
  px_last = returns['PX_LAST']
  bb_ma = returns['BB_MA']
  macd_diff = returns['MACD_DIFF']
  trender_up = returns['TRENDER_UP']
  trender_down = returns['TRENDER_DN']
  tas_k = returns['TAS_K']
  tas_d = returns['TAS_D']
  ema_5 = returns['EMA(5)']
  ema_20 = returns['EMA(20)']
  
  px_open = returns['PX_OPEN']
  px_last = returns['PX_LAST']
  cap_dail_p = returns['PX_LAST']/returns['PX_LAST'].shift(1)
  cap_dail_p[0] = 1.0
  
  buy = sell = 0
  status = 0
  
  for i in xrange(dmi_plus.size-1) :
    score.append(0)
    #cap_dail_p.append(0)
    if i>0:
      capital.append(capital[i-1])
    if (dmi_plus[i] > dmi_minus[i]) :
      score[i] += 1
    elif (dmi_plus[i] < dmi_minus[i]) :
      score[i] -= 1
    if (px_last[i] > bb_ma[i]) :
      score[i] += 1
    elif (px_last[i] < bb_ma[i]) :
      score[i] -= 1
    if (macd_diff[i] > 0) :
      score[i] += 2
    elif (macd_diff[i] < 0) :
      score[i] -= 2
    if (trender_up[i] == "#N/A N/A") :
      score[i] += 1
    if (trender_down[i] == "#N/A N/A") :
      score[i] -= 1
    if (tas_k[i] > tas_d[i]) :
      score[i] += 1
    elif (tas_k[i] < tas_d[i]) :
      score[i] -= 1
    if (ema_5[i] > ema_20[i]) :
      score[i] += 1
    elif (ema_5[i] > ema_20[i]) :
      score[i] -= 1
      
    if (status == 1):
      capital[i] = capital[i] * cap_dail_p[i]
      
    if (score[i] >= 4 and status == 0):
      buy = i
      status = 1
    if (score[i] <= -4 and status == 1):
      sell = i
      status = 0
      #capital[i] = capital[i] * cap_dail_p[i]
    
  return score, capital, cap_dail_p
