##https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.datetime.html
##http://python-awips.readthedocs.io/en/latest/examples/generated/Profiler_Wind_Barb_Time-Series.html
from matplotlib.cm import get_cmap
from datetime import datetime, timedelta
from matplotlib.dates import date2num
#from metpy.units import units
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
from wrf import getvar,  ll_to_xy, ALL_TIMES, extract_times
# Query ESRL/PSD profiler data from Unidata AWIPS
ncfile = Dataset("../wrfout_d04_2018-06-11_00:00:00")
x_y = ll_to_xy(ncfile, '36.067', '120.390')
x=x_y[0]
y=x_y[1]
#print(x)
#print(y)
#wrftime=extract_times(ncfile,timeidx=ALL_TIMES,do_xtime=True)
wrftime=extract_times(ncfile,timeidx=ALL_TIMES)
print(wrftime)
p = getvar(ncfile, "pressure",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
#p = getvar(ncfile, "pressure")[:,:,x,y]
#pblh = getvar(ncfile, "PBLH",timeidx=ALL_TIMES,squeeze=False)[:,x,y]
times = getvar(ncfile, "times",timeidx=ALL_TIMES,squeeze=False)
#times = getvar(ncfile, "XTIME")
print(times)
heights = getvar(ncfile, "z", units="km",timeidx=ALL_TIMES,squeeze=False)[0,:,x,y]
#print(heights)
u = getvar(ncfile, "ua", units="kt",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
v = getvar(ncfile, "va", units="kt",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
rh = getvar(ncfile, "rh",timeidx=ALL_TIMES,squeeze=False)[:,:,x,y]
#print(rh[0,:])
#print(u)
#wspd = getvar(ncfile, "wspd_wdir", units="kts")[0,:]
fig = plt.figure(figsize=(16,7))
cmap=plt.cm.RdYlGn_r
# Build arrays
# Convert u,v components to knots and transpose arrays to match t,h
#u = (np.asarray(u, dtype=np.float32) * units('m/s')).to('knots').T
#v = (np.asarray(v, dtype=np.float32) * units('m/s')).to('knots').T
#T, H = np.meshgrid(heights,wrftime)
T, H = np.meshgrid(wrftime,heights)
C = np.sqrt(u**2 + v**2)
fig, ax = plt.subplots()    
#xy=ax.barbs(t, h, u, v)
xy=ax.barbs(T, H, u, v)
#xy=ax.quiver(T, H, u, v)
ax.title.set_text("test_profile")
# Make the contour plot
#rh_contours=ax.pcolormesh(T,H,rh, cmap=get_cmap("YlGn"))
#rh_contours=ax.contourf(T,H,rh, cmap=get_cmap("YlGn"))

# Add the color bar
#plt.colorbar(rh_contours)
#ax.xaxis_date()
#ax.set_xlim(times[0]-timedelta(hours=1), times[-1]+timedelta(hours=1))
ax.set_xlim(wrftime[0]-np.timedelta64(1, 'h'), wrftime[-1]+np.timedelta64(1, 'h'))
#ax.set_ylim(0,10000)
#ax.grid(axis='x', which='major', alpha=0.5)
#ax.grid(axis='y', which='major', linestyle=':')
#plt.gca().invert_xaxis()
plt.savefig("wind_profile2-barbs.png",dpi=600,bbox_inches='tight')
#plt.show()
