import re
S="h hp heep heeep heeeep"
print(re.findall("^h",S)) # ^: This method is used to check if the string starts with a certain character.
print(re.findall("^e",S))