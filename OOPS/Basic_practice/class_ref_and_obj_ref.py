class Room203:
    Course="Python Full Stack"
    Bcode="M17"
    timings='4:30 PM'
Kiran=Room203()
Chiku=Room203()
Subha=Room203()

Chiku.Course="Java Full Stack"
Subha.Bcode="J18"
# Accessing using Class references
print(Room203.Course)
print(Room203.Bcode)
print(Room203.timings)

# Accessing using Object references
print(Kiran.Course,Kiran.Bcode,Kiran.timings)
print(Chiku.Course,Chiku.Bcode,Chiku.timings)
print(Subha.Course,Subha.Bcode,Subha.timings)