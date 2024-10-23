# Write a recursion function to convert Integer number to binary number
def convertToBinary(num):
   if num == 0:
       return 0
   return (num % 2 + 10 * convertToBinary(num // 2))

# decimal number
IntegerNum = int(input("Enter a number: "))
print(f"Binary number of {IntegerNum} is {convertToBinary(IntegerNum)}")
