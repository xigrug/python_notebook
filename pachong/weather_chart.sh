#!/bin/bash
# -----------------------------------------------------
# AUTHOR: Xxiaodong, NANJING UNIVERSITY, 01/25/2016
# HISTORY： modified 09/03/2018
# run once an hour
# download china weather figure
# -----------------------------------------------------
#source ./downpath
# set path for weather download

export home_path=/public/home/hysplit/work/study/python-ppt/pachong/data
export path_obs=$home_path/obs
export path_wea_c=$home_path/weather
export path_wea_f=$home_path/weather2

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
mkdir -p ${path_wea_c}/${Cur_date}
cd ${path_wea_c}/${Cur_date}   
#气温实况 http://image.nmc.cn/product/2017/01/24/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_20170124120000000.jpg
   file="NMCtem_obs_${wTsec_date}0000000.jpg"
   #echo $file
   wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${wTfir_date}/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_${wTsec_date}0000000.jpg" -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
#cp ${file} ../temp
 
#风场实况 http://image.nmc.cn/product/2017/01/24/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_20170124130000000.jpg?v=1485266014901
   file="NMCwind_obs_${wTsec_date}0000000.jpg"
   #echo $file
   wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${wTfir_date}/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_${wTsec_date}0000000.jpg" -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
#cp ${file} ../temp

#卫星云图45mins http://image.nmc.cn/product/2017/01/24/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170124134500000.JPG?v=1485266160691
#卫星云图15mins http://image.nmc.cn/product/2017/01/24/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170124131500000.JPG?v=1485264960610
        file="SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}4500000.JPG"
        wget -4  -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}4500000.JPG" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
#cp ${file} ../temp
        file="SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}1500000.JPG"
        wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}1500000.JPG" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
#cp ${file} ../temp

