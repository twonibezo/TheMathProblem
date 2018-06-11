arrayX = list(range(-30,31))
arrayY = list(range(-30,31))
arrayZ = list(range(-30,31))

x = y = z = 0
a = 0
count = 0

while a < 61:
    count = arrayX[x+1] + arrayY[y+1] + arrayZ[z+1]
    a = a+1
    x = x + 1
    y = y + 1
    z = z + 1
    if count >= 0:
        print (count)