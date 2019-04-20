# -*- coding: utf-8 -*-  
import os  
  
def listdir(path):
    a=[]  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path)  
        elif os.path.splitext(file_path)[1]==':00':  
            a=list_name.append(file_path)
        return(a) 
listname=listdir('/public/product/WrfData/wrf_seven_day/'+'20180521')
print(listname) 
