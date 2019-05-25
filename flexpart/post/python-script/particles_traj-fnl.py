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
filename_fnl="trajectories.txt"
search('partposit_20150421120000', '.')
filenames=sorted(filenames)#;防止顺序不对
for filename in filenames:
    print(filename)
    data=pd.read_table(filename_fnl,sep='\s+',header=None,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])#数量不定的空格符可以用正>则表达式\s+表示 
    names=['npoint','itramem','xlon', 'ylat', 'ztra1','topo', 'pvi', 'qvi', 'rhoi', 'hmix', 'tri', 'tti','xmass']
    cities=pd.read_table(filename,sep='\s+',names=names,skiprows=[1],na_values=[-9999])
    cities=cities[cities['npoint']==1]
    #print(cities)
# Extract the data we're interested in
    lont=data.iloc[0::4,2]
    latt=data.iloc[0::4,3]
    heightt=data.iloc[0::4,4]
    lon1t=data.iloc[1::4,2]
    lat1t=data.iloc[1::4,3]
    height1t=data.iloc[1::4,4]
    lon2t=data.iloc[2::4,2]
    lat2t=data.iloc[2::4,3]
    height2t=data.iloc[2::4,4]
    lon3t=data.iloc[3::4,2]
    lat3t=data.iloc[3::4,3]
    height3t=data.iloc[3::4,4]

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
    m = Basemap(llcrnrlon=75,llcrnrlat=35,urcrnrlon=90,urcrnrlat=45, epsg=4269)
    #m = Basemap(projection='lcc', resolution='l', 
#            lat_0=31.5, lon_0=117.5,
    #        lat_0=39.04, lon_0=83.63,
    #        width=4E6, height=4E6)
#######绘制阴暗的浮雕图
#m.shadedrelief()
#m.bluemarble()
#m.etopo()
    m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
    m.drawcoastlines(color='b')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')
#add lon lat sticks
    m.drawparallels(np.arange(30.,45,5),linewidth=1, dashes=[4, 2], labels=[1,0,0,0], color= 'gray',zorder=1, fontsize=10)
    m.drawmeridians(np.arange(70.,90.,10),linewidth=1, dashes=[4, 2], labels=[0,0,0,1], color= 'gray',zorder=1, fontsize=10)
##add shapefile
    m.readshapefile('dijishi_2004','state',color='gray')
# 2. scatter city data, with color reflecting population
# and size reflecting area

    m.scatter(lon, lat, latlon=True,
          c=ccn, 
          s=0.2,
          cmap=CM.get_cmap('terrain',200), alpha=0.5)
#可以有多种选择，这里我最终选择的是spectral，那个1000是热度标尺被分隔成多少块，数字越多，颜色区分越细致
# 3. create colorbar and legend
    plt.colorbar(label=r'Height/m', fraction=0.046)
    plt.clim(0,(ccn_max//1000+1)*1000)
    x, y = m(np.array(lont), np.array(latt))
    m.scatter(x, y, s=1, marker='o',alpha=0.8)
    m.scatter(x[0], y[0], c='r',s=16, marker='8',edgecolors='none',alpha=1)
    #markerfacecolor='none',above line is not work
    #m.scatter(x, y, marker='o',makersize=1,alpha=0.1)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(height.min(), height.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    # Set the values used for colormapping
    lc.set_array(height)
    lc.set_linewidth(4)
    line = ax.add_collection(lc)
    x11,y11 =(76.5, 36)
    plt.annotate('FNL', xy=(x[-1], y[-1]),  xycoords='data',
                    xytext=(x11, y11), textcoords='data',
                    arrowprops=dict(arrowstyle="->")
                 )

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
    plt.savefig('test.png',dpi=200)

