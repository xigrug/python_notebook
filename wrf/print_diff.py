import numpy as np
from netCDF4 import Dataset
from wrf import getvar, xy, interpline, to_np, vertcross, smooth2d, CoordPair, get_basemap, latlon_coords

# Open the NetCDF file
def print_diff(filename,filename1,i):
    ncfile = Dataset(filename)
    ncfile1 = Dataset(filename1)
# Get the WRF variables
    slp = getvar(ncfile, "slp")
    smooth_slp = smooth2d(slp, 3)
    ctt = getvar(ncfile, "PREC_ACC_NC")
    ctt1 = getvar(ncfile1, "PREC_ACC_NC")
    ctt_diff = ctt-ctt1
    print(ctt_diff.max())
    print(ctt_diff.min())
print_diff('02chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',1)
print_diff('10chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',2)
print_diff('100chem_d04_2017-06-10_04:00:00','chem_d04_2017-06-10_04:00:00',3)
