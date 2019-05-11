#!/bin/bash
# -----------------------------------------------------
# AUTHOR: Xxiaodong, NANJING UNIVERSITY, 01/25/2016
# HISTORY： modified 09/03/2018
# download japan satellite figure
# -----------------------------------------------------
source ./downpath
echo "weather download starting!!!!!!!!!!"

Tsec_date=`date +%Y-%m-%d-%H -d "-40 mins"`
Tfir_date=`date +%Y%m%d%H -d "-40 mins"`
Tmin_date=`date +%M -d "-40 mins"`
Tmin=${Tmin_date:0:1}
echo $Tsec_date
echo ${Tmin_date}
echo $Tmin

cd ${path_wea_f}/sat_temp   
# 日本葵花卫星   http://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-2017-04-28-09-20.jpg
        file="japan_sat_${Tfir_date}${Tmin}0.jpg"
        wget -4   -U firefox -S -c  --tries=0 --timeout=60 "http://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/s1p-${Tsec_date}-${Tmin}0.jpg" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
cp ${file} ../temp
