#!/bin/bash
source /public/home/hysplit/.bashrc 
##--Time Settings--
## tomorrow
strDate=`date +%Y%m%d`
yy=`echo $strDate | cut -c1-4`
mm=`echo $strDate | cut -c5-6`
dd=`echo $strDate | cut -c7-8`
echo $yy-$mm-$dd

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

mkdir -p /public/home/hysplit/work/product/$YY-$MM-$DD/
export pptx_pic=/public/home/hysplit/work/product/$YY-$MM-$DD/
export pptx_script=/public/home/hysplit/work/product/script

cd $pptx_pic
ln -s $pptx_script/create_ppt_btraj.py .
ln -s $pptx_script/traj3.pptx .
#ln -s $pptx_script/nju_60x75.jpg .
ln -s /public/product/Trajectory/hysplit/$YY-$MM-$DD/*back.jpg .

##add logo###
counter=1
for i in `ls *back.jpg`; do
    echo "Now working on $i"
    #convert $i  nju_60x75.jpg -gravity southeast -geometry +130+361 -composite $i
    convert -trim $i +repage qd-${i}
    convert qd-${i} -crop 604x584+0+80 tump-${i} 
    #convert -resize 132x165! tump-${i} crop-${i} 
    convert -resize 1650x1320! tump-${i} crop-${i} 
    counter=`expr $counter + 1`
done

convert -delay 100 qd-plot_$yy$mm${dd}16_back.jpg qd-plot_$yy$mm${dd}19_back.jpg qd-plot_$yy$mm${dd}22_back.jpg qd-plot_$YY$MM${DD}01_back.jpg qd-plot_$YY$MM${DD}04_back.jpg qd-plot_$YY$MM${DD}07_back.jpg qd-plot_$YY$MM${DD}10_back.jpg qd-plot_$YY$MM${DD}13_back.jpg qd-plot_$YY$MM${DD}.gif >log.txt
convert -delay 100 qd-plot_$YY$MM${DD}16_back.jpg qd-plot_$YY$MM${DD}19_back.jpg qd-plot_$YY$MM${DD}22_back.jpg qd-plot_$yy1$mm1${dd1}01_back.jpg qd-plot_$yy1$mm1${dd1}04_back.jpg qd-plot_$yy1$mm1${dd1}07_back.jpg qd-plot_$yy1$mm1${dd1}10_back.jpg qd-plot_$yy1$mm1${dd1}13_back.jpg qd-plot_$yy1$mm1${dd1}.gif >log.txt
convert -delay 100 qd-plot_$yy1$mm1${dd1}16_back.jpg qd-plot_$yy1$mm1${dd1}19_back.jpg qd-plot_$yy1$mm1${dd1}22_back.jpg qd-plot_$yy2$mm2${dd2}01_back.jpg qd-plot_$yy2$mm2${dd2}04_back.jpg qd-plot_$yy2$mm2${dd2}07_back.jpg qd-plot_$yy2$mm2${dd2}10_back.jpg qd-plot_$yy2$mm2${dd2}13_back.jpg qd-plot_$yy2$mm2${dd2}.gif >log.txt
convert -delay 100 qd-plot_$yy2$mm2${dd2}16_back.jpg qd-plot_$yy2$mm2${dd2}19_back.jpg qd-plot_$yy2$mm2${dd2}22_back.jpg qd-plot_$yy3$mm3${dd3}01_back.jpg qd-plot_$yy3$mm3${dd3}04_back.jpg qd-plot_$yy3$mm3${dd3}07_back.jpg qd-plot_$yy3$mm3${dd3}10_back.jpg qd-plot_$yy3$mm3${dd3}13_back.jpg qd-plot_$yy3$mm3${dd3}.gif >log.txt
convert -delay 100 qd-plot_$yy3$mm3${dd3}16_back.jpg qd-plot_$yy3$mm3${dd3}19_back.jpg qd-plot_$yy3$mm3${dd3}22_back.jpg qd-plot_$yy4$mm4${dd4}01_back.jpg qd-plot_$yy4$mm4${dd4}04_back.jpg qd-plot_$yy4$mm4${dd4}07_back.jpg qd-plot_$yy4$mm4${dd4}10_back.jpg qd-plot_$yy4$mm4${dd4}13_back.jpg qd-plot_$yy4$mm4${dd4}.gif >log.txt
convert -delay 100 qd-plot_$yy4$mm4${dd4}16_back.jpg qd-plot_$yy4$mm4${dd4}19_back.jpg qd-plot_$yy4$mm4${dd4}22_back.jpg qd-plot_$yy5$mm5${dd5}01_back.jpg qd-plot_$yy5$mm5${dd5}04_back.jpg qd-plot_$yy5$mm5${dd5}07_back.jpg qd-plot_$yy5$mm5${dd5}10_back.jpg qd-plot_$yy5$mm5${dd5}13_back.jpg qd-plot_$yy5$mm5${dd5}.gif >log.txt
convert -delay 100 qd-plot_$yy5$mm5${dd5}16_back.jpg qd-plot_$yy5$mm5${dd5}19_back.jpg qd-plot_$yy5$mm5${dd5}22_back.jpg qd-plot_$yy6$mm6${dd6}01_back.jpg qd-plot_$yy6$mm6${dd6}04_back.jpg qd-plot_$yy6$mm6${dd6}07_back.jpg qd-plot_$yy6$mm6${dd6}10_back.jpg qd-plot_$yy6$mm6${dd6}13_back.jpg qd-plot_$yy6$mm6${dd6}.gif >log.txt
convert -delay 100 qd-plot_$yy6$mm6${dd6}16_back.jpg qd-plot_$yy6$mm6${dd6}19_back.jpg qd-plot_$yy6$mm6${dd6}22_back.jpg qd-plot_$yy7$mm7${dd7}01_back.jpg qd-plot_$yy7$mm7${dd7}04_back.jpg qd-plot_$yy7$mm7${dd7}07_back.jpg qd-plot_$yy7$mm7${dd7}10_back.jpg qd-plot_$yy7$mm7${dd7}13_back.jpg qd-plot_$yy7$mm7${dd7}.gif >log.txt

ls qd-plot*.gif >traj.txt
ls crop-plot_201904??12_back.jpg >>traj.txt
ls crop-plot_201904??12_back.jpg >>traj.txt
#/public/home/hysplit/software/anaconda3/bin/python create_ppt_btraj.pyc  traj3.pptx traj.txt $YY-$MM-$DD-traj.pptx $YY-$MM-$DD-traj_mh.pptx
/public/home/hysplit/software/anaconda3/bin/python create_ppt_btraj.py  traj3.pptx traj.txt $YY-$MM-$DD-traj-add.pptx $YY-$MM-$DD-traj_mh.pptx
echo "traj.pptx done"
#cp $YY-$MM-$DD-traj.pptx /public/product/WrfData/ppt/
cp $YY-$MM-$DD-traj_mh.pptx /public/product/WrfData/ppt/
cp $YY-$MM-$DD-traj-add.pptx /public/product/WrfData/ppt/
mv $YY-$MM-$DD-traj-add.pptx /public/home/hysplit/pptout/
mv $YY-$MM-$DD-traj_mh.pptx /public/home/hysplit/pptout/
:"
ffmpeg -f gif -i qd-plot_$YY$MM${DD}.gif qd-plot_$YY$MM${DD}.wmv
ffmpeg -f gif -i qd-plot_$yy1$mm1${dd1}.gif qd-plot_$yy1$mm1${dd1}.wmv
ffmpeg -f gif -i qd-plot_$yy2$mm2${dd2}.gif qd-plot_$yy2$mm2${dd2}.wmv
ffmpeg -f gif -i qd-plot_$yy3$mm3${dd3}.gif qd-plot_$yy3$mm3${dd3}.wmv
ffmpeg -f gif -i qd-plot_$yy4$mm4${dd4}.gif qd-plot_$yy4$mm4${dd4}.wmv
ffmpeg -f gif -i qd-plot_$yy5$mm5${dd5}.gif qd-plot_$yy5$mm5${dd5}.wmv
ffmpeg -f gif -i qd-plot_$yy6$mm6${dd6}.gif qd-plot_$yy6$mm6${dd6}.wmv
ffmpeg -f gif -i qd-plot_$yy7$mm7${dd7}.gif qd-plot_$yy7$mm7${dd7}.wmv
mkdir wmv
mv *.wmv wmv
"
