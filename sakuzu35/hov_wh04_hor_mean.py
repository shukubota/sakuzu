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

#test rectangle
#lon3=96.
#lon4=101.
#lat3=-5.

#new guinia
#lon3=135.
#lon4=145.
#lat3=-10.

#
#smatrawest
#lon3=94.
#lon4=96.
#lat3=4.

#sm east
#lon3=99.
#lon4=101.
#lat3=0.


#br east
lon3=116.
lon4=120.
lat3=-1.
lat4=7.
dire="breast"
#wide=7.5 #grid の倍数に

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



for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	hov=np.zeros((24,mpsize))
	for hour in range(0,24):
		lt=hour-local
		if lt<0:
			lt+=24
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")


		#################
		#CUT
		################
		#plotcp=plotdata[mstart:mend+1,nstart:nend+1]
		
		for j in range(0,mpsize):
			
			for k in range(0,npsize):
				hov[hour,j]+=plotdata[mstart+k,nstart+j]
			hov[hour,j]=hov[hour,j]/npsize
		#print np.shape(plotcp)
		#print hour
	hovp=np.vstack((hov,hov[0]))
	print np.shape(hovp)

	filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%i+".dat"
	print filename
	#print np.shape(hovp)
	np.savetxt(filename,hovp,delimiter=",")
	



	

	###########################################################


