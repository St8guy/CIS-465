import numpy as np
from PIL import Image
import math

im = Image.open('csu_g.jpg')
im_new = im
width, height = im.size

#n will vary
n = 10
C = np.max(im)/(math.pow(np.max(im), n))

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))

        r_new = C*math.pow(r, n)
        g_new = C*math.pow(g, n)
        b_new = C*math.pow(b, n)

        im_new.putpixel((w, h), (int(r_new), int(g_new), int(b_new)))

im_new.show()