# Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.)

def print_data_types(elements):
    data_types = [type(element).__name__ for element in elements] # Create a list to store the data types (.__name__: gives you the name of the type as a string)   
    
    print("Data types of list elements:", data_types) # Print the data types

# Given list with elements of different data types
elements = [5, 3.4, 'Kiran', {5, 6, 7}, {'a': 6, 'x': [5, 7, 3]}, [7, 2, 0]]
print(f"Given list: {elements}")
print_data_types(elements)