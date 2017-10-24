import numpy as np


local=8


plotdataasa=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/00.dat")
countdataasa=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count00.dat")
plotdatayoru=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/00.dat")
countdatayoru=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count00.dat")
plotdataasa=plotdataasa*0.
plotdatayoru=plotdatayoru*0.
countdataasa=countdataasa*0.
countdatayoru=countdatayoru*0.

for i in range(0,24):
	if (i+local)%24<12:
		plotdataasa+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/%02d.dat"%i)
		countdataasa+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count%02d.dat"%i)
	else:
		plotdatayoru+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/%02d.dat"%i)
		countdatayoru+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count%02d.dat"%i)
	

np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/asa.dat",plotdataasa)
np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/yoru.dat",plotdatayoru)


np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/countasa.dat",countdataasa)
np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/countyoru.dat",countdatayoru)

