#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
local=8
##################
grid2=0.75

##############################
#かきたいえのsize
#########################




#br east
lon3=116.
lon4=120.
lat3=-1.
lat4=7.
dire="breast"
#t=1.292  #alpha=0.1 sample81



#wide=7.5 #grid の倍数に



#mean
#lon3=90.
#lon4=130.
#lat3=-3.
#lat4=5.
#local=7
#dire="mean"
#t=1.292  #alpha=0.1 sample81

#mean2
#lon3=70.
#lon4=160.
#lat3=-3.
#lat4=5.
#local=7
#dire="mean2"
#t=1.292  #alpha=0.1 sample81

#mean3
#lon3=90.
##lon4=130.
#lat3=-15.
#lat4=-8.
#local=7
#dire="mean3"
#t=1.292  #alpha=0.1 sample81

#ng east
#lon3=144.
#lon4=148.
#lat3=-6.



#length=lon4-lon3

#lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
#widenum=int(wide/grid)+1



lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)

print "npsize",npsize

for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	hov=np.zeros((24,mpsize))
	countplot=np.zeros((24,mpsize))
	for hour in range(0,24):
		lt=hour-local
		if lt<0:
			lt+=24
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/count"+"%02d"%lt+".dat")


		#################
		#CUT
		################
		#plotcp=plotdata[mstart:mend+1,nstart:nend+1]
		
		for j in range(0,mpsize):
			#sample=np.zeros(npsize)
			#mean=0.
			#for k in range(0,npsize):
			#	sample[k]=plotdata[mstart+k,nstart+j]
			#sd=np.std(sample,ddof=1)
			#mean=np.mean(sample)
			count=0
			for k in range(0,npsize):
				#if abs(plotdata[mstart+k,nstart+j]-mean)<t*sd/np.sqrt(npsize):
					
				hov[hour,j]+=plotdata[mstart+k,nstart+j]*countdata[mstart+k,nstart+j]
				count+=countdata[mstart+k,nstart+j]
			hov[hour,j]=hov[hour,j]/count
			countplot[hour,j]=count
			if count==0:
				print sample
				print sd,mean
		#print np.shape(plotcp)
		#print hour
	hovp=np.vstack((hov,hov[0]))
	
	print np.shape(hovp)

	filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%i+".dat"
	print filename
	#print np.shape(hovp)
	np.savetxt(filename,hovp,delimiter=",")
	np.save("plotdata/wh04/"+dire+"/countplot%02d.npy"%i,np.vstack((countplot,countplot[0])))
	



	

	###########################################################


