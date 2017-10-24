#coding:utf-8
import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob
import gc

if __name__ == '__main__':
    start = time.time()
    

dhead=np.loadtxt("p1.dat")
#print np.shape(dhead)
#print dhead

max =len(dhead)

for i in range(0,max):
    #print i
    head=str(int(dhead[i][0]))
    print head

    if dhead[i][0]>20140000:
        comand="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*.HDF.Z data/"
    else:
        comand="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*.HDF.gz data/"

    os.system(comand)
    os.system("gunzip data/*")
    list=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/*")
    #print list
    
   
    
    for j in range(0,len(list)):
        filename=list[j]
        hdf=SD(filename,SDC.READ)
        ####################################
        #e_surfrain
        #################################
        data3D=hdf.select('e_SurfRain')
        data=data3D[:]
        #########################################
        #rain levelも含んでいる
        #############################

        #data3D=hdf.select('rain')
        #data=data3D[:]
        del data3D
        gc.collect()
        #print np.shape(data)
        ##############################

        lat=hdf.select('Latitude')
        latitude=lat[:]
        del lat
        gc.collect()
        lon = hdf.select('Longitude')
        longitude = lon[:]
        del lon
        gc.collect() 
        Hour=hdf.select('Hour')
        hour=Hour[:]
        del Hour
        gc.collect()

        #print latitude

    os.system("rm data/*")

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
