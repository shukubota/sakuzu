#nra用


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



for j in range(1,2):
	plotdata=np.zeros((m,n))
	countdatasum=np.zeros((m,n))
	file="p"+"%d"%j
	for i in range(0,24):
		hour="%02d"%i
		
		#data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/"+hour+".dat")
		#countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/count"+hour+".dat")
		data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/"+file+"/"+hour+".dat")
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/count"+hour+".dat")
				

		plotdata+=data*countdata
		countdatasum+=countdata
	np.save("plotdata_wh04/count24h%02d.npy"%j,countdatasum)
	#np.save("plotdata_stra2/count24h%02d.npy"%j,countdatasum)

	print countdatasum
	print plotdata
	countdatasum[countdatasum==0]=1	
	plotdata=plotdata/countdatasum
	#print plotdata

	filename="plotdata_wh04/dailyp"+"%02d"%j+".dat"
	#filename="plotdata_stra2/dailyp"+"%02d"%j+".dat"
	#file=open(filename,"w")
 	np.savetxt(filename,plotdata,delimiter=",")
	

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
