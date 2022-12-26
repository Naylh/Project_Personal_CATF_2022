#substract the image deformed from the original image and if the pixel is not black then change it to white

from PIL import Image

img1 = Image.open("original.png")
img2 = Image.open("Beautiful_Building.png")

img1 = img1.convert("RGB")
img2 = img2.convert("RGB")

width, height = img2.size

for x in range(width):
    for y in range(height):
        r1, g1, b1 = img1.getpixel((x, y))
        r2, g2, b2 = img2.getpixel((x, y))
        #print(r1, g1, b1)

        #if the values of rgb are different then change the pixel to white
        if r1 != r2 or g1 != g2 or b1 != b2:
            img1.putpixel((x, y), (255, 255, 255))
        else : 
            img1.putpixel((x, y), (0, 0, 0))

img1.save("flag.png")
