"""
CTI-110 - P3LAB1 - Letter Grade Branching
Name: Ayinga Kassim Mohammed
Major: Cybersecurity
Date: Fall 2026
"""


print("CTI-110 P3LAB1 - Ayinga Kassim Mohammed")


# Get grade from user
grade = float(input("Enter a grade (0-100): "))


# Branching - check grade
if grade >= 90 and grade <= 100:
    print("Your grade is: A")
elif grade >= 80 and grade <= 89:
    print("Your grade is: B")
elif grade >= 70 and grade <= 79:
    print("Your grade is: C")
elif grade >= 60 and grade <= 69:
    print("Your grade is: D")
elif grade >= 0 and grade <= 59:
    print("Your grade is: F")
else:
    print("Invalid grade - must be between 0 and 100")