import numpy as np



f=open("nradate.txt","w")

for i in range(2007,2014):
	for j in range(6,9):
		for k in range(1,32):
			date="%04d"%i+"%02d"%j+"%02d"%k
			f.write(date)
			f.write("\n")

f.close()

