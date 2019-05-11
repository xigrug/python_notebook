#!/bin/bash
source ./downpath
Dates=`date +%Y%m%d`

cd ${path_obs}
echo "$Dates" 
mkdir $Dates
echo "1111111111111111"
cd ${path_obs}/$Dates
echo "$Dates" &> obs$Dates.txt
#/usr/bin/links http://www.baidu.com/ -source 1 >>ticket_visit.txt
#/usr/bin/links http://221.203.171.112:10015/Handler/SevenDayAQI.ashx -source 1 >>obs$Dates.txt
/usr/bin/wget http://221.203.171.112:10025/Handler/SevenDayAQI.ashx -O obs$Dates.txt
cat obs$Dates.txt |sed 's/\///g' |sed 's/://g' >> temp ;mv temp obs$Dates.txt
