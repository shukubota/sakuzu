import numpy as np 
import math

a=4.*np.arctan(1.)
#print a


test=np.zeros((2,3))
for i in range(0,2):
    for j in range(0,3):
        test[i][j]=i*10.+j

#print test 
test2=test*test
#print test2
test3=np.sqrt(test2)

print test3
