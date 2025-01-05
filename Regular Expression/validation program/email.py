import re
S="malikkiran413@gmail.com"
if re.match("^[a-zA-Z0-9._-]+@gmail[.]com$",S) and (".." not in S) and ("__" not in S) and ("--" not in S):
    print("Valid Email")
else:
    print("Invalid Email")