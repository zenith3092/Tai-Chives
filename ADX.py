# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:55:55 2022

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


#TR caiculation
span = 14
H_L = TW_2330['High'] - TW_2330['Low']
C_H = np.abs(TW_2330['High'] - TW_2330['Close'].shift())
C_L = np.abs(TW_2330['Low'] - TW_2330['Close'].shift())

TR = np.max(pd.concat([H_L, C_H, C_L], axis = 1), axis = 1)
ATR = TR.rolling(span).mean()


#DM calcuiation
PDM = TW_2330['High'] - TW_2330['High'].shift()
NDM = TW_2330['Low'].shift() - TW_2330['Low']

for i in range(len(PDM)):
    if PDM[i] < 0 or PDM[i] < NDM[i]:
        PDM[i] = 0
for i in range(len(NDM)):
    if NDM[i] < 0 or PDM[i] > NDM[i]:
        NDM[i] = 0

#DI calculation
PDI = (PDM.rolling(span).mean()/ATR)*100
NDI = (NDM.rolling(span).mean()/ATR)*100
ADX = (np.abs(PDI - NDI).rolling(span).mean()/(PDI + NDI))*100



