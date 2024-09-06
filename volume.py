def volume_of_cube(side_of_cube):
    return side_of_cube ** 3

def volume_of_cuboid(length, bredth, height):
    return length * bredth * height

def volume_of_cylinder(radius, height):
    return 22/7 * radius ** 2 * height

def volume_of_sphere(radius):
    return 4/3 * 22/7 * radius ** 3

# Dimensions of cube
side_of_cube = int(input(f"Enter the side of cube: "))
print(f"Volume of cube {volume_of_cube(side_of_cube)}")

length = int(input(f"Enter the length of cuboid: "))
bredth = int(input(f"Enter bredth of cuboid: "))
height = int(input(f"Entyer height of cuboid: "))
print(f"Volume of cuboid {volume_of_cuboid(length, bredth, height)}")

radius = int(input(f"Enter the radius of a circle: "))
height = int(input(f"Enter the height of circle: "))
print(f"Volume of a cylinder: {volume_of_cylinder(radius, height)}")
