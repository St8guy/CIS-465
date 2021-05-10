import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from PIL import Image

num_bins = 256
im = Image.open('csu_01.jpg')
width, height = im.size
size = width * height
array = [0 for x in range(size)]
iterator = 0

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))
        avg = (r + g + b) / 3
        array[iterator] = avg
        iterator = iterator + 1


n, bins, patches = plt.hist(array, num_bins, facecolor='blue', alpha=0.5)
plt.show()
