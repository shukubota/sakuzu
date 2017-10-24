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
#lon3=96.
#lon4=101.
#lat3=-5.

#new guinia
#lon3=135.
#lon4=145.
#lat3=-10.



#br west
lon3=116.
lon4=118.
lat3=6.
wide=8. #grid の倍数に
dire="brwest"
local=8
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

cpsize1,cpsize2=np.shape(np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04/p1/01.dat"))
plotcp=np.zeros((24,cpsize1,cpsize2))
hov=np.zeros((24,mpsize))


for hour in range(0,24):
	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04/p1/01.dat")
	
	plotdata=plotdata*0.
	countdatasum=plotdata
	lt=hour-local
	if lt<0:
		lt+=24
	for i in range(1,9):
		plotcell=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_cut/p"+"%d"%i+"/count"+"%02d"%lt+".dat")
		
		plotcp[lt,:,:]+=plotcell*countdata
		countdatasum+=countdata
	plotcp[lt,:,:]=plotcp[lt,:,:]/countdatasum


for lt in range(0,24):
	for j in range(0,mpsize):
		count=0
		for k in range(0,widenum):
			hov[lt,j]+=plotcp[lt,mend-j-k,nstart+j-k]
			count+=1
		hov[lt,j]=hov[lt,j]/count
		#print np.shape(plotcp)
		#print hour
hovp=np.vstack((hov,hov[0]))
print np.shape(hovp)

filename="plotdata/wh04/"+dire+"/meanphase.dat"
print filename
	
np.savetxt(filename,hovp,delimiter=",")
	



	

	###########################################################


