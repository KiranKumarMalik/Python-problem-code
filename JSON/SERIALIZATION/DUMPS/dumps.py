# dumps(): This method is used to convert python data into JSON formatted data.
# Syntax: json.dumps(data,indent=4)
# data: The data which needs to be converted into JSON format.
# indent: It is used to define the number of spaces for indentation.
# We can covert any type of python data into JSON format using dumps() method except complex and set data types.
# dumps() method returns JSON object as a string.
import json
D={'Name':'Kiran','Age':22,'City':'Bhubaneswar','Country':'India'}
with open('details.json','w') as fobj:
    content=json.dumps(D,indent=4)
    fobj.write(content)