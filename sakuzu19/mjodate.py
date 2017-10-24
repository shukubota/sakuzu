#coding:utf-8

import numpy as np

data=np.loadtxt("wh04mjoindex.txt",comments="F")
print np.shape(data)
data2=np.loadtxt("CDR.txt")
#print data2

cols=np.where(np.logical_or((data[:,0]<1998.),(data[:,0]>2015.)))
data=np.delete(data,cols,0)
#print np.shape(data)
cols=np.where(np.logical_or((data[:,6]<1.),(data[:,6]>100.)))
data=np.delete(data,cols,0)
#print np.shape(data)


mjo=np.zeros(len(data))
mjo=data[:,0]*10000+data[:,1]*100+data[:,2]
mjo=mjo.astype(np.int)
print mjo
np.savetxt("wh04.dat",mjo,fmt="%i")

#print len(mjo)
cols=np.where(np.logical_or((data2[:,0]<1998.),(data2[:,0]>2015.)))
data2=np.delete(data2,cols,0)
cols=np.where(np.logical_or((data2[:,6]<1.),(data2[:,6]>100.)))
data2=np.delete(data2,cols,0)
mjo2=np.zeros(len(data2))
mjo2=data2[:,0]*10000+data2[:,1]*100+data2[:,2]

mjo2=mjo2.astype(np.int)
print mjo2
np.savetxt("bimodal.dat",mjo2,fmt="%i")
#print np.shape((mjo2))

sum=np.hstack((mjo,mjo2))
sum=sum.astype(np.int)
#print sum
#print np.shape(sum)
sum=list(sum)
#print sum
#print len(sum)
sum=list(set(sum))
sum.sort()
print sum
print len(sum)
plotdata=np.zeros((len(sum),3))
sum=np.array(sum)
plotdata[:,0]=sum/10000
plotdata[:,1]=(sum%10000)/100
plotdata[:,2]=(sum%100)
np.savetxt("mjodate.txt",plotdata,fmt="%04i,%02d,%02d")
