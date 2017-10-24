#coding:utf-8
import numpy as np
import scipy.stats

for phase in range(1,9):
	diurnal=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/cov/diurnal%02d.npy"%phase)
	mean=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/cov/mean%02d.npy"%phase)
	#mean

	#diurnal=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata/anm/anm%02d.npy"%phase)	
	#ir



	print np.shape(mean)
	print np.shape(diurnal)
	######
	#cut
	######
	size1,size2=np.shape(mean)
	mean=mean[1:size1-1,1:size2-1]
	diurnal=diurnal[1:size1-1,1:size2-1]




	#print np.shape(diurnal)
	#print np.shape(mean)
	#x=[[0,1],[2,3]]
	#y=[[1,2],[3,3]]
	#x=np.reshape(x,((1,-1)))
	#y=np.reshape(y,((1,-1)))
	#print np.shape(x)
	#print np.corrcoef(x,y)
	f=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu38/plotdata/fsakuzu%02d.npy"%phase)
	#print np.shape(f)
	


	#print np.shape(f[(f>3.47)])

	f=np.reshape(f,((1,-1)))
	print "f",np.shape(f)
	diurnal=np.reshape(diurnal,((1,-1)))
	print "diurnal",np.shape(diurnal)
	mean=np.reshape(mean,((1,-1)))
	
	cols=np.where(f<3.47)[1]
	#print cols
	diurnal=np.delete(diurnal,cols,1)
	mean=np.delete(mean,cols,1)
	print np.shape(diurnal)
	print np.shape(mean)

	print np.corrcoef(diurnal,mean)
