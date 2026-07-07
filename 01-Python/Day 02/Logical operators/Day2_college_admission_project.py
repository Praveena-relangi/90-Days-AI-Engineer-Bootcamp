# Mini Project: College Admission Eligibility Checker
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_marks = float(input("Enter your marks (out of 100): "))
Entrance_qualified = input("Have you qualified the entrance exam? (yes/no): ").strip().lower()  

if student_age >= 17 and student_marks >= 75 and Entrance_qualified == "yes":
    print(f"Congratulations {student_name}! You are eligible for college admission.")   
else:
    print(f"Sorry {student_name}, you are not eligible for college admission.") 