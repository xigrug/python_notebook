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
echo $Cur_date


pname[1]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/total-wind-speed-10-meters_1200.html"
pname[2]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/2m-temperature_1200.html"   
pname[3]="http://www.nmc.cn/publish/nwp/t639/ea/850hPa-rh-wind_1200.html"
pname[4]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/mean-sea-level-pressure_1200.html"
pname[5]="http://www.nmc.cn/publish/area/china/radar_1200.html"
pname[6]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/24h-accumulated-rainfall_1200.html"
pname[7]="http://www.nmc.cn/publish/satellite/fy2.htm"

cd /data/forecast/statis/data/weather/wind_temp   
#气温实况 
   wget --tries=25 --wait=5 -c "http://www.nmc.cn/publish/observations/hourly-temperature.html" -O html;sleep 5s
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   filev=$(cut -d '/' -f 10 <<< ${url})
   file=$(cut -d '?' -f 1 <<< $filev})
   F_date=$(cut -d '_' -f 9 <<< ${file})
   file="NMCtem_obs_${F_date}"
   echo $file
   wget -S -c  --tries=25 --wait=5 ${url} -O ${file}; sleep 5s
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
cp ${file} ../temp
 
#风场实况
   wget  --tries=25 --wait=5 -c "http://www.nmc.cn/publish/observations/hourly-winds.html" -O html;sleep 5s
echo "ssssssssssssssssssssss"
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   filev=$(cut -d '/' -f 10 <<< ${url})
   file=$(cut -d '?' -f 1 <<< $filev})
   F_date=$(cut -d '_' -f 9 <<< ${file})
   file="NMCwind_obs_${F_date}"
   echo $file
   wget -S -c  --tries=25 --wait=5 ${url} -O ${file}; sleep 5s
echo "ddddddddddddddddddddddddddddddddddd"
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
cp ${file} ../temp

i=7
echo $i
    echo ${pname[$i]}
    wget -S -c --tries=25 --wait=5 "http://www.nmc.cn/publish/satellite/fy2.htm" -O html;sleep 5s
    urls=$(grep -oP '(?<=data-original=").*?(?=" width)' html)
echo "sssssssssssssssssssssssssssssssssssssssss"
        j=1
        while [ $j != "3" ]
        do
        url=$(cut -d ' ' -f $j <<< ${urls})
echo $url
        echo $url
        filev=$(cut -d '/' -f 10 <<< ${url})
        file=$(cut -d '?' -f 1 <<< $filev})
        echo $file
        wget -S -c  --tries=25 --wait=5 ${url} -O ${file}; sleep 5s
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
        j=$(($j+1))
    done

rm -f html

cd /data/forecast/statis/data/weather

hour=12
i=1
while [ $i != "7" ]
do
echo $i
    echo ${pname[$i]}
    wget ${pname[$i]} -O html
echo "11111111111111111111111111111"
    for url in $(grep -oP '(?<=data-original=").*?(?=" width)' html); do
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

cd $Cur_date
if [ "$Cur_hour" -eq "05" ]; then
 echo $Cur_date
 cp *.* /data/forecast/statis/data/weather/temp/
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
