import re
S="a@$b1 2AB_# 42R"
print(re.findall("\S",S))  # \S: This expression is used to check if the string contains any non-white space character.