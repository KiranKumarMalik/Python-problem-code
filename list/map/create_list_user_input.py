# Create a map fuctions which takes user input elements and separated with spaces to create a list
#   Enter list elements: 5 7 9
#   [5, 7, 9]
print(list(map(int,input("Enter list elements: ").split())))