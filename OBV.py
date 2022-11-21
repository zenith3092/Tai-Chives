# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:28:32 2022

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
TW_2330.head()

#Create a column for OBV
OBV = []
OBV.append(0)
OBV

for i in range(1, len(TW_2330['Adj Close'])):
    if TW_2330['Adj Close'][i] > TW_2330['Adj Close'][i-1]:
        OBV.append(OBV[-1] + TW_2330['Volume'][i])
        
    elif TW_2330['Adj Close'][i] < TW_2330['Adj Close'][i-1]:
        OBV.append(OBV[-1] - TW_2330['Volume'][i])
        
    else:
        OBV.append(OBV[-1])

TW_2330['OBV'] = OBV


#Create a column for OBV's EMA (12 days)
TW_2330['EMA_OBV'] = TW_2330['OBV'].ewm(span = 12).mean()
TW_2330.head()


#Create the graph and plot
plt.figure(figsize = (10, 10))
plt.plot(TW_2330['OBV'], label = "OBV", color = "orange")
plt.plot(TW_2330['EMA_OBV'], label = "EMA for OBV", color = "purple")
plt.tilte("OBV")
plt.xlabel("Date", fontsize = 18)
plt.ylabel("On Balance Volume", fontsize = 16)
plt.show()




##strategy
def strategy(signal, col1, col2):
    sigprice_buy = []
    sigprice_sell = []
    flag = -1

    #loop through the length of data set
    for i in range(0, len(signal)):
        #col1 = OBV；col2 = EMA_OBV
        if signal[col1][i] > signal[col2][i] and flag != 1:
            sigprice_buy.append(signal['Adj Close'][i])
            sigprice_sell.append(np.nan)
            flag = 1
        
        elif signal[col1][i] < signal[col2][i] and flag != 0:
            sigprice_sell.append(signal['Adj Close'][i])
            sigprice_buy.append(np.nan)
            flag = 0
            
        else:
            sigprice_buy.append(np.nan)
            sigprice_sell.append(np.nan)
            
    return (sigprice_buy, sigprice_sell)
            
#Create buy and sell columns
x = strategy(TW_2330, 'OBV', 'EMA_OBV')
TW_2330['Buy_Signal_Price'] = x[0]
TW_2330['Sell_Signal_Price'] = x[1]

#Plot the but and sell prices
plt.figure(figsize = (10, 10))
plt.plot(TW_2330['Adj Close'], label = "Adj Close", color = "blue", alpha = 0.5)
plt.scatter(TW_2330.index, TW_2330['Buy_Signal_Price'], label = "Buy signal", color = "green", marker = '^', alpha = 1)
plt.scatter(TW_2330.index, TW_2330['Sell_Signal_Price'], label = "Sell signal", color = "red", marker = 'v', alpha = 1)
plt.tilte("Buy and Sell signals")
plt.xlabel("Date", fontsize = 18)
plt.ylabel("On Balance Volume", fontsize = 16)
plt.legend("upper left")
plt.show()




