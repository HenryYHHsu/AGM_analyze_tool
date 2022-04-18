#!/usr/bin/env python
# -*- coding: utf-8 -*-

from curses import BUTTON2_DOUBLE_CLICKED
from faulthandler import disable

import tkinter as tk  # 使用Tkinter前需要先匯入
import os
import csv

# import filedialog module
from tkinter import Frame, filedialog
#from tkinter import ttk
from turtle import width

from click import command
from matplotlib.pyplot import fill, text

# import functional file
from agm_temp import *
from agm_tgp import *
from agm_gfx_data import *
from agm_smartshift import *
from agm_gpu_workload import *
from agm_mem_temp import *
from agm_raw_data_collect import *

# global parameters
raw_data_counts=0


# file explorer window


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))

    agm_function['file_name'] = filename

    # Change label contents   
    label_file_explorer_at_file_frame.configure(text=" AGM Log File Opened: \n"+filename)

    #agm_raw_data_collect(filename)
    raw_data_counts = curent_file_counts(filename)
    agm_function['single_file_data_type']['total counts'] = raw_data_counts
    
    # agm raw data range
    agm_data_range_topic.configure(text='Choose AGM Log Data Range - Total counts : '+str(raw_data_counts))

    # Radio Button with data selected



# dropdown select menu

def selected():   
    
    current_function_val = clicked.get()
    current_file_path= agm_function['file_name']
  


    if current_file_path != '':

        if current_function_val == 'DGPU Total power (TGP)':
            tgp_plot(current_file_path)
        elif current_function_val == 'DGPU Thermal data (GPU/MEM)':
            temp_plot(current_file_path)
        elif current_function_val == 'GFX Power behavior':
            gfx_plot(current_file_path)
        elif current_function_val == 'SmartShift':
            smartshift_plot(current_file_path)
        elif current_function_val == 'GPU Workload':
            gpu_workload_plot(current_file_path)
        elif current_function_val == 'VRAM Temp on each channel (1 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,2)
        elif current_function_val == 'VRAM Temp on each channel (2 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,4)
        elif current_function_val == 'VRAM Temp on each channel (4 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,8)
        elif current_function_val == 'VRAM Temp on each channel (5 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,10)
        elif current_function_val == 'VRAM Temp on each channel (6 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,12)        
        elif current_function_val == 'VRAM Temp on each channel (8 pcs VRAM)':
            vram_temp_on_each_channel_plot(current_file_path,16)
        else:
            print('current no support')
    else:
        print ("no load file")

# data capture method
def data_range_selected():

    current_data_range_type = data_range_type.get()
    agm_function['single_file_data_type']['type']= current_data_range_type

    if current_data_range_type == 'Others':
        start_at_data.config(state='normal')
        end_at_data.config(state='normal')

    else:
        start_at_data.config(state='disabled')
        end_at_data.config(state='disabled')
        
        print('Selected ALL data')

# load AGM Data

def load_agm_data():

    if agm_function['single_file_data_type']['type'] == 'Others':
        agm_function['single_file_data_type']['select_data']= {}
        select_start_at= start_at_data.get() # data start at :
        select_end_at = end_at_data.get() # data end at :
        agm_function['single_file_data_type']['select_data'] = validate_data_range(select_start_at,select_end_at)
    else:
        agm_function['single_file_data_type']['select_data'] ='' # clean  previous data

    
    
    if agm_function['file_name']!= '':
        #agm_raw_data_collect(agm_function['file_name'],agm_function['single_file_data_type'])
        print("load file done!")

    else: # no action without explore
        print("without file")



# file load frame
def file_load():
    hide_all_frames()
    file_load_frame.pack(fill='both',expand=1)
    file_frame_topic.pack()
    label_file_explorer_at_file_frame.place(x=20,y=40)
    button_explore_at_file_frame.place(x=450,y=40)
    agm_data_range_topic.place(x=20, y=100)
    choose_all_data_buttion.place(x=20, y=150)
    choose_other_data_range_buttion.place(x=20, y=180)
    data_load_select_Button.place(x=400,y=250)
    start_at_label.place(x=30 , y=220)
    start_at_data.place(x=150,y=220)
    end_at_label.place(x=30 , y=240)
    end_at_data.place(x=150,y=240)



def hide_file_load():
    file_load_frame.pack_forget()
    file_frame_topic.pack_forget()
    label_file_explorer_at_file_frame.place_forget()
    button_explore_at_file_frame.place_forget()
    agm_data_range_topic.place_forget()
    choose_all_data_buttion.place_forget()
    choose_other_data_range_buttion.place_forget()

