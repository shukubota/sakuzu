#coding:utf-8
#決定版

import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

from matplotlib import dates as mdates
from matplotlib import ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import *

##################
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1

##############################
#かきたいえのsize
#########################
#hov,pyとあわせる
#lon3=96.
#lon4=101.
#lat3=-5.


#ng east
lon3=142.
lon4=144.
lat3=-3.
local=9
dire="ng"


#sm east
#lon3=100.
#lon4=103.
#lat3=0.
#local=7
#dire="smeast"


#sm west
#lon3=93.
#lon4=96.
#lat3=4.
#local=7
#dire="smwest"

#br
#lon3=116.
#lon4=118.
#lat3=6.
#local=8
#dire="brwest"


#breast
#lon3=115.
#lon4=119.
#lat3=-1.
#local=8
#dire="breast"

length=lon4-lon3

lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)




lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


mpsize,npsize=getsize(lonp,latp)



houraxis=np.arange(0,25)
#houraxis=np.hstack((houraxis,houraxis))
#tatejiku



#plotfin=np.zeros((len(houraxis),mpsize))


for time in range(1,3):
	if time==1:
		title="Easterly regimes"
		phaselist=[1,2,3,4,8]

	if time==2:
		title="Westerly regimes"
		phaselist=[5,6,7]

	plotdata=np.loadtxt("plotdata/wh04/"+dire+"/hovphase1.dat",delimiter=",")
	sizem,sizen=np.shape(plotdata)
	plotdata=np.zeros((sizem,sizen))
	count=0
	for phase in phaselist:
		count+=1
		#plotdata2=np.zeros((2*npsize,mpsize))
		filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%phase+".dat"
		plotdata+=np.loadtxt(filename,delimiter=",")
		print "plotdata",np.shape(plotdata)
	

	plotdata=plotdata/count	
	X,Y=np.meshgrid(lonp,houraxis)
	

	print "x,y",len(lonp),len(houraxis)


	fig=plt.figure(figsize=(5,12))


	#fig.text(0.1,0.92,"Time series of coastal rainfall [phase=%d][mm/hr]"%phase,fontsize=15)
	fig.text(0.4,0.92,title,fontsize=15)
	#plt.xlabel("Longitude [deg E]")
	#plt.ylabel("Local Time (UTC+7)")
	fig.text(0.05,0.6,"Local Time (UTC+%d)"%local,rotation=90)
	#fig.text(0.35,0.07,"Longitude [deg E]",rotation=0)
	fig.text(0.2,0.08,"West")
	fig.text(0.8,0.08,"East")
	plt.subplots_adjust(left=None, bottom=None, right=None, top=None, hspace=0.0)


	#################
	#max,range
	##############

	max=0.50001
	range=0.05

	#####################

	#fig,(ax1,ax2)=plt.subplots(2,1,sharex=True)
	#ax1.contourf(X,Y,plotdata,np.arange(0.,max,range))

	test1=plt.subplot(211)
	cf=plt.contourf(X,Y,plotdata,np.arange(0.,max,range),extend="max")
	
	
	ax1=plt.gca()
	ax1.yaxis.set_major_locator(MultipleLocator(3))
	ax1.invert_yaxis()
	ax1.set_xticklabels([])
	#ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=0))

	cax=fig.add_axes([0.94,0.1,0.04,0.8])
	plt.colorbar(cf,cax)
	


	#plt.colorbar()

	plt.subplot(212)
	plt.contourf(X,Y,plotdata,np.arange(0.,max,range),extend="max")
	#plt.colorbar()	

	#fig.colorbar()
	#plt.locator_params(axis="y",tight=True,nbins=4)
		
	ax2=plt.gca()
	plt.yticks(np.arange(3,25,3))
	#ax2.yaxis.set_major_locator(MultipleLocator(6))
	ax2.invert_yaxis()
	ax2.set_xticklabels([])
	#plt.colorbar()
	
	

	#axs1.tick_params(labelbottom='off')
	#cax=fig.add_axes([0.9,0.05,0.6,0,015])
	#plt.colorbar(t1,cax,orientation="vertical")
	plt.savefig("figure/wh04_ng_regime/"+title+".png",bbox_inches="tight")
	plt.clf()	

  


#os.system("convert -delay 80 -loop 0 figure/wh04/*.png figure/hov_wh04.gif")

	



