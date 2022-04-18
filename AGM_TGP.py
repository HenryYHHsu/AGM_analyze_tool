# !/usr/bin/env python

import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import MultipleLocator


# create TGP dictionary
TGP_keys = {
    'TGP Power': 'GPU0 Power TGP Power', #  GFX + SOC + MEM0 + MEM1 + ROC_PWR + XGMI POWER
    'PPT0 limit': 'GPU0 PPT PPT0 Limit', # GPU0 PPT PPT0 Limit
    'PPT0 value': 'GPU0 PPT PPT0 Value',# GPU0 PPT PPT0 Value
    'RocPower': 'GPU0 Power Rest of Chip Power', # VDDCI + other small rails
    'XgmiPower': 'GPU0 Power XGMI Power', # XGMI POWER 
}

TGP_dataset= dict()

def tgp_plot(data_path):
    
    # 開啟 CSV 檔案
     with open(data_path, newline='') as csvfile:

    # create TGP dataset dictionary
     
      for key, value in TGP_keys.items():
        
        TGP_dataset[key]=[]
     
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
      rows = csv.DictReader(csvfile)

    # 以迴圈輸出每一列
      for row in rows:
         for key, value in TGP_keys.items():
          TGP_dataset[key].append(row[value])

    # for example : TGP Power

     tgp_real_data= np.array(TGP_dataset['TGP Power'][:-1])
     tgp_real_data_float= tgp_real_data.astype(np.float)

    # for example : ROC Power

     roc_real_data= np.array(TGP_dataset['RocPower'][:-1])
     roc_real_data_float= roc_real_data.astype(np.float)

    # for example : Xgmi Power

     xgmi_real_data= np.array(TGP_dataset['XgmiPower'][:-1])
     xgmi_real_data_float= xgmi_real_data.astype(np.float)


    # DGPU TGP(W) curve

     plt.title(" DGPU Curve with TGP / Roc / Xgmi Power ") 
     plt.xlabel('data of numbers')
     plt.ylabel('Watt (W)')
     plt.plot(tgp_real_data_float, label='TGP Power')
     plt.plot(roc_real_data_float,label='Roc Power')
     plt.plot(xgmi_real_data_float,label='Xgmi POwer')
     plt.grid()

     x_major_locator=MultipleLocator(200)
     y_major_locator=MultipleLocator(25)
     ax=plt.gca()

     ax.xaxis.set_major_locator(x_major_locator)
     ax.yaxis.set_major_locator(y_major_locator)

     plt.legend(loc=1)
     plt.show()