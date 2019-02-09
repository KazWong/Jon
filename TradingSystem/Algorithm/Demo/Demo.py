from ..Template import Template
from ..Library.DailyPct import DailyPct

import pandas as pd

class Model(Template):
  def __init__(self, returns):
    super(Model, self).__init__(returns)
    self.dmi_plus = self.px['DMI_PLUS']
    self.dmi_minus = self.px['DMI_MINUS']
    self.px_last = self.px['PX_LAST']
    self.bb_ma = self.px['BB_MA']
    self.macd_diff = self.px['MACD_DIFF']
    self.trender_up = self.px['TRENDER_UP']
    self.trender_down = self.px['TRENDER_DN']
    self.tas_k = self.px['TAS_K']
    self.tas_d = self.px['TAS_D']
    self.ema_5 = self.px['EMA(5)']
    self.ema_20 = self.px['EMA(20)']
  
    self.px_open = self.px['PX_OPEN']
    self.px_last = self.px['PX_LAST']
    self.cap_dail_p = DailyPct(self.px['PX_LAST'])
    
  def Core(self):
    score = []
    capital = [100]
    buy = sell = 0
    status = 0
  
    for i in xrange(self.dmi_plus.size-1) :
      score.append(0)
      #cap_dail_p.append(0)
      if i>0:
        capital.append(capital[i-1])
      if (self.dmi_plus[i] > self.dmi_minus[i]) :
        score[i] += 1
      elif (self.dmi_plus[i] < self.dmi_minus[i]) :
        score[i] -= 1
      if (self.px_last[i] > self.bb_ma[i]) :
        score[i] += 1
      elif (self.px_last[i] < self.bb_ma[i]) :
        score[i] -= 1
      if (self.macd_diff[i] > 0) :
        score[i] += 2
      elif (self.macd_diff[i] < 0) :
        score[i] -= 2
      if (self.trender_up[i] == "#N/A N/A") :
        score[i] += 1
      if (self.trender_down[i] == "#N/A N/A") :
        score[i] -= 1
      if (self.tas_k[i] > self.tas_d[i]) :
        score[i] += 1
      elif (self.tas_k[i] < self.tas_d[i]) :
        score[i] -= 1
      if (self.ema_5[i] > self.ema_20[i]) :
        score[i] += 1
      elif (self.ema_5[i] > self.ema_20[i]) :
        score[i] -= 1
      
      if (status == 1):
        capital[i] = capital[i] * self.cap_dail_p[i]
      
      if (score[i] >= 4 and status == 0):
        buy = i
        status = 1
      if (score[i] <= -4 and status == 1):
        sell = i
        status = 0
        #capital[i] = capital[i] * cap_dail_p[i]
    
    return score, capital, self.cap_dail_p
