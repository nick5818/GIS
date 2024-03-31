import rasterio
import numpy as np
from rasterio.plot import show
import matplotlib.pyplot as plt
from matplotlib import pyplot

# read tif file and its data seperately
dem = rasterio.open('DEM_all.tif') 
data = dem.read()

# define min, max
data.max()    
data.min()    

# make a copy of the dataset
lst = data.copy()

# reclassify (np.where)
lst[np.where((lst >= -15) & (lst <= 500))] = 1 
lst[np.where((lst >= 500) & (lst <= 1000))] = 2
lst[np.where((lst >= 1000) & (lst <= 1500))] = 3
lst[np.where((lst >= 1500) & (lst <= 1800))] = 4
lst[np.where((lst >= 1800) & (lst <= 2336))] = 5

# write the file
with rasterio.open('dem_re3.tif', 'w', 
                   driver = dem.driver,
                   width = dem.width,
                   height = dem.height,
                   count = dem.count,
                   crs = dem.crs,
                   transform = dem.transform,
                   dtype = data.dtype
) as dst: 
    dst.write(lst)

rec_dem = rasterio.open('dem_re3.tif')

# plot with rasterio
show(rec_dem) # simple
show(rec_dem, cmap = 'terrain_r', title = 'Chelmos Geopark Elevation') # with title, legend etc.










