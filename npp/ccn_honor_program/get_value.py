# coding: utf-8
import pygrib
import pandas as pd
import numpy as np
import os, time, datetime
from datetime import datetime
import glob

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]
    
def potential_temperature(T,p):
    """Compute potential temperature for an air parcel.
         Input:  T is temperature in Kelvin
            p is pressure in mb or hPa
    Output: potential temperature in Kelvin.
    """
    ps=1000
    cp = 1004.     # specific heat at constant pressure for dry air (J / kg / K)
    Rd = 287.         # gas constant for dry air (J / kg / K)
    kappa = Rd/cp
    theta = T*(ps/p)**kappa
    return theta
    
    # Read data
for f in glob.glob("AUTO_5MINS_NPP_MicroPhys_201*filter.csv"):
    print(f)
    df = pd.read_csv(f, sep=',',skiprows=0,header=0,na_values=[-99,-9999])
    time=f[25:33]
    year=time[0:4]
    month=time[4:6]
    day=time[6:8]
    grib='/data/c02n03/archive/ds083.3/'+year+'/gdas1.fnl0p25.'+year+month+day+'06.f00.grib2'
    gr = pygrib.open(grib)
    pblh=gr.select(name='Planetary boundary layer height')[0]
    pblhv=pblh.values
    print(pblhv.shape)
    print(np.amax(pblhv),np.amin(pblhv))
    
    #get record number
    ptems = gr[299] #Potential temperature
    ptemsv=ptems.values
    T1000= gr[208]
    T1000v=T1000.values
    Tsurf = gr[219]
    Tsurfv=Tsurf.values
    T500= gr[112]
    T500v=T500.values
    T850= gr[168]
    T850v=T850.values
    T700= gr[144]
    T700v=T700.values
    Gh1000= gr[216]
    Gh1000v=Gh1000.values
    Gh500= gr[111]
    Gh500v=Gh500.values
    Gh850= gr[167]
    Gh850v=Gh850.values
    Gh700= gr[143]
    Gh700v=Gh700.values
    ST0 = gr[220]
    ST0v=ST0.values
    Sli = gr.select(name='Surface lifted index')[0]
    Sliv=Sli.values
    B4li = gr.select(name='Best (4-layer) lifted index')[0]
    B4liv=B4li.values
    LSM = gr.select(name='Land-sea mask')[0]
    LSMv=LSM.values
    Tozone = gr.select(name='Total ozone')[0]
    Tozonev=Tozone.values
    Srh = gr.select(name='Storm relative helicity')[0]
    Srhv=Srh.values
    Cape = gr.select(name='Convective available potential energy')[0]
    Capev=Cape.values
    Pr = gr.select(name='Cloud water')[0]
    Prv= Pr.values
    Pw = gr.select(name='Precipitable water')[0]
    Pwv=Pw.values
    CIN0 = gr[243]
    CIN0v =CIN0.values
    CIN180 = gr[292]
    CIN180v=CIN180.values
    CIN255 = gr[305]
    CIN255v=CIN255.values
    Sh2 =gr [231]#Specific humidity 2m
    Sh2v=Sh2.values
    TD2 = gr.select(name='2 metre dewpoint temperature')[0]
    TD2v=TD2.values
    RH2 = gr.select(name='2 metre relative humidity')[0]
    RH2v= RH2.values
    
    ptem700v= potential_temperature(T700v, 700)
    #print(np.amax(ptem700v),np.amin(ptem700v))
    
    lts= ptem700v-ptemsv
    lat,lon=df["lat"],df["lon"]
    lon_list,lat_list = ptems.latlons()[1][0],ptems.latlons()[0].T[0]
    
    datasets = []
    datasets1 = []
    datasets2 = []
    datasets3 = []
    datasets4 = []
    datasets5 = []
    datasets6 = []
    datasets7 = []
    datasets8 = []
    datasets9 = []
    datasets10 = []
    datasets11 = []
    datasets12 = []
    datasets13 = []
    datasets14 = []
    datasets15 = []
    datasets16 = []
    datasets17 = []
    datasets18 = []
    datasets19 = []
    datasets20 = []
    datasets21 = []
    datasets22 = []
    datasets23 = []
    datasets24 = []
    datasets25 = []
    datasets26 = []
    datasets27 = []
    datasets28 = []
    for x,y in zip(lon,lat):
            #print(x)
            #print(y)
        x_indice = np.where(lon_list == find_nearest(lon_list,x))[0]
        y_indice = np.where(lat_list== find_nearest(lat_list,y))[0]
        #print(x_indice)
        #print(y_indice)
        #print(pbl.shape)
        #print(lts.shape)
        PBLH=np.around(pblhv[y_indice,x_indice][0], decimals=2)
        LTS=np.around(lts[y_indice,x_indice][0], decimals=2)
        #TEMS=np.around(temsv[y_indice,x_indice][0], decimals=2)
        PTEMS=np.around(ptemsv[y_indice,x_indice][0], decimals=2)-273.15
        PTEM700=np.around(ptem700v[y_indice,x_indice][0], decimals=2)-273.15
        TD2=np.around(TD2v[y_indice,x_indice][0], decimals=2)-273.15
        RH2=np.around(RH2v[y_indice,x_indice][0], decimals=2)
        SH2=np.around(Sh2v[y_indice,x_indice][0], decimals=2)
        PW=np.around(Pwv[y_indice,x_indice][0], decimals=2)
        PR=np.around(Prv[y_indice,x_indice][0], decimals=2)
        CAPE=np.around(Capev[y_indice,x_indice][0], decimals=2)
        SRH=np.around(Srhv[y_indice,x_indice][0], decimals=2)
        TOZONE=np.around(Tozonev[y_indice,x_indice][0], decimals=2)
        LSM=np.around(LSMv[y_indice,x_indice][0], decimals=2)
        B4LI=np.around(B4liv[y_indice,x_indice][0], decimals=2)
        SLI=np.around(Sliv[y_indice,x_indice][0], decimals=2)
        ST0=np.around(ST0v[y_indice,x_indice][0], decimals=2)
        GH1000=np.around(Gh1000v[y_indice,x_indice][0], decimals=2)
        GH850=np.around(Gh850v[y_indice,x_indice][0], decimals=2)
        GH700=np.around(Gh700v[y_indice,x_indice][0], decimals=2)
        GH500=np.around(Gh500v[y_indice,x_indice][0], decimals=2)
        TSURF=np.around(Tsurfv[y_indice,x_indice][0], decimals=2)-273.15
        T1000=np.around(T1000v[y_indice,x_indice][0], decimals=2)-273.15
        T850=np.around(T850v[y_indice,x_indice][0], decimals=2)-273.15
        T700=np.around(T700v[y_indice,x_indice][0], decimals=2)-273.15
        T500=np.around(T500v[y_indice,x_indice][0], decimals=2)-273.15
        CIN0=np.around(CIN0v[y_indice,x_indice][0], decimals=2)
        CIN180=np.around(CIN180v[y_indice,x_indice][0], decimals=2)
        CIN255=np.around(CIN255v[y_indice,x_indice][0], decimals=2)
        datasets.append(PBLH)
        datasets1.append(LTS)
        #datasets2.append(TEMS)
        datasets3.append(PTEMS)
        datasets4.append(PTEM700)
        datasets5.append(TD2)
        datasets6.append(RH2)
        datasets7.append(SH2)
        datasets8.append(PW)
        datasets9.append(PR)
        datasets10.append(CAPE)
        datasets11.append(SRH)
        datasets12.append(TOZONE)
        datasets13.append(LSM)
        datasets14.append(B4LI)
        datasets15.append(SLI)
        datasets16.append(ST0)
        datasets17.append(GH1000)
        datasets18.append(GH850)
        datasets19.append(GH700)
        datasets20.append(GH500)
        datasets21.append(TSURF)
        datasets22.append(T1000)
        datasets23.append(T850)
        datasets24.append(T700)
        datasets25.append(T500)
        datasets26.append(CIN0)
        datasets27.append(CIN180)
        datasets28.append(CIN255)
    print(len(datasets))
    df["PBLH"],df['LTS'],df['PTEMS'],df['PTEM700'],df["TD2"],df["RH2"],df['SH2'],df['PW'],df['PR'],df["CAPE"],df['SRH'],df['TOZONE'],df['LSM'],df['B4LI'],df["SLI"],df["ST0"],df['GH1000'],df['GH850'],df['GH700'],df["GH500"],df['TSURF'],df['T1000'],df['T850'],df['T700'],df["T500"],df["CIN0"],df['CIN180'],df['CIN255'] = datasets,datasets1,datasets3,datasets4,datasets5,datasets6,datasets7,datasets8,datasets9,  datasets10,datasets11,datasets12,datasets13,datasets14,datasets15,datasets16,datasets17,datasets18,datasets19,  datasets20,datasets21,datasets22,datasets23,datasets24,datasets25,datasets26,datasets27,datasets28
    df=df[df['PBLH']>df['H_LCL_nc']]
    df.to_csv(f[:-10]+"necp.csv",index=False,sep=',')
    df.head(10)
