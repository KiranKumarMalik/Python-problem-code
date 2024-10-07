# Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

celcius=float(input("Enter temperature in celcius: "))
fahrenheit=(celcius*9/5)+32   # “F = (C * 9/5) + 32″ AND  “C = (F – 32)/1.8“
print("Temoerature in fahernheit is:", fahrenheit)
