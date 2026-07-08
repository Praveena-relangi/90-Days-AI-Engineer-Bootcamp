# If Statement in Python
# Exercises
# Exercise 1 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

# Exercise 2
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")

# Exercise 3
number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")

# Exercise 4
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")

# Exercise 5
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent!")

# Practice challenge
# program 1
salary = int(input("Enter your salary: "))
if salary > 50000:
    print("You are getting high income.")

# program 2
temperature = float(input("Enter the temperature: "))
if temperature > 35:
    print("It's a hot day.")

# program 3
attendance = int(input("Enter your attendance percentage: "))
if attendance >= 75:
    print("You are eligible for the exam.")

# Mini project: Movie Ticket Eligibility Checker
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are eligible to watch the movie.")