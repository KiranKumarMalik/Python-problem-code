class kiran(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    raise kiran("No QR code")
except kiran as msg:
    print(f"Kiran: {msg}")