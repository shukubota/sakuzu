#coding:utf-8
import numpy as np

def rdef(r1,r2,mnum,nnum):
	#r1=0.732
	#r2=0.728
	#print (1.+r1)/(1.-r2)
	q1=0.5*np.log((1.+r1)/(1.-r1))
	q2=0.5*np.log((1.+r2)/(1.-r2))
	z=abs(q1-q2)/np.sqrt(1./(mnum-3.)+1./(nnum-3.))
	return z


#zalpha=1.645
#zalpha=1.96
zalpha=2.75

r=[0.775,0.843,0.799,0.791,0.810,0.846,0.781,0.740]
plot=np.zeros((8,8))
for i in range(0,8):
	for j in range(0,8):
		fi=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu38/plotdata/fsakuzu%02d.npy"%(i+1))
		fj=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu38/plotdata/fsakuzu%02d.npy"%(j+1))
		mean=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/cov/mean%02d.npy"%(i+1))

		fi=np.reshape(fi,((1,-1)))
		fj=np.reshape(fj,((1,-1)))
		mean=np.reshape(mean,((1,-1)))
		#print np.shape(fi)
		#print np.shape(mean)


		cols=np.where(fi<3.47)[1]
		cols2=np.where(fj<3.47)[1]
		#print cols
		fi=np.delete(mean,cols,1)
		fj=np.delete(fj,cols2,1)
		#print np.shape(m)
		
		mnum=len(fi[0])
		nnum=len(fj[0])
		print i,j,mnum,nnum
		#print np.shape(fi)
		mean=np.delete(mean,cols,1)
		#print np.shape(mean)
		
		#print "nnum,mnum",nnum,mnum
		#print np.shape(m),np.shape(n)
		plot[i,j]=rdef(r[i],r[j],mnum,nnum)
		#print plot[i,j]

plot[plot>zalpha]=0.

plot[plot!=0.]=1.

print plot

#print rdef(r[3],r[1])
