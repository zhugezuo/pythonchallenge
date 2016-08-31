from PIL import Image
im = Image.open('cave.jpg')
w = im.size[0] // 2
h = im.size[1] // 2

oo = ee = oe = eo = Image.new(im.mode,(w,h))
for x in range(2*w):
    for y in range(2*h):
        oo.putpixel((x//2,y//2),im.getpixel((x, y)))
        ee.putpixel((x//2,y//2),im.getpixel((x, y)))


