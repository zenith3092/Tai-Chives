# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:08:55 2023

@author: a0919
"""

import numpy as np
import bokeh as bk
import ffn
from FinMind.Data import Load
import requests
import tkinter as tk
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
 
TW2330 = investment('2330', '2010-01-01', '2012-12-31')
TW2330.MACD()
