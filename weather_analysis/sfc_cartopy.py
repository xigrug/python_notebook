#grug Nju @ 2018-12-31
#https://nbviewer.jupyter.org/github/mccrayc/tutorials/blob/master/2_reanalysis/CFSR_Data_Tutorial.ipynb
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def plotMap1():
    #Set the projection information Cannot label gridlines on a LambertConformal plot. Only PlateCarree and Mercator plots are currently supported.
    proj = ccrs.PlateCarree(central_longitude=83.6)
    #Create a figure with an axes object on which we will plot. Pass the projection to that axes.
    fig, ax = plt.subplots(subplot_kw=dict(projection=proj))
    
    #Zoom in
    ax.set_extent([40, 130, 15, 90])# TaZhong:83.63,39.04
    
    #Add map features
    ax.add_feature(cfeature.LAND, facecolor='0.9') #Grayscale colors can be set using 0 (black) to 1 (white)
    ax.add_feature(cfeature.LAKES, alpha=0.9)  #Alpha sets transparency (0 is transparent, 1 is solid)
    ax.add_feature(cfeature.BORDERS, zorder=10, linestyle=':')
    ax.add_feature(cfeature.COASTLINE, zorder=10, linestyle=':')
    
    #We can use additional features from Natural Earth (http://www.naturalearthdata.com/features/)
    states_provinces = cfeature.NaturalEarthFeature(
            category='cultural',  name='admin_1_states_provinces_lines',
            scale='50m',facecolor='none')
    ax.add_feature(states_provinces, edgecolor='gray', zorder=10)
    
    #Add lat/lon gridlines every 20° to the map
    gl= ax.gridlines(draw_labels=True,linewidth=2, color='gray', alpha=0.5, linestyle='--') 
    
    return fig, ax, gl

dataFile = '../ERA-Int_sfc_20150425.nc'
#Open the dataset and print out metadeta
ds = xr.open_dataset(dataFile)
print(ds)
lat = ds['latitude']
lon = ds['longitude']
lons, lats = np.meshgrid(lon, lat)
ds.sel(time=('2015-04-25T06:00:00'))
psfc=ds.sp.sel(time=('2015-04-25T06:00:00'))
print(psfc.min())
print(psfc.max())
plt.rcParams['figure.figsize'] = (12, 12)
fig, ax,gl = plotMap1()
ax.stock_img()
#Plot the 500-hPa height contours on the map, in black, with line width 1, and plot it above everything else.
hght_levels = np.arange(950,1050,50)
hght_contour=ax.contour(lon, lat,psfc/100, colors='k', levels=hght_levels, linewidths=1, zorder=3, transform = ccrs.PlateCarree())
gl.xlabels_top = False
gl.ylabels_left = False
#gl.xlines = False
gl.xlocator = mticker.FixedLocator([40,60,80,100,120,140])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 15}
gl.ylabel_style = {'size': 15}
#gl.xlabel_style = {'color': 'gray', 'weight': 'bold'}
#Now plot absolute vorticity as filled contours underneath height field, only values above 1.5e-4 s-1, 
# and use the YlOrRd colormap.
#avor_levels = np.linspace(15e-5,60e-5, 10)
plt.clabel(hght_contour,hght_levels, inline=True, fmt='%1i', fontsize=16)
ax.set_title('Sea Level Pressure (hPa), 2015-04-25 06UTC', fontsize=20)
plt.plot(83.63,39.04,'ro', transform=ccrs.PlateCarree())
plt.text(84.03,39.34, 'TZ',color='r',
         horizontalalignment='left',
         transform=ccrs.Geodetic())
#Get the wind components
#urel = ds['u'].sel(level=500).isel(time=0).values*1.944
#vrel = ds['v'].sel(level=500).isel(time=0).values*1.944

#Plot the barbs
#ax.barbs(lon, lat, urel, vrel, regrid_shape=12, zorder=20, transform=ccrs.PlateCarree())

plt.savefig(dataFile[3:23]+"_surface.png")
