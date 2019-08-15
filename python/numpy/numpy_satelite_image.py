import numpy as np
import scipy
import matplotlib.pyplot as plt
from skimage import data

# photo_data = plt.imread('D:/ex/python4ds/wifire/sd-3layers.jpg')
# type(photo_data)

# plt.figure(figsize=(15,15))
#plt.imshow(photo_data)
# photo_data.shape

# photo_data[150, 250] = 0
# plt.figure(figsize=(10,10))
# plt.imshow(photo_data)

# photo_data[200:800, : ,1] = 255
# plt.figure(figsize=(10,10))
# imgplot=plt.imshow(photo_data)

photo_data = plt.imread('D:/ex/python4ds/wifire/sd-3layers.jpg')
photo_copy = photo_data.copy()
print("Shape of photo_data:", photo_copy.shape)
low_value_filter = photo_data < 200
print("Shape of low_value_filter:", low_value_filter.shape)
plt.figure(figsize=(10,10))
plt.imshow(photo_copy)
photo_copy[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_copy)
plt.show()