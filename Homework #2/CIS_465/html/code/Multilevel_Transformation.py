from PIL import Image

im = Image.open('lena_g.jpg')
im_new = im
width, height = im.size

for w in range(width):
    for h in range(height):
        r, g, b = im.getpixel((w, h))

        r_new = r
        g_new = g
        b_new = b

        if r < 50:
            r_new = 0
        elif r >= 50 or r <= 200:
            r_new = r
        elif r > 200:
            r_new = 0

        if g < 50:
            g_new = 0
        elif g >= 50 or g <= 200:
            g_new = g
        elif g > 200:
            g_new = 0

        if b < 50:
            b_new = 0
        elif b >= 50 or b <= 200:
            b_new = b
        elif b > 200:
            b_new = 0

        im_new.putpixel((w, h), (int(r_new), int(g_new), int(b_new)))

im_new.show()