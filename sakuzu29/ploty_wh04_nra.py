#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os.path
import matplotlib.cm as cm
from function import *
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
grid2=0.75
##############################
#かきたいえのsize
#########################
#lon3=108.

#lon4=120
#lat3=-5
#lat4=8

#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

lon3=70.
lon4=160.
lat3=-15.
lat4=30.
##############################
windlevel=20


nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend

#grid2にあわせたlon1をこえる最小のlon,lon1<lon1min,lon2min<=lon2
#PRとECWMFは格子の作り方が異なるので注意
#latは90 to -90の順になっているので注意
#地図で見て格子の上と左端は含まれていない

lon1min=int(lon1/grid2)*grid2+grid2
lon2min=int(lon2/grid2)*grid2
#lon1min<lon2min

lat2min=90.-(int((90.-lat2)/grid2)*grid2+grid2)
lat1min=90.-int((90.-lat1)/grid2)*grid2
print "lat1min:",lat1min

lon3min=int(lon3/grid2)*grid2+grid2
lon4min=int(lon4/grid2)*grid2
#lon1min<lon2min

lat4min=90.-(int((90.-lat4)/grid2)*grid2+grid2)
lat3min=90.-int((90.-lat3)/grid2)*grid2


nstart2=int((lon3min-lon1min)/grid2)
nend2=int((lon4min-lon1min)/grid2)
mstart2=int((lat2min-lat4min)/grid2)
mend2=int((lat2min-lat3min)/grid2)




lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


lonp2=np.arange(lon3min,lon4min+grid2,grid2)
latp2=np.arange(lat3min,lat4min+grid2,grid2)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)
print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)



plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/00.dat")
plotdata=plotdata*0.
countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count00.dat")
countdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count01.dat")
print np.shape(countdata)
print np.shape(countdata2)
countdata=countdata*0.



for i in range(0,4):


	plotcp=np.zeros((npsize,mpsize))


	###################################################
	#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/anmdaily"+"%02d"%i+".dat",delimiter=",")
	plotdata+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/"+"%02d"%i+".dat")
	countdata+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count"+"%02d"%i+".dat")
	#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra2/dailyp"+"%02d"%i+".dat",delimiter=",")
	#######################################################

	
plotdata=plotdata/countdata






#################
#CUT
################
plotcp=plotdata[mstart:mend+1,nstart:nend+1]



m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
	#resolution l m h
m.drawcoastlines(linewidth=1.5,color='black')
m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon3-3,lon4,10.),labels=[False,True,False,True])	#経線


X, Y = np.meshgrid(lonp,latp)
x, y = m(X, Y)	

	###########################################################


	#a=m.contourf(x, y, plotcp,np.arange(-0.7,0.71,0.2),cmap=cm.RdBu_r,extend="both")
a=m.contourf(x, y, plotcp,np.arange(0.,1.01,0.1))
#	b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
#	b.set_label("mm/h")


	#m.contourf(x, y, plotcp)
	#m.contourf(x, y, plotcp,np.arange(0,25,1))
m.colorbar()
	#output="figure/wh04/daily"+"%02d"%i+".png"
output="fig1.png"
	###########################################################




plt.savefig(output,bbox_inches="tight")
print output

plt.clf()


