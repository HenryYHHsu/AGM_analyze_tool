# !/usr/bin/env python

import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import MultipleLocator

# create GFX dictionary
GFX_keys = {
    'VDDCR_GFX Voltage': 'GPU0 Telemetry Telemetry Voltage VDDCR_GFX', # GPU0 Telemetry Telemetry Voltage VDDCR_GFX
    'VDDCR_GFX Power': 'GPU0 Telemetry Telemetry Power VDDCR_GFX', # GPU0 Telemetry Telemetry Power VDDCR_GFX
    'VDDCR_GFX Current': 'GPU0 Telemetry Telemetry Current VDDCR_GFX',# GPU0 Telemetry Telemetry Current VDDCR_GFX
    'VDDCR_GFX GFXCLK': 'GPU0 Frequencies Actual Frequency GFXCLK', # GPU0 Frequencies Actual Frequency GFXCLK
}

GFX= dict()

def gfx_plot(data_path):
    # 開啟 CSV 檔案
    with open(data_path, newline='') as csvfile:

        for key, value in GFX_keys.items():
            GFX[key]=[]

        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # 以迴圈輸出每一列
        for row in rows:
            for key, value in GFX_keys.items():
                GFX[key].append(row[value])



        # for example : GFX Voltage

        gfx_voltage_real_data= np.array(GFX['VDDCR_GFX Voltage'][:-1])
        gfx_voltage_real_data_float= gfx_voltage_real_data.astype(np.float)

        # for example : GFX Power

        gfx_power_real_data= np.array(GFX['VDDCR_GFX Power'][:-1])
        gfx_power_real_data_float= gfx_power_real_data.astype(np.float)

        # for example : GFX Current

        gfx_current_real_data= np.array(GFX['VDDCR_GFX Current'][:-1])
        gfx_current_real_data_float= gfx_current_real_data.astype(np.float)

        # for example : GFXCLK

        gfx_clk_real_data= np.array(GFX['VDDCR_GFX GFXCLK'][:-1])
        gfx_clk_real_data_float= gfx_clk_real_data.astype(np.float)


        # DGPU GFX curve


        fig, ax=plt.subplots(3,1,figsize=(10,10))
        fig.suptitle(" DGPU GFX Power rail behavior") 


        ax[0].plot(gfx_power_real_data_float,c='green', label='GFX Power')
        ax[0].set_ylabel('Power(W)')
        ax[0].legend(loc=1)
        ax[0].grid()

        ax[1].plot(gfx_current_real_data_float,c='red',label='GFX Current')
        ax[1].set_ylabel('Current(A)')
        ax[1].legend(loc=1)
        ax[1].grid()

        ax[2].plot(gfx_clk_real_data_float,c='blue',label='GFXCLK')
        ax[2].set_xlabel('data of numbers')
        ax[2].set_ylabel('GFXCLK (Hz)')
        ax[2].legend(loc=1)
        ax[2].grid()

        plt.show()