#https://unidata.github.io/siphon/latest/examples/upperair/Wyoming_Request.html#sphx-glr-download-examples-upperair-wyoming-request-py
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
#from metpy.cbook import get_test_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#stn = ['52203','51777','51839','51828','51709','51644','51463'] #72572 is ID for SLC
stn = ['51777','51839','51828'] #72572 is ID for SLC
#name = ['HM','RQ','MF','HT','KS','KQ','Urumqi'] #72572 is ID for SLC
name = ['RQ','MF','HT'] #72572 is ID for SLC
date = datetime(2015, 4, 28, 0)
for station,na in zip(stn,name):
    print(station)
    df = WyomingUpperAir.request_data(date, station)
    print(df.units)
    p = df['pressure'].values * units(df.units['pressure'])
    T = df['temperature'].values * units(df.units['temperature'])
    Td = df['dewpoint'].values * units(df.units['dewpoint'])
    u = df['u_wind'].values * units(df.units['u_wind'])
    v = df['v_wind'].values * units(df.units['v_wind'])
    wind_speed = df['speed'].values * units(df.units['speed'])
    
    fig = plt.figure(figsize=(9, 9))
    #add_metpy_logo(fig, 110, 100)
    skew = SkewT(fig, rotation=45)
    
    # Plot the data using normal plotting functions, in this case using
    # log scaling in Y, as dictated by the typical meteorological plot
    skew.plot(p, T, 'r')
    skew.plot(p, Td, 'g')
    skew.plot_barbs(p, u, v)
    skew.ax.set_ylim(1000, 100)
    skew.ax.set_xlim(-40, 60)
    #skew.ax.set_title(na+' '+str(date)[0:13]+' Skew-T', fontsize=20)
    skew.ax.set_xlabel(r'Temperature ($^{o}$c)',fontsize=16)
    skew.ax.set_ylabel('Pressure (hPa)',fontsize=16)
    skew.ax.tick_params(axis='both',width=2,labelsize=16)
    
    # Calculate LCL height and plot as black dot
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
    skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')
    
    # Calculate full parcel profile and add to plot as black line
    
    prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
    skew.plot(p, prof, 'k', linewidth=2)
    
    print(T)
    print(p)
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
    
    # Create a hodograph
    # Create an inset axes object that is 40% width and height of the
    # figure and put it in the upper right hand corner.
    #ax_hod = inset_axes(skew.ax, '20%', '20%', loc='upper left', bbox_to_anchor=(0.5, 1.05))
    ax_hod = inset_axes(skew.ax, '24%', '24%', loc='upper left')
    ax_hod.set_yticklabels([-90,-50,0,50,90],rotation=30,fontsize=15)
    ax_hod.set_xticklabels([-90,-50,0,50,90],rotation=30,fontsize=15)
    h = Hodograph(ax_hod, component_range=80.)
    h.add_grid(increment=20)
    hodo=h.plot_colormapped(u, v, wind_speed)  # Plot a line colored by wind speed
    #fig.colorbar(hodo, ax_hod,orientation='horizontal', shrink=0.74, pad=0.1)
    cbar_ax = fig.add_axes([0.14, 0.63, 0.15, 0.02])
    clevs1 =np.arange(0,50,5)
    cbar=fig.colorbar(hodo, cax=cbar_ax,orientation='horizontal', shrink=0.74, pad=0.1)
    cbar.ax.set_xticklabels(cbar.ax.get_xticklabels(),rotation=90,fontsize=15)
    #fig.colorbar(hodo,orientation='horizontal', shrink=0.74, pad=0.1)
    # Show the plot
    plt.savefig(str(date)[0:13]+str(station)+na+"_cape.pdf",format="pdf")
