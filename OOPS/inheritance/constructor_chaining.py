class BV1:
    def __init__(self,name,mob):
        self.name=name
        self.mob=mob
class BV2(BV1):
    def __init__(self,name,mob,aadhar,PAN):
        super().__init__(name,mob)
        self.Aadhar=aadhar
        self.PAN=PAN
obj=BV2("King",8657469644,31662659844849,'GKTY8752Y')
print(obj.PAN)
