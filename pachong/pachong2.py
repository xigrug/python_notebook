# -*- coding: utf-8 -*-

"""
wget radar png from 中国天气网
@author: kaobozai
"""

import os
import sys
import time
import pandas as pd
import numpy as np


#os.system("rm -rf ")
# 输入前一天选定站点雷达图的url(主要包括中国各区域、北京、天津等)
def get_img(year_in, month_in, day_in, station_info, path_to_save):
    hr = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
          "18", "19", "20", "21", "22", "23"]
    mi = ["00", "06", "12", "18", "24", "30", "36", "42", "48", "54"]
    if station_info[1] == "z":
        image_path = "00000"
    if station_info[1] != "z":
        image_path = "00001"
    for hr_cell in hr:
        hr_str = hr_cell
        for mi_cell in mi:
            mi_str = mi_cell
            url_path = "http://pi.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_" + station_info + "_l88_pi_" + year_in + month_in + day_in + hr_str + mi_str + image_path + ".png"
            save_path = path_to_save + station_info + "/"
            os.system("wget -P " + save_path + " " + url_path)
            flag = year_in + month_in + day_in + hr_str + mi_str
            flag2 = "http://pi.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_" + station_info + "_l88_pi_" + year_in + month_in + day_in + hr_str + mi_str + image_path + ".png"
            print(flag)
            print(flag2)
    return 1

# 调用当天日期并计算前一天，输出数据下载成功与否的结果并压缩文件
a = sys.argv[1]
yesterday = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time() - 86400)).split("-")
yesterday1 = yesterday[0] + yesterday[1] + yesterday[2]  # type: str
path_to_save = "./radar_img/"+yesterday1+"/"
record = []
# 选择下载的雷达站点
radar = pd.read_csv('radar_site.txt')
datax = np.array(radar['site'])  # 读取站点数据转化为nparray
datay = np.array(radar['站名'])
sitelistx = datax.tolist()  # nparray转化为list
sitelisty = datay.tolist()
for i in range(0, 33):
    if a == sitelisty[i]:
        print(sitelistx[i])
        station_info = sitelistx[i]  # 站点选择完毕
        flag = get_img(yesterday[0], yesterday[1], yesterday[2], station_info, path_to_save)
        if flag == 1:
            record += [station_info + " !!!success!!!"]
        else:
            record += [station_info + "!!!fail!!!"]
if os.system("zip -r radar_img_" + yesterday1 +a+ ".zip " + path_to_save+station_info)==0:
    record += ["zip file !!!success!!!"]
else:
    record += ["zip file !!!fail!!!"]
for cell in record:
    print(cell)
    print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))



