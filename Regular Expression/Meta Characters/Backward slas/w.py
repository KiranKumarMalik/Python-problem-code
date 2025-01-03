import re
S="a@$b1 2AB_# 42R"
print(re.findall("\w",S))  # \w: This expression matches the alphanumeric character in the string.