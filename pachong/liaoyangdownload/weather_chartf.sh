#!/bin/bash
# -----------------------------------------------------
# AUTHOR: Xxiaodong, NANJING UNIVERSITY, 01/25/2016
# HISTORY： modified 09/03/2018
# run once an hour
# download korea&ncep weather figure
# -----------------------------------------------------
source ./downpath
echo "weather download starting!!!!!!!!!!"
Cur_date=`date +%Y%m%d`
Past_date=`date +%Y%m%d -d "-1 day"`
Cur_hour=`date +%H`
C_date=`date +%Y/%m/%d -d "-1 day"`
P_date=`date +%Y-%m-%d -d "-2 day"`
Tsec_date=`date +%Y%m%d%H -d "-9 hour"`
Tfir_date=`date +%Y/%m/%d -d "-1 hour"`
echo $Cur_date


if [ "$Cur_hour" -gt "04" ]; then
 echo $Cur_hour
 echo "hour pass 4:00"
 exit 0
fi

Start_date=`date +%Y-%m-%d -d "-1 day"`
echo ${Start_date}
cd ${path_wea_f}
mkdir $Cur_date
cd $Cur_date

hour=00
i=0
while [ $i != "25" ]
do
   echo $hour
   hour=$(printf "%02d" "$hour")
#韩国 700风速和850温度
   Fname1="http://www.kma.go.kr/cht/ra2d/ra2d_asia3_vel700_ft06_pa4_s0${hour}_${Past_date}00.png"
   file1="KOREA700wind_850tem_${Cur_date}_${hour}.png"
   fname1=ra2d_asia3_vel700_ft06_pa4_s0${hour}_${Past_date}00.png
#韩国 500温度和相对涡度   
   Fname3="http://www.kma.go.kr/cht/ra2d/ra2d_asia3_gph500_ft06_pa4_s0${hour}_${Past_date}00.png"
   file3="KOREA500tem_reVor_${Cur_date}_${hour}.png"
   fname3=ra2d_asia3_gph500_ft06_pa4_s0${hour}_${Past_date}00.png
   wget -c -N ${Fname1}
   ln -sf  ${fname1} ${file1}
   wget -c -N ${Fname2}
   ln -sf  ${fname2} ${file2}
   wget -c -N ${Fname3}
   ln -sf  ${fname3} ${file3}
        if [ "`ls -l ${fname1} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname1}
		else
		 cp ${file1} ${path_wea_f}/temp
        fi
        if [ "`ls -l ${fname2} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname2}
		else
		 cp ${file2} ${path_wea_f}/temp		 
        fi
        if [ "`ls -l ${fname3} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname3}
		else
		 cp ${file3} ${path_wea_f}/temp		 
        fi
   i=$(($i+1))
   hour=`expr 6 + $hour`   
done
echo "Done Part1 !!!!!!!!!!!!!!!!!"

hour=00
i=0
while [ $i != "8" ]
do
   echo $hour
   hour=$(printf "%03d" "$hour")

#韩国 海平面累计雨量 
   Fname2="http://web.kma.go.kr/repositary/image/cht/img/g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif"
   fname=g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif
   file2="KOREAmslp_accPre_${Cur_date}_${hour}.gif"


   wget -c -N ${Fname2} 
   ln -sf ${fname} ${file2}
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file2} ${path_wea_f}/temp		 
        fi

   i=$(($i+1))
   hour=`expr 3 + $hour`   
done
hour=30
i=0
while [ $i != "9" ]
do
   echo $hour
   hour=$(printf "%03d" "$hour")

#韩国 海平面累计雨量 
   Fname2="http://web.kma.go.kr/repositary/image/cht/img/g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif"
   fname=g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif
   file2="KOREAmslp_accPre_${Cur_date}_${hour}.gif"


   wget -c -N ${Fname2}
   ln -sf ${fname} ${file2}
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file2} ${path_wea_f}/temp		 
        fi

   i=$(($i+1))
   hour=`expr 6 + $hour`   
done
hour=96
i=0
while [ $i != "7" ]
do
   echo $hour
   hour=$(printf "%03d" "$hour")

#韩国 海平面累计雨量 
   Fname2="http://web.kma.go.kr/repositary/image/cht/img/g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif"
   fname=g213_asia_post_grph_ft12_surfce_pa4_${Past_date}00.s${hour}.gif
   file2="KOREAmslp_accPre_${Cur_date}_${hour}.gif"


   wget -c -N ${Fname2}
   ln -sf ${fname} ${file2}
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file2} ${path_wea_f}/temp		 
        fi

   i=$(($i+1))
   hour=`expr 12 + $hour`   
done


hour=0
i=1
while [ $i != "37" ]
do
   echo $hour
   echo $End_date  
#美国 海平面气压和降水
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_mslp_pcpn_wpac_${i}.png
   fname=gfs_mslp_pcpn_wpac_${i}.png
   file="NCEPmslp_rain_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi
#美国 海平面气压和风场
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_mslp_wind_wpac_${i}.png
   fname=gfs_mslp_wind_wpac_${i}.png
   file="NCEPmslp_wind_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi
#美国 海平面气压和850hPa风场
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_mslp_uv850_wpac_${i}.png
   fname=gfs_mslp_uv850_wpac_${i}.png
   file="NCEPmslp_850wind_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi
#美国 500hPa高度和海平面气压
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_z500_mslp_wpac_${i}.png
   fname=gfs_z500_mslp_wpac_${i}.png
   echo $url
   file="NCEPmslp_500height_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi
#美国 700高度涡度风
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_z700_vort_wpac_${i}.png
   fname=gfs_z700_vort_wpac_${i}.png
   file="NCEP700vort_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi		
#美国 850高度涡度风
   url=http://www.tropicaltidbits.com/analysis/models/gfs/${Past_date}12/gfs_z850_vort_wpac_${i}.png
   fname=gfs_z850_vort_wpac_${i}.png
   file="NCEP850vort_${Cur_date}_${hour}.png"
   echo $file
   wget -c -N ${url}
   ln -sf ${fname} ${file}
   rm -f html
        if [ "`ls -l ${fname} | awk '{print $5}'`" = "0" ]; then
         rm -f ${fname}
		else
		 cp ${file} ${path_wea_f}/temp		 
        fi
   i=$(($i+1))
   hour=`expr 6 + $hour`   
done
echo "Done !!!!!!!!!!!!!!!!!"
	
exit 0
