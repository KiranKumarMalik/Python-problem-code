import re
S="+91-7848051078"
if re.match('^([+]91( |-))?[6-9][0-9]{9}$',S):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")