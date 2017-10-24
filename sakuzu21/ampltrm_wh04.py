#coding:utf-8
#wh04 noMJO両方に使う。170201
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
#hour step
hourstep=1


#file=open("./sakuzu20/plotdata/p1/


phase=0
data=np.zeros((24,m,n))
pi=np.arctan(1.)*4.
#print pi

for i in range(1,9):
	file="p"+"%d"%i
	
	A=np.zeros((m,n))
	B=np.zeros((m,n))
	C=np.zeros((m,n))
	phi=np.zeros((m,n))
	#data=np.zeros((24,

	datamean=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%i+".dat",delimiter=",")
	for j in range(0,24):
		hour="%02d"%j
		rep=j/hourstep
		data[j]=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/"+file+"/"+hour+".dat")
		A+=data[j]*np.cos(2.*pi*(rep+0.5)*hourstep/24.)
		B+=data[j]*np.sin(2.*pi*(rep+0.5)*hourstep/24.)

	A=A/24.
	B=B/24.
	C=np.sqrt(A*A+B*B)
	condition=np.where((A>0.) & (B>=0.))
	phi[condition]=np.arctan(B[condition]/A[condition])
	condition=np.where((A>0.) & (B<0.))
	phi[condition]=np.arctan(B[condition]/A[condition])+2.*pi
	condition=np.where((A<0.) & (B>=0.))
	phi[condition]=np.arctan(B[condition]/A[condition])+pi
	condition=np.where((A<0.) & (B<0.))
	phi[condition]=np.arctan(B[condition]/A[condition])+pi
	condition=np.where((A==0.) & (B==0.))
	phi[condition]=0.
	condition=np.where((A==0.) & (B>0.))
	phi[condition]=pi*0.5
	condition=np.where((A==0.) & (B<0.))
	phi[condition]=pi*1.5
	#print data[0]

	phi=phi*24/(2.*pi)
	datamean[datamean==0.]=1.
	#C=100.*C/datamean
	filephi="plotdata_wh04/phi"+"%02d"%i+".dat"
	filec="plotdata_wh04/c"+"%02d"%i+".dat"
	#filephi="plotdata_no/phi"+"%02d"%i+".dat"
	#filec="plotdata_no/c"+"%02d"%i+".dat"
	np.savetxt(filephi,phi,delimiter=",")
	np.savetxt(filec,C,delimiter=",")


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
