import numpy as np




plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/00.dat")
countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count00.dat")
plotdata=plotdata*0.
countdata=countdata*0.

for i in range(0,24):
	plotdata+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/%02d.dat"%i)
	countdata+=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/count%02d.dat"%i)
	
plotdata=plotdata/countdata

np.savetxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/nradata/month.dat",plotdata)



