#grug Nju @ 2018-12-31
#https://nbviewer.jupyter.org/github/mccrayc/tutorials/blob/master/2_reanalysis/CFSR_Data_Tutorial.ipynb
#"https://unidata.github.io/python-gallery/examples/500hPa_HGHT_Winds.html?highlight=barbs\n",
#"https://unidata.github.io/python-gallery/examples/HILO_Symbol_Plot.html#sphx-glr-examples-hilo-symbol-plot-py"

import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
#import cartopy.io.shapereader as shpreader
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import cartopy.io.img_tiles as cimgt
import scipy.ndimage as ndimage

def plotMap1():
    #Set the projection information Cannot label gridlines on a LambertConformal plot. Only PlateCarree and Mercator plots are currently supported.
    proj = ccrs.PlateCarree(central_longitude=83.6)
    # Create a Stamen terrain background instance.
    #stamen_terrain = cimgt.Stamen('terrain-background')
    #Create a figure with an axes object on which we will plot. Pass the projection to that axes.
    fig, ax = plt.subplots(subplot_kw=dict(projection=proj)) 
    #Zoom in
    ax.set_extent([40, 130, 15, 90])# TaZhong:83.63,39.04
    #Add map features
    #ax.add_image(stamen_terrain, 3)
    ax.add_feature(cfeature.LAND, facecolor='0.9',alpha=0.4) #Grayscale colors can be set using 0 (black) to 1 (white)
    ax.add_feature(cfeature.LAKES, alpha=0.9)  #Alpha sets transparency (0 is transparent, 1 is solid)
    ax.add_feature(cfeature.BORDERS, zorder=10, linestyle=':')
    ax.add_feature(cfeature.COASTLINE, zorder=10, linestyle=':')
    
    #We can use additional features from Natural Earth (http://www.naturalearthdata.com/features/)
    states_provinces = cfeature.NaturalEarthFeature(
            category='cultural',  name='admin_1_states_provinces_lines',
            scale='50m',facecolor='none')
    ax.add_feature(states_provinces, edgecolor='gray', zorder=10)
    #reader = shpreader.Reader("/public/home/hysplit/flex_part-qd/xj-plot/dijishi_2004.shp")
    #ax.add_feature(reader, linewidth=0.5, edgecolor="black",zorder=10)
    #ax.background_img(name='world-topo-1', resolution='largeA1')
    ax.background_img(name='natural-earth-1', resolution='large4096px')
    #fname = "/public/home/hysplit/flex_part-qd/xj-plot/dijishi_2004.shp"
    fname = "/public/home/hysplit/software/MeteoInfo/map/cn_province.shp"
    shape_feature = ShapelyFeature(Reader(fname).geometries(),
                                ccrs.PlateCarree(), facecolor='none',edgecolor='grey')
    ax.add_feature(shape_feature,zorder=20)
    #Add lat/lon gridlines every 20° to the map
    gl= ax.gridlines(draw_labels=True,linewidth=2, color='gray', alpha=0.5, linestyle='--') 
    
    return fig, ax, gl
def plot_maxmin_points(lon, lat, data, extrema, nsize, symbol, color='k',
                       plotValue=True, transform=None):
    """
    This function will find and plot relative maximum and minimum for a 2D grid. The function
    can be used to plot an H for maximum values (e.g., High pressure) and an L for minimum
    values (e.g., low pressue). It is best to used filetered data to obtain  a synoptic scale
    max/min value. The symbol text can be set to a string value and optionally the color of the
    symbol and any plotted value can be set with the parameter color
    lon = plotting longitude values (2D)
    lat = plotting latitude values (2D)
    data = 2D data that you wish to plot the max/min symbol placement
    extrema = Either a value of max for Maximum Values or min for Minimum Values
    nsize = Size of the grid box to filter the max and min values to plot a reasonable number
    symbol = String to be placed at location of max/min value
    color = String matplotlib colorname to plot the symbol (and numerica value, if plotted)
    plot_value = Boolean (True/False) of whether to plot the numeric value of max/min point
    The max/min symbol will be plotted on the current axes within the bounding frame
    (e.g., clip_on=True)
    """
    from scipy.ndimage.filters import maximum_filter, minimum_filter

    if (extrema == 'max'):
        data_ext = maximum_filter(data, nsize, mode='nearest')
    elif (extrema == 'min'):
        data_ext = minimum_filter(data, nsize, mode='nearest')
    else:
        raise ValueError('Value for hilo must be either max or min')

    mxy, mxx = np.where(data_ext == data)

    for i in range(len(mxy)):
        ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]], symbol, color=color, size=24,
                clip_on=True, horizontalalignment='center', verticalalignment='center',
                transform=transform)
        ax.text(lon[mxy[i], mxx[i]], lat[mxy[i], mxx[i]],
                '\n' + str(np.int(data[mxy[i], mxx[i]])),
                color=color, size=12, clip_on=True, fontweight='bold',
                horizontalalignment='center', verticalalignment='top', transform=transform)
