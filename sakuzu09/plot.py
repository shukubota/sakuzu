#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *


#grads format
#grads format
lon1=70.05
lon2=100.05
lat1=5.05
lat2=25.05


lon,lat=getlonlat(lon1,lon2,lat1,lat2)

msize,nsize=getsize(lon,lat)
print "msize:",msize,"nsize:",nsize

plotc=np.zeros((nsize,msize))
plotp=np.zeros((nsize,msize))
fc=open("c.dat","r")
fp=open("phi.dat","r")
#plot=np.fromfile(f,dtype="<f4")
for i in range(0,nsize):
    for j in range(0,msize):
     #   plot[i][j]=np.fromfile(f,dtype=float,count=1)
        plotc[i][j]=fc.readline()
	plotp[i][j]=fp.readline()
fc.close
fp.close
#plot[plot<0.]+=12
#plot=np.reshape(plot,(nsize,msize))
#print plot.shape
#print plot

m = Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2-0.05,llcrnrlon=lon1, urcrnrlon=lon2-0.05, resolution='l')
#resolution l m h
m.drawcoastlines(linewidth=2,color='black')
m.drawparallels(np.arange(lat1-0.05,lat2,5.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon1-0.05,lon2,10.),labels=[False,True,False,True])  #経線
#plt.title("phase 2009July[local time]")
plt.title("diurnal amplitude 2009July[mm/h]")

X, Y = np.meshgrid(lon,lat)
x, y = m(X, Y)  


m.contourf(x, y, plotc,np.arange(0,1.,0.1))
m.colorbar()
plt.savefig("c.png")


#m.contourf(x, y, plotp,np.arange(0,25,1.))
#m.colorbar()
#plt.savefig("phi.png")


plt.show()
