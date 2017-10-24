#coding:utf-8
#phase の中心
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

def harmonic(data):
	pi=4.*np.arctan(1.)
	
	sum1=np.zeros((1,len(data[0])))
	sum2=np.zeros((1,len(data[0])))
	suma=np.zeros((1,len(data[0])))
	sumb=np.zeros((1,len(data[0])))
	s2=np.zeros((1,len(data[0])))
	for i in range(0,24):
		sum1+=data[i,:]*data[i,:]
		sum2+=data[i,:]
		
		suma+=data[i,:]*np.cos(2.*pi*i/24.)
		sumb+=data[i,:]*np.sin(2.*pi*i/24.)
		#plt.plot(np.arange(0,31,1),data[i,:])
		#plt.savefig("figure/%d"%i+".png")
	suma=suma/12.
	
	sumb=sumb/12.
	sum2=sum2/24.
	print suma,sumb,sum1,sum2
	#print pi
	s2=(sum1-24.*sum2*sum2-0.5*24.*(suma*suma+sumb*sumb))/(24.-2.-1.)
	f=24.*(suma*suma+sumb*sumb)/(4.*s2)
	f[f<3.47]=0.
	f[f>=3.47]=1.
	
	#ff=np.zeros((len(data),len(data[0])))
	#for i in range(0,24):
	#	ff[i,:]=f[:]
		
	return f




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

#test rectangle
#lon3=96.
#lon4=101.
#lat3=-5.
#local=7


#new guinia
#lon3=135.
#lon4=145.
#lat3=-10.

#local=7
#
#smatrawest
lon3=93.
lon4=96.
lat3=4.
local=7
wide=12.
dire="smwest"
#t=1.288

#sm east
#lon3=100.
#lon4=103.
#lat3=0.
#local=7
#wide=9
#dire="smeast"
#t=1.290


#ng east
#lon3=142.
#lon4=144.
#lat3=-3.
#wide=11
#local=9
#dire="ng"
#t=1.289 #sample111 alpha0.1


#ng west
#lon3=135.
#lon4=137.
#lat3=-5
#local=9


#wide=7.5 #grid の倍数に

length=lon4-lon3

lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
widenum=int(wide/grid)+1

print "widenum sample num" ,widenum 

lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)

cpsize1,cpsize2=np.shape(np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p1/01.dat"))
	
plotcp=np.zeros((24,cpsize1,cpsize2))
hov=np.zeros((24,mpsize))


for hour in range(0,24):
	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p1/01.dat")
	
	plotdata=plotdata*0.
	countdatasum=plotdata
	lt=hour-local
	if lt<0:
		lt+=24
	for i in range(1,9):
		plotcell=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/count"+"%02d"%lt+".dat")
  	
		plotcp[hour,:,:]+=plotcell*countdata
		countdatasum+=countdata

	plotcp[hour,:,:]=plotcp[hour,:,:]/countdatasum



for time in range(0,24):
	
		

	for j in range(0,mpsize):
		
		count=0
		for k in range(0,widenum):
			
			hov[time,j]+=plotcp[time,mstart+j-k,nstart+j+k]
			count+=1
		hov[time,j]=hov[time,j]/count
		
hovp=np.vstack((hov,hov[0]))
	
print np.shape(hovp)

filename="plotdata/wh04/"+dire+"/meanphase.dat"
	
print filename

np.savetxt(filename,hovp,delimiter=",")



