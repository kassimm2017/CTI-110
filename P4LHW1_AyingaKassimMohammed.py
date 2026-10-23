# CTI-110 P4HW1 - Score Average
# Ayinga Kassim Mohammed
# Oct 28, 2026

def main():
    print("Ayinga Kassim Mohammed - P4HW1")
    num = int(input("How many scores do you want to enter? "))
    while num < 1:
        num = int(input("How many scores? Must be >0: "))
    
    scores = []
    for i in range(num):
        s = float(input(f"Enter score #{i+1}: "))
        while s < 0 or s > 100:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            s = float(input(f"Enter score #{i+1} again: "))
        scores.append(s)
    
    total = sum(scores)
    avg = total / len(scores)
    lowest = min(scores)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print("\n------------Results------------")
    print(f"Lowest Score : {lowest}")
    print(f"Average      : {avg:.2f}")
    print(f"Grade        : {grade}")
    print("-------------------------------")

if __name__ == "__main__":
    main()
