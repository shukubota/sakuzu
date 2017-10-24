#coding:utf-8
#phaseの平均出してそこからのずれ、ぜったいちをけいさんした


import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os.path
import matplotlib.cm as cm
from function import *
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
grid2=0.75
##############################
#かきたいえのsize
#########################
#lon3=108.

#lon4=120
#lat3=-5
#lat4=8

#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

lon3=93.
lon4=155.
lat3=-12.
lat4=8.
##############################
windlevel=20


nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend

#grid2にあわせたlon1をこえる最小のlon,lon1<lon1min,lon2min<=lon2
#PRとECWMFは格子の作り方が異なるので注意
#latは90 to -90の順になっているので注意
#地図で見て格子の上と左端は含まれていない

lon1min=int(lon1/grid2)*grid2+grid2
lon2min=int(lon2/grid2)*grid2
#lon1min<lon2min

lat2min=90.-(int((90.-lat2)/grid2)*grid2+grid2)
lat1min=90.-int((90.-lat1)/grid2)*grid2
print "lat1min:",lat1min

lon3min=int(lon3/grid2)*grid2+grid2
lon4min=int(lon4/grid2)*grid2
#lon1min<lon2min

lat4min=90.-(int((90.-lat4)/grid2)*grid2+grid2)
lat3min=90.-int((90.-lat3)/grid2)*grid2


nstart2=int((lon3min-lon1min)/grid2)
nend2=int((lon4min-lon1min)/grid2)
mstart2=int((lat2min-lat4min)/grid2)
mend2=int((lat2min-lat3min)/grid2)




lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


lonp2=np.arange(lon3min,lon4min+grid2,grid2)
latp2=np.arange(lat3min,lat4min+grid2,grid2)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)
print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)



plotdum=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu41/plotdata/dailyp01.dat",delimiter=",")
plotdum=plotdum*0.
for i in range(1,9):
	dum=np.abs(np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu41/plotdata/dailyp"+"%02d"%i+".dat",delimiter=","))
	plotdum+=dum
plotdum=plotdum/8.	
plotdum=plotdum[mstart:mend+1,nstart:nend+1]

for i in range(1,9):


	plotcp=np.zeros((npsize,mpsize))


	###################################################
	#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/anmdaily"+"%02d"%i+".dat",delimiter=",")
	plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu41/plotdata/dailyp"+"%02d"%i+".dat",delimiter=",")
	#######################################################


	print np.shape(plotdata)

	plotdata1=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/uphase"+str(i)+".npy")
	plotdata2=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/vphase"+str(i)+".npy")

	#################
	#CUT
	################
	plotcp=np.abs(plotdata[mstart:mend+1,nstart:nend+1])-plotdum

	
	print plotdata
	print "plotcp:",np.shape(plotcp)



	plotu=(plotdata1[0,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[1,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[2,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[3,windlevel,mstart2:mend2+1,nstart2:nend2+1])/4.

	plotv=(plotdata2[0,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[1,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[2,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[3,windlevel,mstart2:mend2+1,nstart2:nend2+1])/4.
	#latは逆に入っている
	plotu=plotu[::-1,:]
	plotv=plotv[::-1,:]

	m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
	#resolution l m h
	m.drawcoastlines(linewidth=1.5,color='black')
	m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
	m.drawmeridians(np.arange(lon3-3,lon4,10.),labels=[False,True,False,True])	#経線


	X, Y = np.meshgrid(lonp,latp)
	x, y = m(X, Y)	

	###########################################################


	#np.save("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/cov/mean%02d.npy"%i,plotcp)
	#a=m.contourf(x, y, plotcp,np.arange(-3.5,3.51,1.),cmap=cm.RdBu_r,extend="both")
	a=m.contourf(x, y, plotcp,cmap=cm.RdBu_r,extend="both")
	#a=m.contourf(x, y, plotcp,np.arange(0.,1.1,0.1))
	print plotcp
#	b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
#	b.set_label("mm/h")


	#m.contourf(x, y, plotcp)
	#m.contourf(x, y, plotcp,np.arange(0,25,1))
	m.colorbar()
	output="figure/wh04/daily"+"%02d"%i+".png"
	#output="figure/all/daily"+"%02d"%i+".png"
	#output="figure/wh04/strm2"+"%02d"%i+".png"
	#output="figure/meanphi.png"
	#plt.title("Phase of Diurnal Precipitation in MJO [UTC]")
	#plt.title("Precipitation Rate in MJO  [Phase="+"%02d"%i+"]  [mm/h]")
	plt.title("Phase%2d"%i)
	###########################################################





	###########################################################
	#wind plot
	##########################
	

	X, Y = np.meshgrid(lonp2,latp2)
	x, y = m(X, Y)	
  
	mabiki=3
	#q=m.quiver(x[::mabiki,::mabiki],y[::mabiki,::mabiki],plotu[::mabiki,::mabiki],plotv[::mabiki,::mabiki],scale=100,color="black",headwidth=5.)
	#qk = plt.quiverkey(q, 0.68, -0.26, 5, 'Wind 5 m/s', labelpos='W',color="black")
	#qk = plt.quiverkey(q, 1.09, -0.06, 5, '5 m/s', labelpos='W',color="black")

	plt.savefig(output,bbox_inches="tight")
	print output
	#plt.show()

	plt.clf()


#os.system("convert -delay 80 -loop 0 figure/wh04/*.png figure/daily_wh04.gif")
