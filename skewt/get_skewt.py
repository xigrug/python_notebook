# Brian Blaylock
# July 6, 2015

# Download, process, and Plot Sounding Data from University of Wyoming

import urllib3
from bs4 import BeautifulSoup
from skewt import SkewT
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
daterange = pd.date_range(start='20140601',periods=184,freq='0.5D')
stn=["58238","58457","58362","54511","45004","59280"]#nj hz,sh,bj,hk,gz
#stn = ['52203','51777','51839','51828','51709','51644','51463'] #72572 is ID for SLC
#name = ['HM','RQ','MF','HT','KS','KQ','Urumqi'] #72572 is ID for SLC
for date in daterange:
    print(date)
    year=str(date)[0:4]
    month =str(date)[5:7]
    day = str(date)[8:10]
    hour = str(date)[11:13] #either 12 or 00

# 1) 
# Wyoming URL to download Sounding from
    http = urllib3.PoolManager()
    for sta in stn:
        print(sta)
        url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR='+year+'&MONTH='+month+'&FROM='+day+hour+'&TO='+day+hour+'&STNM='+sta
    #print(url)
        response = http.request('GET', url)
# 2)
# Remove the html tags
        soup = BeautifulSoup(response.data)
        data_text = soup.get_text()

#text_file = open(stn+year+month+day+hour+'.txt', "w")
#text_file.write("Purchase Amount: %s" % data_text)
#text_file.close()

#data_text.to_csv(stn+year+month+day+hour+'.csv',encoding='gbk')
# 3)
# Split the content by new line.
        splitted = data_text.split("\n",data_text.count("\n"))

# 4)
# Write this splitted text to a .txt document
        Sounding_filename = str(sta)+'_'+str(year)+str(month)+str(day)+str(hour)+'.txt'
        f = open(Sounding_filename,'w')
        for line in splitted[4:]:
            f.write(line+'\n')
        f.close()

