# earth-science-maps

Plot ocean surface temperature

The objective is to plot the ocean surface temperature for the dates:

- 1992-08-16
- 1999-09-08
- 2004-09-05
- 2005-08-23

The data files were downloaded in NetCDF format from NASA's
[OpeNDAP](https://podaac-opendap.jpl.nasa.gov/opendap/allData/ghrsst/data/GDS2/L4/GLOB/CMC/CMC0.2deg/v2/1992/contents.html) repository.

It looks like a good start is supplied by [Hansen Johnson](https://hansenjohnson.org/post/sst-in-r/). 

An example by [Mark Payne](https://rpubs.com/markpayne/358146) is helpful.


The [processNC](https://rdrr.io/github/RS-eco/processNC/f/README.md) package may help.

[Stackoverflow](https://stackoverflow.com/questions/21280104/how-to-take-a-subset-from-a-netcdf-file-using-latitude-longitude-boundaries-in-r) has a decent example.

# More references

- [NWS Environmental Center](https://polar.ncep.noaa.gov/global/examples/usingpython.shtml)

- [Cartopy](https://scitools.org.uk/cartopy/docs/latest/index.html)

- [Matplotlib Base map plotting examples](https://matplotlib.org/basemap/users/examples.html)

- [Matplotlib basemap tookit](https://matplotlib.org/basemap/api/basemap_api.html)

- [Python datetime examples](https://docs.python.org/3/library/datetime.html)

- [Optimmum Interpolation Sea Surface Temperature (OISST)](https://www.ncdc.noaa.gov/oisst)

- [AMS - Daily High-Resolution-Blended Analyses for Sea Surface Temperature](https://journals.ametsoc.org/doi/10.1175/2007JCLI1824.1)

- [get a subset from netcdf in r](https://stackoverflow.com/questions/21280104/how-to-take-a-subset-from-a-netcdf-file-using-latitude-longitude-boundaries-in-r)


 - From [here](https://stackoverflow.com/questions/21280104/how-to-take-a-subset-from-a-netcdf-file-using-latitude-longitude-boundaries-in-r)

> You can also use CDO to extract the area from the bash command line first and
> then read the file in R:
> 
> `cdo sellonlatbox,-5,12,34.5,44.5 in.nc out.nc`
>
> I note in the above discussion that there was a problem concerning the order
> of the latitudes. You can also use the CDO command "invertlat" to sort that
> out for you. (edited Jan 17 '18 at 9:27)

Also

> Cut a regional window using cdo sellonlatbox
> 
> posted Feb 20, 2013, 1:57 AM by gibies george
cdo sellonlatbox,LON1,LON2,LAT1,LAT2 INAME ONAME
> 
> to cut an area deﬁned by
>
> – LON1 and LON2 are the lower and upper longitude of your window
>
> – LAT1 and LAT2 the lower and upper latitiude of your window
> 
> – INAME is your input ﬁlename
> 
> – OUTPUT is your output ﬁlename



- [Data Carpentry R GDAL example](https://datacarpentry.org/r-raster-vector-geospatial/01-raster-structure/index.html) This plots a GeoTIF Raster file