i=0
hour=0
while [ $i != "8" ]
do
    hour=$(printf "%02d" "$hour")
    Tsec_date=`date +%Y%m%d -d "0 day"`${hour}
    Tfir_date=`date +%Y/%m/%d -d "0 hour"`
  
    #地面分析 http://image.nmc.cn/product/2017/10/12/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_20171012090000000.jpg
       file="NMCsur_ana_${Tsec_date}.jpg"
       file1="CHNsur_ana_${Tsec_date}.jpg"
       fname="SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       fname1="SEVP_NMC_WESA_SFER_EGH_ACHN_L00_P9_${Tsec_date}0000000.jpg"
       #echo "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/SEVP_NMC_WESA_SFER_EGH_ACHN_L00_P9_${Tsec_date}0000000.jpg"
       ln -sf  ${fname} ${file}   
            if [ ! -e ${fname} ]; then
             rm -f ${file}
            elif [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname} ${file}
            fi
       ln -sf  ${fname1} ${file1}   
            if [ ! -e ${fname1} ]; then
             rm -f ${file1}
            elif [ "`ls -l ${fname1} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname1} ${file1}
            fi
    echo "Done Part8 !!!!!!!!!!!!!!!!!"
    #cp ${file} ../temp
    #cp ${file1} ../temp
    i=$(($i+1))
    hour=`expr 3 + $hour`
done

i=0
hour=0
while [ $i != "8" ]
do
    hour=$(printf "%02d" "$hour")
    Tsec_date=`date +%Y%m%d -d "-1 day"`${hour}
    Tfir_date=`date +%Y/%m/%d -d "-1 day"`
 
    #地面分析 http://image.nmc.cn/product/2017/10/12/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_20171012090000000.jpg
       file="NMCsur_ana_${Tsec_date}.jpg"
       file1="CHNsur_ana_${Tsec_date}.jpg"
       fname="SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       fname1="SEVP_NMC_WESA_SFER_EGH_ACHN_L00_P9_${Tsec_date}0000000.jpg"
       #echo "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/SEVP_NMC_WESA_SFER_EGH_ACHN_L00_P9_${Tsec_date}0000000.jpg"
       ln -sf  ${fname} ${file}   
            if [ ! -e ${fname} ]; then
             rm -f ${file}
            elif [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname} ${file}
            fi
       ln -sf  ${fname1} ${file1}   
            if [ ! -e ${fname1} ]; then
             rm -f ${file1}
            elif [ "`ls -l ${fname1} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname1} ${file1}
            fi
    echo "Done Part8 !!!!!!!!!!!!!!!!!"
    #cp ${file} ../temp
    #cp ${file1} ../temp
    i=$(($i+1))
    hour=`expr 3 + $hour`
done

i=0
hour=0
while [ $i != "2" ]
do
  hour=$(printf "%02d" "$hour")
  if [ $i = "0" ]; then
    Tsec_date=`date +%Y%m%d -d "0 day"`${hour}  
    Tfir_date=`date +%Y/%m/%d -d "0 hour"`
  else
    Tsec_date=`date +%Y%m%d -d "-1 day"`${hour} 
    Tfir_date=`date +%Y/%m/%d -d "-1 day"`
  fi
   echo $i ${Tsec_date}
     #statements 
         
    #850分析 http://image.nmc.cn/product/2017/10/12/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L85_P9_20171012000000000.jpg
       file="NMC850_ana_${Tsec_date}.jpg"
       file1="CHN850_ana_${Tsec_date}.jpg"
       fname="SEVP_NMC_WESA_SFER_EGH_ACWP_L85_P9_${Tsec_date}0000000.jpg"
       fname1="SEVP_NMC_WESA_SFER_EGH_ACHN_L85_P9_${Tsec_date}0000000.jpg"
       #echo "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L85_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L85_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/SEVP_NMC_WESA_SFER_EGH_ACHN_L85_P9_${Tsec_date}0000000.jpg"
       ln -sf  ${fname} ${file}
            if [ ! -e ${fname} ]; then
             rm -f ${file}
            elif [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname} ${file}
            fi
    echo "Done Part8 !!!!!!!!!!!!!!!!!"
    #cp ${file} ../temp
    #cp ${file1} ../temp

    #700分析
       file="NMC700_ana_${Tsec_date}.jpg"
       file1="CHN700_ana_${Tsec_date}.jpg"
       fname="SEVP_NMC_WESA_SFER_EGH_ACWP_L70_P9_${Tsec_date}0000000.jpg"
       fname1="SEVP_NMC_WESA_SFER_EGH_ACHN_L70_P9_${Tsec_date}0000000.jpg"
       #echo "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L70_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L70_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/SEVP_NMC_WESA_SFER_EGH_ACHN_L70_P9_${Tsec_date}0000000.jpg"
       ln -sf  ${fname} ${file}   
            if [ ! -e ${fname} ]; then
             rm -f ${file}
            elif [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname} ${file}
            fi
       ln -sf  ${fname1} ${file1}   
            if [ ! -e ${fname1} ]; then
             rm -f ${file1}
            elif [ "`ls -l ${fname1} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname1} ${file1}
            fi
    echo "Done Part8 !!!!!!!!!!!!!!!!!"
    #cp ${file} ../temp
    #cp ${file1} ../temp

    #500分析
       file="NMC500_ana_${Tsec_date}.jpg"
       file1="CHN500_ana_${Tsec_date}.jpg"
       fname="SEVP_NMC_WESA_SFER_EGH_ACWP_L50_P9_${Tsec_date}0000000.jpg"
       fname1="SEVP_NMC_WESA_SFER_EGH_ACHN_L50_P9_${Tsec_date}0000000.jpg"
       #echo "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L50_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/medium/SEVP_NMC_WESA_SFER_EGH_ACWP_L50_P9_${Tsec_date}0000000.jpg"
       wget -4 -S -c -N  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WESA/SEVP_NMC_WESA_SFER_EGH_ACHN_L50_P9_${Tsec_date}0000000.jpg"
       ln -sf  ${fname} ${file}   
            if [ ! -e ${fname} ]; then
             rm -f ${file}
            elif [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname} ${file}
            fi
       ln -sf  ${fname1} ${file1}   
            if [ ! -e ${fname1} ]; then
             rm -f ${file1}
            elif [ "`ls -l ${fname1} | awk '{print $5}'`" = "0" ]; then
             rm -f ${fname1} ${file1}
            fi
    echo "Done Part8 !!!!!!!!!!!!!!!!!"
    #cp ${file} ../temp
    #cp ${file1} ../temp
    i=$(($i+1))
    hour=`expr 12 + $hour`
done

pname[1]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/total-wind-speed-10-meters_1200.html"
pname[2]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/2m-temperature_1200.html"   
pname[3]="http://www.nmc.cn/publish/nwp/t639/ea/850hPa-rh-wind_1200.html"
pname[4]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/mean-sea-level-pressure_1200.html"
pname[5]="http://www.nmc.cn/publish/area/china/radar_1200.html"
pname[6]="http://www.nmc.cn/publish/nwp/t639gep/single/mean-dispersion/24h-accumulated-rainfall_1200.html"
pname[7]="http://www.nmc.cn/publish/satellite/fy2.htm"
pname[8]="http://www.nmc.cn/publish/nwp/t639/ea/500hPa-hgt.html"
pname[9]="http://www.nmc.cn/publish/nwp/t639/ea/700hPa-wind.html"
pname[10]="http://www.nmc.cn/publish/nwp/t639/ea/850hPa-wind.html"

cd ${path_wea_c}
mkdir $Cur_date
hour=12
i=1
while [ $i != "11" ]
do
echo $i
    echo ${pname[$i]}
    wget ${pname[$i]} -O html
    for url in $(grep -oP '(?<=data-original=").*?(?=" width)' html); do
        url=$( sed 's/small/medium/g' <<< ${url})
        echo $url
        dirv=$(cut -d '/' -f 5,6,7 <<< ${url})
        dir=$( sed 's/\///g' <<< ${dirv}); mkdir -p ${dir}
        #echo $dir
        filev=$(cut -d '/' -f 10 <<< ${url})
        file=${dir}/$(cut -d '?' -f 1 <<< $filev})
        #echo $file

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

cd ${path_wea_c}/$Cur_date
if [ "$Cur_hour" -eq "05" ]; then
 echo $Cur_date
 cp *.* ${path_wea_c}/temp
 cd ${path_wea_c}/$Past_date
 cp *.* ${path_wea_c}/temp
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
   #echo $url
   file="NMCpollution_${Cur_date}_${hour}.JPG"
   #echo $file
   i=$(($i+1))
   hour=`expr 24 + $hour`    
   if [ ! -e ${file} ]; then
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi 
   fi
done
echo "Done Part4 !!!!!!!!!!!!!!!!!"

cd ${path_wea_c}/$Cur_date

   echo 'xxxxxxxxxxxxxx'  
#雾预报
   Fname="http://www.nmc.cn/publish/fog.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   #echo $url
   file="NMCfog${Cur_date}.JPG"
   #echo $file
   if [ ! -e ${file} ]; then
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
   fi
echo "Done Part5 !!!!!!!!!!!!!!!!!"		

cd ${path_wea_c}/$Cur_date
   echo 'xxxxxxxxxxxxxx'  
#霾预报
   Fname="http://www.nmc.cn/publish/haze.html"
   wget $Fname -O html
   url=`grep -oP '(?<=" src=").*?(?=" onerror=)' html`
   #echo $url
   file="NMChaze${Cur_date}.JPG"
   #echo $file
   if [ ! -e ${file} ]; then
   wget -c -N ${url} -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
   fi
echo "Done Part6 !!!!!!!!!!!!!!!!!"	

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
