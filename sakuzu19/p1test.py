#coding:utf-8
import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob

if __name__ == '__main__':
    start = time.time()
    

data=np.loadtxt("p1.dat")
print np.shape(data)


max =len(data)

for i in range(0,max):
    #print i
    head=str(int(data[i][0]))
    print head

    
    filename="2A25."+head+".*"
    #print filename
    comand="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/disc1/work/kubota/data/TRMM_PR/2A25/data97_15/"+filename+" data"
   # print comand
    os.system(comand)

    filelist=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/*")
    print filelist
    
    if os.path.isfile(filename):
        print filename
        hdf=SD(filename,SDC.READ)
        data3D=hdf.select('e_SurfRain')
        data=data3D[:,:]
        lat=hdf.select('Latitude')
        latitude=lat[:,:]
        lon = hdf.select('Longitude')
        longitude = lon[:,:]
        hour=hdf.select('Hour')




elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
