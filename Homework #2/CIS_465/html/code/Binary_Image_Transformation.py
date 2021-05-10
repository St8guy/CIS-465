from PIL import Image

im = Image.open('csu_g.jpg')
im_new = im
width, height = im.size

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))

        r_new = r
        g_new = g
        b_new = b

        if r < 200:
            r_new = 0
        elif r >= 200:
            r_new = 255 - r

        if g < 200:
            g_new = 0
        elif g >= 200:
            g_new = 255 - g

        if b < 200:
            b_new = 0
        elif b >= 200:
            b_new = 255 - b

        im_new.putpixel((w, h), (int(r_new), int(g_new), int(b_new)))

im_new.show()
