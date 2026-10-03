"""
CTI-110 - P2HW1 - Test Average
Name: Ayinga Kassim Mohammed
Major: Cybersecurity
Date: Fall 2026
"""


print("CTI-110 P2HW1 - Ayinga Kassim Mohammed")
print("Cybersecurity Major")
print("--------------------------------------")


# Get grades for 6 modules
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))


# Put grades in a list to find low/high
grades = [grade1, grade2, grade3, grade4, grade5, grade6]


lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)


# Display results
print("\n------------Results------------")
print(f"Lowest Grade:  {lowest}")
print(f"Highest Grade: {highest}")
print(f"Sum of Grades: {total}")
print(f"Average:       {average:.2f}")
print("--------------------------------")