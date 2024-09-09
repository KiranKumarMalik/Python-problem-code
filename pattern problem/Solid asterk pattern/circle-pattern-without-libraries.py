diameter = int(input("Enter the diameter of the circle: "))

radius = diameter / 2 - .5  # subtracting .5 to make the circle look more circular
r = (radius + .25)**2 + 1   # adding .25 to make the circle look more circular and r is the square of the radius

result = ''

for i in range(diameter): 
    y = (i - radius)**2 # y is the square of the radius
    for j in range(diameter): # j is the diameter
        x = (j - radius)**2 # x is the square of the radius
        if x + y <= r: 
            result = result + '*  ' 
        else:
            result = result + '   '
    result = result + '\n' # \n is used to print the next line
print(result)

result = result.split('\n')[:-1]    # split the result by '\n' and remove the last element
pixels_per_line = [x.count('*') for x in result]  # count the number of '*' in each line

print(f'The pixels per line are {pixels_per_line}.')