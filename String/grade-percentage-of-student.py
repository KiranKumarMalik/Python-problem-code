# Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade 
# according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

def grade_percentage(percentage):
    if percentage>=90:
        print(f"Your grade is A+")
    elif percentage>=80:
        print(f"Your grade is A")
    elif percentage>=70:
        print(f"Your grade is B")
    elif percentage>=60:
        print(f"Your grade is C")
    elif percentage<60:
        print(f"Fail")

percentage=float(input("Enter the percentage of student: "))
grade_percentage(percentage)
