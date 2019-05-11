#!/bin/bash
# -----------------------------------------------------
# AUTHOR: Xxiaodong, NANJING UNIVERSITY, 01/25/2016
# HISTORY： modified 09/03/2018
# download japan ana
# -----------------------------------------------------
source ./downpath
echo "weather download starting!!!!!!!!!!"

Tsec_date=`date +%y%m%d%H -d "-3 hours"`
Tfir_date=`date +%Y%m%d%H -d "-3 hours"`

echo $Tsec_date

cd ${path_wea_f}/sat_temp   
# 日本地面分析   http://www.jma.go.jp/jp/g3/images/jp_c/17042806.png
        file="japan_surface_${Tfir_date}.png"
        wget -4   -U firefox -S -c  --tries=0 --timeout=60 "http://www.jma.go.jp/jp/g3/images/jp_c/${Tsec_date}.png" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
cp ${file} ../temp
