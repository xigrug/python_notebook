#!/bin/bash
echo "weather download starting!!!!!!!!!!"
which python

#python
export PATH=/data/software/python/bin:${PATH}
#phantomjs
export PATH=/data/forecast/statis/data/weather2/src_code/phantomjs-2.1.1-linux-x86_64/bin/:$PATH

which python

cd /data/forecast/statis/data/weather2
python down.py >> down.log

Cur_date=`date +%Y%m%d`
echo $Cur_date

cd eu/$Cur_date
cp *.png  /data/forecast/statis/data/weather2/temp
echo "weather download end !!!!!!!!!!!!!!"
