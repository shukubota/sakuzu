#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm
from pylab import *
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1

##################
grid2=0.75

##############################
#かきたいえのsize
#########################
#smatra
#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

#maritime
lon3=93.
lon4=155.
lat3=-12.
lat4=8.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.


#test
#lon3=90.
#lon4=160.
#lat3=1.5
#lat4=1.501
##############################
#ampl,olr or mean 1,2,3
#####################
which=1
local=7
windlevel=20
#[100,125,150,175,200,225,250,300,350,400,450,500,550,600,650,700,750,775,800,825,850,875,900,925,950,975,1000]
#20:850hpa
##################


nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)

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


#print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend
#print "mstart2:",mstart2,"mend2:",mend2,"nstart2:",nstart2,"nend2:",nend2
lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

lonp2=np.arange(lon3min,lon4min+grid2,grid2)
latp2=np.arange(lat3min,lat4min+grid2,grid2)
#print "lonp2",np.shape(lonp2)
#print "latp2",np.shape(latp2)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)

mpsize2,npsize2=getsize(lonp2,latp2)

print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)
#print len(lon),len(lat)
#print lon



  
if which==1:

	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu33/plotdata/wh04/phiampl.dat",delimiter=",")
   
elif which==2:
	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu33/plotdata/wh04/phiolr.dat",delimiter=",")


elif which==3:
    plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu33/plotdata/wh04/phimean.dat",delimiter=",")


#################
#CUT
################
plotcp=plotdata[mstart:mend+1,nstart:nend+1]
#plotcp+=1.



m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
m.drawcoastlines(linewidth=1.5,color='black')
m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon3-3,lon4,10.),labels=[False,True,False,True])	#経線


X, Y = np.meshgrid(lonp,latp)
x, y = m(X, Y)	

###########################################################

plotcp[plotcp>8.5]-=8.

a=m.contourf(x, y, plotcp,np.arange(0.5,9,1.),cmap=cm.spectral_r)
#a=m.contourf(x, y, plotcp,[0.5,1,2,3,4,5,6,7,8,8.5],cmap=cm.hsv)
#m.colorbar()
b=plt.colorbar(a,orientation="horizontal",shrink=0.5,pad=0.07)
#b.set_label("mm/h")	 

if which==1:
	output="figure/mjophase_ampl_wh04.png"
	#plt.title("MJO phase as maximum diurnal precipitation")
	#b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
	#b.set_label("mm/h")
elif which==2:
    output="figure/mjophase_olr_wh04.png"
    plt.title("phase_olr")

elif which==3:
    output="figure/mjophase_mean_wh04.png"
    #plt.title("MJO phase as maximum mean precipitation")


  

plt.savefig(output,bbox_inches='tight')	


plt.clf()

#os.system("convert -delay 80 -loop 0 figure/c/c*.png figure/c.gif")
#os.system("convert -delay 80 -loop 0 figure/phi/phi*.png figure/phi.gif")
