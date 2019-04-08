# coding: utf-8
import pandas as pd
import glob
#import datetime
from datetime import datetime, timedelta, timezone
data=pd.read_csv("traj8.tgs")
date= data.apply(lambda x:datetime.strptime("{0} {1} {2} {3}"\
                 .format(int(x['year']),int(x['month']),int(x['day']),int(x['hour'])),\
                  "%y %m %d %H"),axis=1)
data.insert(0,'Date_BJC',date+timedelta(hours=8))
print(data.head())
data1=pd.read_csv("NanJ_hour.csv")
data1["Date_BJC"]=pd.to_datetime(data1["Date_BJC"])
print(data1.head())
data_out=pd.merge(data,data1,how="inner")
print(data_out.head())

data_out.to_csv('traj8_add.tgs', sep=',',encoding='utf-8',index=False)
