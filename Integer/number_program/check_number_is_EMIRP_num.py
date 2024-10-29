# Write a program to check the input number is EMIRP number or not
#************ Conditions ***********************
# Given number should not be palindrome
# Number should be Prime number
# Reverse of the number is also prime number

num=int(input("Enter a number: "))
dup=num
res=0
while num > 0:
    ld=num%10
    res=res*10+ld
    num=num//10
if res!=dup:
    if dup>1:
        for val in range(2, dup//2+1):
            if num%val==0:
                print(f"{num} is not EMIRP number")
                break
        else:
            if res>1:
                for val in range(2,res//2+1):
                    if res%val==0:
                        print("The number is not a EMIRP number")
                        break
                else:
                    print("The number is EMIRP number")
            else:
                print("The number is not EMIRP number")
    else:
        print("The number is not a EMIRP number")
else:
    print("The number is not a EMIRP number")