# single analyze frame

def single_analyze():
    hide_all_frames()
    single_file_frame.pack(fill='both',expand=1)
    single_frame_topic.pack()
    single_file_drop.place(x=20,y=200)
    single_file_plotButton.place(x=450,y=200)
    
    if agm_function['file_name']!= '':
        current_single_file_path.config(text= 'Current Load File is \n' + agm_function['file_name'])
        current_single_file_path.place(x=20,y=40)
        
        if agm_function['single_file_data_type']['type'] == 'ALL':                  
        # component place
            current_single_file_data_range.config(text='Choose Data range is Total counts : '+str(agm_function['single_file_data_type']['total counts']))
            current_single_file_data_range.place(x=20,y=100)

    else:        
        # component place
        current_single_file_path.place(x=20,y=40)
        current_single_file_data_range.place(x=20,y=100)



def hide_single_analyze():
    single_file_frame.pack_forget()


def compare_analyze():
    hide_all_frames()
    compare_file_frame.pack(fill='both',expand=1)
    compare_frame_topic.pack()




def hide_compare_analyze():
    compare_file_frame.pack_forget()


# hide all frames function

def hide_all_frames():
    hide_file_load()
    hide_single_analyze()
    hide_compare_analyze()
    

# agm function define on dictionary
agm_function= {
    'DGPU Total power (TGP)': "agm_tgp.py",
    'DGPU Thermal data (GPU/MEM)': "agm_temp.py",
    'GFX Power behavior': "agm_gfx.py",
    'SmartShift': "agm_smartshift.py",
    'GPU Workload':"agm_gpu_workload.py",
    'VRAM Temp on each channel (1 pcs VRAM)':"agm_mem_temp.py",
    'VRAM Temp on each channel (2 pcs VRAM)':"agm_mem_temp.py",
    'VRAM Temp on each channel (4 pcs VRAM)':"agm_mem_temp.py",
    'VRAM Temp on each channel (5 pcs VRAM)':"agm_mem_temp.py",
    'VRAM Temp on each channel (6 pcs VRAM)':"agm_mem_temp.py",
    'VRAM Temp on each channel (8 pcs VRAM)':"agm_mem_temp.py",
    'file_name':'',
    'single_file_data_type':{'type':'ALL','select_data':''},
}

options = [
    "DGPU Total power (TGP)",
    "DGPU Thermal data (GPU/MEM)",
    "GFX Power behavior",
    "SmartShift",
    "GPU Workload",
    'VRAM Temp on each channel (1 pcs VRAM)',
    'VRAM Temp on each channel (2 pcs VRAM)',
    'VRAM Temp on each channel (4 pcs VRAM)',
    'VRAM Temp on each channel (5 pcs VRAM)',
    'VRAM Temp on each channel (6 pcs VRAM)',
    'VRAM Temp on each channel (8 pcs VRAM)',
]



# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('Henry AGM Analyzer Tool')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('600x480')  # 這裡的乘是小x

# Set window background color
window.config(background="white")


# 第4步，在圖形介面上設定標籤
label_file_explorer= tk.Label(window, text='This is AGM analyzer file explorer', font=('Arial', 12), width=45, height=2)
#button_explore = tk.Button(window,text = "Browse Files",command = browseFiles)
#button_exit = tk.Button(window,text = "Exit",command = exit)

clicked = tk.StringVar()
clicked.set(options[0])

data_range_type=tk.StringVar()
data_range_type.set('ALL')

# # 放置label的方法有：1）l.pack(); 2)l.place();


# 建立一個選單欄，這裡我們可以把他理解成一個容器，在視窗的上方
menubar = tk.Menu(window)

# 建立一個File選單項（預設不下拉，下拉內容包括New，Open，Save，Exit功能項）
filemenu = tk.Menu(menubar, tearoff=0)
# # 將上面定義的空選單命名為File，放在選單欄中，就是裝入那個容器中
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Load file', command=file_load)
filemenu.add_command(label='Exit', command=exit)



# 建立一個Function選單項（預設不下拉，下拉內容包括Cut，Copy，Paste功能項）
functionmenu = tk.Menu(menubar, tearoff=0)
# 將上面定義的空選單命名為 Function，放在選單欄中，就是裝入那個容器中
menubar.add_cascade(label='Function', menu=functionmenu)
# 建立第二級選單，即選單項裡面的選單
function_submenu = tk.Menu(functionmenu) # 和上面定義選單一樣，不過此處實在File上建立一個空的選單
functionmenu.add_cascade(label='Select Plot type',menu=function_submenu, underline=0) # 給放入的選單submenu命名為Import

