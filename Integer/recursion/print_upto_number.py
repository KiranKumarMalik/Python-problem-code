# Write a recursion function to print from 1 to 10
def Sample(num):
    if num==11:
        return
    print(num)
    Sample(num+1)
num=int(input("Enter a number: "))
Sample(1)