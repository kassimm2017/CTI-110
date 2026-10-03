# CTI-110 - P2LAB2 - Cybersecurity Major
# Your Name - Replace with your name
# Date


# P2LAB2 - Auto/Course Grade Calculator with if/else


# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")


# Perform operation with if/elif
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation entered!")


# Additional - Grade check for cybersecurity context
grade = float(input("Enter your current grade (0-100): "))
if grade >= 90:
    print("Grade: A - Excellent!")
elif grade >= 80:
    print("Grade: B - Good job!")
elif grade >= 70:
    print("Grade: C - Keep studying!")
else:
    print("Grade: Below C - Need to improve!")