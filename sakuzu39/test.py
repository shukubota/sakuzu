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

#data=np.zeros((m,n))

#head=("head","<i")
#tail=("tail","<i")
#dt=np.dtype([head,("arr","<1d"),tail])

file=open("merg_2001010100_4km-pixel","rb")
data=np.fromfile(file,dtype=np.uint8)
print len(data)
data=np.resize(data,((2,m,n)))
print np.shape(data)
#for i in range(0,m):
#	for j in range(0,n):
#		data[i,j]=np.fromfile(file,dtype=np.uint8,count=1)


#arr=chunk[0]
#arr=chunk[0]["arr"].reshape((m,n))
#print data
#print np.shape(data)

#x,y=np.meshgrid(np.arange(0,n,1),np.arange(0,m,1))
#plt.contourf(x,y,data)
#plt.show()

