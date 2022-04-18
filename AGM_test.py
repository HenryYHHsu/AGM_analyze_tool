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

# create smartshift dictionary

  smartshift = dict()
  smartshift['fPPT']=[]
  smartshift['sPPT']=[]
  smartshift['APU_only']=[]
  

# 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)

# 以迴圈輸出每一列
  for row in rows:
    smartshift['fPPT'].append(row['CPU0 INFRASTRUCTURE Value PPT FAST'])
    smartshift['sPPT'].append(row['CPU0 INFRASTRUCTURE Value PPT SLOW'])    
    smartshift['APU_only'].append(row['CPU0 INFRASTRUCTURE Value PPT APU ONLY'])


# for example : fPPT

fppt_real_data= np.array(smartshift['fPPT'][:-1])
fppt_real_data_float= fppt_real_data.astype(np.float)

# for example : sPPT

sppt_real_data= np.array(smartshift['sPPT'][:-1])
sppt_real_data_float= sppt_real_data.astype(np.float)

# for example : APU only 

apu_only_real_data= np.array(smartshift['APU_only'][:-1])
apu_only_real_data_float= apu_only_real_data.astype(np.float)


# fppt/sppt/apu only curve
plt.title("Smartshift Curve with fppt/sppt/apu only") 
plt.xlabel('data of numbers')
plt.ylabel('TGP(W)')
plt.plot(fppt_real_data_float,c='green', label='fppt')
plt.plot(sppt_real_data_float,c='red',label='sppt')
plt.plot(apu_only_real_data_float,c='gray',label='apu only')

x_major_locator=MultipleLocator(200)
y_major_locator=MultipleLocator(25)
ax=plt.gca()

ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.legend()
plt.show()
