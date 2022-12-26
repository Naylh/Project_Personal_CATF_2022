#hide the qrcode into the original.png by changing the rgb value of the pixel of original.png

from PIL import Image


img1 = Image.open("original.png")
img2 = Image.open("QRCode.png")

img1 = img1.convert("RGB")
img2 = img2.convert("RGB")

width, height = img2.size

for x in range(width):
    for y in range(height):
        r1, g1, b1 = img1.getpixel((x, y))
        r2, g2, b2 = img2.getpixel((x, y))

        #if the pixel of the qrcode is black then change the rgb value by adding 3
        if r2 == 0 and g2 == 0 and b2 == 0:
            r1 += 3
            g1 += 3
            b1 += 3

        img1.putpixel((x, y), (r1, g1, b1))

img1.save("test.png")
