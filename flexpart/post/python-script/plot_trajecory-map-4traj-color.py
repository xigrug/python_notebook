# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as CM
from mpl_toolkits.basemap import Basemap
import matplotlib.collections as mcoll
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.patches import Polygon
#读取txt数据
def plot_rec(map,lower_left,upper_left,upper_right,lower_right,text):
    lon_poly = np.array([lower_left[0], upper_left[0],upper_right[0], lower_right[0]])
    lat_poly = np.array([lower_left[1], upper_left[1],upper_right[1], lower_right[1]])
    X, Y  = map(lon_poly, lat_poly)
    xy = np.vstack([X,Y]).T

    poly = Polygon(xy, closed=True, \
            facecolor='None',edgecolor='red', \
            linewidth=1.\
            )
    ax, ay = map(lower_left[0],lower_left[1])
    plt.text(ax, ay,text,fontsize=6,fontweight='bold',
                    ha='left',va='bottom',color='k')
    plt.gca().add_patch(poly)

filename_100="trajectories4.txt"
data=pd.read_table(filename_100,sep='\s+',header=None,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])#数量不定的空格符可以用正则表达式\s+表示
lon=data.iloc[0::4,2]
lat=data.iloc[0::4,3]
height=data.iloc[0::4,4]
lon1=data.iloc[1::4,2]
lat1=data.iloc[1::4,3]
height1=data.iloc[1::4,4]
lon2=data.iloc[2::4,2]
lat2=data.iloc[2::4,3]
height2=data.iloc[2::4,4]
lon3=data.iloc[3::4,2]
lat3=data.iloc[3::4,3]
height3=data.iloc[3::4,4]
# 1. Draw the map background
#fig = plt.figure(figsize=(8, 8))
#fig, ax = plt.figure(figsize=(8, 8))
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111)
#m = Basemap(projection='lcc', resolution='h', 
#            lat_0=36.5, lon_0=76,
#            width=3E5, height=4E5)
m = Basemap(llcrnrlon=75,llcrnrlat=35,urcrnrlon=90,urcrnrlat=45, epsg=4269)
#m = Basemap(llcrnrlon=74.5,llcrnrlat=37.,urcrnrlon=78.5,urcrnrlat=38.5, epsg=4269)
#m = Basemap(llcrnrlon=74.,llcrnrlat=35.,urcrnrlon=78.,urcrnrlat=38., epsg=3825)
#######绘制阴暗的浮雕图
#m.shadedrelief()
#m.bluemarble()
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
#m.arcgisimage(service='World_Shaded_Relief', xpixels = 1500, verbose= True)

#m.drawcoastlines(color='b')
#m.drawcountries(color='gray')
#m.drawstates(color='gray')
#m.drawmapscale(75, 35, 76, 36.5, 100)
#add lon lat sticks
m.drawparallels(np.arange(35.,45.,2.5),linewidth=1, dashes=[4, 2], labels=[1,0,0,0], color= 'gray',zorder=1, fontsize=10)
m.drawmeridians(np.arange(75.,90.,2.5),linewidth=1, dashes=[4, 2], labels=[0,0,0,1], color= 'gray',zorder=1, fontsize=10)
##add shapefile
m.readshapefile('dijishi_2004','state',color='gray')
#m.readshapefile('dijishi_2004','state',color='gray')
#plot_rec(m,[36.5,73.5],[36.5,76.5],[39.5,76.5],[39.5,73.5],"aera")
x, y = m(np.array(lon), np.array(lat))
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
x1, y1 = m(np.array(lon1), np.array(lat1))
m.scatter(x1, y1, s=1, marker='o',alpha=0.8)
m.scatter(x1[0], y1[0], c='r',s=16, marker='s',edgecolors='none',alpha=1)
points1 = np.array([x1, y1]).T.reshape(-1, 1, 2)
segments1 = np.concatenate([points1[:-1], points1[1:]], axis=1)
# Create a continuous norm to map from data points to colors
norm1 = plt.Normalize(height1.min(), height1.max())
lc1 = LineCollection(segments1, cmap='viridis', norm=norm1)
# Set the values used for colormapping
lc1.set_array(height1)
lc1.set_linewidth(4)
line1 = ax.add_collection(lc1)
x2, y2 = m(np.array(lon2), np.array(lat2))
m.scatter(x2, y2, s=1, marker='o',alpha=0.8)
m.scatter(x2[0], y2[0], c= 'r',s=16, marker='x',edgecolors='none',alpha=1)
points2 = np.array([x2, y2]).T.reshape(-1, 1, 2)
segments2 = np.concatenate([points2[:-1], points2[1:]], axis=1)
# Create a continuous norm to map from data points to colors
norm2 = plt.Normalize(height2.min(), height2.max())
lc2 = LineCollection(segments2, cmap='viridis', norm=norm2)
# Set the values used for colormapping
lc2.set_array(height2)
lc2.set_linewidth(4)
line2 = ax.add_collection(lc2)
x3, y3 = m(np.array(lon3), np.array(lat3))
m.scatter(x3, y3, s=1, marker='o',alpha=0.8)
m.scatter(x3[0], y3[0], c= 'r',s=16, marker='x',edgecolors='none',alpha=1)
points3 = np.array([x3, y3]).T.reshape(-1, 1, 2)
segments3 = np.concatenate([points3[:-1], points3[1:]], axis=1)
# Create a continuous norm to map from data points to colors
norm3 = plt.Normalize(height3.min(), height3.max())
lc3 = LineCollection(segments3, cmap='viridis', norm=norm3)
# Set the values used for colormapping
lc3.set_array(height3)
lc3.set_linewidth(4)
line3 = ax.add_collection(lc3)
#fig.colorbar(line, ax)
# create an axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(lc,cax)
#plt.show()
plt.savefig('traject-3height.png',dpi=500)
