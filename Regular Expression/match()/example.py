import re
S="A8hduBREw9745"
print(re.match("A",S)) # Match the first character in the string
print(re.match("A8h",S)) # Match the first three characters in the string
print(re.match("h",S)) # No match