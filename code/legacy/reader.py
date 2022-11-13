from PIL import Image

days = 171

def color(x, y, a, l1, l2, pix):
    if pix[x,y] == (170, 170, 170) or pix[x,y] == (0,0,0) or pix[x,y] == (255,255,255):
        x1=x+1
        color(x1,y,a,l1,l2,pix)

    elif pix[x,y] == (248, 248, 248) :
        l2.append(0)
    elif pix[x,y] == (220, 220, 250):
        l2.append(0.25)
    elif pix[x,y] == (170, 170, 200):
        l2.append(0.75)
    elif pix[x,y] == (117, 186, 255):
        l2.append(1.5)
    elif pix[x,y] == (53, 154, 255):
        l2.append(2.5)
    elif pix[x,y] == (4, 130, 255):
        l2.append(3.5)
    elif pix[x,y] == (0, 105, 210):
        l2.append(4.5)
    elif pix[x,y] == (0, 79, 157):
        l2.append(6)
    elif pix[x,y] == (0, 50, 127):
        l2.append(8.5)
    elif pix[x,y] == (75, 0, 127):
        l2.append(12.5)
    elif pix[x,y] == (100, 0, 127):
        l2.append(17.5)
    elif pix[x,y] == (145, 0, 187):
        l2.append(25)
    elif pix[x,y] == (194, 0, 251):
        l2.append(35)
    else:
        l2.append(None)

def run(model, l2):
    l1 = []
    a = 0

    #Location
    x=545
    y=359

    while a < days:
        year = 2020
        month = 11
        day = 1

        if(model=="harmonie"):
            z = "0"
            t = "06_"
            folder = "HAR06z"
        elif(model=="swisseu"):
            z = "6"
            t = "00_"
            folder = "SWISS00z"
        else:
            z = "6"
            t = "00_"
            folder = "SWISSEC00z"

        if(a >= 61):
            year = 2021
        if(a < 30):
            month = 11
            day = a+1
        if(a >= 30 and a < 61):
            month = 12
            day=a+1-30
        elif(a >= 61 and a < 92):
            month = 1
            day=a+1-61
        elif(a >= 92 and a < 120):
            month = 2
            day=a+1-92
        elif(a >= 120 and a < 151):
            month = 3
            day=a+1-120
        elif(a >= 151):
            month = 4
            day=a+1-151

        if (day < 10):
            if(month < 10): #Delete -zz for OLD files
                im = Image.open("C:/Users/Maarten/Documents/SRoA/DATA/" + folder +"/xx_model-en-312-0-zz_mod" + model + "_" + str(year) + "0" + str(month) + "0" + str(day) + t + z + "_644_108.png" )
            else:
                im = Image.open("C:/Users/Maarten/Documents/SRoA/DATA/" + folder + "/xx_model-en-312-0-zz_mod" + model + "_" + str(year) + str(month) + "0" + str(day) + t + z + "_644_108.png" )
        else:
            if(month < 10):
                im = Image.open("C:/Users/Maarten/Documents/SRoA/DATA/" + folder + "/xx_model-en-312-0-zz_mod" + model + "_" + str(year) + "0" + str(month) + str(day) + t + z + "_644_108.png" )
            else:
                im = Image.open("C:/Users/Maarten/Documents/SRoA/DATA/" + folder + "/xx_model-en-312-0-zz_mod" + model + "_" + str(year) + str(month) + str(day) + t + z + "_644_108.png" )
        pix = im.load()

        if pix[x,y] == (170, 170, 170) or pix[x,y] == (0,0,0) or pix[x,y] == (255,255,255):
            y1 = y-1
            color(x, y1, a, l1, l2, pix)
        else:
            color(x, y, a, l1, l2, pix)

        a = a+1
    return l2

l2 = []
har = []
eu = []
ec = []

b=0
while b<3:
    if b==0:
        model="harmonie"
    elif b==1:
        model="swisseu"
    else:
        model="ezswiss"
    run(model, l2)

    if b == 0:
        har = l2
    elif b == 1:
        eu = l2
    else:
        ec = l2
    b = b+1

a=0
maxs = 0
cm1days = 0
cm5days = 0
cm10days = 0
cm20days = 0

#Writing to txt file
f = open("C:/Users/Maarten/Documents/SRoA/DATA/data.txt", "w")
while a < days:
    avg = (har[a] + eu[a+days] + ec[a+days*2])/3
    f.write(str(avg) + ", ")
    a = a+1

    if avg >= 1:
        cm1days = cm1days + 1
    if avg >= 5:
        cm5days = cm5days + 1
    if avg >= 10:
        cm10days = cm10days + 1
    if avg >= 20:
        cm20days = cm20days + 1
    if avg > maxs:
        maxs = avg

f.write("\n" + str(cm1days) + "_" + str(cm5days) + "_" + str(cm10days) + "_" + str(cm20days) + "__" + str(maxs)) 
print("DONE")