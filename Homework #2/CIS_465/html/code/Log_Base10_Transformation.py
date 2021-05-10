import numpy as np
from PIL import Image

im = Image.open('lena_g.jpg')
im_new = im
width, height = im.size
C = 255/np.log(1 + np.max(im))

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))

        r_new = C*np.log(1 + r)
        g_new = C*np.log(1 + g)
        b_new = C*np.log(1 + b)

        im_new.putpixel((w, h), (int(r_new), int(g_new), int(b_new)))

im_new.show()