import numpy as np
import scipy
import matplotlib.pyplot as plt
from skimage import data

photo_data = plt.imread('D:/ex/python4ds/wifire/sd-3layers.jpg')
type(photo_data)

plt.figure(figsize=(15,15))
plt.imshow(photo_data)
photo_data.shape