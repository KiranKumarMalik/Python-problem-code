# Write a program to print the range of element using while loop

num=int(input("Enter the number of natural number: "))
val=1                      # Initialize the value to 1
while val<num:             # Given the condition that value will be less then num upto num, if num=5, then val=1,2,3,4
    print(val, end=" ")    # To print the values in the same line I use end=" " 
    val=val+1              # Increment the value by 1