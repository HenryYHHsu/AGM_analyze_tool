#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.base64mime import header_encode
import os
import glob
import csv
import pandas as pd
import numpy as np
import json


def agm_raw_data_collect(data_path,data_type):
    
    #pm_log_raw_data=dict()

    with open(data_path, encoding='utf-8') as csvfile:
    # path = os.getcwd()

    # reading the csv file using DictReader
    #  #csv_reader = csv.DictReader(csvfile) # raw data
     agm_raw_data_df=pd.read_csv(csvfile,sep=',')
     #output_path = r'/home/pi/Desktop/python/agm_data.json'
     agm_raw_data = agm_raw_data_df.to_json("single_agm_log.json", orient = "records")
     agm_raw_data_json = agm_raw_data_df.to_json(orient = "records")
     agm_raw_data=json.loads(agm_raw_data_json)
     print("json-------------------------")


def curent_file_counts(data_path):

    num_rows = 0

    for row in open(data_path):
        num_rows += 1
    
    return num_rows

    
def validate_data_range(start_at,end_at):

    data_range = {'status':True}

    if start_at.isdigit() & end_at.isdigit():

        if 0 < int(start_at) < int(end_at):
            data_range['range']= [int(start_at),int(end_at)]
        else:
            data_range['status'] = False
    else:
        data_range['status'] = False

    
    return data_range

