#coding:utf-8
import numpy as np

def getstart(lon1,lon2,lat1,lat2):
    starti=int((-lat2+59.95)*10)  #危険
    startj=int((lon1-0.05)*10)

    print 'starti',starti,'startj',startj

    return starti,startj
    
def getlonlat(lon1,lon2,lat1,lat2):
   

    lon=np.arange(lon1,lon2,0.1)
    lat=np.arange(lat1,lat2,0.1)
    return lon,lat


def getsize(lon,lat):
    msize=len(lon)
    nsize=len(lat)
    print "msize:",msize,"nsize:",nsize
    return msize,nsize

 
def getdata(filename,msize,nsize,starti,startj):
   
  
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

   # print data[700][600]
  #  print 'data[starti][startj]:',data[starti][startj]

    dataex=np.zeros((nsize,msize))
   # print dataex
    #抽出する
    for i in range(0,nsize):
        for j in range(0,msize):
            dataex[i][j]=data[starti+i][startj+j]


    return dataex

def getAB(data,hour):
    pi=4.*np.arctan(1.)
  #  print pi
    A=data*np.cos(hour*2.*pi/24.)
    B=data*np.sin(hour*2.*pi/24.)
   # C=np.sqrt(A*A+B*B)
    return A,B
    #A,Bは各地点の降水量で計算している。平均降水量になっていない
#A,Bの各cell を計算している。



def getdata2(filename,msize,nsize,starti,startj):
    N=1200
    M=3600
    f=open(filename,"rb")
    data=np.fromfile(f,dtype="<f4")
    f.close
    data=np.reshape(data,(N,M))
    data=data[starti:starti+nsize,startj:startj+msize]
    data[data<0.]=0.

    return data



