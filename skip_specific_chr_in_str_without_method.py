# Write a program to skip specific character in a string

orgStr=str(input("Enter the Original String: "))
specificCh=str(input("Enter the Specific Character: "))

storeStr=''
for i in orgStr: # i is the characher in orgStr
    if i==specificCh:
      continue
    storeStr=storeStr+i
print(storeStr)