import matplotlib.pyplot as plt
import statistics
from PIL import Image
import numpy as np

#read in image
im = Image.open('Project-Data/lena.png')
im_g = im
im_g.show()

#variables for future use
width, height = im_g.size
totalPixels = width*height
num_bins = 256
hist = [0 for x in range(totalPixels)]
iterator = 0
values = [0 for x in range(256)]

#Otsu uses gray-scale images as a base so creating a copy of the image in grey-scale
for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))
        avg = (0.21*r + 0.72*g + 0.07*b)
        im_g.putpixel((w, h), (int(avg), int(avg), int(avg)))

im_g.show()
iterator = 0

#Apply a mean smoothing filter to the image
for w in range(width):
    for h in range(height):
        average = [0 for x in range(9)]
        for kernelW in range(3):
            for kernelH in range(3):
                try:
                    average[iterator], null, null = im_g.getpixel((w-1+kernelW, h-1+kernelH))
                except IndexError:
                    average[iterator] = 0
                iterator = iterator + 1
        iterator = 0
        avg = statistics.mean(average)
        im_g.putpixel((w, h), (int(avg), int(avg), int(avg)))
im_g.show()
iterator = 0

#make a histogram from the image post-smoothing
for w in range(width):
    for h in range(height):
        avg, null, null = im_g.getpixel((w, h))
        hist[iterator] = avg
        values[int(avg)] = values[int(avg)] + 1
        iterator = iterator + 1

n, bins, patches = plt.hist(hist, num_bins, facecolor='blue', alpha=0.5)
plt.show()
maxVal = -999
threshold = -999
#Next we find the threshold value
for t in range(1, 255):
    w0 = 0
    w1 = 0
    temp0 = 0
    temp1 = 0
    for x in range(t):
        w0 = values[x] + w0
    w0 = w0/totalPixels
    w1 = 1-w0
    for x in range(t):
        temp0 = temp0 + values[x]*x
    ut = temp0/totalPixels
    for x in range(256):
        temp1 = temp1 + values[x]*x
    uT = temp1/totalPixels
    u0 = ut/(w0+.000001)
    u1 = (uT-ut)/(1-w0+.000001)
    classVar = (w0*w1)*((u1-u0)**2)
    totalVar = 0
    for x in range(255):
        totalVar = totalVar + (((x-uT)**2)*values[x])
    totalVar = totalVar/totalPixels
    curMax = classVar/totalVar
    if curMax > maxVal:
        maxVal = curMax
        threshold = t

for w in range(width):
    for h in range(height):
        avg, null, null = im_g.getpixel((w, h))
        if avg > threshold:
            im_g.putpixel((w, h), (255, 255, 255))
        elif avg < threshold:
            im_g.putpixel((w, h), (0, 0, 0))
im_g.show()