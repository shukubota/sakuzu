#coding:utf-8

import numpy as np



plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c01.dat",delimiter=",")
#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_no/c01.dat",delimiter=",")
m,n=np.shape(plotdata)

plotdata=np.zeros((m,n))

for phase in range(1,9):
	#plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_no/c"+"%02d"%phase+".dat",delimiter=",")
	plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c_ratio"+"%02d"%phase+".dat",delimiter=",")
	plotdata+=plotcp

plotdata=plotdata/8.


for phase in range(1,9):
	#plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_no/c"+"%02d"%phase+".dat",delimiter=",")
	plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c_ratio"+"%02d"%phase+".dat",delimiter=",")
	plotcp-=plotdata

	#file="/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_no/anmc"+"%02d"%phase+".dat"
	file="/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/anmc_ratio"+"%02d"%phase+".dat"
	np.savetxt(file,plotcp,delimiter=",")
