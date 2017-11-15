#coding:utf-8
#mjo phase grid 修正版
#家から
#nra


import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob
import gc

if __name__ == '__main__':
	start = time.time()
	


#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
##############################
lonsize=int((lon2-lon1)/grid)+1
latsize=int((lat2-lat1)/grid)+1
level=80
slev=79  #調べたい高度0-79 79が地表
plotdata=np.zeros((24,lonsize,latsize))
count=np.zeros((24,lonsize,latsize))
print np.shape(plotdata)


#logfile=open("log.txt","w")


for phase in range(1,2):

	phasename="p"+str(phase)

	#dhead=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/wh04date/wh04"+phasename+".dat")
	dhead=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/nradate.txt")
	#print np.shape(dhead)
	#print dhead
	plotdata=np.zeros((24,lonsize,latsize))
	plotdata2=np.zeros((24,lonsize,latsize))
	count=np.zeros((24,lonsize,latsize))
	count2=np.zeros((24,lonsize,latsize))
	print "plotdata ",np.shape(plotdata)


	max =len(dhead)



	for i in range(0,1):
		#print i
		head=str(int(dhead[i]))
		print head

		if dhead[i]>20140000:
			comand="sshpass -p  'mitsuyacider' scp -o StrictHostKeyChecking=no -P 20022 kubota@localhost:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*.HDF.Z data/"
		else:
			comand="sshpass -p 'mitsuyacider'  scp -o StrictHostKeyChecking=no -P 20022 kubota@localhost:/box03/TRMM/V7/L2/2A25/*/*/2A25."+head+"*.HDF.gz data/"

		os.system(comand)
		os.system("gunzip data/*")
		list=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/data/*")
		#print list



		for j in range(0,len(list)):
			filename=list[j]
			if os.path.getsize(filename)<100000:
				continue
			hdf=SD(filename,SDC.READ)
			####################################
			#e_surfrain
			#################################
			data3D=hdf.select('e_SurfRain')
			data=data3D[:]
			data=np.reshape(data,(-1,1))
			#########################################
			#rain levelも含んでいる
			#############################

			#data3D=hdf.select('rain')
			#data=data3D[:]
			del data3D
			gc.collect()
			#print np.shape(data)
			##############################
			lat=hdf.select('Latitude')
			latitude=lat[:]
			latitude=np.reshape(latitude,(-1,1))
			#print np.shape(latitude)
			del lat
			gc.collect()
			lon = hdf.select('Longitude')
			longitude = lon[:]
			#print np.shape(longitude)
			longitude=np.reshape(longitude,(-1,1))
			#print np.shape(longitude)
			del lon
			gc.collect() 
			Hour=hdf.select('Hour')
			hour=Hour[:]
			hour=np.reshape(hour,(-1,1))
			hourlong=hour
			#print hour
			del Hour
			gc.collect()
			Flag=hdf.select('rainType')
			flag=Flag[:]
			flag=np.reshape(flag,(-1,1))
			

			for a in range(0,48):	#48回足す
				hourlong=np.vstack((hourlong,hour))
			#print np.shape(hourlong)

			#print longitude
			array=np.hstack((longitude,latitude))
			array=np.hstack((array,data))

			array=np.hstack((array,hourlong))

			#print np.shape(array)



			################################
			#cut
			################################
			cols=np.where(array[:,2]<0.)
			array=np.delete(array,cols,0)
			flag=np.delete(flag,cols,0)
			cols=np.where(array[:,0]<lon1-0.5*grid)
			array=np.delete(array,cols,0)
			flag=np.delete(flag,cols,0)
			cols=np.where(array[:,0]>=lon2+0.5*grid)
			array=np.delete(array,cols,0)
			flag=np.delete(flag,cols,0)
			cols=np.where(array[:,1]<lat1-0.5*grid)
			array=np.delete(array,cols,0)
			flag=np.delete(flag,cols,0)
			cols=np.where(array[:,1]>=lat2+0.5*grid)
			array=np.delete(array,cols,0)
			flag=np.delete(flag,cols,0)
			#print array
			#print np.shape(array)
			
			array[:,3]+=np.round(array[:,0]/15.)
			array[:,3]=array[:,3]%24

			#print array


			
			if len(array)!=0:


				m=(array[:,0]+0.5*grid-lon1)/grid
				n=(array[:,1]+0.5*grid-lat1)/grid
				mint=m.astype(np.int)
				nint=n.astype(np.int)
				hourcell=array[:,3]
				hourint=hourcell.astype(np.int)
				datacell=array[:,2]
				#print len(m),len(n),len(hourcell),len(datacell)
				#print mint
				#print n
				#print nint[:]

				for k in range(0,len(datacell)):
					if datacell[k]>0.:
						#if (flag[k]>99.) and (flag[k]<200): 
						plotdata[hourint[k]][mint[k]][nint[k]]+=datacell[k]

					count[hourint[k]][mint[k]][nint[k]]+=1.





		os.system("rm data/*")

	for p in range(0,24):
		hourname="%02d"%p
		filename="nradata/count"+hourname+".dat"
		#filename2="plotdata2/"+phasename+"/count"+hourname+".dat"
		fp=open(filename,"w")
		#fp2=open(filename2,"w")
		for k in range(0,len(plotdata[0][0])):
			for l in range(0,len(plotdata[0])):
				fp.write(str(count[p][l][k])+" ")
			fp.write("\n")
		fp.close()


	#count[count==0.]=1.
	

	#plotdata=plotdata/count
	#plotdata2=plotdata2/count

	for p in range(0,24):
		hourname="%02d"%p
		filename="nradata/"+hourname+".dat"
		#countfilename="nradata/count"+hourname+".dat"
		fp=open(filename,"w")
		#filename2="plotdata2/"+phasename+"/"+hourname+".dat"
		#fp2=open(filename2,"w")
		#np.savetxt(filename,plotdata,delimiter=" ")
		#np.savetxt(countfilename,count,delimiter=" ")
		for k in range(0,len(plotdata[0][0])):
			for l in range(0,len(plotdata[0])):
				fp.write(str(plotdata[p][l][k])+" ")

			fp.write("\n")
		fp.close()
	#	for k in range(0,len(plotdata2[0][0])):
	#		for l in range(0,len(plotdata2[0])):
	#			fp2.write(str(plotdata2[p][l][k])+" ")
	#
	#		fp2.write("\n")
	#	fp2.close()


#logfile.close()
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
