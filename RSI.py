# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:04:08 2022

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
TW_2330['DIF'] = TW_2330['Adj Close'].diff()


def U_calc(num):
    if num >= 0:
        return num
    else:
        return 0

def D_calc(num):
    num = -num
    return U_calc(num)

TW_2330['U'] = TW_2330['DIF'].apply(U_calc)
TW_2330['D'] = TW_2330['DIF'].apply(D_calc)
TW_2330.head()

TW_2330['EMA_U'] = TW_2330['U'].ewm(span = 14).mean()
TW_2330['EMA_D'] = TW_2330['D'].ewm(span = 14).mean()
TW_2330.head()
TW_2330 = TW_2330['2021-10-01':]

TW_2330['RS'] = TW_2330['EMA_U'].div(TW_2330['EMA_D'])
TW_2330['RSI'] = TW_2330['RS'].apply(lambda rs: rs / (1 + rs) * 100)
TW_2330.head()

plt.figure(figsize = (10,10))
plt.plot(TW_2330['RSI'])
plt.plot(TW_2330.index, [70] * len(TW_2330.index))
plt.plot(TW_2330.index, [30] * len(TW_2330.index))
plt.legend()
plt.show()
