import rasterio
import matplotlib.pyplot as plt
from rasterio.plot import show, show_hist
import numpy as np

# load the tif, img file
img_dir = r'AC-GC-TC-85.img' # set directory
img = rasterio.open(img_dir) # open thorugh it

# read image data (array)
data = img.read()

# read metadata (crs, width/height etc.)
img.meta

# acquire metadata separately
img.name
img.shape
img.count # bands
img.driver # filetype
img.crs
img.transform
img.descriptions # shows different bands

# info for the dataset
data.size
data.max()
data.min()
data.dtype

# Visualize with rasterio
show(img)

# cmap = matplotlib colormaps
show(img, cmap='Spectral') 
show(img, cmap = 'terrain')

# add text
show(img, cmap = 'terrain_r', title = 'Island of Thasos')
plt.colorbar()
# histogram
show_hist(img, bins=50, title='Pixel values')
rasterio.plot.show_hist(img, bins=100, title='Pixel values', histtype='stepfilled', lw=0.0, stacked=False, alpha=0.3)

# plot different bands in one plot (subplots)
band_4 = img.read(4)
band_3 = img.read(3)
band_2 = img.read(2)

fig = fig = plt.figure(figsize=(10, 10)) # set frame for the plot
ax1 = fig.add_subplot(2,2,1) # last number indicates position from left to right
ax1.imshow(band_2)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(band_3)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(band_4)         # subplots

# Calculate NDVI
# 1st assign the bands
# !WE READ THE DATASET NOT THE IMAGE!
red = data[3].astype('f4') # f4 = float32
nir = data[4].astype('f4')
ndvi = (nir - red)/(nir + red)
plt.imshow(ndvi, cmap='terrain_r')
plt.colorbar()
show_hist(ndvi, bins=20, title = 'NDVI values')
rasterio.plot.show_hist(ndvi, bins=50, title='NDVI values', histtype='stepfilled', lw=0.0, stacked=False, alpha=0.3)

# plot map and graph
fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14,7))
show(ndvi, ax=axrgb)
show_hist(ndvi, bins=50, histtype='stepfilled', lw=0.0, stacked=False, alpha=0.3, ax=axhist)
plt.show()

# assign values to NoValue data
# we use numpy
img_2 = np.divide(np.subtract(nir, red), np.add(nir, red)) # (should be checked)
img_3 = np.nan_to_num(img_2, nan=-1)
plt.imshow(img_3, cmap='viridis')
plt.colorbar()


# write file, with all details (crs, width, height etc)
with rasterio.open('ndvi.tif', 'w', driver = img.driver, width = img.width, 
                   height = img.height, count = img.count, transform = img.transform,
                   dtype = data.dtype,  ) as dst: 
    dst.write(ndvi)







