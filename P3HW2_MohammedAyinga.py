"""
CTI-110 - P3HW2 - Salary
Name: Ayinga Kassim Mohammed
Major: Cybersecurity
Date: Fall 2026
"""


print("CTI-110 P3HW2 - Ayinga Kassim Mohammed")
print("----------------------------------------")


# Get employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# Calculate pay with overtime
if hours > 40:
    overtime_hours = hours - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
else:
    overtime_hours = 0
    regular_hours = hours
    overtime_pay = 0
    regular_pay = hours * pay_rate
    gross_pay = regular_pay


# Display results
print("\n----------------------------------------")
print(f"Employee name: {name}")
print("\nHours Worked  Pay Rate   OverTime  OverTime Pay  RegHour Pay  Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours:<13} {pay_rate:<10} {overtime_hours:<9} ${overtime_pay:<11.2f} ${regular_pay:<10.2f} ${gross_pay:.2f}")
print("----------------------------------------")