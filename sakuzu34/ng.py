#coding:utf-8

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import*
import numpy as np
import datetime
import matplotlib.cm as cm
#########################

#sm br
#lon1=95.
#lon2=120.
#latitude=2.
#lat2=8.
#grid=2.5
#ng
lon1=135.
lon2=150.
latitude=-6.




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


cols=np.where(lat<latitude-0.1)
lat=np.delete(lat,cols,0)
level=np.delete(level,cols,0)
cols=np.where(lat>latitude+0.1)
level=np.delete(level,cols,0)
lat=np.delete(lat,cols,0)
#print np.delete(lat,cols,0)
cols=np.where(lon<lon1)
level=np.delete(level,cols,1)
lon=np.delete(lon,cols,0)
cols=np.where(lon>lon2)
level=np.delete(level,cols,1)
lon=np.delete(lon,cols,0)
level[level<0.]=0.
level=level.mean(axis=0)


print lon
print lat
print level

print np.shape(lat),np.shape(lon)
print np.shape(level)


#m=Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2,llcrnrlon=lon1, urcrnrlon=lon2, resolution='l')
#resolution l m h
#m.drawcoastlines(linewidth=1.5,color='black')
#m.drawparallels(np.arange(lat1,lat2,2.),labels=[True,False,False,True])    #緯線
#m.drawmeridians(np.arange(lon1-3,lon2,10.),labels=[False,True,False,True])	#経線


#X, Y = np.meshgrid(lon,lat)
#x, y = m(X, Y)	

#colors = cm.gist_earth(np.arange(0.6,1.,0.037))
#con=m.contourf(x,y,level,np.arange(0.,2500,200),extend="max",colors=colors)
#m.contourf(x,y,level,np.arange(0.,2200,200),extend="max",cmap=cm.YlOrBr)
#con.clabel()
#m.colorbar()
#plt.show()

plt.plot(lon,level,color="black")
plt.ylim([0,3500])
plt.xlabel("Longitude [degree E]")
plt.ylabel("Level[m]")
#plt.title("Level distribution on Latitude=6 deg S")
plt.savefig("ng.png",bbox_inches="tight")



