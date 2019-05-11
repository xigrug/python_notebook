#!/bin/bash
echo "weather download starting!!!!!!!!!!"
Cur_date=`date +%Y%m%d`
Past_date=`date +%Y%m%d -d "-1 day"`
Cur_hour=`date +%H`
C_date=`date +%Y/%m/%d -d "-1 day"`
P_date=`date +%Y-%m-%d -d "-2 day"`
Tsec_date=`date +%Y%m%d%H -d "-9 hour"`
wTsec_date=`date +%Y%m%d%H -d "-12 hour"`
Tfir_date=`date +%Y/%m/%d -d "-9 hour"`
wTfir_date=`date +%Y/%m/%d -d "-12 hour"`
echo $Cur_date

cd /data/forecast/statis/data/weather/wind_temp   
#气温实况 http://image.nmc.cn/product/2017/01/24/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_20170124120000000.jpg
   file="NMCtem_obs_${wTsec_date}0000000.jpg"
   echo $file
   wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${wTfir_date}/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_${wTsec_date}0000000.jpg" -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
cp ${file} ../temp
 
#风场实况 http://image.nmc.cn/product/2017/01/24/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_20170124130000000.jpg?v=1485266014901
   file="NMCwind_obs_${wTsec_date}0000000.jpg"
   echo $file
   wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${wTfir_date}/STFC/medium/SEVP_NMC_STFC_SFER_EDA_ACHN_L88_PB_${wTsec_date}0000000.jpg" -O ${file}
   rm -f html
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f ${file}
        fi
echo "Done Part8 !!!!!!!!!!!!!!!!!"
cp ${file} ../temp

#卫星云图45mins http://image.nmc.cn/product/2017/01/24/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170124134500000.JPG?v=1485266160691
#卫星云图15mins http://image.nmc.cn/product/2017/01/24/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_20170124131500000.JPG?v=1485264960610
        file="SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}4500000.JPG"
        wget -4  -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}4500000.JPG" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
cp ${file} ../temp
        file="SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}1500000.JPG"
        wget -4 -S -c  --tries=0 --timeout=60 "http://image.nmc.cn/product/${Tfir_date}/WXCL/medium/SEVP_NSMC_WXCL_ASC_E99_ACHN_LNO_PY_${Tsec_date}1500000.JPG" -O ${file}
        if [ "`ls -l ${file} | awk '{print $5}'`" = "0" ]; then
         rm -f $file
        fi
cp ${file} ../temp

