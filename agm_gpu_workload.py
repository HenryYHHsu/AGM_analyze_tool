# !/usr/bin/env python

import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import MultipleLocator

gpu_workload_keys = {
    'TGP Power': 'GPU0 Power TGP Power', # GPU0 Power TGP Power -> GFX + SOC + MEM0 + MEM1 + ROC_PWR + XGMI POWER
    'GPU_Default_Workload': 'GPU0 Workload Default', # GPU idle state
    'GPU_Active_Workload': 'GPU0 Workload Active',# GPU active state
    'GPU_Compute_Workload': 'GPU0 Workload Compute', # GPU compute state
    'GPU_FullScreen3D_Workload': 'GPU0 Workload Full screen 3D' # GPU FullScreen3D state
}

gpu_workload= dict()


def gpu_workload_plot(data_path):
    # 開啟 CSV 檔案
    with open(data_path, newline='') as csvfile:
        for key, value in gpu_workload_keys.items():
            gpu_workload[key]=[]

        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # 以迴圈輸出每一列
        for row in rows:
            for key, value in gpu_workload_keys.items():
                gpu_workload[key].append(row[value])
                
        # for example : TGP

        tgp_real_data= np.array(gpu_workload['TGP Power'][:-1])
        tgp_real_data_float= tgp_real_data.astype(np.float)

        # for example : GPU Default Workload

        workload_default_real_data= np.array(gpu_workload['GPU_Default_Workload'][:-1])
        workload_default_real_data_float= workload_default_real_data.astype(np.float)

        # for example : GPU Active Workload

        workload_active_real_data= np.array(gpu_workload['GPU_Active_Workload'][:-1])
        workload_active_real_data_float= workload_active_real_data.astype(np.float)


        # for example : GPU Compute Workload

        workload_compute_real_data= np.array(gpu_workload['GPU_Compute_Workload'][:-1])
        workload_compute_real_data_float= workload_compute_real_data.astype(np.float)


        # for example : GPU Full Screen 3D Workload

        workload_fullscreen3D_real_data= np.array(gpu_workload['GPU_FullScreen3D_Workload'][:-1])
        workload_fullscreen3D_real_data_float= workload_fullscreen3D_real_data.astype(np.float)




        # GPU Workload curve

        fig, ax=plt.subplots(2,1,figsize=(10,10))
        fig.suptitle(" DGPU Workload Behavior") 


        ax[0].plot(tgp_real_data_float, label='DGPU TGP Power')
        ax[0].set_ylabel('Power(W)')
        ax[0].legend(loc=1)
        ax[0].grid()

        ax[1].plot(workload_default_real_data_float,c='red',label='GPU Default Workload')
        ax[1].plot(workload_active_real_data_float,c='green',label='GPU Active Workload')
        ax[1].plot(workload_compute_real_data_float,c='orange',label='GPU Compute Workload')
        ax[1].plot(workload_fullscreen3D_real_data_float,c='purple',label='GPU FullScreen3D Workload')
        ax[1].legend(loc=1)
        ax[1].grid()

        #plt.legend()
        plt.show()