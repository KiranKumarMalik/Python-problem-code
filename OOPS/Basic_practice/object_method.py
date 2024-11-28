class c203:
    course="PFS"
    Bcode="M17"
    timings="4:00 PM"
    def __init__(self,name,mobno,Aadhar):
        self.Name=name
        self.Mobileno=mobno
        self.Aadharno=Aadhar
    def Details(self):
        print(f"Name: {self.Name}")
        print(f"Mobile Number: {self.Mobileno}")
        print(f"Aadhaar Number: {self.Aadharno}")
obj1=c203("Kiran", 6579464764687, 316449499664)
obj2=c203("Subham",36566643516,26797984914666446)
# Accessing using object name
obj1.Details()
print("________________________________________")
# Modifying object variables
obj1.Name="Chiku"
# Accessing using class name
c203.Details(obj1)