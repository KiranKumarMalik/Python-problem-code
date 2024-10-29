# Write a program to print all odd numbers between 1 and 11 or given user input by using for loop continue

startRange=int(input("Enter the starting range number: "))
endRange=int(input("Enter the ending range number: "))

for ele in range(startRange, endRange+1):
    if ele % 2 == 0:
        continue # continue skips the even number iteration and execute other iteration
    print(ele)