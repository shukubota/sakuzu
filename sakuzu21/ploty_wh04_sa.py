#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

#####################
#fileのサイズ
#########################
lon1=-90.
lon2=-70.
lat1=0.
lat2=15.
grid=0.1

##################
grid2=0.75

##############################
#かきたいえのsize
#########################
#smatra
#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

#sa
lon3=-90.
lon4=-70.
lat3=0.
lat4=15.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.


#test
#lon3=90.
#lon4=160.
#lat3=1.5
#lat4=1.501
##############################
#c or phi(c:1 phiZ:2)
#####################
which=1
local=-6
windlevel=20
#[100,125,150,175,200,225,250,300,350,400,450,500,550,600,650,700,750,775,800,825,850,875,900,925,950,975,1000]
#20:850hpa
##################


nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)

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


#print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend
#print "mstart2:",mstart2,"mend2:",mend2,"nstart2:",nstart2,"nend2:",nend2
lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

lonp2=np.arange(lon3min,lon4min+grid2,grid2)
latp2=np.arange(lat3min,lat4min+grid2,grid2)
#print "lonp2",np.shape(lonp2)
#print "latp2",np.shape(latp2)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)

mpsize2,npsize2=getsize(lonp2,latp2)

print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)
#print len(lon),len(lat)
#print lon


for i in range(1,2):

  
	plotcp=np.zeros((npsize,mpsize))
	plotu=np.zeros((npsize2,mpsize2))
	plotv=np.zeros((npsize2,mpsize2))

	if which==1:
		#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/p1test/00.dat")
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/sa/c.dat",delimiter=",")

	elif which==2:
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/sa/phi.dat",delimiter=",")
	else:
		print "error"
	print np.shape(plotdata)
   
   
	plotdata1=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/uphase"+str(i)+".npy")
	plotdata2=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/vphase"+str(i)+".npy")

	#print plotdata1[0,0,:,:]
	#print "v",np.shape(plotdata2)


	#################
	#CUT
	################
	plotcp=plotdata[mstart:mend+1,nstart:nend+1]
	if which==2:
		plotcp+=local
		plotcp[plotcp>23]-=24
		plotcp[plotcp<0]+=24
	#print "plotcp:",np.shape(plotcp)
	#plotu=plotdata1[0,20,mstart2:mend2+1,nstart2:nend2+1]
	#plotv=plotdata2[0,20,mstart2:mend2+1,nstart2:nend2+1]

	plotu=(plotdata1[0,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[1,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[2,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata1[3,windlevel,mstart2:mend2+1,nstart2:nend2+1])/4.

	#print "nstart,nend",nstart2,nend2
	#print "windlevel",windlevel
	print "mstart,mend",mstart2,mend2
	plotv=(plotdata2[0,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[1,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[2,windlevel,mstart2:mend2+1,nstart2:nend2+1]+plotdata2[3,windlevel,mstart2:mend2+1,nstart2:nend2+1])/4.

	#print "plotu"
	#print plotu
	#plotv=plotdata2[0,20,mstart2:mend2+1,nstart2:nend2+1]
	#latは逆に入っている
	plotu=plotu[::-1,:]
	plotv=plotv[::-1,:]
	#print "plotu",np.shape(plotu)
	#print "plotv",np.shape(plotv)


	#print np.shape(plotcp),np.shape(plotu),np.shape(plotv)
	m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
	#resolution l m h
	m.drawcoastlines(linewidth=1.5,color='black')
	m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
	m.drawmeridians(np.arange(lon3-3,lon4,10.),labels=[False,True,False,True])	#経線


	X, Y = np.meshgrid(lonp,latp)
	x, y = m(X, Y)	

	###########################################################

	#fig=plt.figure()

	if which==1:
		a=m.contourf(x, y, plotcp,np.arange(0.,0.35,0.05),extend="max")
		#np.save("cov/diurnal%02d.npy"%i,plotcp)
		print "test\n"
		b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
		b.set_label("mm/h")
	else:
		a=m.contourf(x, y, plotcp,np.arange(0,25,1))

		
		b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
		b.set_label("LT(UTC-6)")

	if which==1.:
		output="figure_wh04/sa/c.png"
		plt.title("Phase%d"%i)
		#plt.title("Amplitude of Diurnal Precipitation anomaly[Phase="+"%02d"%i+"] [mm/h]")
	 
	if which==2:
		output="figure_wh04/sa/phi.png"
		#plt.title("Phase of Diurnal Precipitation [Phase="+"%02d"%i+"] LT(UTC+"+"%d"%local+")")
		plt.title("Phase%02d"%i)
	###########################################################
	#wind plot
	##########################
	

	X, Y = np.meshgrid(lonp2,latp2)
	x, y = m(X, Y)	
  
	if which==1:
		mabiki=3
		#q=m.quiver(x[::mabiki,::mabiki],y[::mabiki,::mabiki],plotu[::mabiki,::mabiki],plotv[::mabiki,::mabiki],scale=100,color="black",headwidth=5.)
		#qk = plt.quiverkey(q, 0.68, -0.26, 5, 'Wind 5 m/s', labelpos='W',color="black")
		print "test\n"
	else:
		#q=m.quiver(x,y,plotu,plotv,scale=40)
		#qk = plt.quiverkey(q, 0.5, 0., 2, 'Wind Speed 2 m/s', labelpos='W',color="black")
		print "test\n"


	plt.savefig(output,bbox_inches="tight")
	#print output
	#plt.show()

	plt.clf()

#os.system("convert -delay 80 -loop 0 figure_wh04/c/c*.png figure_wh04/c_wh04.gif")
#os.system("convert -delay 80 -loop 0 figure_wh04/phi/phi*.png figure_wh04/phi_wh04.gif")
