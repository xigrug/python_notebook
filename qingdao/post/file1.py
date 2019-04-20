# -*- coding: utf-8 -*-   
  
import os  
  
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            #if os.path.splitext(file)[1] == ':00':  
            L.append(os.path.join(root, file))  
    return L
wrffile=file_name('/product/WrfData/wrf_seven_day/20180521/')
print(wrffile)
