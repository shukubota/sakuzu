#coding:utf-8
from function import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os.path
import math


#grads format
#lon1=70.05
#lon2=100.05
#lat1=5.05
#lat2=25.05

lon1=0.05
lon2=360.05
lat1=-59.95
lat2=60.05


#地図処理
m = Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2-0.05,llcrnrlon=lon1, urcrnrlon=lon2-0.05, resolution='c')
m.drawcoastlines()
m.drawparallels(np.arange(lat1,lat2,30.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon1,lon2,30.),labels=[False,True,False,True])  #経線
plt.title("Mercator Projection")

#map = Basemap(width=12000000,height=9000000,projection='merc',resolution=None,lat_1=-10,lat_2=0,lat_0=10,lon_0=100.)

lon,lat=getlonlat(lon1,lon2,lat1,lat2)
#lat=getlonlat(lon1,lon2,lat1,lat2)[1]
starti,startj=getstart(lon1,lon2,lat1,lat2)
msize,nsize=getsize(lon,lat)
filename="07/01/gsmap_mvk.20090701.0000.v5.222.1.dat"

plot=np.zeros((nsize,msize))
plot=getdata2(filename,msize,nsize,starti,startj)
#print plot.shape

#print plot 

plot=plot[::-1][::]

X, Y = np.meshgrid(lon,lat)
x, y = m(X, Y)                    #projection='cycl' の場合はこの操作はなくてもよい。

m.contourf(x, y, plot,np.arange(0,10.,1.))
m.colorbar()
m.bluemarble()
plt.savefig("test.eps")
plt.show()


