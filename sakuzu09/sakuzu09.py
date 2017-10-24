#coding:utf-8

import numpy as np
from sakuzu09sub1 import *


filename='/media/kubotashu/HDPC-UT/data/07/01/gsmap_mvk.20090701.0000.v5.222.1.dat'
import numpy as np
import os.path

head='/media/kubotashu/HDPC-UT/data/'
mid='/gsmap_mvk.2009'
tail='00.v5.222.1.dat'

for i in range(0,33):
    day='%02d'%(i+1)
    for j in range(0,24):
        hour='%02d'%j
        name=head+str(mon)+'/'+str(day)+mid+str(mon)+str(day)+'.'+hour+tail
        

        if os.path.isfile(name):

            print name
