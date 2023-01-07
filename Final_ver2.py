# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:16:52 2022

@author: a0919
"""
##import packages
import numpy as np
import bokeh as bk
import ffn
from FinMind.Data import Load
import requests
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk 
from pandas_datareader import data
import psycopg2 as sql



url = 'https://api.finmindtrade.com/api/v4/data?'

class investment:
    def __init__(self, symbol, start, end):
        parameter = {
            "dataset" : "TaiwanStockPrice",
            "data_id" : symbol,
            "start_date" : start,
            "end_date" : end
            }
        data_ver1 = (requests.get(url, params = parameter)).json()
        self.data = pd.DataFrame(data_ver1["data"])
        self.data = self.data.set_index(pd.to_datetime(self.data['date'], format = "%Y/%m/%d"))
        self.data = self.data.drop('date', axis = 1)
        
    def BBand(self):
        MA = self.data['close'].rolling(window = 20).mean()
        SD = self.data['close'].rolling(window = 20).std()
        UB = MA + 2 * SD
        LB = MA - 2 * SD
        
        win = tk.Tk()
        win.title('MACD')
        win.geometry('200x200')
        plt.style.use('tableau-colorblind10')
        plt.plot(self.data.index, MA, color = "red")
        plt.plot(self.data.index, UB, color = "purple")
        plt.plot(self.data.index, LB, color = "yellow")
        plt.title("Bollinger Band")
        plt.xlabel('date')
        plt.ylabel('close')
        plt.show()
        win.mainloop()

        
    def MACD(self):
        self.data['EMA_12'] = self.data['close'].ewm(span=12).mean()
        self.data['EMA_26'] = self.data['close'].ewm(span=26).mean()
        self.data['DIF'] = self.data['EMA_12'] - self.data['EMA_26']
        self.data['DEM'] = self.data['DIF'].ewm(span=9).mean()
        self.data['bar_MACD'] = self.data['DIF'] - self.data['DEM']

        win = tk.Tk()
        win.title('MACD')
        win.geometry('200x200')
        fig,ax = plt.subplots(2,1,figsize=(10,10))
        plt.subplots_adjust(hspace=0.8)
        self.data['EMA_12'].plot(ax=ax[0], color = "purple")
        self.data['EMA_26'].plot(ax=ax[0], color = "yellow")
        self.data['close'].plot(ax=ax[0], color = "blue")
        ax[0].legend()
        self.data['DIF'].plot(ax=ax[1])
        self.data['DEM'].plot(ax=ax[1])
        ax[1].fill_between(self.data.index,0,self.data['bar_MACD'])
        ax[1].legend()
        plt.show()
        win.mainloop()
        
    def RSI(self):
        def U_calc(num):
            if num >= 0:
                return num
            else:
                return 0

        def D_calc(num):
            num = -num
            return U_calc(num)
        
        U = self.data['spread'].apply(U_calc)
        D = self.data['spread'].apply(D_calc)
        
        self.data['EMA_U'] = U.ewm(span = 14).mean()
        self.data['EMA_D'] = D.ewm(span = 14).mean()
        
        self.data['RS'] = self.data['EMA_U'].div(EMA_D)
        self.data['RSI'] = self.data['RS'].apply(lambda rs: rs / (1 + rs) * 100)
        
        plt.figure(figsize = (10,10))
        plt.plot(RSI)
        plt.plot(self.data.index, [70] * len(self.date))
        plt.plot(self.data.index, [30] * len(self.date))
        plt.legend()
        plt.show()
        
    def OBV(self):
        
    def KDJ(self):
        
    def ATR(self):
        
    def ADX(self):
        
    def CCI(self):
        
    def Parabolic_SAR(self):
        
    def DMI(self):
        
    def bias(self):
        
        
        
TW2330 = investment('2330', '2010-01-01', '2012-12-31')
TW2357 = investment('2357', '2010-01-01', '2012-12-31')


