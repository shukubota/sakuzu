#coding:utf-8

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import*
import numpy as np
import datetime
import matplotlib.cm as cm
#########################
lon1=94.
lon2=155.
lat1=-17.
lat2=13.
#grid=2.5
#lon1=30.
#lon2=180.
#lat1=-16.
#lat2=16.
grid=2.5
##############################
index=2
###########
#bimodal 1 wh04 2
###############



leveldata=Dataset("ETOPO1_Bed_g_gmt4.grd")
leveldata.close
#olrdata2=Dataset("olr.day.mean_uninterpolated.nc")
#olrdata.close



lat=leveldata.variables["y"][:]
lon=leveldata.variables['x'][:]
level=leveldata.variables["z"][:]

#print lat
#print level

print np.shape(level)
print np.shape(lat),np.shape(lon)
#print lon[lon1num],lon[lon2num],lat[lat1num],lat[lat2num]
#print lon1num,lon2num,lat1num,lat2num
#time=olrdata.variables['time'][:]
#units=olrdata.variables["time"].units
#dtime=num2date(time,units=units)
#print dtime
#timevar=olrdata.variables['time']
#print timevar

cols=np.where(lat<lat1)
lat=np.delete(lat,cols,0)
level=np.delete(level,cols,0)
cols=np.where(lat>lat2)
level=np.delete(level,cols,0)
lat=np.delete(lat,cols,0)
#print np.delete(lat,cols,0)
cols=np.where(lon<lon1)
level=np.delete(level,cols,1)
lon=np.delete(lon,cols,0)
cols=np.where(lon>lon2)
level=np.delete(level,cols,1)
lon=np.delete(lon,cols,0)


print lon
print lat
print level

print np.shape(lat),np.shape(lon)
print np.shape(level)


m=Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2,llcrnrlon=lon1, urcrnrlon=lon2, resolution='l')
#resolution l m h
m.drawcoastlines(linewidth=1.5,color='black')
#m.drawparallels(np.arange(lat1+1,lat2,5.),labels=[True,False,False,True])    #緯線
#m.drawmeridians(np.arange(lon1,lon2,20.),labels=[False,True,False,True])	#経線
m.drawparallels(np.arange(lat1,lat2,2.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon1-3,lon2,10.),labels=[False,True,False,True])

X, Y = np.meshgrid(lon,lat)
x, y = m(X, Y)	

m.contourf(x,y,level,np.arange(0.,2200,200),extend="max",cmap=cm.YlOrBr)

m.colorbar(location="bottom",pad="15%")


#brwest
#rlon3=116.
#rlon4=118.
#rlat3=6.
#wide=8.
#x1, y1 = m(rlon3, rlon4-rlon3+rlat3)
#x2, y2 = m(rlon4, rlat3)
#x4, y4 = m(rlon3-wide*0.5*np.sqrt(2.), rlon4-rlon3+rlat3-wide*0.5*np.sqrt(2.))
#x3, y3 = m(rlon4-wide*0.5*np.sqrt(2.), rlat3-wide*0.5*np.sqrt(2.))

#xtrack = [x1,x2,x3,x4,x1]
#ytrack = [y1,y2,y3,y4,y1]
#m.plot(xtrack, ytrack,color="black",lw=2)

#smwest
#rlon3=93.
#rlon4=96.
#rlat3=4.
#wide=12.
#x1, y1 = m(rlon3, rlat3)
#x2, y2 = m(rlon4, rlon4-rlon3+rlat3)
#x4, y4 = m(rlon3+wide*0.5*np.sqrt(2.), rlat3-wide*0.5*np.sqrt(2.))
#x3, y3 = m(rlon4+wide*0.5*np.sqrt(2.), rlon4-rlon3+rlat3-wide*0.5*np.sqrt(2.))


#xtrack = [x1,x2,x3,x4,x1]
#ytrack = [y1,y2,y3,y4,y1]
#m.plot(xtrack, ytrack,color="black",lw=2)



rlon3=100.
rlon4=150.
rlat3=-15.
rlat4=10.
x1, y1 = m(rlon3, rlat3)
x2, y2 = m(rlon4, rlat3)
x3, y3 = m(rlon4, rlat4)
x4, y4 = m(rlon3, rlat4)


xtrack = [x1,x2,x3,x4,x1]
ytrack = [y1,y2,y3,y4,y1]
m.plot(xtrack, ytrack,color="black",lw=2)


rlon3=100.
rlon4=120.
rlat3=-7.
rlat4=10.
x1, y1 = m(rlon3, rlat3)
x2, y2 = m(rlon4, rlat3)
x3, y3 = m(rlon4, rlat4)
x4, y4 = m(rlon3, rlat4)


xtrack = [x1,x2,x3,x4,x1]
ytrack = [y1,y2,y3,y4,y1]
m.plot(xtrack, ytrack,color="black",lw=2)

plt.savefig("map.png",bbox_inches="tight")



