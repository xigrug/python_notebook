##https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.datetime.html
##http://python-awips.readthedocs.io/en/latest/examples/generated/Profiler_Wind_Barb_Time-Series.html
from matplotlib.cm import get_cmap
from datetime import datetime, timedelta
from matplotlib.dates import date2num
#from metpy.units import units
import matplotlib.pyplot as plt
import numpy as np
import os
from netCDF4 import Dataset
from wrf import getvar,  ll_to_xy, ALL_TIMES, extract_times
# Query ESRL/PSD profiler data from Unidata AWIPS
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
search('wrfout_d04_2017-06', '..')
filenames=sorted(filenames)#;防止顺序不对
a=range(0,len(filenames))
ncfile=[None]*len(filenames)
for i,filename in zip(a,filenames):
    ncfile[i] = Dataset(filename)
x_y = ll_to_xy(ncfile[0], '32.067', '118.390')
x=48
y=18
wrftime=extract_times(ncfile,timeidx=ALL_TIMES)
p = getvar(ncfile, "pressure",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
times = getvar(ncfile, "times",timeidx=ALL_TIMES,squeeze=False)
heights = getvar(ncfile, "z", units="km",timeidx=ALL_TIMES,squeeze=False)[0,:,x,y]
u = getvar(ncfile, "ua", units="kt",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
v = getvar(ncfile, "va", units="kt",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
w = getvar(ncfile, "wa", units="m s-1",timeidx=ALL_TIMES,method="cat")[:,:,x,y]
temp = getvar(ncfile, "temp", units="degC",timeidx=ALL_TIMES,method="cat")[:,:,x,y]
rh = getvar(ncfile, "rh",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
fig = plt.figure(figsize=(16,7))
cmap=plt.cm.RdYlGn_r
# Build arrays
H, T = np.meshgrid(heights,wrftime)
#T, H = np.meshgrid(wrftime,heights)
C = np.sqrt(u**2 + v**2)
fig, ax = plt.subplots()    
#xy=ax.barbs(t, h, u, v)
#xy=ax.quiver(T, H, u, v)
ax.title.set_text("test_profile")
# Make the contour plot
rh_contours=ax.contourf(T,H,rh,  levels=[60,70,80,90,95,98,100],cmap=get_cmap("Blues"),extend='both')#YlGn
# Add the color bar
plt.colorbar(rh_contours)
################
levels = np.arange(-60, 20, 10)
temp_contours=ax.contour(T,H,temp,levels=levels,colors='red',linewidths=0.7)#inline=True, fontsize=10)
w_contours=ax.contour(T,H,w,colors='cyan',linewidths=0.7)#inline=True, fontsize=10)
plt.clabel(temp_contours, inline=True, inline_spacing=1, fmt='%1.0f',rightside_up=True, fontsize=4)
plt.clabel(w_contours, inline=True, inline_spacing=1, fmt='%1.2f',rightside_up=True, fontsize=4)

#########
#xy=ax.barbs(T, H, u, v, length=4.5,fill_empty=False, rounding=False,sizes=dict(emptybarb=0.25, spacing=0.4, height=0.2),linewidth=0.5)
#Q=ax.quiver(T, H, u, v, linewidth=0.5,pivot='mid', units='inches')
Q=ax.quiver(T, H, u, v, linewidth=0.5, units='width')
qk = plt.quiverkey(Q, 0.763, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
#ax.xaxis_date()
#ax.set_xlim(wrftime[0]-np.timedelta64(10, 'm'), wrftime[-1]+np.timedelta64(10, 'm'))
ax.tick_params(axis='both', which='major', labelsize=6,rotation=15)
#plt.setp(ax.get_xticklabels()[-1],visible=False)
#ax.set_xticks(ax.get_xticks()[1:-1])
#plt.gca().invert_xaxis()
plt.savefig("mwind_profile-02.png",dpi=600,bbox_inches='tight')
#plt.show()
