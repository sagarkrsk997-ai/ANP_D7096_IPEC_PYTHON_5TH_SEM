# Function to calculate grade
def calculate_grade(marks):

    if marks > 100:
        return "Invalid Input"
    elif marks < 0:
        return "Marks In-apropriate"
    elif marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"
        


# Main Program
for i in range(1, 6):
    marks = int(input("Enter marks of Student " + str(i) + ": "))

    grade = calculate_grade(marks)

    print("Student", i)
    print("Marks =", marks)
    print("Grade =", grade)
    print()