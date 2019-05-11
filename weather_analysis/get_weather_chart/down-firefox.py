#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from requests.exceptions import RequestException
from datetime import timedelta, datetime
import time
import os

def get_url(browser,url):
    # 开启一个浏览器
    browser.get(url)
    wait = WebDriverWait(browser, 30)
    #time.sleep(60)
    browser.save_screenshot("1.png")
    # 等待直到元素加载出
    wait.until(EC.presence_of_element_located((By.ID, 'map_0_image')))
    time.sleep(10)
    # 在打开的网页响应中根据id查找元素
    figure = browser.find_element_by_id('map_0_image')
    fig_url = figure.get_attribute('src')
    return fig_url

def download(url,fname,pre_path):
    try:
        response = requests.get(url=url)
        # 获取二进制数据
        with open(pre_path + '/' + fname, 'wb') as f:
            f.write(response.content)
            f.close()
    except RequestException as e:
        print(e)
        pass
    
def get_date(n):
    """
    返回n天后（n>0）,前(n<0)的时间
    """
    sdate = datetime.today() + timedelta(n)      
    sdate_format = sdate.strftime('%Y%m%d')
    return sdate_format

def main():
    browser = webdriver.Firefox(executable_path="./geckodriver")
    time.sleep(1)  
    print (browser.get_window_size()) 
    browser.maximize_window() 
    time.sleep(1)  
    print (browser.get_window_size()) 
    browser.set_window_size(1600,900)
    time.sleep(1)  
    print (browser.get_window_size()) 
    ctime = get_date(0)
    stime = get_date(-1)
    print ctime,stime
    pre_path = '/data/forecast/statis/data/weather2/eu/' + ctime
    if not os.path.exists(pre_path):
        os.makedirs(pre_path)
    ftype = ['medium-z500-t850-public','medium-z500-t850-public',\
             'medium-mslp-wind850','medium-mslp-wind850']
    itime = ['00','12','00','12']
    ntype = ['ECMWF500geo_850tem_','ECMWF500geo_850tem_',\
             'ECMWF850wind_mslp_','ECMWF850wind_mslp_']
    for item in range(0,4):
        print item
        for it in range(0,9):
            #browser = webdriver.PhantomJS()
            nhour = it * 24
            etime = get_date(it-1)
            url = 'https://www.ecmwf.int/en/forecasts/charts/catalogue/' + \
                   ftype[item] + '?time=' + stime + itime[item] +',' + str(nhour) + \
                   ',' + etime + itime[item] + '&projection=classical_eastern_asia'
            fname = ntype[item] + ctime + '_' + str(nhour) + '_' + itime[item] + '.png'
            if not os.path.exists(pre_path + '/' + fname):
                print url,fname
                furl = ""
                furl = get_url(browser,url)
                print furl
                download(furl,fname,pre_path)
    browser.close()
            
if __name__=='__main__':
    main()            

