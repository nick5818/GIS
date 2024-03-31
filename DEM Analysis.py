import rasterio
import richdem as rd
import matplotlib.pyplot as plt

#wrk = "C:\Users\user\Desktop\eu_dem_v11_E10N10"
dem = rasterio.open("Samos-DEM-eudem-5deg.tif")

dem.count
dem.crs
dem.bounds

# rasterio.plot.show(dem, cmap = 'terrain_r')

# dem to array
dem_1 = dem.read(1).astype('float64')

# dem to richdem array
dem_rich = rd.rdarray(dem_1, no_data=-9999)

# plot it with richdem
rd.rdShow(dem_rich, axes = False, cmap = 'terrain_r')

# create slope layer
slope = rd.TerrainAttribute(dem_rich, attrib='slope_degrees')
rd.rdShow(slope, axes = False, cmap = 'YlOrBr') #plot 

aspect = rd.TerrainAttribute(dem_rich, attrib='aspect')
rd.rdShow(aspect, axes = False, cmap = 'terrain') #plot

slope.max()
aspect.max()
dem_rich.max()


import numpy as np

dem_re = dem.read()


dlst = dem_re.copy()

dem_re.min()
dem_re.max()
dlst[np.where((dlst >= -1.85) & (dlst <= 1))] = 0
dlst[np.where((dlst >= 1) & (dlst <= 200))] = 1
dlst[np.where((dlst >= 200) & (dlst <= 400))] = 2
dlst[np.where((dlst >= 400) & (dlst <= 600))] = 3
dlst[np.where((dlst >= 600) & (dlst <= 800))] = 4
dlst[np.where((dlst >= 800) & (dlst <= 1000))] = 5
dlst[np.where((dlst >= 1000) & (dlst <= 1200))] = 6
dlst[np.where((dlst >= 1200) & (dlst <= 1400))] = 7
dlst[np.where((dlst >= 1400) & (dlst <= 1416.29))] = 8


with rasterio.open('dem_re5.tif', 'w', 
                   driver = dem.driver,
                   width = dem.width,
                   height = dem.height,
                   count = dem.count,
                   crs = dem.crs,
                   transform = dem.transform,
                   dtype = dem_re.dtype
) as dst: 
    dst.write(dlst)

dem_rec = rasterio.open('dem_re5.tif')

demre = dem_rec.read(1).astype('float64')
demre = rd.rdarray(demre, no_data=-9999)
rd.rdShow(demre, axes = False, cmap = 'terrain_r', vmin = 0, vmax = 8)








