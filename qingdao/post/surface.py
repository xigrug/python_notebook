# coding: utf-8
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.patches import Polygon
from wrf import getvar, interplevel, to_np, get_basemap, latlon_coords,ALL_TIMES
import time
from datetime import date, timedelta
import os
def wea(fname,figname,itime):
    ncfile = Dataset(fname)
    # Creating a simple test list with three timesteps
    #ncfile = [ #Dataset("wrfout_d01_2017-05-30_00:00:00")]
    #          Dataset("wrfout_d01_2017-05-31_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-01_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-02_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-03_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-04_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-05_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-06_00:00:00"),
    #          Dataset("wrfout_d02_2017-06-07_00:00:00")]
    #          Dataset("wrfout_d01_2017-06-08_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-09_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-10_00:00:00"),
    #          Dataset("wrfout_d01_2017-06-11_00:00:00")]
    
    # Extract the pressure, geopotential height, and wind variables
    #p0 = getvar(ncfile, "slp", timeidx=ALL_TIMES, method="cat")
    z0 = getvar(ncfile, "slp", units="hPa", timeidx=ALL_TIMES, method="cat")
    ua0 = getvar(ncfile, "uvmet10", units="m s-1", timeidx=ALL_TIMES, method="cat")
    rh0 = getvar(ncfile, "rh2", timeidx=ALL_TIMES, method="cat")
    print(rh0)    
    #wspd0 = getvar(ncfile, "wspd_wdir", units="m s-1", timeidx=ALL_TIMES, method="cat")[0,:]
    
    #p    = p0[itime,:,:,:] 
    ht_500    = z0[itime,:,:]
    u_500   = ua0[0,itime,:,:]
    v_500   = ua0[1,itime,:,:]
    rh  = rh0[itime,:,:]
    #wspd = wspd0[itime,:,:,:]

    print(ht_500.shape)
    # Get the lat/lon coordinates
    lats, lons = latlon_coords(ht_500)

    # Get the basemap object

    
    # Create the figure
    fig = plt.figure(figsize=(12,9))
    ax = plt.axes()

    bm = get_basemap(ht_500)    
    shp_info = bm.readshapefile("CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域
    
    for info, shp in zip(bm.states_info, bm.states):
        proid = info['NAME_1']  # 可以用notepad打开CHN_adm1.csv文件，可以知道'NAME_1'代表各省的名称
        if proid == 'Shandong':
            poly = Polygon(shp,facecolor='g',edgecolor='c', lw=3) # 绘制广东省区域
            ax.add_patch(poly)    
        #proid = info['NAME_2']  # 可以用notepad打开CHN_adm1.csv文件，可以知道'NAME_1'代表各省的名称
        #if proid == 'Qingdao':
        #    poly = Polygon(shp,facecolor='r',edgecolor='c', lw=3) # 绘制广东省区域
        #    ax.add_patch(poly)
    
    bm.shadedrelief()
    
    # Convert the lat/lon coordinates to x/y coordinates in the projection space
    x, y = bm(to_np(lons), to_np(lats))
    
    # Add the 500 hPa geopotential height contours
    levels = np.arange(960., 1050., 2.5)
    contours = bm.contour(x, y, to_np(ht_500), levels=levels, colors="blue")
    plt.clabel(contours, inline=1, fontsize=10, fmt="%i")
    
    # Add the wind speed contours
    levels = [ 70.,75, 80, 85, 90, 95, 100.]
    wspd_contours = bm.contourf(x, y, to_np(rh), levels=levels,
                                cmap=get_cmap("rainbow"))
    bm.colorbar(wspd_contours, ax=ax, pad=.15)
    
    # Add the geographic boundaries
    #bm.drawcoastlines(linewidth=0.25)
    #bm.drawstates(linewidth=0.25)
    #bm.drawcountries(linewidth=0.25)

    parallels = np.arange(0.,60,10.)
    bm.drawparallels(parallels, color='k', linewidth=.01,
     zorder=0, dashes=[1, 1], labels=[1,0,0,0], fmt='%g')
    meridians = np.arange(90.,150.,10.)
    bm.drawmeridians(meridians, color='k', linewidth=1.0,
     zorder=0, dashes=[1, 1], labels=[0,0,0,1], fmt='%g')

    # Add the 500 hPa wind barbs, only plotting every 125th data point.
    bm.barbs(x[::5,::5], y[::5,::5], to_np(u_500[::5, ::5]),
             to_np(v_500[::5, ::5]), length=6)
    

    
    #plt.title("500 MB Height (dm), Wind Speed (m s-1), Barbs (m s-1)")
    
    plt.savefig(figname, dpi=300)

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
    list_name = list(set(list_name))        #列表去重复
    list_name = sorted(list_name)           #列表排序
    return list_name

def getTomorrow():
    today=date.today()
    oneday=timedelta(days=1)
    tomorrow=today+oneday
    return tomorrow

def main():
    datetext=getTomorrow().strftime('%Y%m%d')
    print(datetext)
    path = "/public/product/WrfData/wrf_seven_day/"+datetext
    print(path)
    list_name=[]
    listdir(path,list_name)
    list_name = list(set(list_name))        #列表去重复
    list_name = sorted(list_name)           #列表排序
    for i in range(len(list_name)-1):
        for itime in [0,12]:
            fname=list_name[i]
            print(fname)
            figname = "sur_wea_day_"+fname[58:68]+"_"+str(itime)
            wea(fname,figname,itime)

if __name__=='__main__':
    sta = time.clock()
    main()
    end = time.clock()
    print("finished all in %s seconds" %str(end-sta))        
