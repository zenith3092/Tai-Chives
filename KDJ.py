# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:26:28 2022

@author: a0919
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

TW_2330 = pd.read_csv("C:/Users/a0919/Desktop/github/Tai-Chives/data/2330.TW.csv")
TW_2330 = TW_2330.set_index(pd.to_datetime(TW_2330['Date'], format = "%Y/%m/%d"))
TW_2330 = TW_2330.drop('Date', axis = 1)
TW_2330['Close'] = pd.to_numeric(TW_2330['Close'])

span = 9
RSV = []
for i in range((span - 1), (len(TW_2330['Close']))):
    numb = [i, i-1, i-2, i-3, i-4, i-5, i-6, i-7, i-8]
    RSV.append((TW_2330['Close'][i] - np.min(TW_2330['Low'][numb]))/(np.max(TW_2330['High'][numb]) - np.min(TW_2330['Low'][numb]))*100)
    
K = [50]
D = [50]
J = []
for i in range(len(RSV)-1):
    K.append(((2/3) * K[i] +((1/3) * RSV[i])))
    D.append(((2/3) * D[i] +((1/3) * K[i+1])))
    J.append(3*D[i] - 2*K[i])
    
             



