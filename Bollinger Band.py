import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from datetime import datetime
from ipywidgets import interact
import tkinter as tk



##insert data
TW_2330 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2330.TW.csv")
TW_2303 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2303.TW.csv")
TW_2404 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2404.TW.csv")
TW_2454 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2454.TW.csv")
TW_4938 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/4938.TW.csv")

##sort out the data
#transfer the data into date form
TW_2330['Date'] = pd.to_datetime(TW_2330['Date'], format = "%Y/%m/%d")
TW_2303['Date'] = pd.to_datetime(TW_2303['Date'], format = "%Y/%m/%d")
TW_2404['Date'] = pd.to_datetime(TW_2404['Date'], format = "%Y/%m/%d")
TW_2454['Date'] = pd.to_datetime(TW_2454['Date'], format = "%Y/%m/%d")
TW_4938['Date'] = pd.to_datetime(TW_4938['Date'], format = "%Y/%m/%d")

#detect whether there are missing values
np.where(TW_2330.isna())
TW_2330.isna().sum()
np.where(TW_2303.isna())
TW_2303.isna().sum()
np.where(TW_2404.isna())
TW_2404.isna().sum()
np.where(TW_2454.isna())
TW_2454.isna().sum()
np.where(TW_4938.isna())
TW_4938.isna().sum()

#calculate simple return
TW_2330['return'] = TW_2330['Adj Close'].pct_change(1)
TW_2330['return'][0] = 0

TW_2303['return'] = TW_2303['Adj Close'].pct_change(1)
TW_2303['return'][0] = 0

TW_2404['return'] = TW_2404['Adj Close'].pct_change(1)
TW_2404['return'][0] = 0

TW_2454['return'] = TW_2454['Adj Close'].pct_change(1)
TW_2454['return'][0] = 0

TW_4938['return'] = TW_4938['Adj Close'].pct_change(1)
TW_4938['return'][0] = 0

#calculate cumulated return
TW_2330['cum.return'] = (1 + TW_2330['return']).cumprod()
TW_2303['cum.return'] = (1 + TW_2303['return']).cumprod()
TW_2404['cum.return'] = (1 + TW_2404['return']).cumprod()
TW_2454['cum.return'] = (1 + TW_2454['return']).cumprod()
TW_4938['cum.return'] = (1 + TW_4938['return']).cumprod()

#make plots of prices & MA
plt.plot(TW_2330['Date'], TW_2330['return'] )
plt.plot(TW_2330['Date'], TW_2330['Adj Close'] )
plt.plot(TW_2330['Date'], TW_2330['Adj Close'].rolling(window = 20).mean())
window = tk.Tk()
window.title('Bollinger Band')
window.geometry("1000x800+100+50")
window.mainloop()

##Bollinger Band with wondow & bottom
mu = ((((TW_2330['Adj Close'] - TW_2330['Adj Close'].rolling(window = 20).mean()) ** 2).sum())/len(TW_2330['Date'])) ** 0.5
import matplotlib
matplotlib.use('TkAgg')    
class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = tk.Entry(window)
        self.button = tk.Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()
    


    def plot (self):
        D = TW_2330['Date']
        MA = TW_2330['Adj Close'].rolling(window = 20).mean()
        UB = TW_2330['Adj Close'].rolling(window = 20).mean() + 2 * mu
        LB = TW_2330['Adj Close'].rolling(window = 20).mean() - 2 * mu
        
        plt.plot(D, TW_2330['Adj Close'].rolling(window = 20).mean(), color = "red")
        plt.plot(D, UB, color = "blue")
        plt.plot(D, LB, color = "blue")
        plt.title("Bollinger Band for 2330")
        plt.xlabel('Date')
        plt.ylabel('Adj Close')

        canvas = FigureCanvasTkAgg(tk.Figure(figsize=(8,6)), master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= tk.Tk()
start= mclass (window)
window.mainloop()

##MACD
EMA_12 = TW_2330['Adj Close'].ewm(span=12).mean()
EMA_26 = TW_2330['Adj Close'].ewm(span=26).mean()
DIF = EMA_12 - EMA_26
DEM = DIF.ewm(span=9).mean()
bar_MACD = DIF - DEM

plt.plot(TW_2330['Date'], DIF, color = "purple")
plt.plot(TW_2330['Date'], DEM, color = "yellow")

plt.title("MACD for 2330")
plt.xlabel('Date')
plt.show()



fig,ax = plt.subplots(3,1,figsize=(10,10))
plt.subplots_adjust(hspace=0.8)
EMA_12.plot(ax=ax[1])
EMA_26.plot(ax=ax[1])
TW_2330['Adj Close'].plot(ax=ax[0])
TW_2330['Adj Close'].plot(ax=ax[1])
ax[0].legend()
ax[1].legend()
DIF.plot(ax=ax[2])
DEM.plot(ax=ax[2])
ax[2].fill_between(TW_2330.Date,0,bar_MACD)
ax[2].legend()
plt.show()

##OBV


##RSI
