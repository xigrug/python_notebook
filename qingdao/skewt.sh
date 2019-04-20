strDate=`date +%Y%m%d -d "1 days"`
YY=`echo $strDate | cut -c1-4`
MM=`echo $strDate | cut -c5-6`
DD=`echo $strDate | cut -c7-8`
echo $YY-$MM-$DD
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_$YY-${MM}-${DD}_00\:00\:00 --lat 36.067 --lon 120.390 -t 0 skewt_$YY$MM$DD-00.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_$YY-${MM}-${DD}_00\:00\:00 --lat 36.067 --lon 120.390 -t 6 skewt_$YY$MM$DD-06.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_$YY-${MM}-${DD}_00\:00\:00 --lat 36.067 --lon 120.390 -t 12 skewt_$YY$MM$DD-12.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_${YY}-${MM}-${DD}_00\:00\:00 --lat 36.067 --lon 120.390 -t 18 skewt_$YY$MM$DD-18.png
for i in {2..8..1}
do
strDate=`date +%Y%m%d -d "$i days"`
yy=`echo $strDate | cut -c1-4`
mm=`echo $strDate | cut -c5-6`
dd=`echo $strDate | cut -c7-8`
echo ${yy}_${mm}_${dd}
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_${yy}-${mm}-${dd}_00\:00\:00 --lat 36.067 --lon 120.390 -t 0 skewt_$yy$mm$dd-00.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_${yy}-${mm}-${dd}_00\:00\:00 --lat 36.067 --lon 120.390 -t 6 skewt_$yy$mm$dd-06.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_${yy}-${mm}-${dd}_00\:00\:00 --lat 36.067 --lon 120.390 -t 12 skewt_$yy$mm$dd-12.png
/public/home/hysplit/software/anaconda3/bin/skewt wrf -f /public/product/WrfData/wrf_seven_day/$YY$MM$DD/wrfout_d04_${yy}-${mm}-${dd}_00\:00\:00 --lat 36.067 --lon 120.390 -t 18 skewt_$yy$mm$dd-18.png
done
ls skewt*.png >>skewt.txt
