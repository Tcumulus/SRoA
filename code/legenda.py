from PIL import Image

im = Image.open('./data/callib2.png')
pix = im.load()
print(pix[10,10]) #sea
print(pix[20,680]) #<0.1
print(pix[50,680]) #0.1-0.5
print(pix[80,680]) #0.5-1
print(pix[110,680]) #1-2
print(pix[150,680]) #2-3
print(pix[180,680]) #3-4
print(pix[210,680]) #4-5
print(pix[240,680]) #5-7
print(pix[270,680]) #7-10
print(pix[300,680]) #10-15
print(pix[330,680]) #15-20
print(pix[370,680]) #20-30
print(pix[400,680]) #30-40

print(pix[564,312]) #LINE
print(pix[572,299]) #NUMBWHITE
print(pix[573,297]) #NUMBBLACK
