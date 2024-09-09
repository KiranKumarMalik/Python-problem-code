import math
radius = 12
for i in range(-radius,radius+1):
    for j in range(-radius, radius +1):
        if math.sqrt(i**2 + j**2) <= radius:
            print("*",end = " ")
        else:
            print(" ", end = ' ')
    print()