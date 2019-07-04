from __future__ import print_function, division

from netCDF4 import Dataset
from wrf import getvar, CoordPair, ll_to_xy
import pandas as pd
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.plots import  Hodograph,SkewT
from metpy.units import units
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# for ssh plot
plt.switch_backend('agg')
names=['PRES','HGHT','TEMP','DWPT','RELH','MIXR','DRCT','SKNT','U','V','THTA','THTE','THTV']
df = pd.DataFrame(columns = names) 
#stn = ['52203','51777','51839','51828','51709','51644','51463'] #72572 is ID for SLC
name = ['Nanjing']#,'Urumqi'] #72572 is ID for SLC
#name ='RQ'
lat=[32.00]
lon=[118.80]
number=[0]
#filenames=["wrfout_d01_2015-04-27_00:00:00","wrfout_d01_2015-04-27_12:00:00","wrfout_d01_2015-04-27_18:00:00","wrfout_d01_2015-04-28_00:00:00","wrfout_d01_2015-04-28_12:00:00","wrfout_d01_2015-04-26_12:00:00","wrfout_d01_2015-04-26_00:00:00"]
filenames=["wrfout_d05_2018-01-17_00:00:00","wrfout_d05_2018-01-17_12:00:00","wrfout_d05_2018-01-18_00:00:00","wrfout_d05_2018-01-18_12:00:00","wrfout_d05_2018-01-19_00:00:00","wrfout_d05_2018-01-19_12:00:00","wrfout_d05_2018-01-20_00:00:00","wrfout_d05_2018-01-20_12:00:00","wrfout_d05_2018-01-21_00:00:00","wrfout_d05_2018-01-21_12:00:00","wrfout_d05_2018-01-22_00:00:00","wrfout_d05_2018-01-22_12:00:00","wrfout_d05_2018-01-23_00:00:00"]
#filenames=["wrfout_d05_2018-01-21_00:00:00","wrfout_d05_2018-01-21_12:00:00","wrfout_d05_2018-01-22_00:00:00","wrfout_d05_2018-01-22_12:00:00","wrfout_d05_2018-01-23_00:00:00"]
#for i,filename in zip(number,filenames):
for i in number:
    for filename in filenames:
        ncfile = Dataset(filename)
    #    x_y = ll_to_xy(ncfile, 37.13,79.93)
        x_y = ll_to_xy(ncfile, lat[i],lon[i])
        
        print (x_y)
        # Get the geopotential height (m) and pressure (hPa).
        z = getvar(ncfile, "z")
        time = getvar(ncfile, "times")
        zp= z[:,x_y[0],x_y[1]]
        p = getvar(ncfile, "pressure")
        pp= p[:,x_y[0],x_y[1]]
        rh = getvar(ncfile, "rh")
        rhp= rh[:,x_y[0],x_y[1]]
        td = getvar(ncfile, "td")
        tdp= td[:,x_y[0],x_y[1]]
        tc = getvar(ncfile, "tc")
        tcp= tc[:,x_y[0],x_y[1]]
        wspd = getvar(ncfile, "wspd_wdir",units='kt')[0]
        ua = getvar(ncfile, "ua",units='ms-1')
        wdir = getvar(ncfile, "wspd_wdir",units='kt')[1]
        va = getvar(ncfile, "va",units='ms-1')
        wspdp= wspd[:,x_y[0],x_y[1]]
        wdirp= wdir[:,x_y[0],x_y[1]]
        u= ua[:,x_y[0],x_y[1]]
        v= va[:,x_y[0],x_y[1]]
        df.PRES=pp
        df.HGHT=zp
        df.RELH=rhp
        df.DWPT=tdp
        df.TEMP=tcp
        df.DRCT=wdirp
        df.SKNT=wspdp
        df.U=u
        df.V=v
        df.MIXR=None
        df.THTA=None
        df.THTE=None
        df.THTV=None
        df.to_csv(name[i]+str(time.values)[0:13]+'.txt',sep=' ',float_format='%.2f',header=True, index=False,na_rep='NaN')
        ##
        p = df['PRES'].values * units('hPa')
        T = df['TEMP'].values * units('degC')
        Td = df['DWPT'].values * units('degC')
        u = df['U'].values * units('knot')*1.944
        v = df['V'].values * units('knot')*1.944
        wind_speed = df['SKNT'].values * units('knot')
        
        fig = plt.figure(figsize=(9, 9))
        skew = SkewT(fig, rotation=45)
        
        # Plot the data using normal plotting functions, in this case using
        # log scaling in Y, as dictated by the typical meteorological plot
        skew.plot(p, T, 'r')
        skew.plot(p, Td, 'g')
        skew.plot_barbs(p, u, v)
        skew.ax.set_ylim(1000, 100)
        skew.ax.set_xlim(-40, 60)
        #skew.ax.set_title(name[i]+" "+str(time.values)[0:13]+' Skew-T', fontsize=20)
        skew.ax.set_title('WRF Skew-T', fontsize=20)
        skew.ax.set_xlabel(r'Temperature ($^{o}$c)',fontsize=16)
        skew.ax.set_ylabel('Pressure (hPa)',fontsize=16)
        skew.ax.tick_params(axis='both',width=2,labelsize=16)
    
        # Calculate LCL height and plot as black dot
        lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
        skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')
        # Calculate full parcel profile and add to plot as black line
        prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
        skew.plot(p, prof, 'k', linewidth=2)
        
        # Shade areas of CAPE and CIN
        skew.shade_cin(p, T, prof)
        skew.shade_cape(p, T, prof)
        
        # An example of a slanted line at constant T -- in this case the 0
        # isotherm
        skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)
        
        # Add the relevant special lines
        skew.plot_dry_adiabats()
        skew.plot_moist_adiabats()
        skew.plot_mixing_lines()
        
        
        #Create a hodograph
        # Create an inset axes object that is 40% width and height of the
        # figure and put it in the upper right hand corner.
        #ax_hod = inset_axes(skew.ax, '20%', '20%', loc='upper left', bbox_to_anchor=(0.5, 1.05))
        ax_hod = inset_axes(skew.ax, '24%', '24%', loc=2)
        ax_hod.set_yticklabels([-90,-50,0,50,90],rotation=30,fontsize=15)
        ax_hod.set_xticklabels([-90,-50,0,50,90],rotation=30,fontsize=15)
        h = Hodograph(ax_hod, component_range=80.)
        h.add_grid(increment=20)
        hodo=h.plot_colormapped(u, v, wind_speed)  # Plot a line colored by wind speed
        #fig.colorbar(hodo, ax_hod,orientation='horizontal', shrink=0.74, pad=0.1)
        cbar_ax = fig.add_axes([0.14, 0.630, 0.15, 0.02])
        cbar=fig.colorbar(hodo, cax=cbar_ax,orientation='horizontal', shrink=0.74, pad=0.1)
        cbar.ax.set_xticklabels(cbar.ax.get_xticklabels(),rotation=90,fontsize=15)
     
        plt.savefig(name[i]+str(time.values)[0:13]+'.png')
