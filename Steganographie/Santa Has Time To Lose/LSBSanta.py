from PIL import Image

im = Image.open("test.png")

res = Image.new("RGB", (4, im.size[1]), (255, 255, 255))

cols = ""
for y in range(im.size[1]):
    for i in range(4):
        if im.getpixel((0, y))[i] == 255:
            cols += "1" 
        else:
            cols += "0"
print(len(cols))

n = 8
print("".join([chr(int(cols[i:i+n], 2)) for i in range(0, len(cols), n)]))