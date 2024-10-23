# Write a python program to check the number is facinating number or not
#   let num=192
#       192*1=192
#       192*2=384
#       192*3=576
#     In above products from 1 to 9 are available 192384576
num=int(input("Enter the number: "))
ans=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in ans:
        print(f"{num} is not a facinating number")
        break
else:
    print(f"{num} is a facinating number")