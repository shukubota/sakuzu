#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

##################
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1

##############################
#かきたいえのsize
#########################
#hov,pyとあわせる
lon3=96.
lon4=101.
lat3=-5.

#lon3=136.
#lon4=144.
#lat3=-10.
length=lon4-lon3

lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)




lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


mpsize,npsize=getsize(lonp,latp)



houraxis=np.arange(0,24)
#houraxis=np.hstack((houraxis,houraxis))
#tatejiku



#plotfin=np.zeros((len(houraxis),mpsize))
for phase in range(1,9):
	
	plotdata=np.zeros((npsize,mpsize))
	#plotdata2=np.zeros((2*npsize,mpsize))
	filename="plotdata/bimodal/hovphase"+"%d"%phase+".dat"
	plotdata=np.loadtxt(filename,delimiter=",")
	#plotdata2=np.vstack((plotdata,plotdata))
	print "plotdata",np.shape(plotdata)
	#print "plotdata2",np.shape(plotdata2)
	X,Y=np.meshgrid(lonp,houraxis)
	print "x,y",len(lonp),len(houraxis)
	plt.contourf(X,Y,plotdata,np.arange(0.,5.,0.5))
	plt.colorbar()
	
	ax=plt.gca()
	ax.invert_yaxis()
	plt.title("Propagation of pricipitation [phase=%d][mm/hr]"%phase)
	plt.savefig("figure/bimodal/hov_biimodal_p"+"%d"%phase+".png")
	plt.clf()	

  

os.system("convert -delay 80 -loop 0 figure/bimodal/*.png figure/hov_bimodal.gif")


	



