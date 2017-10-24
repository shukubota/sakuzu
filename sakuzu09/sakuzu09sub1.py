#coding:utf-8
#filenameからdataをとりだす
#month day folder から24*31個のデータセットを取り出しharmonic function A,Bの配列3600*1200を返す
#A=sum_1,24 rain(t)*cos(2*pi*t/24)
#B=sum_1,24 rain(t)*sin(2*pi*t/24)

mon='07'

'/media/kubotashu/HDPC-UT/data/07/01/gsmap_mvk.20090701.0000.v5.222.1.dat'
head='/media/kubotashu/HDPC-UT/data/'
mid='/gsmap_mvk.2009'
tail='.0000.v5.222.1.dat'
for i in range(0,31):
    day='%02d'%i+1
    for j in range(0,24):
        hour='%02d'%j
        name=head+mon+'/'+day+mid+mon+day+tail
        print name
        
        









def getdata(filename):
    import numpy as np
    
    M=3600
    N=1200
    

    
    data=np.zeros((N,M))
    file=open(filename,'rb')
    
    for i in range(0,N):
        for j in range(0,M):
            data[i][j]=np.fromfile(file,dtype="<f4",count=1)
            if data[i][j]<0.:
                data[i][j]=0.
    

    file.close

    return data
