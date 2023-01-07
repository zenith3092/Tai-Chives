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
        data = (requests.get(url, params = parameter)).json()
        self.data = pd.DataFrame(data["data"])
        self.date = pd.to_datetime(self.data.date, format = "%Y/%m/%d")
        self.Open = self.data.open
        self.High = self.data.max
        self.Low = self.data.min
        self.Close = self.data.close
        self.Volumn = self.data.Trading_Volume
        self.Turnover = self.data.Trading_turnover
        self.spread = self.data.spread
    
    def BBand(self):
        MA = self.Close.rolling(window = 20).mean()
        SD = self.Close.rolling(window = 20).std()
        UB = MA + 2 * SD
        LB = MA - 2 * SD
        
        plt.style.use('tableau-colorblind10')
        plt.plot(self.date, MA, color = "red")
        plt.plot(self.date, UB, color = "purple")
        plt.plot(self.date, LB, color = "yellow")
        plt.title("Bollinger Band")
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.show()

        
    def MACD(self):
        EMA_12 = self.Close.ewm(span=12).mean()
        EMA_26 = self.Close.ewm(span=26).mean()
        DIF = EMA_12 - EMA_26
        DEM = DIF.ewm(span=9).mean()
        bar_MACD = DIF - DEM

        fig,ax = plt.subplots(2,1,figsize=(10,10))
        plt.subplots_adjust(hspace=0.8)
        EMA_12.plot(ax=ax[0], color = "purple")
        EMA_26.plot(ax=ax[0], color = "yellow")
        Close.plot(ax=ax[0], color = "blue")
        ax[0].legend()
        DIF.plot(ax=ax[1])
        DEM.plot(ax=ax[1])
        ax[1].fill_between(self.data.index,0,bar_MACD)
        ax[1].legend()
        plt.show()
        
    def RSI(self):
        
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


