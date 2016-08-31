import urllib.request,io
from PIL import Image

img = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
im = Image.open(io.BytesIO(img))

print(im.size)
for y in range(95):
    for x in range(629):
        r,g,b,a = im.getpixel((x, y))
        if ((r==g) & (g==b)):
            print((x,y),[r,g,b,a])


w,h=im.size
print(''.join([chr(im.getpixel((i, h // 2))[0]) for i in range(0, w, 7)]))
print(chr(105)+chr(110)+chr(116)+chr(101)+chr(103)+chr(114)+chr(105)+chr(116)+chr(121))