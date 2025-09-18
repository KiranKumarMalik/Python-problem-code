import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+917848051078")
phone_number2 = phonenumbers.parse("+919348198155")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))