# 建立第三級選單命令，即選單項裡面的選單項裡面的選單命令
function_submenu.add_command(label='Single file analyze Plot', command=single_analyze)   # 這裡和上面建立原理也一樣，在Import選單項中加入一個小選單命令Submenu_1
function_submenu.add_command(label='Compare file analyze Plot', command=compare_analyze)   # 這裡和上面建立原理也一樣，在Import選單項中加入一個小選單命令Submenu_1


# # 第11步，建立選單欄完成後，配置讓選單欄menubar顯示出來
window.config(menu=menubar)

#label_file_explorer.place(x=20,y=40)#
#button_explore.place(x=450,y=40)#.grid(column=1,row=2)
#button_exit.place(x=500,y=300)#.grid(column=1,row=3)
#drop.place(x=20,y=100)
#plotButton.place(x=450,y=100)

# create load file frame

file_load_frame= Frame(window,width="600",height='480',bg='light blue')
label_file_explorer_at_file_frame= tk.Label(file_load_frame, text='file load frame', font=('Arial', 12), width=45, height=2)
button_explore_at_file_frame = tk.Button(file_load_frame,text = "Browse Files",command = browseFiles)

file_frame_topic= tk.Label(file_load_frame, text='File frame', font=('Arial', 12), width=45, height=1)
agm_data_range_topic = tk.Label(file_load_frame, text='Choose AGM Log Data Range - Total counts :', font=('Arial', 12), width=45, height=1)
choose_all_data_buttion=tk.Radiobutton(file_load_frame, text= 'All Data', variable=data_range_type,value='ALL',command=data_range_selected)
choose_other_data_range_buttion=tk.Radiobutton(file_load_frame, text= 'Others', variable=data_range_type,value='Others',command=data_range_selected)
start_at_label = tk.Label(file_load_frame, text='Start At :', font=('Arial', 12), width=15, height=1)
end_at_label = tk.Label(file_load_frame, text='End At :', font=('Arial', 12), width=15, height=1)
start_at_data = tk.Entry(file_load_frame, font=('Arial', 12),state='disabled')
end_at_data = tk.Entry(file_load_frame, font=('Arial', 12),state='disabled')
data_load_select_Button=tk.Button(file_load_frame,text="Load AGM Data ",command=load_agm_data)


# create function (single file) analyze frame
single_file_frame= Frame(window,width="600",height='480',bg='light green')
current_single_file_path= tk.Label(single_file_frame, text=' Without analyze File', font=('Arial', 12), width=45, height=2)
current_single_file_data_range = tk.Label(single_file_frame, text=' Without analyze File', font=('Arial', 12), width=45, height=2)
single_frame_topic= tk.Label(single_file_frame, text='Single file frame', font=('Arial', 12), width=45, height=1)
single_file_drop = tk.OptionMenu(single_file_frame,clicked,*options)
single_file_drop.config(width=40,height=1)
single_file_plotButton=tk.Button(single_file_frame,text="Plot",command=selected)

# create function (compare file) analyze frame
compare_file_frame= Frame(window,width="600",height='480',bg='light pink')
#current_single_file_path= tk.Label(single_file_frame, text=' Without analyze File', font=('Arial', 12), width=45, height=2)
# button_explore_at_file_frame = tk.Button(file_load_frame,text = "Browse Files",command = browseFiles)
compare_frame_topic= tk.Label(compare_file_frame, text='Compare file frame', font=('Arial', 12), width=45, height=1)
#single_file_drop = tk.OptionMenu(single_file_frame,clicked,*options)
#single_file_drop.config(width=40,height=1)
#single_file_plotButton=tk.Button(single_file_frame,text="Plot",command=selected)



# 第8步，主視窗迴圈顯示
window.mainloop()

# 注意，loop因為是迴圈的意思，window.mainloop就會讓window不斷的重新整理，如果沒有mainloop,就是一個靜態的window,傳入進去的值就不會有迴圈，mainloop就相當於一個很大的while迴圈，有個while，每點選一次就會更新一次，所以我們必須要有迴圈
# 所有的視窗檔案都必須有類似的mainloop函式，mainloop是視窗檔案的關鍵的關鍵。