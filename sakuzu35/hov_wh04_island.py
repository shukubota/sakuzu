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
#lon3=95.
#lon4=96.6
#lat3=6.
#local=7
#wide=15.5
#dire="smwest"
#t=1.288

#sm east
lon3=93.
lon4=95.
lat3=4.
local=7
wide=15.5
dire="smeast"
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

y=[]
yerr=[]
y2=[]
yerr2=[]
y3=[]
yerr3=[]
y4=[]
yerr4=[]

for i in range(1,9):

  	grid=np.zeros((mpsize,widenum))
  	grid2=np.zeros((mpsize,widenum))
  	grid3=np.zeros((mpsize,widenum))
  	grid4=np.zeros((mpsize,widenum))
	plotcp=np.zeros((npsize,mpsize))
	#hov=np.zeros((24,mpsize))
	#for hour in range(0,24):
	#	lt=hour-local
	#	if lt<0:
	#		lt+=24
	#	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%lt+".dat")
	

	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%i+".dat",delimiter=",")

	plotdata2=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata_0228/plotdata%02d.npy"%i)

	plotdata3=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra/dailyp"+"%02d"%i+".dat",delimiter=",")

	plotdata4=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra2/dailyp"+"%02d"%i+".dat",delimiter=",")

		#countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p"+"%d"%i+"/count"+"%02d"%lt+".dat")

	countdata=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/count24h"+"%02d"%i+".npy")


		#################
		#CUT
		################
		#plotcp=plotdata[mstart:mend+1,nstart:nend+1]
	x=[]
	for j in range(0,mpsize):
			
		count=0
		for k in range(0,widenum):
				#hov[hour,j]+=plotdata[mstart+j-k,nstart+j+k]*countdata[mstart+j-k,nstart+j+k]
			grid[j,k]=plotdata[mstart+j-k,nstart+j+k]
			grid2[j,k]=plotdata2[mstart+j-k,nstart+j+k]
			grid3[j,k]=plotdata3[mstart+j-k,nstart+j+k]
			grid4[j,k]=plotdata4[mstart+j-k,nstart+j+k]
				#count+=countdata[mstart+j-k,nstart+j+k]
			#hov[hour,j]=hov[hour,j]/count
			
	#hovp=np.vstack((hov,hov[0]))


	size1,size2= np.shape(grid)
	print size1*size2
	yerr.append(np.std(grid,ddof=1)/np.sqrt(size1*size2)*1.96)
	mean=grid.mean(axis=(0,1))
	y.append(mean)

	yerr2.append(np.std(grid2,ddof=1)/np.sqrt(size1*size2)*1.96)
	mean=grid2.mean(axis=(0,1))
	y2.append(mean)

	yerr3.append(np.std(grid3,ddof=1)/np.sqrt(size1*size2)*1.96)
	mean=grid3.mean(axis=(0,1))
	y3.append(mean)

	yerr4.append(np.std(grid4,ddof=1)/np.sqrt(size1*size2)*1.96)
	mean=grid4.mean(axis=(0,1))
	y4.append(mean)




	#print np.shape(hov)
	print "mean",y


	#filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%i+".dat"
	#filename2="plotdata/wh04/"+dire+"/f"+"%d"%i+".dat"
	#filename2="plotdata/wh04/"+dire+"/sd"+"%d"%i+".dat"
	#print filename
	#print np.shape(hovp)

	#np.savetxt(filename,hovp,delimiter=",")
	#np.savetxt(filename2,harmonic(hov),delimiter=",")

x=[1,2,3,4,5,6,7,8]

fig,ax1=plt.subplots()
ax2=ax1.twinx()

#print yerr
#plt.plot(x,y)
plt.xlim(0.,9,1)
ax1.errorbar(x,y,yerr=yerr,capsize=10)
ax2.errorbar(x,y2,yerr=yerr2,capsize=10,color="y")
ax1.errorbar(x,y3,yerr=yerr3,capsize=10)
ax1.errorbar(x,y4,yerr=yerr4,capsize=10)
#plt.show()	
plt.savefig("figure/"+dire+".png")



	

	###########################################################


