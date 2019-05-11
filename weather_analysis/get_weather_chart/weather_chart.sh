#!/bin/bash
# -----------------------------------------------------
# AUTHOR: XIE & JIANG, NANJING UNIVERSITY, 01/25/2016
# -----------------------------------------------------

echo "weather download starting!!!!!!!!!!"
echo "current time: `date +%Y%m%d%H`"
Cur_date=`date +%Y%m%d`
Past_date=`date +%Y%m%d -d "-1 day"`
Cur_hour=`date +%H`
C_date=`date +%Y/%m/%d -d "-1 day"`
P_date=`date +%Y-%m-%d -d "-2 day"`
echo /data/forecast/statis/data/weather/$Cur_date


pname[1]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/total-wind-speed-10-meters_1200.html"
pname[2]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/2m-temperature_1200.html"   
pname[3]="http://www.nmc.cn/publish/nwp/t639/ea/850hPa-rh-wind_1200.html"
pname[4]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/mean-sea-level-pressure_1200.html"
pname[5]="http://www.nmc.cn/publish/area/china/radar_1200.html"
pname[6]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/24h-accumulated-rainfall_1200.html"
pname[7]="http://www.nmc.cn/publish/satellite/fy2.htm"


cd /data/forecast/statis/data/weather
mkdir $Cur_date
hour=12
i=1
while [ $i != "8" ]
do
echo $i
    echo ${pname[$i]}
    wget ${pname[$i]} -O html
echo "11111111111111111111111111111"
    for url in $(grep -oP '(?<=data-original=").*?(?=" width)' html); do
        url=$( sed 's/small/medium/g' <<< ${url})
        echo $url
echo "222222222222222222222222"
        dirv=$(cut -d '/' -f 5,6,7 <<< ${url})
        dir=$( sed 's/\///g' <<< ${dirv}); mkdir -p ${dir}
        echo $dir
        filev=$(cut -d '/' -f 10 <<< ${url})
        file=${dir}/$(cut -d '?' -f 1 <<< $filev})
        echo $file

        [[ -e ${file} ]] && continue
       # wget -S -c -N --tries=5 --wait=5 --no-proxy --no-check-certificate ${url} -O ${file}; sleep 5s
        wget -c -N  ${url} -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
    done

rm -f html

i=$(($i+1))
done

cd /data/forecast/statis/data/weather/$Cur_date
if [ "$Cur_hour" -eq "05" ]; then
 echo $Cur_date
 cp *.* /data/forecast/statis/data/weather/temp
 cd /data/forecast/statis/data/weather/$Past_date
 cp *.* /data/forecast/statis/data/weather/temp
 exit 0
fi

if [ "$Cur_hour" -gt "04" ]; then
 echo $Cur_hour
 echo "hour pass 4:00"
 exit 0
fi

hour=24
i=0
while [ $i != "2" ]
do
   echo 'xxxxxxxxxxxxxx'

   echo $hour
   echo $End_date   
#污染气象条件
   Fname="http://www.nmc.cn/publish/environment/air_pollution-${hour}.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   echo $url
   file="NMCpollution_${Cur_date}_${hour}.JPG"
   echo $file
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
   i=$(($i+1))
   hour=`expr 24 + $hour`   
done
echo "Done Part4 !!!!!!!!!!!!!!!!!"

cd /data/forecast/statis/data/weather/$Cur_date

   echo 'xxxxxxxxxxxxxx'  
#雾预报
   Fname="http://www.nmc.cn/publish/fog.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   echo $url
   file="NMCfog${Cur_date}.JPG"
   echo $file
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part5 !!!!!!!!!!!!!!!!!"		

cd /data/forecast/statis/data/weather/$Cur_date
   echo 'xxxxxxxxxxxxxx'  
#霾预报
   Fname="http://www.nmc.cn/publish/haze.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   echo $url
   file="NMChaze${Cur_date}.JPG"
   echo $file
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part6 !!!!!!!!!!!!!!!!!"	

cd /data/forecast/statis/data/weather/$Cur_date
day=1
i=0
while [ $i != "6" ]
do
   echo 'xxxxxxxxxxxxxx'

   echo $day
   
#降水预报
   Fname="http://www.nmc.cn/publish/precipitation/${day}-day.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   echo $url
   file="NMCprecipitation${Cur_date}_${day}day.JPG"
   echo $file
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
   i=$(($i+1))
   day=`expr 1 + $day`   
done
echo "Done Part7 !!!!!!!!!!!!!!!!!"
	

cd /data/forecast/statis/data/weather/$Cur_date
	
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
   echo $url
   file="NMCtemperature_${Cur_date}_${hour}hour.JPG"
   echo $file
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
   i=$(($i+1))
done
echo "Done Part9 !!!!!!!!!!!!!!!!!"	


exit 0
