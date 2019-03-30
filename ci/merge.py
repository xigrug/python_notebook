import pandas as pd
import os
import glob
inputfile_dir= glob.iglob(r'ci*.csv')
inputfile_dir=sorted(inputfile_dir)
for inputfile in inputfile_dir:
    print(inputfile)
    a=pd.read_csv(inputfile, sep=',',skiprows=0,header=0)
    a.to_csv("all.csv", mode='a', index=False, header=False)

