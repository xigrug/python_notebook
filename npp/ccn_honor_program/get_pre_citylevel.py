# -*- coding: utf-8 -*-

"""
Created on  Dec 17 15:30:00 2017

@author: grug in xi'an
"""
import os
import pylab  as pl
import pandas  as pd
import numpy  as np
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
def plotData(X, y,ptype, plabel):
    pl.figure(1)
    #配置一下坐标刻度等 
    #xlabel=np.linspace(0,1,25)
    # You can specify a rotation for the tick labels in degrees or with keywords.
    pl.xticks(rotation='30')
    #pl.xticks(fontsize = 17)
    # Pad margins so that markers don't get clipped by the axes
    pl.margins(0.2)
    pl.plot(X, y, ptype,label=plabel) # 加上label参数添加图例
    #pl.axes(fontsize=16)
    pl.xlabel('time(BJT)',fontsize=16)
    pl.ylabel('PM10 ug/m-3',fontsize=16)
    pl.legend()  # 让图例生效 
    #pl.show()#让绘制的图像在屏幕上显示出来；注释后才能叠加到一起
    #配置一下坐标刻度等
name1=["Stid","pro","name","n","style","level","city_level","begin","end","lost","Lat","Lon","Hgt"]
station=pd.read_table('huadong-station.csv',sep=',',names=names1,skiprows=[0],index_col='Stid')
print(station.index)
filenames=[]
#OUT = pd.DataFrame(columns=['Stid','Lat','Lon','year', 'month','day','rain','rain208','rain820'])
OUT = pd.DataFrame(columns=['Stid','year', 'month', 'day', 'hour', 'tem', 'pre','wspd', 'wdir'])
search('PRE', '1980')
filenames=sorted(filenames)#;防止顺序不对
for filename in filenames:
    print(filename)
#读取txt数据
    names=['Stid','year', 'month', 'day', 'hour', 'tem', 'pre','wspd', 'wdir']
    data=pd.read_table(filename,sep='\s+',names=names,skiprows=[0],index_col='Stid',na_values=[32700])#数量不定的空格符可以用正则表达式\s+表示
    for a in station.index:
        PRE= data.loc[[a], ['Lat', 'Lon', 'Height','rain','rain208','rain820']]
        time=pd.to_datetime(data.loc[[a],['year', 'month', 'day']])
        PRE.insert(0,'citylevel',station.citylevel)
        PRE.insert(0,'Stid',station.sname)
        PRE.insert(0,'Time',time)
        OUT=pd.concat([OUT,PRE])
OUT.sort_values("Time",inplace=True)
OUT.to_csv('yrd.csv', encoding='utf-8',index=False)  
