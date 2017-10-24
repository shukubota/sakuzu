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
local=7
##################
grid2=0.75

##############################
#かきたいえのsize
#########################

#test rectangle
lon3=96.
lon4=101.
lat3=-5.

#lon3=136.
#lon4=144.
#lat3=-10.

wide=1. #grid の倍数に

length=lon4-lon3

lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
widenum=int(wide/grid)+1



lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)



for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	hov=np.zeros((24,mpsize))
	for hour in range(0,24):
		lt=hour-local
		if lt<0:
			lt+=24
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_1209/p"+"%d"%i+"/"+"%02d"%lt+".dat")


		#################
		#CUT
		################
		#plotcp=plotdata[mstart:mend+1,nstart:nend+1]
		
		for j in range(0,mpsize):
			
			for k in range(0,widenum):
				hov[hour,j]+=plotdata[mstart+j-k,nstart+j+k]
			hov[hour,j]=hov[hour,j]/widenum
		#print np.shape(plotcp)
		#print hour
	filename="plotdata/bimodal/hovphase"+"%d"%i+".dat"
	print filename
	print np.shape(hov)
	np.savetxt(filename,hov,delimiter=",")
	



	

	###########################################################


