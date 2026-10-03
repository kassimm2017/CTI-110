"""
CTI-110 - P3HW1 - Grades with Lowest Dropped
Name: Ayinga Kassim Mohammed
Major: Cybersecurity
Date: Fall 2026
"""


print("CTI-110 P3HW1 - Ayinga Kassim Mohammed")
print("----------------------------------------")


# Get 6 module grades
m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))


grades = [m1, m2, m3, m4, m5, m6]


lowest = min(grades)
grades.remove(lowest)


# Calculate with lowest dropped
total = sum(grades)
average = total / len(grades)


# Letter grade
if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"


# Output
print("\n------------Results------------")
print(f"Lowest Grade Dropped: {lowest}")
print(f"Grades Remaining: {grades}")
print(f"Sum of Remaining: {total}")
print(f"Average (with lowest dropped): {average:.2f}")
print(f"Letter Grade: {letter}")
print("--------------------------------")