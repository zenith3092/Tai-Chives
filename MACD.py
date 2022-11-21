# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:24:57 2022

@author: a0919
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

TW_2330 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2330.TW.csv")
TW_2330 = TW_2330.set_index(pd.to_datetime(TW_2330['Date'], format = "%Y/%m/%d"))
TW_2330 = TW_2330.drop('Date', axis = 1)
TW_2330['Adj Close'] = pd.to_numeric(TW_2330['Adj Close'])

TW_2330['EMA_12'] = TW_2330['Adj Close'].ewm(span=12).mean()
TW_2330['EMA_26'] = TW_2330['Adj Close'].ewm(span=26).mean()
TW_2330['DIF'] = TW_2330['EMA_12'] - TW_2330['EMA_26']
TW_2330['DEM'] = TW_2330['DIF'].ewm(span=9).mean()
TW_2330['bar_MACD'] = TW_2330['DIF'] - TW_2330['DEM']
TW_2330 = TW_2330['2021-11-01':]


fig,ax = plt.subplots(2,1,figsize=(10,10))
plt.subplots_adjust(hspace=0.8)
TW_2330['EMA_12'].plot(ax=ax[0], color = "purple")
TW_2330['EMA_26'].plot(ax=ax[0], color = "yellow")
TW_2330['Adj Close'].plot(ax=ax[0], color = "blue")
ax[0].legend()
TW_2330['DIF'].plot(ax=ax[1])
TW_2330['DEM'].plot(ax=ax[1])
ax[1].fill_between(TW_2330.index,0,TW_2330['bar_MACD'])
ax[1].legend()
plt.show()
