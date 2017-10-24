#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm
from mpl_toolkits.basemap import maskoceans

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
#lon3=93.
#lon4=155.
#lat3=-12.
#lat4=8.
#t=


#peatman
lon3=100.
lon4=120.
lat3=-7.
lat4=10.
#t=

#tian
#lon3=100.
#lon4=150.
#lat3=-15.
#lat4=10.
#t=

#sui
#lon3=119.
#lon4=121.
#lat3=-11.
#lat4=-9.
#t=

#kamimera
#lon3=99.
#lon4=102.
#lat3=-2.
#lat4=3
#t=

#iroiro
#lon3=120.
#lon4=150.
#lat3=-7.
#lat4=10.



##############################
#c or phi(c:1 phiZ:2)
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

mean1=np.zeros(8)
mean2=np.zeros(8)
mean3=np.zeros(8)
mean1err=np.zeros(8)
mean2err=np.zeros(8)
mean3err=np.zeros(8)
for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	plotu=np.zeros((npsize2,mpsize2))
	plotv=np.zeros((npsize2,mpsize2))

	if which==1:
		#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/p1test/00.dat")
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c"+"%02d"%i+".dat",delimiter=",")
		plotdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%i+".dat",delimiter=",")
		plotdata3=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata_0228/plotdata%02d.npy"%i)

		plotdata4=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra/daily"+"%02d.npy"%i)


	
	#################
	#CUT
	################
	plotcp=plotdata[mstart:mend+1,nstart:nend+1]
	plotcp2=plotdata2[mstart:mend+1,nstart:nend+1]
	plotcp3=plotdata3[mstart:mend+1,nstart:nend+1]
	plotcp4=plotdata4[mstart:mend+1,nstart:nend+1]


	mean1[i-1]=plotcp.mean()
	mean1err[i-1]=1.96*np.std(plotcp,ddof=1)/np.sqrt(np.size(plotcp))
	mean2[i-1]=plotcp2.mean()
	mean2err[i-1]=1.96*np.std(plotcp2,ddof=1)/np.sqrt(np.size(plotcp2))
	mean3[i-1]=plotcp3.mean()
	mean3err[i-1]=1.96*np.std(plotcp3,ddof=1)/np.sqrt(np.size(plotcp3))
	mean4[i-1]=plotcp4.mean()
	mean4err[i-1]=1.96*np.std(plotcp3,ddof=1)/np.sqrt(np.size(plotcp3))


meanall1=mean1.mean()
meanall2=mean2.mean()
meanall2=mean2.mean()


print np.size(plotcp),np.size(plotcp2)


fig,ax1=plt.subplots()
ax2=ax1.twinx()

x=[1,2,3,4,5,6,7,8]
ax1.plot(x,mean2,label="Mean Precipitation" )
ax1.errorbar(x,mean2,yerr=mean2err,capsize=10)
ax1.plot(x,mean1,label="Diurnal Precipitation")
ax1.errorbar(x,mean1,yerr=mean1err,capsize=10)
ax2.plot(x,mean3,"r",label="T")
ax2.errorbar(x,mean3,yerr=mean3err,capsize=10)

#plt.legend(loc="best right")
meanall=np.zeros(8)
meanall[:]=meanall1
#plt.plot(x,meanall,"black")
meanall[:]=meanall2
#plt.plot(x,meanall,"black")

#ax1.xlabel("MJO phase")
#ax1.ylabel("Precipitation rate[mm/h]")
#ax2.ylabel("Brightness temperature[K]")
fig.text(0.45,0.91,"MJO phase",fontsize=15,color="black")
fig.text(0.95,0.65,"Brightness temperature[K]",fontsize=15,color="black",rotation=90)
fig.text(0.04,0.6,"Precipitation rate[mm/h]",fontsize=15,color="black",rotation=90)
plt.savefig("figure_wh04/meanall_iroiro.png")







