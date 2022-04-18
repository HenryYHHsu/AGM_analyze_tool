# !/usr/bin/env python

import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import MultipleLocator

#首先去讀目前資料夾的檔案有多少


#os.chdir(os.getlogin()+'/Desktop/data') # 切換路徑到指定資料夾
#os.chdir('/home/'+os.getlogin()+'/Desktop/data') # 切換路徑到指定資料夾
path = os.getcwd()
#file_lists = glob.glob(r'*.csv')


print("------------------------")
print("現在的檔案位置:"+ path)
print("------------------------")

file_path= path+'/test.csv'

# 開啟 CSV 檔案
with open(file_path, newline='') as csvfile:

# create DGPU degree dictionary

  Temperature = dict()
  Temperature['TGP Power']=[] #GPU0 Power TGP Power
  Temperature['Temp Hotspot']=[] #GPU0 Temperature Hotspot 
  Temperature['VDDCR_GFX GFXCLK']=[] #GPU0 Frequencies Actual Frequency GFXCLK

# 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)

# 以迴圈輸出每一列
  for row in rows:
    Temperature['TGP Power'].append(row['GPU0 Power TGP Power'])
    Temperature['Temp Hotspot'].append(row['GPU0 Temperature Hotspot'])    
    Temperature['VDDCR_GFX GFXCLK'].append(row['GPU0 Frequencies Actual Frequency GFXCLK'])

# for example : TGP Power

tgp_power_real_data= np.array(Temperature['TGP Power'][:-1])
tgp_power_real_data_float= tgp_power_real_data.astype(np.float)

# for example : DGPU Temp

dgpu_temp_real_data= np.array(Temperature['Temp Hotspot'][:-1])
dgpu_temp_real_data_float= dgpu_temp_real_data.astype(np.float)

# for example : GFXCLK

gfx_clk_real_data= np.array(Temperature['VDDCR_GFX GFXCLK'][:-1])
gfx_clk_real_data_float= gfx_clk_real_data.astype(np.float)


# DGPU GFX curve

# plt.title(" DGPU Curve with TGP Power/PPT0 limit/ PPT0 value ") 
# plt.xlabel('data of numbers')
# plt.ylabel('TGP(W)')
# plt.plot(tgp_real_data_float,c='green', label='TGP Power')
# plt.plot(ppt0_limit_real_data_float,c='red',label='PPT0 Limit')
# plt.plot(ppt0_value_real_data_float,c='gray',label='PPT0 Value')

# x_major_locator=MultipleLocator(200)
# y_major_locator=MultipleLocator(25)
# ax=plt.gca()

# ax.xaxis.set_major_locator(x_major_locator)
# ax.yaxis.set_major_locator(y_major_locator)


fig, ax=plt.subplots(3,1)
fig.suptitle(" DGPU Power/Thermal/CLK") 


ax[0].plot(tgp_power_real_data_float,c='green', label='DGPU Power')
#ax[0].set_xlabel('data of numbers')
ax[0].set_ylabel('Power(W)')
ax[0].grid()

ax[1].plot(dgpu_temp_real_data_float,c='red',label='DGPU Temp')
#ax[1].set_xlabel('data of numbers')
ax[1].set_ylabel('Degree(C)')
ax[1].grid()

# ax[2].plot(gfx_voltage_real_data_float,c='blue',label='GFX Voltage')
# ax[2].set_xlabel('data of numbers')
# ax[2].set_ylabel('Voltage(V)')

ax[2].plot(gfx_clk_real_data_float,c='blue',label='GFXCLK')
ax[2].set_xlabel('data of numbers')
ax[2].set_ylabel('GFXCLK (Hz)')
ax[2].grid()

plt.legend()
plt.show()