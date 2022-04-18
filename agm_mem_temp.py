# !/usr/bin/env python

from cProfile import label
import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import MultipleLocator


def vram_temp_on_each_channel_plot(data_path,channel_count):

    # 開啟 CSV 檔案
    with open(data_path, newline='') as csvfile:

        # create VRAM Temp  dictionary

        vram_temp= dict()
        vram_temp['Average Temp']=[]
        vram_temp_on_each_channel_data={}

        for i in range(channel_count):
          vram_temp['VRAM Temp Ch'+str(i)] = []  #  CH0-Ch015 GPU0 Temperature MEM_0

        
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # # 以迴圈輸出每一列
        for row in rows:

           vram_temp['Average Temp'].append(row['GPU0 Temperature Hotspot'])
           
           for i in range(channel_count):
               vram_temp['VRAM Temp Ch'+str(i)].append(row['GPU0 Temperature MEM_'+str(i)])

        # for example : MEM Average

        vram_average_real_data= np.array(vram_temp['Average Temp'][:-1])
        vram_average_data_float= vram_average_real_data.astype(np.float)

        fig, ax=plt.subplots(2,figsize=(10,10),constrained_layout=True)
        fig.suptitle(" VRAM Temp on each channel ")

        ax[0].plot(vram_average_data_float,'g', label='VRAM Average Degree')
        ax[0].set_ylabel('Degree(C)')
        ax[0].grid()
        ax[0].legend()

        # for example : VRAM temp on each channel
        for i in range(channel_count):
          vram_raw_data = np.array(vram_temp['VRAM Temp Ch'+str(i)][:-1])
          vram_temp_on_each_channel_data[i]= vram_raw_data.astype(np.float)

          ax[1].plot(vram_temp_on_each_channel_data[i],label='VRAM Ch'+str(i))
          ax[1].set_ylabel('Degree(C)')
          ax[1].legend()
 
        ax[1].grid()
        plt.show()