#!/usr/bin/env python
# coding: utf-8
# https://stackoverflow.com/questions/9775297/append-a-numpy-array-to-a-numpy-array
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
#import matplotlib.colors as colors
#import matplotlib as mpl
from dateutil.relativedelta import *
import datetime as dt
import os
import glob
#import cartopy.crs as ccrs
def search(s, path=os.path.abspath('.')):  #os.path.abspath(path)：绝对路径
    filenames=[]
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
    return filenames

days =[str(x)[1:3]  for x in np.arange(101,132,1)] 
print(days)
for day in days:
    #filenames=search(day+'.grd', '.')
    filenames = glob.glob(r'*'+day+'??.grd')
    #Don't use os/re. Use glob.glob as the way to do it.
    print(filenames)
    try:
        filenames
        filenames=sorted(filenames)#;防止顺序不对
        l=np.zeros(shape=(440,700,0))
        for filename in filenames:
            data=np.fromfile(filename,dtype=np.float32)
            data=data.reshape(2,440,700)
            pre=np.maximum(data[0,:,:],0)
            #np.savetxt(filename[4:]+'utc.csv',pre,delimiter=',')
            utc_time=dt.datetime.strptime(filename[42:52], "%Y%m%d%H")
            #draw_cmorph(pre)
            #l=[l]
            l = np.dstack((l,pre))
        print(l.shape)
        out_max=np.max(l,axis=2)
        b=np.zeros((440, 700),dtype=np.int)
        for i in range(440):
            for j in range(700):
                ll=l[i,j,:]
                arg=np.argmax(ll)
                b[i,j]=arg 
        #print(np.where(a==np.max(l,axis=1)))
        print(out_max.shape)
        print(b.shape)
        #out_max=np.max(l,axis=2)
        out_max.tofile(filename[:-6]+'_day_max.grd')
        b.tofile(filename[:-6]+'_day_argmax.grd')
        #np.savetxt(hour+'utc_max.csv',out_max,delimiter=',')
    except:
        continue
