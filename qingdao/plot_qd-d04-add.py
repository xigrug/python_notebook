# -*- coding: utf-8 -*-

"""
Created on  Dec 17 15:30:00 2017

@author: grug in xi'an
"""
import os
import sys
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('agg') #deactivate matplotlib x11 backend #5
import pandas  as pd
import numpy  as np
import matplotlib.dates as dates
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
def plotData(ax,x,y,ptype):
    times=pd.to_datetime(x,format='%Y-%m-%d_%H_%M_%S')
    ax.xaxis.set_minor_locator(dates.DayLocator(interval=2))
    ax.xaxis.set_minor_formatter(dates.DateFormatter('%m-%d'))
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('\n'))

    ax.xaxis.grid(True, which="minor",color='lightgray', linestyle='-.', linewidth=0.2)
    ax.yaxis.grid(True, which="major",color='lightgray', linestyle='-.', linewidth=0.2)
    ax.tick_params(axis='both', which='major', labelsize=4)
    ax.tick_params(axis='both', which='minor', labelsize=4)
    ax.spines['top'].set_visible(False)  #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框`
    xx=times.to_pydatetime()
    ax.plot(xx, y,ptype,alpha=0.6,markersize=1,linewidth=1) # 加上label参数添加图例 no color

def plotDatah(ax,x,y,ptype):
    times=pd.to_datetime(x,format='%Y-%m-%d_%H_%M_%S')
    ax.xaxis.set_minor_locator(dates.DayLocator(interval=2))
    ax.xaxis.set_minor_formatter(dates.DateFormatter('%m-%d'))
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('\n'))

    ax.xaxis.grid(True, which="minor",color='lightgray', linestyle='-.', linewidth=0.2)
    ax.yaxis.grid(True, which="major",color='lightgray', linestyle='-.', linewidth=0.2)
    ax.tick_params(axis='both', which='major', labelsize=4)
    ax.tick_params(axis='both', which='minor', labelsize=4)
    ax.spines['top'].set_visible(False)  #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框`
    xx=times.to_pydatetime()
    #ax.plot(xx, y,ptype,alpha=0.6,markersize=1,linewidth=1) # 加上label参数添加图例 no color
    ax.bar(xx, y, 0.05,alpha=0.8,color='b') # 加上label参数添加图例 no color


def plot1station(value,base,ytext,ptype):
    data=pd.read_table(base,sep='\s+',skiprows=1,names=["BJC","SITE","U10","V10","W","T2","SLP","RH2","RAIN","CLFRL","CLFRT","SWDN"])#数量不定的空格符可以用正则表达式\s+表示
    print(data.head())
    zhfont1 = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc')
    data.set_index(['BJC','SITE'], inplace=True)
    data["T2"]=data["T2"]-273.15
    station= [
              u'qingdao',u'shinanxi',u'shibeinan',u'shibeibei',
              u'licangbei',u'laoshanxi',u'chengyangbei',u'huangdaodong1',u'qingdao' 
             ]
    stationcn= [
              u'青岛',u'市南西',u'市北南',u'市北北',
              u'李沧北',u'崂山西',u'城阳北',u'黄岛东1',u"青岛" 
             ]
    plt.switch_backend('agg')#deactivate matplotlib x11 backend #5
    fig, ax= plt.subplots(1, 1, figsize=(6,3))
    fig.subplots_adjust(left=0.1, bottom=0.08, right=0.9, top=0.96,hspace=0.3, wspace=0.2)
    t="WRF Weather Forecast\nAtmospheric Environment Research Center\nNanjing University"
    fig.suptitle(t,fontsize=6,x=0.53,y=1.1)
    #axes=(ax1, ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9)
    for i in range(0,1):
        stat='SITE=="{stat_name}"'
        sta=stat.format(stat_name=station[i])
        print(sta)
        plotData(ax,data.index.levels[0],data.query(sta)[value],ptype)#注意下站点对不对应
        #axes[i].set_title(station[i],fontsize=4,loc='left')
        ax.annotate(stationcn[i], xy=(0.8, 1.0), xycoords="axes fraction",fontsize=6,fontproperties=zhfont1)
    #fig.text(0.05, 0.5, r'%s'%ytext, va='center', rotation='vertical',fontsize=4,fontproperties=zhfont1)
    fig.text(0.5, -0.02, 'Time(BJT)', ha='center',fontsize=6)
    plt.savefig(value+'_qd04new.png',dpi=300,bbox_inches='tight')
    plt.close()

