# Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

def is_vowel(S):
    if S in "aeiouAEIOU":
        print(f"{S} is a vowel")
    else:
        print(f"{S} is a consonant")

S=str(input("Enter the character: "))
len(S)==1
is_vowel(S)