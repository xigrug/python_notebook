##https://blog.csdn.net/lsq2902101015/article/details/51305825
##https://www.cnblogs.com/rohero/p/6145736.html
import os, sys

# 打开文件
path = "/public/product/WrfData/wrf_seven_day/20180521/"
import os
list_name=[]   
def listdir(path, list_name): 
    for file in os.listdir(path): 
        file_path = os.path.join(path, file) 
        if os.path.isdir(file_path): 
            listdir(file_path, list_name) 
        #else:
        elif os.path.splitext(file_path)[0][47:57]=='wrfout_d01': 
        #else:
            #print(os.path.splitext(file_path)[0][0:10])
            list_name.append(file_path)
    return list_name
listdir(path,list_name)
list_name = sorted(list_name)           #列表排序
#list_name = list(set(list_name))        #列表去重复
print(list_name)
print(len(list_name))
