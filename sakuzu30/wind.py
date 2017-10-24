#coding:utf-8

from netCDF4 import*
import numpy as np
import datetime
import matplotlib.pyplot as plt

#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=2.5
##############################
lon1num=int(lon1/grid)
lat1num=int((90.-lat1)/grid)
lon2num=int(lon2*0.4)
lat2num=int((90.-lat2)/grid)
lonsize=lon2num-lon1num+1
latsize=lat1num-lat2num+1

wind=Dataset("1999test.nc","r")
wind.close

lat=wind.variables["latitude"][:]
#print lat
#print lon
lon=wind.variables['longitude'][:]
time=wind.variables['time'][:]
timevar=wind.variables["time"]
print len(time)
print timevar


year=1999
month=2
day=1
hour=6


nt=date2index(datetime.datetime(year,month,day,hour),timevar)

u=wind.variables['u10'][nt,lat2num:lat1num+1,lon1num:lon2num+1]
v=wind.variables['v10'][nt,lat2num:lat1num+1,lon1num:lon2num+1]


ufile="u.dat"
vfile="v.dat"
np.savetxt(ufile,u,delimiter=",")
np.savetxt(vfile,v,delimiter=",")

