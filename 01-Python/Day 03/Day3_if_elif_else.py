# if elif and else statements
# Exercises
# Exercise 1
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

else:
    print("Fail")

# Exercise 2
age = int(input("Enter your age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")

# Exercise 3
signal = input("Enter signal color: ").lower()

if signal == "red":
    print("Stop")

elif signal == "yellow":
    print("Get Ready")

elif signal == "green":
    print("Go")

else:
    print("Invalid Signal")

# Exercise 4
temperature = float(input("Enter temperature: "))

if temperature < 20:
    print("Cold")

elif temperature <= 30:
    print("Pleasant")

else:
    print("Hot")

# Exercise 5
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal Weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")

# Practice challenge
# program 1
salary = float(input("Enter your salary: "))
if salary >= 100000:
    print("You are in the high-income group.")
elif salary >= 50000:
    print("You are in the middle-income group.")
else:
    print("You are in the low-income group.")

# program 2
amount = float(input("Enter the amount: "))
if amount >= 5000:
    print("You are eligible for a 20'%' discount.")
elif amount >= 2000:
    print("You are eligible for a 10'%' discount.") 
else:
    print("You are not eligible for any discount.")

# program 3
battery_percentage = int(input("Enter battery percentage: "))
if battery_percentage > 80:
    print("Battery is Full")
elif battery_percentage > 30:
    print("Battery is Moderate")
else:
    print("Battery is Low")

# Mini project: Student Report Card System
student_name = input("Enter student name: ")
marks = int(input("Enter marks obtained: "))
if marks >= 90:
    print(f"{student_name} has scored an A grade.")
    print("Outstanding performance! Keep it up!")
elif marks >= 75:
    print(f"{student_name} has scored a B grade.")
    print("Good job! You can do even better!")
elif marks >= 60:
    print(f"{student_name} has scored a C grade.")
    print("You passed! Keep working hard!")
elif marks >= 35:
    print(f"{student_name} has scored a D grade.")
    print("You need to improve. Keep trying!")
else:
    print(f"{student_name} has failed.")
    print("Don't give up! Practice consistentlyand you will improve!")