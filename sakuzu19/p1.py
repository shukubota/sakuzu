#coding:utf-8
import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob

if __name__ == '__main__':
    start = time.time()

#########################
lon1=90
lon2=160
lat1=-15
lat2=10
grid=1.
##############################

lonsize=int((lon2-lon1)/grid)+1
latsize=int((lat2-lat1)/grid)+1
level=80
slev=79  #調べたい高度0-79 79が地表


plotdata=np.zeros((24,level,lonsize,latsize))
count=np.zeros((24,level,lonsize,latsize))
print np.shape(plotdata)
#print len(plotdata),len(plotdata[0]),len(plotdata[0][0]),len(plotdata[0][0][0])
    

#list=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/2A25.1997120*")
list=glob.glob("/media/kubotashu/strage/data_mjo/p1/2A25.19990226.07177*")
print list
print len(list)




for i in range(0,len(list)):
    #command="gunzip "+list[i]
    #os.system(command)
    #list2=glob.glob("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/*.HDF")
    filename=list[i]
    print filename
    hdf=SD(filename,SDC.READ)
    ####################################
    #e_surfrain
    #################################
    #data3D=hdf.select('e_SurfRain')
    #data=data3D[:,:]
    #########################################
    #rain levelも含んでいる
    #############################
    
    data3D=hdf.select('rain')
    data=data3D[:,:,:]
    #print np.shape(data)
    ##############################

    lat=hdf.select('Latitude')
    latitude=lat[:,:]
    lon = hdf.select('Longitude')
    longitude = lon[:,:]
    Hour=hdf.select('Hour')
    hour=Hour[:]

    ##############confirmation#############
    #print np.shape(hour)
    #print hour
    #print np.shape(longitude)
    #print longitude
    #print np.shape(latitude)
    #print np.shape(data)
    ##################################

    for p in range(79,level):
        for j in range(0,len(longitude)):
            for k in range(0,len(longitude[0])):
                if(longitude[j][k]>=lon1-0.5*grid and longitude[j][k]<lon2+0.5*grid):
                    if (data[j][k][p]>0.):
                        m=int((longitude[j][k]+0.5*grid-lon1)/grid)
                        n=int((latitude[j][k]+0.5*grid-lat1)/grid)

                        for l in range(0,24):
                            if (hour[j]==l):
                                #plotdata[l][p][m][n]+=data[j][k]    #e_surf
                                plotdata[l][p][m][n]+=data[j][k][p] #rain
                                count[l][p][m][n]+=1
        print p



count[count==0.]=1
plotdata=plotdata/count
print np.shape(count)
#print len(plotdata[0][slev]),len(plotdata[0][slev][0])

for l in range(0,24):
    phase="%02d"%l
    name="/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/result/utc"+phase+".dat"
    filename=open(name,"w")
    for a in range(0,len(plotdata[0][slev])):
        for b in range(0,len(plotdata[0][slev][0])):
            filename.write(str(int(plotdata[l][slev][a][b]))+" ")
    
        filename.write("\n")
    filename.close()






#command="gzip /home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu19/data/*.HDF"
#os.system(command)




elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
