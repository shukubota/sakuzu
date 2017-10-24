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




for i in range(0,24):
	plotdata1=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata07-13/%02d.dat"%i)
	plotdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata99-06/%02d.dat"%i)
	plotdata3=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata98/%02d.dat"%i)

	countdata1=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata07-13/count%02d.dat"%i)
	countdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata99-06/count%02d.dat"%i)
	countdata3=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata98/count%02d.dat"%i)

	plotdata=plotdata1+plotdata2+plotdata3
	countdata=countdata1+countdata2+countdata3

	np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/%02d.dat"%i,plotdata)
	np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count%02d.dat"%i,countdata)





