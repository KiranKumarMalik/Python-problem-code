def volume_of_cube(side_of_cube):
    return side_of_cube ** 3

def volume_of_cuboid(length, bredth, height):
    return length * bredth * height

def volume_of_cylinder(diameter, height):
    return 22/7 * diameter//2 ** 2 * height

def volume_of_sphere(diameter):
    return 4/3 * 22/7 * diameter//2 ** 3

# Dimensions of cube
side_of_cube = int(input(f"Enter the side of cube: "))
print(f"Volume of cube {volume_of_cube(side_of_cube)}")

#Dimensions of cuboid
length = int(input(f"Enter the length of cuboid: "))
bredth = int(input(f"Enter bredth of cuboid: "))
height = int(input(f"Enter height of cuboid: "))
print(f"Volume of cuboid {volume_of_cuboid(length, bredth, height)}")

#Dimensions of cylinder
diameter = int(input(f"Enter the radius of a cylinder: "))
height = int(input(f"Enter the height of cylinder: "))
print(f"Volume of a cylinder: {volume_of_cylinder(diameter, height)}")

#Dimensions of sphere
diameter=int(input("Enter the radius of the sphere: "))
print("Volume of the sphere: ", volume_of_sphere(diameter))
