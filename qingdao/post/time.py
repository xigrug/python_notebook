import time  
print(time.time()) 
timea=time.localtime(time.time()) 
print(timea) 
#time.struct_time(tm_year=2010, tm_mon=7, tm_mday=19, tm_hour=22, tm_min=33, tm_sec=39, tm_wday=0, tm_yday=200, tm_isdst=0)
timeb=time.strftime("%Y-%m-%d",time.localtime(time.time()))
print(timeb)
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime) 
