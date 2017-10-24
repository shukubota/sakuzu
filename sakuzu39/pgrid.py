#coding:utf-8

import os
import glob
import pygrib
import numpy as np
import time
import matplotlib.pyplot as plt


if __name__ == '__main__':
    start = time.time()


#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
##############################

m,n=3298,9896

lon1num=int((lon1-180./9896.)*9896/360.+1.)
lon2num=int((lon2-180./9896.)*9896/360.)
lat1num=int((lat1+60.-60./3298.)*3298./120.+1)
lat2num=int((lat2+60.-60./3298.)*3298./120.)





for phase in range(1,9):
	phasename="p"+str(phase)
	dhead=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/wh04date/wh04"+phasename+".dat")


	data=np.zeros((2,lat2num+1-lat1num,lon2num+1-lon1num))
	count=np.zeros((2,lat2num+1-lat1num,lon2num+1-lon1num))
	max=len(dhead)
	
	for i in range(0,max):
		if dhead[i]<20000000:#2000年からしかないようです
		#if dhead[i]<20040326:
			continue
		if dhead[i]>20140000:
			continue
		for hour in range(0,24):
			filename="merg_"+str(int(dhead[i]))+"%02d"%hour+"_4km-pixel"
			command="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/box03/TRMM/ANCILLARY/MERG/*/*/"+filename+".bz2 data/"
			os.system(command)
			os.system("bunzip2 data/*")
 			flist=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/data/*")
			if len(flist)<1:
				continue
			
			file=open("data/"+filename,"rb")
			datacell=np.fromfile(file,dtype=np.uint8)
			datacell=np.resize(datacell,((2,m,n)))
			datacell=datacell[:,lat1num:lat2num+1,lon1num:lon2num+1]
			data[datacell<255]+=datacell[datacell<255]
			count[datacell<255]+=1
			print filename
			os.system("rm data/*")
		
	
	np.save("plotdata/count%02d.npy"%phase,count)
	count[count==0]=1
	data=data/count

	np.save("plotdata/irp%02d"%phase,data)

	


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
