#coding:utf-8

import numpy as np

#file=open("CDR.txt","r")
#data=np.zeros(5)
#dum=file.readline()
#for line in file:
    #data=(line.split(' '))
    #print data[0],data[1],data[2],data[5],data[6]
    #print data



data2=np.loadtxt("CDR.txt")
print np.shape(data2)

file1=open("p1.dat","w")
file2=open("p2.dat","w")
file3=open("p3.dat","w")
file4=open("p4.dat","w")
file5=open("p5.dat","w")
file6=open("p6.dat","w")
file7=open("p7.dat","w")
file8=open("p8.dat","w")
for i in  range(0,13364):
    if data2[i][0]>1996:
        if data2[i][6]>=1.:
            year=int(data2[i][0])
            mon=int(data2[i][1])
            day=int(data2[i][2])
            yearmonday=str(year).zfill(4)+str(mon).zfill(2)+str(day).zfill(2)
            if data2[i][5]==1.:
                file1.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==2.:
                file2.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==3.:
                file3.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==4.:
                file4.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==5.:
                file5.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==6.:
                file6.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            elif data2[i][5]==7.:
                file7.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')
            else:
                file8.write(yearmonday+' '+str(data2[i][5])+' '+str(data2[i][6])+'\n')

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()        

