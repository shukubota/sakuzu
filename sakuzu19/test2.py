#coding:utf-8
import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob

if __name__ == '__main__':
    start = time.time()


#filename="/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/2A25.19990226.07177.7.HDF"
list=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/2A25.*")
#print list
print len(list)
for i in range(0,len(list)):
    filename=list[0]
 

    hdf=SD(filename,SDC.READ)
    data3D=hdf.select('e_SurfRain')
    data=data3D[:,:]
    lat=hdf.select('Latitude')
    latitude=lat[:,:]



    print latitude






elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
