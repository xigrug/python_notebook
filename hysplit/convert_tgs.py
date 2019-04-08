# coding: utf-8
import pandas as pd
import glob
import datetime

filenames = glob.glob('tback_2017*')
name=["start_year","start_month","start_date","start_hour","year","month","day","hour","age_hour","latitude","longitude","height","press"]
OUT = pd.DataFrame(columns=name)
filenames=sorted(filenames)

for filename in filenames:
    print(filename)
    data=pd.read_table(filename,sep='\s+',skiprows=[0,1,2,3,4],names=['traj_nums','grib_nums','year','month','day','hour', 'min','forecast_hours','age_hour','latitude','longitude','height','press'])
    df=data[['year','month','day','hour','age_hour','latitude','longitude','height','press']]
    date= df.apply(lambda x:datetime.datetime.strptime("{0} {1} {2} {3}"
                .format(int(x['year']),int(x['month']),int(x['day']),int(x['hour'])), "%y %m %d %H"),axis=1)
    df["longitude"]=df["longitude"].round(3)
    df["latitude"]=df["latitude"].round(3)
    year=pd.to_datetime(df['year'],format='%y').dt.strftime('%y')
    month=pd.to_datetime(df['month'],format='%m').dt.strftime('%m')
    date=pd.to_datetime(df['day'],format='%d').dt.strftime('%d')
    hour=pd.to_datetime(df['hour'],format='%H').dt.strftime('%H')
    df.insert(0,'start_hour',hour)
    df.insert(0,'start_date',date)
    df.insert(0,'start_month',month)
    df.insert(0,'start_year',year)
    OUT=pd.concat([OUT,df])
OUT.to_csv('traj.tgs', sep=',',encoding='utf-8',index=False)
