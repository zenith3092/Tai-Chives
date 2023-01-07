# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:21:43 2022

@author: a0919
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import pandas_datareader as pdr

TW_2330 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2330.TW.csv")
TW_2330 = TW_2330.set_index(pd.to_datetime(TW_2330['Date'], format = "%Y/%m/%d"))
TW_2330 = TW_2330.drop('Date', axis = 1)
TW_2330['Adj Close'] = pd.to_numeric(TW_2330['Adj Close'])
TW_2330['Close'] = pd.to_numeric(TW_2330['Close'])
TW_2330['High'] = pd.to_numeric(TW_2330['High'])
TW_2330['Low'] = pd.to_numeric(TW_2330['Low'])

TR = []
ATR = []
H_L = []
C_H = []
C_L = []

for i in range(1, len(TW_2330['Close'])):
    H_L.append(TW_2330['High'][i] - TW_2330['Low'][i])
    C_H.append(np.abs(TW_2330['Close'][i-1] - TW_2330['High'][i]))
    C_L.append(np.abs(TW_2330['Close'][i-1] - TW_2330['Low'][i]))
    ATR.append(max(H_L[i], C_H[i], C_L[i]))
     
 
    
 
    
 
    
 
#another way
H_L = TW_2330['High'] - TW_2330['Low']
C_H = np.abs(TW_2330['High'] - TW_2330['Close'].shift())
C_L = np.abs(TW_2330['Low'] - TW_2330['Close'].shift())

TR = np.max(pd.concat([H_L, C_H, C_L], axis = 1), axis = 1)
ATR = TR.rolling(14).mean()

fig, ax = plt.subplots()
ATR.plot(ax = ax)
ax2 = TW_2330['Close'].plot(ax = ax, secondary_y = True, alpha = .5)
ax.set_ylabel("ATR")
ax2.set_ylabel("Close Price")