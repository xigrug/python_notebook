#!/bin/bash
# -----------------------------------------------------
# AUTHOR: Xxiaodong, NANJING UNIVERSITY, 01/25/2016
# HISTORY： modified 09/03/2018
# run once an hour
# download china weather figure
# -----------------------------------------------------
source ./downpath
echo "weather download starting!!!!!!!!!!"
echo "current time: `date +%Y%m%d%H`"
Cur_date=`date +%Y%m%d`
Past_date=`date +%Y%m%d -d "-1 day"`
Cur_hour=`date +%H`
C_date=`date +%Y/%m/%d -d "-1 day"`
P_date=`date +%Y-%m-%d -d "-2 day"`
Tsec_date=`date +%Y%m%d%H -d "-9 hour"`
Tfir_date=`date +%Y/%m/%d -d "-9 hour"`
wTsec_date=`date +%Y%m%d%H -d "-12 hour"`
wTfir_date=`date +%Y/%m/%d -d "-12 hour"`
echo $Cur_date

cd ${path_wea_c}/wind_temp   
#气温实况 http://image.nmc.cn/product/2017/01/24/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_20170124120000000.jpg
   file="NMCtem_obs_${wTsec_date}0000000.jpg"
   #echo $file
   wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${wTfir_date}/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_${wTsec_date}0000000.jpg" -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
cp ${file} ../temp
 

cd ${path_wea_c}/$Cur_date
day=1
i=0
while [ $i != "4" ]
do
   echo 'xxxxxxxxxxxxxx'

   echo $day
   
#降水预报 1-3天
   Fname="http://www.nmc.cn/publish/precipitation/${day}-day.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   #echo $url
   file="NMCprecipitation${Cur_date}_${day}day.JPG"
   #echo $file
   i=$(($i+1))
   day=`expr 1 + $day`   
   [[ -e ${file} ]] && continue
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi   
done
day=4
i=0
while [ $i != "8" ]
do
   echo 'xxxxxxxxxxxxxx'

   echo $day
   
#降水预报 4-7天
   Fname="http://www.nmc.cn/publish/precipitation/day${day}.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   #echo $url
   file="NMCprecipitation${Cur_date}_${day}day.JPG"
   #echo $file
   i=$(($i+1))
   day=`expr 1 + $day`   
   [[ -e ${file} ]] && continue
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi   
done
echo "Done Part7 !!!!!!!!!!!!!!!!!"
	

cd ${path_wea_c}/$Cur_date
	
i=0
hour=0
while [ $i != "7" ]
do
   echo 'xxxxxxxxxxxxxx'  
   hour=`expr 24 + $hour`
#气温预报
   Fname="http://www.nmc.cn/publish/temperature/hight/${hour}hour.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   #echo $url
   file="NMCtemperature_${Cur_date}_${hour}hour.JPG"
   #echo $file
   i=$(($i+1))   
   [[ -e ${file} ]] && continue
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
done
echo "Done Part9 !!!!!!!!!!!!!!!!!"	


exit 0
