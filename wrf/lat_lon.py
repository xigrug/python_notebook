from __future__ import print_function

from netCDF4 import Dataset
from wrf import getvar, interpline, CoordPair, xy_to_ll, ll_to_xy

ncfile = Dataset("wrfout_d04_2018-06-12_00:00:00")

lat_lon = xy_to_ll(ncfile, 40, 20)

print(lat_lon)

x_y = ll_to_xy(ncfile, lat_lon[0], lat_lon[1])
x=x_y[0]
y=x_y[1]

print (x_y)
print (x)
print (y)
