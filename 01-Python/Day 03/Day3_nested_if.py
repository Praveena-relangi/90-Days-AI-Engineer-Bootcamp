# Nested if
# Exercises
# Exercise 1: 
age = int(input("Enter your age: "))

if age >= 18:

    marks = int(input("Enter your marks: "))

    if marks >= 75:
        print("Admission Approved")
        
# Exercise 2:
pin = input("Enter PIN: ")

if pin == "1234":

    amount = int(input("Enter Amount: "))

    if amount <= 10000:
        print("Transaction Successful") 

# Exercise 3:
marks = int(input("Enter Marks: "))

if marks >= 90:

    income = int(input("Enter Family Income: "))

    if income < 500000:
        print("Scholarship Approved")

# Exercise 4:
age = int(input("Enter Age: "))

if age >= 18:

    ticket = input("VIP Ticket? (yes/no): ").lower()

    if ticket == "yes":
        print("VIP Seat Booked")

# Exercise 5:
employee_id = input("Enter Employee ID: ")

if employee_id == "EMP101":

    password = input("Enter Password: ")

    if password == "python123":
        print("Login Successful")

# Practice challenges
# Challenge 1:
age = int(input("Enter your age: "))

if age >= 18:
    test_results = input("Enter test results (pass/fail): ").lower()
    if test_results == "pass":
        print("Driving License Approved")

# Challenge 2:
budget = int(input("Enter your budget: "))
if budget >= 50000:
    laptop_available = input("Is Laptop Available? (yes/no): ").lower()
    if laptop_available == "yes":
        print("Laptop Purchase Successful")
    else:
        print("Laptop Not Available")
else:
    print("Budget Insufficient")

# Challenge 3:
age = int(input("Enter your age: "))
if age >= 18:
    medical_fitness_certificate = input("Do you have a medical fitness certificate? (yes/no): ").lower()
    if medical_fitness_certificate == "yes":
        print("Eligible for Gym Membership")
    else:
        print("Medical Fitness Certificate Required")
else:
    print("Not Eligible for Gym Membership")

# Mini Project: Bank Account Opening System
customer_name = input("Enter Customer Name: ")
customer_age = int(input("Enter Customer Age: "))
if customer_age >= 18:
    aadhar_availability = input("Do you have Aadhar Card? (yes/no): ").lower()
    if aadhar_availability == "yes":
        initial_deposit = int(input("Enter Initial Deposit Amount: "))
        if initial_deposit >= 1000:
            print(f"Account Opening Successful for {customer_name}")
        else:
            print("Initial Deposit must be at least 1000")
    else:
        print("Aadhar Card Verification failed")
else:
    print("Not Eligible for Account Opening. You must be at least 18 years old to open an account.")
