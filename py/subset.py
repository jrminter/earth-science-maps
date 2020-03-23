# use 'orthogonal indexing' feature to subselect data over CONUS.
import netCDF4
import numpy as np
import matplotlib.pyplot as plt

# use real data from CFS reanlysis.
# note:  we're reading GRIB2 data!
# URL="http://nomads.ncdc.noaa.gov/thredds/dodsC/modeldata/cmd_flxf/2010/201007/20100701/flxf00.gdas.2010070100.grb2"
URL = "/Users/jrminter/Documents/git/earth-science-maps/data/netcdf/19920816.nc"
nc = netCDF4.Dataset(URL)
lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
# time = nc.variables(nc, "time")
latselect = np.logical_and(lat>25,lat<50)
lonselect = np.logical_and(lon>230,lon<305)
data = nc.variables['analysed_sst'][0,0,latselect,lonselect]
# plt.contourf(data[::-1]) # flip latitudes so they go south -> north
# plt.show()