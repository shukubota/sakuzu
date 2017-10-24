#coding:utf-8
#mjophaseごとにharmonic analysisを行っている。
import numpy as np
import time

if __name__ == '__main__':
	start = time.time()

##################
#size of plotdata(m,n)
##################
#m=451
#n=901
########################
#hour step
hourstep=1


#file=open("./sakuzu20/plotdata/p1/


phase=0
#data=np.zeros((m,n))
pi=np.arctan(1.)*4.
#print pi

	

m,n=np.shape(np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata/anm/anm01.npy"))


for var in range(0,1):

	A=np.zeros((m,n))
	B=np.zeros((m,n))
	phi=np.zeros((m,n))
	for phase in range(1,9):
		print phase	
		
		data=-np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata/anm/anm%02d.npy"%phase)
		
		
		print np.shape(data)



		B+=data*np.sin(2.*pi*(phase-1)/8.)
		A+=data*np.cos(2.*pi*(phase-1)/8.)
		
	
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
		phi=phi+1
		phi[phi>9.]-=8.
				
		
		if var==0:	
			phiampl=phi
		elif var==1:
			phiolr=phi
		else:
			phimean=phi


#difampl=phiampl-phiolr
#difmean=phimean-phiolr

#filelag="plotdata/bimodal/lag_ampl.dat"
#filec="plotdata/c"+"%02d"%i+".dat"
filename1="plotdata/anm/phiampl.npy"
#filename2="plotdata/wh04/phiolr.dat"
#filename3="plotdata/wh04/phimean.dat"
np.save(filename1,phiampl)
#np.savetxt(filename2,phiolr,delimiter=",")
#np.savetxt(filename3,phimean,delimiter=",")
#np.savetxt(filec,C,delimiter=",")


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