for i in range(25,31):
    day=str(i)
    dataFile = '/public/home/hysplit/data/ecwmf/ERA-Int_sfc_201504'+day+'.nc'
#Open the dataset and print out metadeta
    ds = xr.open_dataset(dataFile)
    lat = ds['latitude']
    lon = ds['longitude']
    lons, lats = np.meshgrid(lon, lat)
    ds.sel(time=('2015-04-'+day+'T12:00:00'))
    psfc=ds.sp.sel(time=('2015-04-'+day+'T12:00:00'))/100
    # Smooth the 850-hPa geopotential height field
    # Be sure to only smooth the 2D field
    psfc = ndimage.gaussian_filter(psfc, sigma=5, order=0)
    plt.rcParams['figure.figsize'] = (12, 12)
    fig, ax,gl = plotMap1()
#ax.stock_img()
    print(psfc.max())
    print(psfc.min())
#Plot the 500-hPa height contours on the map, in black, with line width 1, and plot it above everything else.
#hght_levels = np.arange(4800,5880,60)
# Plot thickness with multiple colors
    clevs = (np.arange(500, 950, 80),
             np.array([950]),
             np.arange(950, 1150, 20))
#clevs=np.arange(5900, 5944, 4)
#colors = ('tab:blue', 'b', 'tab:red')
    kw_clabels = {'fontsize': 11, 'inline': True, 'inline_spacing': 5, 'fmt': '%i',
              'rightside_up': True, 'use_clabeltext': True}
#for clevthick, color in zip(clevs, colors):
    for clevthick in clevs:
        print(clevthick)
        cs = ax.contour(lon, lat, psfc, levels=clevthick, colors='k',
                    linewidths=1.0, linestyles='solid', transform=ccrs.PlateCarree())
        plt.clabel(cs, **kw_clabels)
#hght_contour=ax.contour(lon, lat,hgt, colors='k', levels=hght_levels, linewidths=1.25, linestyles="solid",zorder=3, transform = ccrs.PlateCarree())
#plt.clabel(hght_contour,hght_levels, inline=True, fmt='%1i', fontsize=16)
    plot_maxmin_points(lons, lats, psfc, 'max', 100, symbol='H', color='b',  transform=ccrs.PlateCarree())
    plot_maxmin_points(lons, lats, psfc, 'min', 100, symbol='L', color='r', transform=ccrs.PlateCarree())
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
    ax.set_title('Surface Pressure(hPa), 2015-04-'+day+' 12:00:00UTC', fontsize=20)

    plt.plot(83.63,39.04,'go', transform=ccrs.PlateCarree())
    plt.text(84.03,39.34, 'TZ', color='g',
         horizontalalignment='left',
         transform=ccrs.Geodetic())
#Get the wind components
#urel = ds['u'].sel(level=500).isel(time=0).values*1.944
#vrel = ds['v'].sel(level=500).isel(time=0).values*1.944
    urel=ds.u10.sel(time=('2015-04-'+day+'T12:00:00')).values*1.944
    vrel=ds.v10.sel(time=('2015-04-'+day+'T12:00:00')).values*1.944

#Plot the barbs
    ax.barbs(lon, lat, urel, vrel, regrid_shape=12, zorder=20, transform=ccrs.PlateCarree())

#plt.savefig(dataFile[3:23]+"_500hpaWind.png")
    plt.savefig(day+"12_sfc-smoothHL.png",bbox_inches='tight')
