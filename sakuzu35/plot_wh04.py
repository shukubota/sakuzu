#coding:utf-8
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
from mpl_toolkits.axes_grid1 import ImageGrid
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


#ng
#lon3=135.
#lon4=145.
#lat3=-10.

#smwest
lon3=93.
lon4=96.
lat3=4.



length=lon4-lon3

lat4=lat3+length



nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)




lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


mpsize,npsize=getsize(lonp,latp)



houraxis=np.arange(0,24)
#houraxis=np.hstack((houraxis,houraxis))
#tatejiku



#plotfin=np.zeros((len(houraxis),mpsize))
for phase in range(1,9):
	
	plotdata=np.zeros((npsize,mpsize))
	#plotdata2=np.zeros((2*npsize,mpsize))
	filename="plotdata/wh04/hovphase"+"%d"%phase+".dat"
	plotdata=np.loadtxt(filename,delimiter=",")
	#plotdata2=np.vstack((plotdata,plotdata))
	print "plotdata",np.shape(plotdata)
	#print "plotdata2",np.shape(plotdata2)

	print houraxis
	#houraxis=houraxis[::-1]
	X,Y=np.meshgrid(lonp,houraxis)
	

	print "x,y",len(lonp),len(houraxis)


	fig=plt.figure(4,(4.,14.))
	grid=ImageGrid(fig,(2,1,1),nrows_ncols = (2, 1),cbar_mode="single")

	ax=grid[0]
	#plt.colorbar()
	#t3=grid[2].contourf(X,Y,plotdata,np.arange(0.,max,range))
	
	#axs1=fig.add_axes((0.1,0.5,0.48,0.4))
	#axs2=fig.add_axes((0.1,0.1,0.6,0.4),sharex=axs1)	
	#left,bottom,width,height	


	#fig.text(0.1,0.92,"Propagation of pricipitation [phase=%d][mm/hr]"%phase,fontsize=15)
	#plt.xlabel("Longitude [deg E]")
	#plt.ylabel("Local Time (UTC+7)")
	#fig.text(0.05,0.6,"Local Time (UTC+7)",rotation=90)




	#################
	#max,range
	##############

	max=0.8
	range=0.05

	#####################


	#t1=grid[0].contourf(X,Y,plotdata,np.arange(0.,max,range))
	#t2=grid[1].contourf(X,Y,plotdata,np.arange(0.,max,range))
	t1=grid[0].contourf(plotdata)
	grid.cbar_axes[0].colorbar(t1)
	#grid.axes_llc.set_xticks([lon3,lon4+grid,grid])	

	
	#ax=t1.gca()
	#ax.invert_yaxis()
	t2=grid[1].contourf(plotdata)
	grid.cbar_axes[1].colorbar(t2)
	#plt.subplot(211)

	#t1=axs1.contourf(X,Y,plotdata,np.arange(0.,max,range))
	#fig.colorbar(t1,orientation="vertical")
	#ax=plt.gca()
	#ax.invert_yaxis()
	


	#ax.set_xticklabels([])
	#ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=0))

	


	#plt.colorbar()

	#plt.subplot(212)
	#t2=plt.contourf(X,Y,plotdata,np.arange(0.,max,range))
	#fig.colorbar(t2)	

	#fig.colorbar()
	
	#ax2=plt.gca()
	#ax2.invert_yaxis()
	#plt.colorbar()
	
	

	#axs1.tick_params(labelbottom='off')
	#cax=fig.add_axes([0.9,0.05,0.6,0,015])
	#plt.colorbar(t1,cax,orientation="vertical")
	plt.savefig("figure/wh04/hov_wh04_p"+"%d"%phase+".png",bbox_inches="tight")
	#plt.clf()	

  


os.system("convert -delay 80 -loop 0 figure/wh04/*.png figure/hov_wh04.gif")

	



