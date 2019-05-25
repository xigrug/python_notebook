from netCDF4 import Dataset,MFDataset
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature

from wrf import (getvar, interplevel, to_np, latlon_coords, get_cartopy,
                 cartopy_xlim, cartopy_ylim, ALL_TIMES )
ncfile = Dataset("wrfout_d01_2019-03-22_00:00:00")
# Extract the pressure, geopotential height, and wind variables
p = getvar(ncfile, "pressure",timeidx=ALL_TIMES)
z = getvar(ncfile, "z", timeidx=ALL_TIMES,units="dm")
u10 = getvar(ncfile, "U10", timeidx=ALL_TIMES)
v10 = getvar(ncfile, "V10", timeidx=ALL_TIMES)
wspd = getvar(ncfile, "wspd_wdir", timeidx=ALL_TIMES,units="kts")[0,:]
# Get the lat/lon coordinates
lats, lons = latlon_coords(u10)

# Get the map projection information
cart_proj = get_cartopy(u10)

# Create the figure
fig = plt.figure(figsize=(12,9))
ax = plt.axes(projection=cart_proj)

# Download and add the states and coastlines
states = NaturalEarthFeature(category="cultural", scale="50m",
                             facecolor="none",
                             name="admin_1_states_provinces_shp")
ax.add_feature(states, linewidth=0.5, edgecolor="black")
ax.coastlines('50m', linewidth=0.8)

lat = lats[:,:].squeeze()
lon = lons[:,:].squeeze()
u_wind = u10[0, :, :].squeeze()
v_wind = v10[0, :, :].squeeze()

# Add the 500 hPa wind barbs, only plotting every 125th data point.
q=ax.quiver(to_np(lon[::3]), to_np(lat[::3]),
          to_np(u_wind[::3]), to_np(v_wind[::3]),color='blue',
          scale=500,
          width=0.001, headwidth=5, headlength=1.,
          transform=crs.PlateCarree())
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
# Set the map bounds
ax.set_xlim(cartopy_xlim(u10))
ax.set_ylim(cartopy_ylim(u10))

ax.gridlines()

plt.title("500 MB Height (dm), Wind Speed (kt), Barbs (kt)")

plt.show()
