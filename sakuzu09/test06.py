import numpy as np

nsize=4
msize=5
A=np.zeros((nsize,msize))
B=np.zeros((nsize,msize))

A=[[-21.,-19.,-17.,-15.,-13.],
   [-11.,-9.,-7.,-5.,-3.],
   [-1.,1.,0.,5.,7.],
   [9.,11.,13.,15.,17.]]


B=[[1.,2.,3.,4.,5.],
   [-1.,-2.,-3.,-4.,-5.],
   [2.,3.,-4.,5.,6.],
   [-2.,-3.,-4.,-5.,-6.]]

print A
print B
pi=4.*np.arctan(1.)
#print pi

phisum=np.zeros((nsize,msize))
for i in range(0,nsize):
    for j in range(0,msize):
        if A[i][j]==0.:
            if B[i][j]>=0.:
                phisum[i][j]=6.
            else:
                phisum[i][j]=18.
        elif A[i][j]<0.:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi+12.
        elif B[i][j]>0.:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi
        else:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi+24.

print phisum
