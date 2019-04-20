#!/bin/bash
source /public/home/hysplit/.bashrc 
##--Time Settings--
## tomorrow
strDate=`date +%Y%m%d -d "1 days"`
YY=`echo $strDate | cut -c1-4`
MM=`echo $strDate | cut -c5-6`
DD=`echo $strDate | cut -c7-8`
echo $YY-$MM-$DD

strDate=`date +%Y%m%d -d "2 days"`
yy1=`echo $strDate | cut -c1-4`
mm1=`echo $strDate | cut -c5-6`
dd1=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "3 days"`
yy2=`echo $strDate | cut -c1-4`
mm2=`echo $strDate | cut -c5-6`
dd2=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "4 days"`
yy3=`echo $strDate | cut -c1-4`
mm3=`echo $strDate | cut -c5-6`
dd3=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "5 days"`
yy4=`echo $strDate | cut -c1-4`
mm4=`echo $strDate | cut -c5-6`
dd4=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "6 days"`
yy5=`echo $strDate | cut -c1-4`
mm5=`echo $strDate | cut -c5-6`
dd5=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "7 days"`
yy6=`echo $strDate | cut -c1-4`
mm6=`echo $strDate | cut -c5-6`
dd6=`echo $strDate | cut -c7-8`

strDate=`date +%Y%m%d -d "8 days"`
yy7=`echo $strDate | cut -c1-4`
mm7=`echo $strDate | cut -c5-6`
dd7=`echo $strDate | cut -c7-8`

mkdir -p /public/home/hysplit/work/product/$YY-$MM-$DD-add/
export pptx_pic=/public/home/hysplit/work/product/$YY-$MM-$DD-add/
export pptx_script=/public/home/hysplit/work/product/script

cd $pptx_pic
ln -s $pptx_script/plot_*d04-add.py .
ln -s $pptx_script/create_ppt_mete-add.py  .
ln -s $pptx_script/500heightwind-add850.py  .
ln -s $pptx_script/surface.pyc  .
ln -s $pptx_script/weather3.pptx .
ln -s $pptx_script/post/CHN_adm1* .
#ln -s $pptx_script/skewt.sh .
#ln -s $pptx_script/gif.sh .
ln -s $pptx_script/nju_*.jpg .
ln -s /public/product/WrfData/wrfout/$YY$MM$DD/*t2*.png .
convert -delay 100 d03_cn_t2_*00_00.png d03_cn_t2.gif >>log.txt
convert -delay 100 d04_cn_t2_*00_00.png d04_cn_t2.gif >>log.txt
ln -s /public/product/WrfData/wrfout/$YY$MM$DD/*rh2*.png .
convert -delay 100 d03_cn_rh2_*00_00.png d03_cn_rh2.gif >>log.txt
convert -delay 100 d04_cn_rh2_*00_00.png d04_cn_rh2.gif >>log.txt
ln -s /public/product/WrfData/wrfout/$YY$MM$DD/*wind*.png .
convert -delay 100 d03_cn_wind_*00_00.png d03_cn_wind.gif >>log.txt
convert -delay 100 d03_cn_wind850_*00_00.png d03_cn_wind850.gif >>log.txt
convert -delay 100 d03_cn_wind700_*00_00.png d03_cn_wind700.gif >>log.txt
convert -delay 100 d03_cn_wind500_*00_00.png d03_cn_wind500.gif >>log.txt
convert -delay 100 d04_cn_wind_*00_00.png d04_cn_wind.gif >>log.txt
convert -delay 100 d04_cn_wind850_*00_00.png d04_cn_wind850.gif >>log.txt
convert -delay 100 d04_cn_wind700_*00_00.png d04_cn_wind700.gif >>log.txt
convert -delay 100 d04_cn_wind500_*00_00.png d04_cn_wind500.gif >>log.txt
ln -s /public/product/WrfData/wrfout/$YY$MM$DD/d04_mete.txt .
/public/home/hysplit/software/anaconda3/bin/python plot_qd-d04-add.py 
#/public/home/hysplit/software/anaconda3/envs/ppt/bin/python plot_qd-d04.pyc
/public/home/hysplit/software/anaconda3/bin/python plot_wqd-d04-add.py
#/public/home/hysplit/software/anaconda3/envs/ppt/bin/python plot_wqd-d04.pyc
counter=1
for i in `ls *_qd04.png`; do
    echo "Now working on $i"
    convert $i  nju_60x75.jpg -gravity southeast -geometry +5+930 -composite $i
    counter=`expr $counter + 1`
done

rm -f name.txt
ls d03_cn_t2_????-??-??.png >name.txt
ls d04_cn_t2_????-??-??.png >>name.txt
ls d03_cn_rh2_????-??-??.png >>name.txt
ls d04_cn_rh2_????-??-??.png >>name.txt
ls d03_cn_wind_????-??-??.png >>name.txt
ls d04_cn_wind_????-??-??.png >>name.txt
ls T2_qd04new.png >>name.txt
cp T2_qd04new.png /public/product/WrfData/wrfout/$YY$MM$DD/
ls RH2_qd04new.png >>name.txt
cp RH2_qd04new.png /public/product/WrfData/wrfout/$YY$MM$DD/
ls wspd10_qd04new.png >>name.txt
cp wspd10_qd04new.png /public/product/WrfData/wrfout/$YY$MM$DD/
ls wind10_qd04new.png >>name.txt
cp wind10_qd04new.png /public/product/WrfData/wrfout/$YY$MM$DD/
ls RAIN_qd04new.png >>name.txt
cp RAIN_qd04new.png /public/product/WrfData/wrfout/$YY$MM$DD/
ls d03_cn_t2.gif >>name.txt
ls d04_cn_t2.gif >>name.txt
ls d03_cn_rh2.gif >>name.txt
ls d04_cn_rh2.gif >>name.txt
ls d03_cn_wind.gif >>name.txt
ls d04_cn_wind.gif >>name.txt
ls d03_cn_wind850.gif >>name.txt
ls d04_cn_wind850.gif >>name.txt
ls d03_cn_wind700.gif >>name.txt
ls d04_cn_wind700.gif >>name.txt
ls d03_cn_wind500.gif >>name.txt
ls d04_cn_wind500.gif >>name.txt
/public/home/hysplit/software/anaconda3/bin/python 500heightwind-add850.py
#/public/home/hysplit/software/anaconda3/envs/ppt/bin/python 500heightwind.py

counter=1
for i in `ls 500-850_wea*.png`; do
    echo "Now working on $i"
    convert $i  nju_60x75.jpg -gravity southeast -geometry +178+100 -composite $i
    counter=`expr $counter + 1`
done
/public/home/hysplit/software/anaconda3/bin/python surface.pyc 
#/public/home/hysplit/software/anaconda3/envs/ppt/bin/python surface.py
counter=1
for i in `ls sur_wea*.png`; do
    echo "Now working on $i"
    convert $i  nju_60x75.jpg -gravity southeast -geometry +206+100 -composite $i
    counter=`expr $counter + 1`
done
convert -delay 100 500-850_wea*_0.png 500_wea_0.gif >>log.txt
convert -delay 100 500-850_wea*_12.png 500_wea_12.gif >>log.txt
ls 500_wea_*gif >>name.txt
zip 500_wea${YY}${MM}${DD}.zip 500_wea*png 500_wea*gif
convert -delay 100 sur_wea*_0.png sur_wea_0.gif >>log.txt
convert -delay 100 sur_wea*_12.png sur_wea_12.gif >>log.txt
ls sur_wea_*gif >>name.txt
zip sur_wea${YY}${MM}${DD}.zip sur_wea*png sur_wea*gif
ls 500-850_wea_day_2019-04-* >>name.txt
#counter=1
/public/home/hysplit/software/anaconda3/bin/python create_ppt_mete-add.py  weather3.pptx name.txt $YY-$MM-$DD-weather-add.pptx
#/public/home/hysplit/software/anaconda3/envs/ppt/bin/python create_ppt_mete.py  weather3.pptx name.txt $YY-$MM-$DD-weather.pptx
echo "weather.pptx done"
cp $YY-$MM-$DD-weather-add.pptx /public/product/WrfData/ppt/
mv $YY-$MM-$DD-weather-add.pptx /public/home/hysplit/pptout/
mv *.zip /public/home/hysplit/pptout/*-add.zip
#bash gif.sh >gif.log
'''
/usr/local/bin/ffmpeg -f gif -i 500_wea_0.gif 500_wea_0.wmv
/usr/local/bin/ffmpeg -f gif -i 500_wea_12.gif 500_wea_12.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_rh2.gif d03_cn_rh2.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_t2.gif d03_cn_t2.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_wind500.gif d03_cn_wind500.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_wind700.gif d03_cn_wind700.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_wind850.gif d03_cn_wind850.wmv
/usr/local/bin/ffmpeg -f gif -i d03_cn_wind.gif d03_cn_wind.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_rh2.gif d04_cn_rh2.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_t2.gif d04_cn_t2.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_wind500.gif d04_cn_wind500.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_wind700.gif d04_cn_wind700.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_wind850.gif d04_cn_wind850.wmv
/usr/local/bin/ffmpeg -f gif -i d04_cn_wind.gif d04_cn_wind.wmv
/usr/local/bin/ffmpeg -f gif -i skewt00.gif skewt00.wmv
/usr/local/bin/ffmpeg -f gif -i skewt06.gif skewt06.wmv
/usr/local/bin/ffmpeg -f gif -i skewt12.gif skewt12.wmv
/usr/local/bin/ffmpeg -f gif -i skewt18.gif skewt18.wmv
/usr/local/bin/ffmpeg -f gif -i sur_wea_0.gif sur_wea_0.wmv
/usr/local/bin/ffmpeg -f gif -i sur_wea_12.gif sur_wea_12.wmv
mkdir wmv
mkdir -p /public/home/hysplit/pptout/wmv/$YY-$MM-$DD/
mv *.wmv /public/home/hysplit/pptout/wmv/$YY-$MM-$DD/
'''
