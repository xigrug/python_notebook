import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from netCDF4 import Dataset
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from wrf import getvar, to_np, vertcross, smooth2d, CoordPair, get_basemap, latlon_coords

# Open the NetCDF file
ncfile = Dataset("../domain04/use_d04/wrfout_d04_2017-06-10_04:00:00")

# Get the WRF variables
slp = getvar(ncfile, "slp")
smooth_slp = smooth2d(slp, 3)
ctt = getvar(ncfile, "PREC_ACC_NC")
z = getvar(ncfile, "z")
dbz = getvar(ncfile, "dbz")
Z = 10**(dbz/10.)
wspd =  getvar(ncfile, "wa", units="m s-1")

# Set the start point and end point for the cross section
start_point = CoordPair(lat=31.36, lon=118)
end_point = CoordPair(lat=32, lon=119.5)

# Compute the vertical cross-section interpolation.  Also, include the lat/lon points
# along the cross-section in the metadata by setting latlon to True.
z_cross = vertcross(Z, z, wrfin=ncfile, start_point=start_point, end_point=end_point,
                    latlon=True, meta=True)
wspd_cross = vertcross(wspd, z, wrfin=ncfile, start_point=start_point, end_point=end_point,
                       latlon=True, meta=True)
dbz_cross = 10.0 * np.log10(z_cross)

# Get the latitude and longitude points
lats, lons = latlon_coords(slp)

# Create the figure that will have 3 subplots
fig = plt.figure(figsize=(10,7))
ax_ctt = fig.add_subplot(1,2,1)
ax_wspd = fig.add_subplot(2,2,2)
ax_dbz = fig.add_subplot(2,2,4)

# Get the basemap object
bm = get_basemap(slp)

# Convert the lat/lon points in to x/y points in the projection space
x, y = bm(to_np(lons), to_np(lats))

# Make the pressure contours
contour_levels = [1001, 1002, 1003, 1004, 1005, 1006,1007,1008,1009]
c1 = bm.contour(x, y, to_np(smooth_slp), levels=contour_levels, colors="blue",
                zorder=3, linewidths=1.0, ax=ax_ctt,alpha=0.5)
plt.clabel(c1, inline=1, fontsize=10, fmt="%i",alpha=0.5)
# Create the filled cloud top temperature contours
contour_levels = [ 0,5, 10,15,20,25,30,35,40]
ctt_contours = bm.contourf(x, y, to_np(ctt), contour_levels, cmap=get_cmap("Greys"),
                           zorder=2, ax=ax_ctt)

point_x, point_y = bm([start_point.lon, end_point.lon], [start_point.lat, end_point.lat])
bm.plot([point_x[0], point_x[1]], [point_y[0], point_y[1]], color="yellow",
        marker="o", markersize=5,zorder=3, ax=ax_ctt,alpha=0.5,linewidth=0.8)

# Create the color bar for cloud top temperature
cb_ctt = fig.colorbar(ctt_contours, ax=ax_ctt, shrink=.60)
cb_ctt.ax.tick_params(labelsize=5)

# Draw the oceans, land, and states
#bm.drawcoastlines(linewidth=0.25, ax=ax_ctt)
#bm.drawstates(linewidth=0.25, ax=ax_ctt)
#bm.drawcountries(linewidth=0.25, ax=ax_ctt)
#bm.fillcontinents(color=np.array([ 0.9375 , 0.9375 , 0.859375]),
                  #ax=ax_ctt, lake_color=np.array([ 0.59375 , 0.71484375, 0.8828125 ]))
#bm.drawmapboundary(fill_color=np.array([ 0.59375 , 0.71484375, 0.8828125 ]), ax=ax_ctt)

# Draw Parallels
parallels = np.arange(np.amin(lats), np.amax(lats), 0.5)
bm.drawparallels(np.round(parallels,decimals=2), ax=ax_ctt, color="white",labels=[1,0,0,0],fontsize=7)

merids = np.arange(np.amin(lons), np.amax(lons), 0.5)
bm.drawmeridians(np.round(merids,decimals=2), ax=ax_ctt, color="white",labels=[0,0,0,1],fontsize=7)

# Crop the image to the hurricane region
x_start, y_start = bm(np.amin(lons), np.amin(lats))
x_end, y_end = bm(np.amax(lons), np.amax(lats))

ax_ctt.set_xlim([x_start, x_end])
ax_ctt.set_ylim([y_start, y_end])
#axmajorFormatter = FormatStrFormatter('%6.2f') #设置x轴标签文本的格式
#ax_ctt.xaxis.set_major_formatter(xmajorFormatter)
#ymajorFormatter = FormatStrFormatter('%6.2f') #设置x轴标签文本的格式
#ax_ctt.yaxis.set_major_formatter(ymajorFormatter)
#ax_ctt.xaxis.set_major_locator(MultipleLocator(10.00))
#ax_ctt.yaxis.set_major_locator(MultipleLocator(10.00))
#ax_ctt.xaxis.set_minor_locator(MultipleLocator(1))
#ax_ctt.yaxis.set_minor_locator(MultipleLocator(1))
#ax_ctt.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#ax_ctt.xaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
#ax_ctt.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#ax_ctt.yaxis.set_minor_formatter(FormatStrFormatter('%.2f'))

# Make the contour plot for wspd
wspd_contours = ax_wspd.contourf(to_np(wspd_cross), cmap=get_cmap("jet"))
# Add the color bar
cb_wspd = fig.colorbar(wspd_contours, ax=ax_wspd)
cb_wspd.ax.tick_params(labelsize=5)

# Make the contour plot for dbz
levels = [5 + 5*n for n in range(15)]
dbz_contours = ax_dbz.contourf(to_np(dbz_cross), levels=levels, cmap=get_cmap("jet"))
cb_dbz = fig.colorbar(dbz_contours, ax=ax_dbz)
cb_dbz.ax.tick_params(labelsize=5)

# Set the x-ticks to use latitude and longitude labels.
coord_pairs = to_np(dbz_cross.coords["xy_loc"])
x_ticks = np.arange(coord_pairs.shape[0])
x_labels = [pair.latlon_str() for pair in to_np(coord_pairs)]
ax_wspd.set_xticks(x_ticks[::10])
ax_wspd.set_xticklabels([], rotation=30)
ax_dbz.set_xticks(x_ticks[::10])
ax_dbz.set_xticklabels(x_labels[::10], rotation=30, fontsize=4)

# Set the y-ticks to be height.
vert_vals = to_np(dbz_cross.coords["vertical"])
v_ticks = np.arange(vert_vals.shape[0])
#np.round(vert_vals) wrong
ax_wspd.set_yticks(v_ticks[::20])
ax_wspd.set_yticklabels(np.around(vert_vals[::20],decimals=-2), fontsize=4)
ax_dbz.set_yticks(v_ticks[::20])
ax_dbz.set_yticklabels(np.around(vert_vals[::20],decimals=-2), fontsize=4)
# Set the x-axis and  y-axis labels
ax_dbz.set_xlabel("Latitude, Longitude", fontsize=5)
ax_wspd.set_ylabel("Height (m)", fontsize=5)
ax_dbz.set_ylabel("Height (m)", fontsize=5)

# Add titles
ax_ctt.set_title("Precipitation (mm/h)", {"fontsize" : 10})
ax_wspd.set_title("Cross-Section of Wind Speed (m s-1)", {"fontsize" : 7})
ax_dbz.set_title("Cross-Section of Reflectivity (dBZ)", {"fontsize" : 7})

plt.savefig("cross12bjt.png",dpi=200)
