#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

from function import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os.path
import math



#grads format
lon1=70.05
lon2=100.05
lat1=5.05
lat2=25.05


#地図処理
m = Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2-0.05,llcrnrlon=lon1, urcrnrlon=lon2-0.05, resolution='l')
m.drawcoastlines(color='white')
m.drawparallels(np.arange(lat1-0.05,lat2,5.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon1-0.05,lon2,10.),labels=[False,True,False,True])  #経線
plt.title("Mercator Projection")






lon,lat=getlonlat(lon1,lon2,lat1,lat2)
#lat=getlonlat(lon1,lon2,lat1,lat2)[1]
starti,startj=getstart(lon1,lon2,lat1,lat2)
msize,nsize=getsize(lon,lat)
print "msize:",msize,"nsize:",nsize



#file control
head='/media/kubotashu/HDPC-UT/data/'
#head='07/'
mid='/gsmap_mvk.2009'
tail='00.v5.222.1.dat'


A=np.zeros((nsize,msize))
B=np.zeros((nsize,msize))
C=np.zeros((nsize,msize))
phisum=np.zeros((nsize,msize))
data=np.zeros((nsize,msize))

tmax=24
monmin=7
monmax=7
daymin=1
daymax=31
local=6
datasum=np.zeros((tmax,nsize,msize))


#月間(24*31hour)合計値を取得する
for i in range(monmin,monmax+1):
    mon='%02d'%i
    for j in range(daymin,daymax+1):
        day='%02d'%j
        for k in range(0,tmax):
            hour='%02d'%k
            filename=head+mon+'/'+day+mid+mon+day+'.'+hour+tail
            #filename="07/01/gsmap_mvk.20090701.0000.v5.222.1.dat"
            if os.path.isfile(filename):
                print 'sum'+filename
                data=getdata2(filename,msize,nsize,starti,startj)
                datasum[k]+=data
            else:
                print error



#合計値datasumから平均値rain(t)を出す
span=24*31
data=np.zeros((nsize,msize))
for i in range(monmin,monmax+1):
    mon='%02d'%i
    for j in range(daymin,daymax+1):
        day='%02d'%j
        for k in range(0,tmax):
            hour='%02d'%k
            A+=getAB(datasum[k],k+local)[0]/span
            B+=getAB(datasum[k],k+local)[1]/span
         
  
       
A=A/24.
B=B/24.


C=np.sqrt(A*A+B*B)



pi=4.*np.arctan(1.)
#print pi

for i in range(0,nsize):
    for j in range(0,msize):
        if A[i][j]==0.:
            if B[i][j]==0.:
                phisum[i][j]=0.
            elif B[i][j]>=0.:
                phisum[i][j]=6.
            else:
                phisum[i][j]=18.
        elif B[i][j]==0.:
            if A[i][j]>0.:
                phisum[i][j]=24.
            else:
                phisum[i][j]=12.

        elif A[i][j]<0.:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi+12.
        elif B[i][j]>0.:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi
        else:
            phisum[i][j]=np.arctan(B[i][j]/A[i][j])*12./pi+24.



#配列を並べ替える
plot=C[::-1,::]
plot2=phisum[::-1,::]
A=A[::-1,::]
B=B[::-1,::]
#plot=C[-1::-1]



filephi=open("phi.dat","w")
filec=open("c.dat","w")
filea=open("a.dat","w")
fileb=open("b.dat","w")
for i in range(0,nsize):
    for j in range(0,msize):
        filec.write (str(plot[i][j])+"\n")
        filephi.write (str(plot2[i][j])+"\n")
	filea.write (str(A[i][j])+"\n")
	#filea.write (str(A))
	fileb.write (str(B[i][j])+"\n")

      #  print 'i:',i,'j:',j
        #filec.write("\n")
        
#filec.write(str(plot))
filec.close
filephi.close
filea.close
fileb.close

X, Y = np.meshgrid(lon,lat)
x, y = m(X, Y)                    #projection='cycl' の場合はこの操作はなくてもよい。
m.contourf(x, y, plot,np.arange(0,0.6,0.1))
m.colorbar()
plt.savefig("test03.eps")
plt.show()
