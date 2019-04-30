import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.colors as colors
import numpy as np
from netCDF4 import Dataset
from wrf import getvar, xy, interpline, to_np, vertcross, smooth2d, CoordPair, get_basemap, latlon_coords
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition
fig, big_axes = plt.subplots(figsize=(15.0, 15.0) , nrows=1, ncols=1, sharey=True) 

#for row, big_ax in enumerate(big_axes, start=1):
    #big_ax.set_title("Subplot row %s \n" % row, fontsize=16)

    # Turn off axis lines and ticks of the big subplot 
    # obs alpha is 0 in RGBA string!
big_axes.tick_params(labelcolor=(0,0,0,0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
big_axes._frameon = False

def get_axis_limits(ax, scalex=.03,scaley=0.93):
    return ax.get_xlim()[1]*scalex, ax.get_ylim()[1]*scaley
axes=['ax1', 'ax2','ax3','ax4']
#axes=['ax1', 'ax2','ax3','ax4','ax5','ax6','ax7','ax8','ax9','ax10','ax11','ax12']
#NUM=['A', 'B','C','D','E','F','G','H','I','G','K','L']
NUM=['A', 'B','C','D']
for i in range(0,4):
    axes[i] = fig.add_subplot(1,4,i+1)
    plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
    #axes[i].set_title('Plot title ' + str(i+1))
    #axes[i].annotate(NUM[i], xy=get_axis_limits(axes[i]))
fig.set_facecolor('w')
plt.tight_layout()

class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        # https://matplotlib.org/users/colormapnorms.html#custom-normalization-two-linear-ranges
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))
# Open the NetCDF file
def plot_cross(filename,filename1,i):
    ncfile = Dataset(filename)
    ncfile1 = Dataset(filename1)
# Get the WRF variables
    slp = getvar(ncfile, "slp")
    smooth_slp = smooth2d(slp, 3)
    ctt = getvar(ncfile, "PREC_ACC_NC")
    ctt1 = getvar(ncfile1, "PREC_ACC_NC")
    ctt_diff = ctt-ctt1
# Get the basemap object
    # Get the latitude and longitude points
    lats, lons = latlon_coords(slp)


    bm = get_basemap(slp)
    x, y = bm(to_np(lons), to_np(lats))
# Convert the lat/lon points in to x/y points in the projection space

# Make the pressure contours
    contour_levels = [1001, 1002, 1003, 1004, 1005, 1006,1007,1008,1009]
    c1 = bm.contour(x, y, to_np(smooth_slp), levels=contour_levels, colors="blue",
                zorder=3, linewidths=1.0, ax=axes[i],alpha=0.5)
    plt.clabel(c1, inline=1, fontsize=10, fmt="%i",alpha=0.5)
# Create the filled cloud top temperature contours
    #contour_levels = [ 0,5, 10,15,20,25,30,35,40,45,50,55,60]
    contour_levels = [ -50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5, 10,15,20,25,30,35,40,45,50,]
    ctt_contours = bm.contourf(x, y, to_np(ctt_diff), contour_levels, cmap=get_cmap("coolwarm"),
                           zorder=2, ax=axes[i])

# Create the color bar for cloud top temperature
    #cb_ctt = fig.colorbar(ctt_contours, ax=axes[i], extend='both',shrink=.60)
    #cb_ctt.ax.tick_params(labelsize=9)

# Draw Parallels
    parallels = np.arange(np.amin(lats), np.amax(lats), 0.5)
    if i ==0 :
        bm.drawparallels(np.round(parallels,decimals=2), ax=axes[i], color="white",labels=[1,0,0,0],fontsize=15)

    merids = np.arange(np.amin(lons), np.amax(lons), 0.5)
    bm.drawmeridians(np.round(merids,decimals=2), ax=axes[i], color="white",labels=[0,0,0,1],rotation=18,fontsize=15)


#np.round(vert_vals) wrong
# Set the x-axis and  y-axis labels
    #axes[i+8].set_xlabel("Latitude, Longitude", fontsize=10)
    #axes[i+4].set_ylabel("Height (m)", fontsize=10)
    #axes[i+8].set_ylabel("Height (m)", fontsize=10)
# Add titles
#    axes[i].set_title("Precipitation (mm/h)", {"fontsize" : 10})
#    axes[i+4].set_title(r"Wind Speed (m $s^{-3}$)", {"fontsize" : 10})
#    axes[i+8].set_title(r"Reflectivity(dBZ)& CCN(S=0.2%,$cm^{-3}$) ", {"fontsize" : 10})
    return ctt_contours
plot_cross('chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',0)
plot_cross('02chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',1)
plot_cross('10chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',2)
ctt=plot_cross('100chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',3)
for i in range(0,3):
    axes[i].annotate(NUM[i], xy=get_axis_limits(axes[i]),fontsize=15)
#plt.tight_layout()
# Add titles
#big_axes.set_title("Precipitation (mm/h)", {"fontsize" : 20})
fig.text(0.5, 0.65, 'Precipitation (mm/h)', ha='center',fontsize=20)
#[left, bottom, width, height] 
cax = fig.add_axes([1.01, 0.4, 0.02, 0.2])
#cax1 = fig.add_axes([1.01, 0.42, 0.02, 0.2])
#cax2 = fig.add_axes([1.01, 0.08, 0.02, 0.2])
# The colorbar is also based on this master image.
cbar=fig.colorbar(ctt, cax, orientation='vertical')
#cbar=fig.colorbar(ctt, orientation='vertical')
cbar.ax.tick_params(labelsize=15)
fig.text(0.5, 0.35, 'Latitude, Longitude', ha='center',fontsize=20)
#fig.text( 'Latitude, Longitude', ha='center',fontsize=20)
fig.text(-0.04, 0.50, 'Height (m)', va='center', rotation='vertical',fontsize=20)
#fig.text('Height (m)', va='center', rotation='vertical',fontsize=20)
plt.savefig("diff_panel1.png",dpi=600,bbox_inches='tight')
#plt.show()
