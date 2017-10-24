#coding:utf-8

import pygrib
import numpy as np
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.75
##############################


lon1num=int(lon1/grid)+1
lat1num=int((90.-lat1)/grid)
lon2num=int(lon2/grid)
lat2num=int((90.-lat2)/grid)+1
print lon1num,lon2num,lat1num,lat2num
lonsize=lon2num-lon1num+1
latsize=lat1num-lat2num+1

#gribs = pygrib.open('20010104sfc-uv.grib')
#gribs=pygrib.open("20010104prs-uv.grib")
gribs=pygrib.open("data/20051120prs-q.grib")

for g in gribs:
	print g.typeOfLevel,g.level,g.name ,g.validDate,g.analDate
	#print g.latitude	

#u=gribs.select(name="10U",typeOfLevel="isovaricInhPa")
#u=gribs.select(name="10U",typeOfLevel="surface")




for hournum in range(0,4):
	for i in range(0,27):
		unum=hournum*27+i+1
		msgu=gribs[unum]
		print msgu.level

msgu=gribs[27]
lats,lons=msgu.latlons()
print msgu.level
#print lons

#print lats
#msgv=gribs[2]
#print msgu
##u=msgu.values
#v=msgv.values
#print u

#u=u[lat2num:lat1num+1,lon1num:lon2num+1]
#v=v[lat2num:lat1num+1,lon1num:lon2num+1]
	
#print "u",np.shape(u)
#print "v",np.shape(v)
#np.savetxt("u.dat",u,delimiter=",")
#np.savetxt("v.dat",v,delimiter=",")
	
	
	
	#lats,lons=msgu.latlons()
#print lons
#print u


#u=10U
#lats,lons=msg.latlons()
#msg=gribs.read()
#print msg
#print len(g)
