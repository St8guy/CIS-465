from PIL import Image

im = Image.open('lena_g.jpg')
im_new = im
width, height = im.size

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))

        r_new = 255 - r
        g_new = 255 - g
        b_new = 255 - b

        im_new.putpixel((w, h), (int(r_new), int(g_new), int(b_new)))

im_new.show()
