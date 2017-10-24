#coding:utf-8
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
#lon3=93.
#lon4=96.
#lat3=4.
#local=7
#wide=12.
#dire="smwest"
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



for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	hov=np.zeros((24,mpsize))
	for hour in range(0,24):
		lt=hour-local
		if lt<0:
			lt+=24
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/count"+"%02d"%lt+".dat")
		


		#################
		#CUT
		################
		#plotcp=plotdata[mstart:mend+1,nstart:nend+1]
		
		for j in range(0,mpsize):
			#sample=np.zeros(widenum)
			#mean=0.
			#for k in range(0,widenum):
				
			#	sample[k]=plotdata[mstart+j-k,nstart+j+k]
			#sd=np.std(sample,ddof=1)
			#mean=np.mean(sample)
			count=0
			for k in range(0,widenum):
			#	if abs(plotdata[mstart+j-k,nstart+j+k]-mean)<t*sd/np.sqrt(widenum):
				hov[hour,j]+=plotdata[mstart+j-k,nstart+j+k]*countdata[mstart+j-k,nstart+j+k]
				count+=countdata[mstart+j-k,nstart+j+k]
			hov[hour,j]=hov[hour,j]/count
			#if count==0:
			#	print sd,mean,j
			#	filename3="test/%d"%j+".dat"
			#	np.savetxt(filename3,sample,delimiter=",")
			#print np.shape(hov)
			#print np.shape(sigma)
		#print np.shape(plotcp)
		#print hour
	#hov=hov*harmonic(hov)
	hovp=np.vstack((hov,hov[0]))
	
	print np.shape(hovp)

	filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%i+".dat"
	#filename2="plotdata/wh04/"+dire+"/f"+"%d"%i+".dat"
	#filename2="plotdata/wh04/"+dire+"/sd"+"%d"%i+".dat"
	print filename
	#print np.shape(hovp)
	np.savetxt(filename,hovp,delimiter=",")
	#np.savetxt(filename2,harmonic(hov),delimiter=",")
	



	

	###########################################################


