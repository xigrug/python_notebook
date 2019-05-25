# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as CM
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import LogNorm
import os
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
#times=pd.to_datetime(filename[66:74],format='%Y%m%d')
filenames=[]
search('partposit_2015042', '.')
filenames=sorted(filenames)#;防止顺序不对
for filename in filenames:
    print(filename)
    names=['npoint','itramem','xlon', 'ylat', 'ztra1','topo', 'pvi', 'qvi', 'rhoi', 'hmix', 'tri', 'tti','xmass']
    cities=pd.read_table(filename,sep='\s+',names=names,skiprows=[1],na_values=[-9999])
    cities=cities[cities['npoint']==1]
    #print(cities)
# Extract the data we're interested in

    lat = cities['ylat'].values
    lon = cities['xlon'].values
    ccn = cities['ztra1'].values
#tcb = cities[''].values
    ccn_max=np.nanmax(ccn)
    lat_max=np.nanmax(lat)
    lon_max=np.nanmax(lon)
    lat_min=np.nanmin(lat)
    lon_min=np.nanmin(lon)
    #print(ccn_max)
    ccn_min=np.nanmin(ccn)
##print(ccn_min)
    ccn_max=np.nanmax(ccn)
#print(ccn_max)
    ccn_min=np.nanmin(ccn)
#print(ccn_min)
#tcb_max=np.nanmax(tcb)
#tcb_min=np.nanmin(tcb)
# 1. Draw the map background
    fig = plt.figure(figsize=(8, 8))
    #m = Basemap(projection='lcc', resolution='l', 
#            lat_0=31.5, lon_0=117.5,
    #        lat_0=39.04, lon_0=83.63,
    #        width=2E6, height=2E6)
    m = Basemap(llcrnrlon=65,llcrnrlat=35,urcrnrlon=95,urcrnrlat=50, epsg=4269)
#######绘制阴暗的浮雕图
#m.shadedrelief()
#m.bluemarble()
#m.etopo()
    m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
    #m.drawcoastlines(color='b')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')
#add lon lat sticks
    m.drawparallels(np.arange(30.,50,5),linewidth=1, dashes=[4, 2], labels=[1,0,0,0], color= 'gray',zorder=1, fontsize=10)
    m.drawmeridians(np.arange(70.,100.,5),linewidth=1, dashes=[4, 2], labels=[0,0,0,1], color= 'gray',zorder=1, fontsize=10)
##add shapefile
    m.readshapefile('dijishi_2004','state',color='gray')
# 2. scatter city data, with color reflecting population
# and size reflecting area

    m.scatter(lon, lat, latlon=True,
          c=ccn, 
          s=0.2,
          cmap=CM.get_cmap('jet',200), alpha=0.5)#Spectral_r
#可以有多种选择，这里我最终选择的是spectral，那个1000是热度标尺被分隔成多少块，数字越多，颜色区分越细致
# 3. create colorbar and legend
    plt.colorbar(label=r'Height/m', fraction=0.020)
    plt.clim(0,10000)

# make legend with dummy points
#for a in [-100,-75,-50,-25,0,25]:
#    plt.scatter([], [], c='k', alpha=0.5, s=(a+105),
#                label=str(a)+'')
#plt.legend(scatterpoints=1, frameon=False,
#           labelspacing=1, loc='lower left',title= 'AQI',
#           bbox_to_anchor=(,0),ncol=5)
#plt.legend(scatterpoints=1, frameon=False,
#           labelspacing=1, loc='lower left',title= 'Tcbtemp',
#           bbox_to_anchor=(0,-0.15,1,0.2),
#           mode="expand", borderaxespad=0, ncol=7)
#plt.title("2015/JULY", fontsize=20)
#plt.show()
    #plt.savefig(filename[12:22]+'.png',dpi=600)
    plt.savefig(filename[12:22]+'_testmap.png')

