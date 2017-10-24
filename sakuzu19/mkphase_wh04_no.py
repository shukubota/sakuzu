#coding:utf-8
import numpy as np

data=np.loadtxt("wh04mjoindex.txt",comments="F")

cols=np.where(np.logical_or((data[:,0]<1998.),(data[:,0]>2015.)))
data=np.delete(data,cols,0)
#print np.shape(data)
cols=np.where(np.logical_or((data[:,6]>1.),(data[:,6]>100.)))
data=np.delete(data,cols,0)
cols=np.where(data[:,6]==1.)
data=np.delete(data,cols,0)
#print data
print len(data)


for phase in range(1,9):

    cols=np.where(data[:,5]!=phase)

    data2=np.delete(data,cols,0)
    plot=np.zeros((len(data2),1))
    plot=data2[:,0]*10000+data2[:,1]*100+data2[:,2]
    print np.shape(plot)
    filename="noMJO/wh04p"+str(phase)+".dat"
    np.savetxt(filename,plot,fmt="%i")


