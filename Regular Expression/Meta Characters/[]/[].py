import re
S="abc.3.2.11.fde"
print(re.findall("[.]",S)) # [.] : This expression matches any character except a newline.
print(re.findall("[3]",S)) # [3] : This expression matches the digit 3 in the string.
print(re.findall("[13]",S)) # [13] : This expression matches the digit 1 or 3 in the string.