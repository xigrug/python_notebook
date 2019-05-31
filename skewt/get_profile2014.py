#!/usr/bin/env python
# coding: utf-8
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
#from metpy.cbook import get_test_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from sndfilter import soundingFilter
daterange = pd.date_range(start='20140819',periods=26,freq='0.5D')
station=["58238","58457","58362","54511","45004","59280"]#nj hz,sh,bj,hk,gz

for date in daterange:
    for sta in station:
        try:
            df = WyomingUpperAir.request_data(date,sta)
            df.to_csv(sta+'_'+str(date)[0:10]+"_"+str(date)[11:13]+".csv")
        #except OSError:
        except ValueError:
            pass
        continue
