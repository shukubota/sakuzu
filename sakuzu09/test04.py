#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *

nsize=4
msize=3
plot=np.zeros((nsize,msize))
f=open("test.dat","r")
for i in range(0,nsize):
    for j in range(0,msize):
      #  plot[i][j]=f.readline(f,dtype='float',count=1)
        plot[i][j]=f.readline()
#plot=np.loadtxt(f,dtype='float')
f.close

print plot
