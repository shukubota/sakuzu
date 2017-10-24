#coding:utf-8

import os
import glob
import pygrib
import numpy as np
import time

if __name__ == '__main__':
    start = time.time()


#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.75
##############################
#bimodal 1 wh04 2
index=2


lon1num=int(lon1/grid)+1
lat1num=int((90.-lat1)/grid)
lon2num=int(lon2/grid)
lat2num=int((90.-lat2)/grid)+1
print lon1num,lon2num,lat1num,lat2num
lonsize=lon2num-lon1num+1
latsize=lat1num-lat2num+1


timestep=4  #00 06 12 18
level=[100,125,150,175,200,225,250,300,350,400,450,500,550,600,650,700,750,775,800,825,850,875,900,925,950,975,1000]

levelnum=len(level)
print levelnum


for phase in range(1,9):
	
	u=np.zeros((timestep,levelnum,lat1num+1-lat2num,lon2num+1-lon1num))
	v=np.zeros((timestep,levelnum,lat1num+1-lat2num,lon2num+1-lon1num))
	count=np.zeros((timestep,levelnum,lat1num+1-lat2num,lon2num+1-lon1num))
	
	
	phasename="p"+str(phase)
	print phasename

	print index
	if index==2:
		dhead=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/wh04date/wh04"+phasename+".dat")
	elif index==1:
		dhead=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/"+phasename+".dat")
		dhead=dhead[:,0]
		#print dhead	
	else:
		print "wrong index"
		break

	dhead=dhead.astype(np.int)
	max=len(dhead)
	maxdate=max
	
	for date in range(0,maxdate):
	
		if ((dhead[date]>19980100)&(dhead[date]<20141008))or((dhead[date]>20150210)&(dhead[date]<20150402)):
		#if dhead[i]<20150402:
			year=int(dhead[date]/10000)
			comand="sshpass -p 'mitsuyacider' scp kubota@10.226.168.181:/disc10/yamamoto/GRIBdata/kubota/"+str(year)+"/"+str(int(dhead[date]))+"prs-uv.grib data/"
	
		else:
			print "解析期間範囲外"
			continue
	       
		os.system(comand)
	   
		list=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/data/*")
		if len(list)==0:
			print "len(list)==0"
			continue
		print list[0]
		gribs=pygrib.open(list[0])
			
	
		for hournum in range(0,timestep):
		    for i in range(0,levelnum): 
		        unum=hournum*levelnum*2+i*2+1
		        vnum=hournum*levelnum*2+i*2+2
		        msgu=gribs[unum]
		        msgv=gribs[vnum]
		        #print msgu
		        #print msgv
		        ucell=msgu.values
		        vcell=msgv.values
		        ucell=ucell[lat2num:lat1num+1,lon1num:lon2num+1]
		        vcell=vcell[lat2num:lat1num+1,lon1num:lon2num+1]
		        u[hournum,i,:,:]+=ucell[:,:]
		        v[hournum,i,:,:]+=vcell[:,:]
	
		os.system("rm data/*")
	
	
	
	u=u/float(maxdate)
	v=v/float(maxdate)
	
	#print u
	#print "u",np.shape(u)
	#print "v",np.shape(v)




	np.save("winddata/uphase"+str(phase)+".npy",u)
	np.save("winddata/vphase"+str(phase)+".npy",v)
	#time,level,lat,lon,4,27,latsize,lonsize


print u[0,21,:,:]
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"


#lats,lons=msgu.latlons()
#print lons
#print u


#u=10U
#lats,lons=msg.latlons()
#msg=gribs.read()
#print msg
#print len(g)

