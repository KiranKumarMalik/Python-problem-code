# Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines 
# whether it forms an equilateral, isosceles, or scalene triangle.

def sidesOftriangle(a,b,c):
    if a==b==c:
        print("The triangle is Equilateral triangle")
    elif a==b or a==c  or b==c:
        print("The triangle is isosceles triangle")
    elif a != b != c:
        print("The triangle is Scalene triangle")

a=int(input("Enter the first side of the triangle: "))
b=int(input("Enter the second side of the triangle: "))
c=int(input("Eneter the third side of the triangle: "))
sidesOftriangle(a,b,c)