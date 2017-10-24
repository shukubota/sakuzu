#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


#peatman
#lon3=100.
#lon4=120.
#lat3=-7.
#lat4=10.
#savefile="peatman"
#t=1.96

#tian
lon3=100.
lon4=150.
lat3=-15.
lat4=10.
t=1.96
savefile="tian"

#sui
#lon3=119.
#lon4=121.
#lat3=-11.
#lat4=-9.
#t=1.98
#savefile="sui"


#kamimera
#lon3=99.
#lon4=102.
#lat3=-2.
#lat4=3
#t=1.96
#savefile="kamimera"

#iroiro
#lon3=120.
#lon4=150.
#lat3=-7.
#lat4=10.
#t=1.96
#savefile="iroiro"

ocean=np.loadtxt("plotdata_wh04/"+savefile+"/ocean.dat")
oceanerr=np.loadtxt("plotdata_wh04/"+savefile+"/oceanerr.dat")
land=np.loadtxt("plotdata_wh04/"+savefile+"/land.dat")
landerr=np.loadtxt("plotdata_wh04/"+savefile+"/landerr.dat")

ocean2=np.loadtxt("plotdata_wh04/"+savefile+"/ocean2.dat")
ocean2err=np.loadtxt("plotdata_wh04/"+savefile+"/ocean2err.dat")
land2=np.loadtxt("plotdata_wh04/"+savefile+"/land2.dat")
land2err=np.loadtxt("plotdata_wh04/"+savefile+"/land2err.dat")

ocean3=np.loadtxt("plotdata_wh04/"+savefile+"/ocean3.dat")
ocean3err=np.loadtxt("plotdata_wh04/"+savefile+"/ocean3err.dat")
land3=np.loadtxt("plotdata_wh04/"+savefile+"/land3.dat")
land3err=np.loadtxt("plotdata_wh04/"+savefile+"/land3err.dat")


ocean4=np.loadtxt("plotdata_wh04/"+savefile+"/ocean4.dat")
ocean4err=np.loadtxt("plotdata_wh04/"+savefile+"/ocean4err.dat")
land4=np.loadtxt("plotdata_wh04/"+savefile+"/land4.dat")
land4err=np.loadtxt("plotdata_wh04/"+savefile+"/land4err.dat")

ocean5=np.loadtxt("plotdata_wh04/"+savefile+"/ocean5.dat")
ocean5err=np.loadtxt("plotdata_wh04/"+savefile+"/ocean5err.dat")
land5=np.loadtxt("plotdata_wh04/"+savefile+"/land5.dat")
land5err=np.loadtxt("plotdata_wh04/"+savefile+"/land5err.dat")

ocean6=np.loadtxt("plotdata_wh04/"+savefile+"/ocean6.dat")
ocean6err=np.loadtxt("plotdata_wh04/"+savefile+"/ocean6err.dat")
land6=np.loadtxt("plotdata_wh04/"+savefile+"/land6.dat")
land6err=np.loadtxt("plotdata_wh04/"+savefile+"/land6err.dat")



meandataaxis=[1,2,3,4,5,6,7,8]

fig,ax1=plt.subplots()
ax2=ax1.twinx()
##ax1.plot(meandataaxis,ocean,label="ratio on the ocean")
##ax1.errorbar(meandataaxis,ocean,yerr=oceanerr,capsize=10)
##ax1.plot(meandataaxis,land,label="ratio on the land")
##ax1.errorbar(meandataaxis,land,yerr=landerr,capsize=10)

ax1.errorbar(meandataaxis,ocean2,fmt="r",yerr=ocean2err,capsize=10,ecolor="r")
##ax1.plot(meandataaxis,ocean2,"r--",label="diurnal on the ocean")
##ax1.plot(meandataaxis,land2,"b-",label="diurnal on the land")
#ax1.errorbar(meandataaxis,land2,fmt="r",yerr=land2err,capsize=10)

##ax1.plot(meandataaxis,ocean3,label="daily on the ocean")
ax1.errorbar(meandataaxis,ocean3,fmt="b",ecolor="b",yerr=ocean3err,capsize=10)
##ax1.plot(meandataaxis,land3,label="daily on the land")
#ax1.errorbar(meandataaxis,land3,fmt="b",ecolor="b",yerr=land3err,capsize=10)

ax1.errorbar(meandataaxis,ocean5,fmt="y",ecolor="y",yerr=ocean5err,capsize=10)
#ax1.errorbar(meandataaxis,land5,fmt="y",ecolor="y",yerr=land5err,capsize=10)
ax1.errorbar(meandataaxis,ocean6,fmt="k",ecolor="k",yerr=ocean6err,capsize=10)
#ax1.errorbar(meandataaxis,land6,fmt="k",ecolor="k",yerr=land6err,capsize=10)


##ax2.plot(meandataaxis,ocean4,label="ir on the ocean")
ax2.errorbar(meandataaxis,ocean4,fmt="g",ecolor="g",yerr=ocean4err,capsize=10)
##ax2.plot(meandataaxis,land4,label="ir on the land")
#ax2.errorbar(meandataaxis,land4,fmt="g",ecolor="g",yerr=land4err,capsize=10)
fig.text(0.45,0.03,"MJO phase",fontsize=15,color="black")
fig.text(0.95,0.65,"Brightness temperature[K]",fontsize=15,color="black",rotation=90)
fig.text(0.04,0.6,"Precipitation rate[mm/h]",fontsize=15,color="black",rotation=90)
plt.xlim(0.5,8.5)
plt.savefig("figure_wh04/ratio_new_"+savefile+".png")

