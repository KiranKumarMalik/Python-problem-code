# load(): This method is used to convert JSON object into Python data with the help of file object.
# Syntax: json.load(file_object)
# No need of reading the content of the file. It will automatically read the content of the file.

import json
with open('details.json','r') as fobj:
    pydata=json.load(fobj)
    print(pydata)
    print(type(pydata))