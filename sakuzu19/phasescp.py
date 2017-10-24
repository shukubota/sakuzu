#coding:utf-8
#python phasescp.py >& p1.log で実行


import numpy as np
import os
import time
import glob

if __name__ == '__main__':
    start = time.time()

data=np.loadtxt("p1.dat")
print np.shape(data)

max =len(data)
#print max
#print data[34][0]

for i in range(0,max):
    head=str(int(data[i][0]))
    print head
    comand1="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*HDF.gz /media/kubotashu/strage/data_mjo/p1/"

    comand2="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*HDF.Z /media/kubotashu/strage/data_mjo/p1/"

    os.system(comand1)
    os.system(comand2)



elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
