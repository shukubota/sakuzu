#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=2.5
##############################
#かきたいえのsize
#########################
lon3=90.
lon4=155.
lat3=-15.
lat4=10.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.
##############################
index=1



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend

lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)
print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)
#print len(lon),len(lat)
#print lon


for i in range(1,2):

	#plotc=np.zeros((nsize,msize))
	#plotp=np.zeros((nsize,msize))
	plotcp=np.zeros((npsize,mpsize))
	#plotpp=np.zeros((npsize,mpsize))


	#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu23/p"+"%d"%i+".dat",delimiter=",")

	if index==1:
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu33/plotdata/bimodal/phiolr_2.5.dat",delimiter=",")
	
	elif index==2:
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu23/plotdata_wh04/p"+"%d"%i+".dat",delimiter=",")

	else:
		print "wrong index"
		break
	print np.shape(plotdata)


	#################
	#CUT
	################
	plotcp=plotdata[mstart:mend+1,nstart:nend+1]
	plotcp+=1.
	print "plotcp:",np.shape(plotcp)


	m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
	#resolution l m h
	m.drawcoastlines(linewidth=1.5,color='black')
	m.drawparallels(np.arange(lat3,lat4,5.),labels=[True,False,False,True])    #緯線
	m.drawmeridians(np.arange(lon3,lon4,10.),labels=[False,True,False,True])  #経線


	X, Y = np.meshgrid(lonp,latp)
	x, y = m(X, Y)	

	###########################################################



	#m.contourf(x, y, plotcp,np.arange(0,1.6,0.1))
	m.contourf(x, y, plotcp,np.arange(1,10,1.))
	m.colorbar()
	#output="figure/c/c"+"%02d"%i+".png"

	if index==1:
	
		output="figure/mjophase_olr_bimodal2.5.png"
	
	else:
		output="figure/wh04/olr_p_wh04"+"%d"%i+".png"
	#plt.title("Phase of Diurnal Precipitation [Phase="+"%02d"%i+"] [UTC]")
	#plt.title("Amplitude of Diurnal Precipitation [Phase="+"%02d"%i+"] [mm/h]")
	plt.title("OLR_mjophase")
																		
	###########################################################


	plt.savefig(output,bbox_inches="tight")
	print output
	#plt.show()

	plt.clf()


#os.system("convert -delay 80 -loop 0 figure/bimodal/*.png olr_bimodal.gif")
#os.system("convert -delay 80 -loop 0 figure/wh04/*.png olr_wh04.gif")
