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
data=np.zeros((m,n))
countdata=np.zeros((m,n))
pi=np.arctan(1.)*4.
#print pi
A=np.zeros((m,n))
A2=np.zeros((m,n))
B=np.zeros((m,n))
B2=np.zeros((m,n))#フーリエ級数0次
C=np.zeros((m,n))
phi=np.zeros((m,n))
eps2=np.zeros((m,n))#zansa 2jou
sum2=np.zeros((m,n))#heihouwa
sum3=np.zeros((m,n))#heikin


for i in range(1,9):
	file="p"+"%d"%i
	

		
	rep=(i)
	data=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata/plotdata%02d.npy"%i)
	#countdata=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/countfor8p%02d.npy"%i)
		#data[j]=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_no/"+file+"/"+hour+".dat")
		#print np.shape(data)
	A+=data*np.cos(2.*pi*rep*hourstep/8.)
	B+=data*np.sin(2.*pi*rep*hourstep/8.)
	
	sum2+=(data)*(data)
	sum3+=data
	print i
A=A/4.
B=B/4.

s2=(sum2-sum3*sum3/8.-0.5*8.*(A*A+B*B))/(8.-2.-1.)
s2[s2==0.]=1.
f0=8.*(A*A+B*B)/(4.*s2)
	

filef0="plotdata/ffor8.npy"
np.save(filef0,f0)


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
