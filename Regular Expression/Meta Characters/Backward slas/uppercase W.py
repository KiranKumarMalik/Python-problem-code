import re
S="a@$b1 2AB_# 42R"
print(re.findall("\W",S))  # \W: This expression matches any non-alphanumeric character.