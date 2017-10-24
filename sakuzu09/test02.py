#coding:utf-8
import numpy as np
def test(i,j):
    return i+1,j+1


u=np.zeros((2,3))
v=2.

U= test(u,v)[0]
V=test(u,v)[1]
#print U
#print V


dataex=np.zeros(())
for i in range(0,2):
    for j in range(0,3):
        dataex[i][j]=10*i+j

print dataex
test2=np.zeros((2,3))

#test2+=testf(1)

#print test2