def plot1stationh(value,base,ytext,ptype):
    data=pd.read_table(base,sep='\s+',skiprows=1,names=["BJC","SITE","U10","V10","W","T2","SLP","RH2","RAIN","CLFRL","CLFRT","SWDN"])#数量不定的空格符可以用正则表达式\s+表示
    print(data.head())
    zhfont1 = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc')
    data.set_index(['BJC','SITE'], inplace=True)
    data["T2"]=data["T2"]-273.15
    station= [
              u'qingdao',u'shinanxi',u'shibeinan',u'shibeibei',
              u'licangbei',u'laoshanxi',u'chengyangbei',u'huangdaodong1',u'qingdao' 
             ]
    stationcn= [
              u'青岛',u'市南西',u'市北南',u'市北北',
              u'李沧北',u'崂山西',u'城阳北',u'黄岛东1',u"青岛" 
             ]
    plt.switch_backend('agg')#deactivate matplotlib x11 backend #5
    fig, ax= plt.subplots(1, 1, figsize=(6,3))
    fig.subplots_adjust(left=0.1, bottom=0.08, right=0.9, top=0.96,hspace=0.3, wspace=0.2)
    t="WRF Weather Forecast\nAtmospheric Environment Research Center\nNanjing University"
    fig.suptitle(t,fontsize=6,x=0.53,y=1.1)
    #axes=(ax1, ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9)
    for i in range(0,1):
        stat='SITE=="{stat_name}"'
        sta=stat.format(stat_name=station[i])
        print(sta)
        plotDatah(ax,data.index.levels[0],data.query(sta)[value],ptype)#注意下站点对不对应
        #axes[i].set_title(station[i],fontsize=4,loc='left')
        ax.annotate(stationcn[i], xy=(0.8, 1.0), xycoords="axes fraction",fontsize=6,fontproperties=zhfont1)
    #fig.text(0.05, 0.5, r'%s'%ytext, va='center', rotation='vertical',fontsize=4,fontproperties=zhfont1)
    fig.text(0.5, -0.02, 'Time(BJT)', ha='center',fontsize=6)
    plt.savefig(value+'_qd04new.png',dpi=300,bbox_inches='tight')
    plt.close()

def plot24station(value,base,ytext,ptype):
    data=pd.read_table(base,sep='\s+',skiprows=1,names=["BJC","SITE","U10","V10","W","T2","SLP","RH2","RAIN","CLFRL","CLFRT","SWDN"])#数量不定的空格符可以用正则表达式\s+表示
    print(data.head())
    data.set_index(['BJC','SITE'], inplace=True)
    data["T2"]=data["T2"]-273.15
    station=[ 
           u'shinandong',u'shinanxi',u'shibeinan', u'shibeibei',u'licangbei',u'licangnan',u'licangdong',
           u'laoshanxi', u'laoshanzhong', u'laoshandong',u'chengyangbei',u'chengyangnan',
           u'huangdaodong1',u'huangdaodong2',u'jimo1',u'jimo2',u'jiaozhou1',u'jiaozhou2',
           u'huangdaoxi1',u'huangdaoxi2',u'pingdu1',u'pingdu2',u'laixi1',u'laixi2'  
             ]
    plt.switch_backend('agg')#deactivate matplotlib x11 backend #5
    fig, ((ax1, ax2,ax3), (ax4, ax5,ax6),(ax7,ax8,ax9),(ax10, ax11,ax12),(ax13, ax14,ax15),(ax16, ax17,ax18),(ax19, ax20,ax21),(ax22, ax23,ax24))= plt.subplots(8, 3, sharex='col', sharey='row',figsize=(6,3))
    fig.subplots_adjust(left=0.1, bottom=0.08, right=0.9, top=0.96,hspace=0.3, wspace=0.2)
    t="WRF Weather Forecast\nAtmospheric Environment Research Center\nNanjing University"
    fig.suptitle(t,fontsize=6,x=0.53,y=1.1)
    axes=(ax1, ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13,ax14,ax15,ax16,ax17,ax18,ax19,ax20,ax21,ax22,ax23,ax24)
    for i in range(0,24):
        stat='SITE=="{stat_name}"'
        sta=stat.format(stat_name=station[i])
        print(sta)
        plotData(axes[i],data.index.levels[0],data.query(sta)[value],'r^-')#注意下站点对不对应
        #axes[i].set_title(station[i],fontsize=4,loc='left')
        axes[i].annotate(station[i], xy=(0.8, 1.0), xycoords="axes fraction",fontsize=4)
    fig.text(0.02, 0.5, r'%s'%ytext, va='center', rotation='vertical',fontsize=6)
    fig.text(0.5, -0.02, 'Time(BJT)', ha='center',fontsize=6)
    plt.savefig(value+'_qd04.png',dpi=300,bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot1station("T2","d04_mete.txt","2m Temperature (Du)",'r^-')
    plot1station("RH2","d04_mete.txt","2m RH (%)",'gs-')
    plot1station("SWDN","d04_mete.txt","SWDN (W/m^2)",'r^-')
    plot1stationh("RAIN","d04_mete.txt","RAIN (mm/h)",'b.-')
    plot1station("CLFRL","d04_mete.txt",u"低云量",'c2-')
    plot1station("CLFRT","d04_mete.txt",u"总云量",'b2-')
