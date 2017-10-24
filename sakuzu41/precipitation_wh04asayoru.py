#coding:utf-8
import numpy as np
import time


if __name__ == '__main__':
	start = time.time()

##################
#size of plotdata(m,n)
##################
m=451
n=901
########################

local=8


for j in range(1,9):
	print "phase",j
	plotdata=np.zeros((m,n))
	plotdataasa=np.zeros((m,n))
	plotdatayoru=np.zeros((m,n))
	countdatasum=np.zeros((m,n))
	countdatasumasa=np.zeros((m,n))
	countdatasumyoru=np.zeros((m,n))
	file="p"+"%d"%j
	for i in range(0,24):
		hour="%02d"%i
		
		#data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/"+hour+".dat")
		#countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/count"+hour+".dat")
		data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/"+hour+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/count"+hour+".dat")
				
		if (i+24+local)%24<12:
			print "asa"
			plotdataasa+=data*countdata
			countdatasumasa+=countdata
			print np.shape(countdata)
			#print data,countdata
		else:
			print "yoru"
			plotdatayoru+=data*countdata
			countdatasumyoru+=countdata
			#print data,countdata



	countall=countdatasumasa+countdatasumyoru
	#countall[countall==0]=1
	countdatasumasa[countdatasumasa==0]=1	
	countdatasumyoru[countdatasumyoru==0]=1
	plotdataall=plotdataasa+plotdatayoru
	#print countall
	#print plotdataall
	plotdataall[plotdataall==0.]=1.
	
	plotdata=(plotdatayoru/countdatasumyoru-plotdataasa/countdatasumasa)*countall/plotdataall
	#print plotdata
	#np.save("plotdata/count24h%02d.npy"%j,countdatasum)
	#np.save("plotdata_stra2/count24h%02d.npy"%j,countdatasum)
	#countdatasum[countdatasum==0]=1	
	#plotdata=plotdata/countdatasum


	#countall[countall==0]=1
	#filename="plotdata_wh04/dailyp"+"%02d"%j+".dat"
	filename="plotdata/dailyp"+"%02d"%j+".dat"
	filenameasa="plotdataasa/dailyp"+"%02d"%j+".dat"
	filenameyoru="plotdatayoru/dailyp"+"%02d"%j+".dat"
	filenameall="plotdataall/dailyp"+"%02d"%j+".dat"
	#file=open(filename,"w")
 	np.savetxt(filename,plotdata,delimiter=",")
	np.savetxt(filenameasa,plotdataasa/countdatasumasa,delimiter=",")
	np.savetxt(filenameyoru,plotdatayoru/countdatasumyoru,delimiter=",")	
	#np.savetxt(filenameall,plotdataall/countall,delimiter=",")	


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
