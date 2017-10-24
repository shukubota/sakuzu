#coding:utf-8

import os
import glob
import pygrib
import numpy as np
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    start = time.time()


#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
##############################

m,n=3298,9896


lon1num=int((lon1-180./9896.)*9896/360.+1.)
lon2num=int((lon2-180./9896.)*9896/360.)
lat1num=int((lat1+60.-60./3298.)*3298./120.+1)
lat2num=int((lat2+60.-60./3298.)*3298./120.)

lonp=np.arange(lon1num,lon2num+1,1)
latp=np.arange(lat1num,lat2num+1,1)
print np.shape(lonp),np.shape(latp)
data=np.zeros((lat2num+1-lat1num,lon2num+1-lon1num))
count=np.zeros((lat2num+1-lat1num,lon2num+1-lon1num))


for phase in range(1,2):
	
	plotdata=np.load("plotdata/irp%02d.npy"%phase)
	countdata=np.load("plotdata/count%02d.npy"%phase)
	print np.shape(plotdata)
	
	plotdata=plotdata*countdata
	data=plotdata[0,:,:]+plotdata[1,:,:]
	count=countdata[0,:,:]+countdata[1,:,:]	
	count[count==0]=1
	data=data/count
	data+=75.
	
	#plotdata=plotdata.mean(axis=0)
	print np.shape(data)
	x,y=np.meshgrid(lonp,latp)
	#plotdata=plotdata.transpose()
	plt.contourf(x,y,data)
	plt.colorbar()
	plt.show()

