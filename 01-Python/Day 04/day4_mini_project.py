# Mini project: Smart Student Result Analyzer
student_name = input("Enter the student's name: ")
maths_marks = int(input("Enter the student's mathematics marks: "))
physics_marks = int(input("Enter the student's physics marks: "))
chemistry_marks = int(input("Enter the student's chemistry marks: "))
english_marks = int(input("Enter the student's English marks: "))
python_marks = int(input("Enter the student's Python programming marks: "))

total_marks = maths_marks + physics_marks + chemistry_marks + english_marks + python_marks
average_marks = total_marks / 5
percentage = (total_marks / 500) * 100
result = "Pass" if percentage >= 40 else "Fail"
grade = "Distinction" if percentage >= 75 else "First Class" if percentage >= 60 else "Second Class" if percentage >= 50 else "Third Class" if percentage >= 40 else "Fail"

print("============== STUDENT REPORT CARD ==============")
print(f"Student Name: {student_name}")
print()
print(f"Mathematics Marks: {maths_marks}")
print(f"Physics Marks: {physics_marks}")
print(f"Chemistry Marks: {chemistry_marks}")
print(f"English Marks: {english_marks}")
print(f"Python Programming Marks: {python_marks}")
print()
print('---------------------------------------------------------------')
print()
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {result}")
print(f"Grade: {grade}")
print("===================================================")