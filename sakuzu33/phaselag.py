#coding:utf-8
#mjophaseごとにharmonic analysisを行っている。
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

	




for var in range(0,3):

	A=np.zeros((m,n))
	B=np.zeros((m,n))
	phi=np.zeros((m,n))
	for phase in range(1,9):
		print phase	
		if var==0:
			data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata/c%02d.dat"%phase,delimiter=",")
		
		elif var==1:
			data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu23/plotdata_bimodal/p%d_rv.dat"%phase,delimiter=",")
		
		
			#olr の温度
			data=data*(-1.)


		else:
			data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata/dailyp%02d.dat"%phase,delimiter=",")




		B+=data*np.sin(2.*pi*phase/8.)
		A+=data*np.cos(2.*pi*phase/8.)
		
	
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
		
		phi=phi*8/(2.*pi)
		
		
		
		if var==0:	
			phiampl=phi
		elif var==1:
			phiolr=phi
		else:
			phimean=phi


difampl=phiampl-phiolr
difmean=phimean-phiolr

#filelag="plotdata/bimodal/lag_ampl.dat"
#filec="plotdata/c"+"%02d"%i+".dat"
filename1="plotdata/bimodal/difampl.dat"
filename2="plotdata/bimodal/difmean.dat"
np.savetxt(filename1,difampl,delimiter=",")
np.savetxt(filename2,difmean,delimiter=",")
#np.savetxt(filec,C,delimiter=",")


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
