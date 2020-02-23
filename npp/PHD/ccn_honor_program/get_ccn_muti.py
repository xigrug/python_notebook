# coding: utf-8
'''
 [https://www.cnblogs.com/bjwu/p/8970818.html](https://www.cnblogs.com/bjwu/p/8970818.html)
 [https://blog.csdn.net/qq_16234613/article/details/78245325](https://blog.csdn.net/qq_16234613/article/details/78245325)
 [pandas 判断某列状态变化](https://blog.csdn.net/xinming31/article/details/80267516)
 [Pandas “diff()” with string](https://stackoverflow.com/questions/40348541/pandas-diff-with-string)
'''
import os
import pylab  as pl
import pandas  as pd
import numpy  as np
import math
import datetime
def get_mean(a):
    number=a.size
    down=math.ceil(number*0.25)
    top=math.floor(number*0.75)
    print(number)
    print(number)
    print(top)
    if number> 50:
        average=a[down-1:top-1].mean()
        return average
def time_mean(a):
    b=pd.to_datetime(a).dropna().astype(np.int64)
    number=a.size
    down=math.ceil(number*0.25)
    top=math.floor(number*0.75)
    print(number)
    print(number)
    print(top)
    if number> 50:
        average=b[down-1:top-1].mean()
        time_ave=pd.to_datetime(average,format='%Y-%m-%d %H:%M:%S')
        time_ave=datetime.datetime.strftime(time_ave,"%Y-%m-%d %H:%M:%S")
        return time_ave

def search(s, path=os.path.abspath('.')):  #os.path.abspath(path)：绝对路径

    for z in os.listdir(path):
        if os.path.isdir(path + os.path.sep + z):  # os.path.sep:路径分隔符 linux下就用这个了’/’
            #print('Currnet:', path)
            path2 = os.path.join(path, z) #；os.path.join(): 常用来链接路径
            #print('future:', path2)
            search(s, path2)
        elif os.path.isfile(path + os.path.sep + z): #检验给出的路径是否是一个文件：os.path.isfile()来自 <http://blog.csdn.net/devil_2009/article/details/7941241>
            if s in z:
                #print(os.path.join(path, z))
                filenames.append(os.path.join(path, z))
                #with open(path + os.path.sep + z, 'r') as fr:
                #    with open('save.txt', 'a') as fw:
                #        fw.write(path + '\t' + fr.read())

filenames=[]
#OUT = pd.DataFrame(columns=['Stid','Lat','Lon','year', 'month','day','rain','rain208','rain820'])
OUT = pd.DataFrame()
search('ccn_100', '.')
filenames=sorted(filenames)#;防止顺序不对
for filename in filenames:
    data=pd.read_csv(filename,sep=',',skiprows=[0,1,2,3])
    print(filename[15:23])
    data['diff_or'] = (data[" Current SS"].diff().ne(0)).astype(int)
    data['labels'] = data['diff_or'].cumsum()
    data=data.sort_values(by=['    Time'],na_position='first')
# #df=data.groupby(["labels"])[' CCN Number Conc'].agg([get_mean])
    da=data.groupby(["labels"]).agg({' CCN Number Conc':[get_mean],' Current SS':["mean"],'    Time':[time_mean]})
#读取txt数据
    times=pd.to_datetime(filename[15:23],format='%y%m%d%H')
    print(times)
    da.insert(0,'DATE',times)
    #time=pd.to_datetime(data.loc[[a],['year', 'month', 'day']])
    #PRE.insert(0,'Date',a)
    OUT=pd.concat([OUT,da])
OUT.sort_values(by=['DATE','    Time'],inplace=True)
OUT.to_csv('NUIST_CCN_ave.csv', encoding='utf-8',index=False)

