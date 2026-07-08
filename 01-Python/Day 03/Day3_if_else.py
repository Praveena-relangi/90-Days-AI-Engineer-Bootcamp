# If-Else Statement in Python
# Exercies
# Exercise 1:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Exercise 2:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Exercise 3:
marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Exercise 4:
number = int(input("Enter a number: "))

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# Exercise 5:
password = input("Enter password: ")

if password == "python123":
    print("Login Successful")
else:
    print("Invalid Password")

# Practice challenge
# program 1:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for Driving License .")
else:
    print("You are not eligible for Driving License .")

# program 2:
bill_paid = input("Have you paid the bill? (yes/no): ")
if bill_paid.lower() == "yes":
    print("Your Electricity Supply is active.")
else:
    print("Your Electricity Supply is inactive. Please pay the bill.")

# program 3:
amount = float(input("Enter the amount: "))
if amount >= 500:
    print("You are eligible for a free delivery.")
else:
    print("You are not eligible for a free delivery. Please pay the delivery charges.")

# Mini Project: Movie Ticket Booking System
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Welcome {name}")
    print("Adult Ticket Booked Successfully.")
else:
    print(f"Sorry {name}")
    print("You are not eligible to watch this movie.")