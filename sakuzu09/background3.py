from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
#m = Basemap(width=12000000,height=9000000,projection='lcc', resolution=None,lat_1=-40.,lat_2=0,lat_0=0,lon_0=0.)

lon1=0.05
lon2=360.05
lat1=-59.95
lat2=60.05
#m = Basemap(width=12000000,height=9000000,projection='merc',resolution=None,lat_1=lat1,lat_2=lat2,lon_1=lon1,lon_2=lon2)
m = Basemap(projection='merc', llcrnrlat=lat1, urcrnrlat=lat2-0.05,llcrnrlon=lon1, urcrnrlon=lon2-0.05, resolution='c')

m.bluemarble()
plt.show()
