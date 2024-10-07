# Write a program to skip specific character in a string with method

orgStr=str(input("Enter the Original String: "))
specificCh=str(input("Enter the Specific Character: "))

storeStr=[]
for i in orgStr:
    if i==specificCh:
      continue
    storeStr.append(i)
print(storeStr)