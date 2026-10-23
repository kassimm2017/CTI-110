# CTI-110 P4LAB2 - Loops
# Ayinga Kassim Mohammed
# Date: Oct 23, 2026

def main():
    print("CTI-110 P4LAB2 - Running Total with Loops")
    print("Ayinga Kassim Mohammed")
    print("----------------------------------------")
    
    # Part 1: While loop - Running total (Bug Collector style)
    total = 0
    num_days = int(input("Enter number of days: "))
    
    # Input validation with while loop
    while num_days <= 0:
        print("Days must be greater than 0")
        num_days = int(input("Enter number of days: "))
    
    # For loop to collect data for each day
    for day in range(1, num_days + 1):
        bugs = int(input(f"Enter bugs collected on day {day}: "))
        while bugs < 0:
            print("Bugs cannot be negative")
            bugs = int(input(f"Enter bugs collected on day {day}: "))
        total += bugs
    
    print(f"\nTotal bugs collected over {num_days} days: {total}")
    
    # Part 2: For loop - Multiplication table display
    print("\nMultiplication Table (1 to 5):")
    for num in range(1, 6):
        result = num * total if total > 0 else num * 2
        print(f"{num} x {total if total>0 else 2} = {result}")

if __name__ == "__main__":
    main()
