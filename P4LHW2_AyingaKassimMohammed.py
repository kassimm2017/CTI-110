# CTI-110 P4HW2 - Salary Calculator with Overtime
# Ayinga Kassim Mohammed
# Fall 2026

def main():
    print("Ayinga Kassim Mohammed - P4HW2 Salary Calculator")
    print("-------------------------------------------------")
    
    total_employees = 0
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    
    # Loop to enter multiple employees
    employee_name = input('Enter employee\'s name or "None" to terminate: ')
    
    while employee_name != "None":
        hours = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
        print(f"Employee name: {employee_name}")
        print("")
        
        # Calculate pay
        if hours > 40:
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * pay_rate * 1.5
            regular_pay = 40 * pay_rate
            gross_pay = regular_pay + overtime_pay
        else:
            overtime_hours = 0
            overtime_pay = 0
            regular_pay = hours * pay_rate
            gross_pay = regular_pay
        
        # Display results
        print("-------------------------------------------------")
        print(f"Employee name:      {employee_name}")
        print(f"Hours Worked        Pay Rate        OverTime        OverTime Pay      RegHour Pay       Gross Pay")
        print("-------------------------------------------------------------------------------------------------")
        print(f"{hours:.2f}                {pay_rate:.2f}            {overtime_hours:.2f}            ${overtime_pay:.2f}           ${regular_pay:.2f}          ${gross_pay:.2f}")
        print("-------------------------------------------------------------------------------------------------")
        print("")
        
        # Add to totals
        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        
        # Next employee
        employee_name = input('Enter employee\'s name or "None" to terminate: ')
    
    # Final summary
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()
