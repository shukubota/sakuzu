#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=2.5
##############################
#かきたいえのsize
#########################
lon3=90.
lon4=155.
lat3=-15.
lat4=10.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.
##############################

nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend

lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)
print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)

for i in range(1,2):

 
    plotu=np.zeros((npsize,mpsize))
    plotv=np.zeros((npsize,mpsize))
    plotdata1=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu30/u.dat",delimiter=",")
    plotdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu30/v.dat",delimiter=",")

 


    #################
    #CUT
    ################
    plotu=plotdata1[mstart:mend+1,nstart:nend+1]
    plotv=plotdata2[mstart:mend+1,nstart:nend+1]
  

    m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
    #resolution l m h
    
    m.drawcoastlines(linewidth=1.5,color='black')
    m.drawparallels(np.arange(lat3,lat4,5.),labels=[True,False,False,True])    #緯線
    m.drawmeridians(np.arange(lon3,lon4,10.),labels=[False,True,False,True])  #経線

    X, Y = np.meshgrid(lonp,latp)
    x, y = m(X, Y)  

    ###########################################################



    #m.contourf(x, y, plotcp,np.arange(0,1.6,0.1))
    #m.contourf(x, y, plotcp,np.arange(145,260,1.))
    #m.colorbar()
    #output="figure/c/c"+"%02d"%i+".png"
    output="figure/olr_p"+"%d"%i+".png"
   
    plt.title("OLR Distribution [Phase="+"%02d"%i+"]  [W/m^2]")
    q=m.quiver(x,y,plotu,plotv,scale=700)
    qk = plt.quiverkey(q, 0.5, -0.16, 20, 'Wind Speed 20 m/s', labelpos='W')
    #plt.quiver(X,Y,plotu,plotv)
    ###########################################################


    #plt.savefig(output)
    #print output
    plt.show()

    #plt.clf()
