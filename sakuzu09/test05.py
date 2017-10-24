#coding:utf-8
from function import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os.path
import math

data=np.zeros((2,3))
data2=np.zeros((2,3))

for i in range(0,2):
    for j in range(0,3):
        data[i][j]=1.+i*10.+j
        data2[i][j]=2.+i*10.+j

#print data
#print data2

data3=[data,data2]
#print data3
#print data3[1][1][0]

test=np.zeros((3,2,3))
for i in range(0,3):
    test[i]=np.zeros((2,3))+2.

print data
print data2

data=data/test[0]
data2=data2/test[1]

print data,data2
