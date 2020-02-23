# -*- coding: utf-8 -*-
#https://stackoverflow.com/questions/26760975/skiprows-list-not-working-in-pandas-read-csv
#https://stackoverflow.com/questions/48063612/read-multiple-txt-files-to-multiple-dataframes-and-concate-later-all-dataframes
#https://stackoverflow.com/questions/21441259/pandas-groupby-range-of-values
#https://stackoverflow.com/questions/46938572/pandas-groupby-mean-into-a-dataframe
#https://stackoverflow.com/questions/39254704/pandas-group-bins-of-data-per-longitude-latitude
#https://stackoverflow.com/questions/48454689/python-average-of-multiple-columns-and-rows
#######################
import glob
import pandas as pd
import numpy as np
import os
#from datetime import datetime

ccn_data = pd.read_csv('all_pc_weather.csv', sep=',',skiprows=0,header=0,na_values=[9999])
pc_data = pd.read_csv('JJA_PPT-all-diff.csv', sep=',',skiprows=0,header=0,na_values=[9999])
ccn_data["DATE"]=pd.to_datetime(ccn_data.DATE)
pc_data["DATE"]=pd.to_datetime(pc_data.DATE)
print(pc_data["DATE"])
print(ccn_data["DATE"])
data_out=pd.merge(ccn_data,pc_data,how="inner")
data_out.to_csv("all_pc_weather-ok.csv",index=False,sep=',')

