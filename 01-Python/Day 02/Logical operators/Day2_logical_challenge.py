# Challenge 1: Job eligibility checker
age = int(input("Enter your age: "))
has_degree = input("Do you have a degree? (yes/no): ")
if age >= 18 and has_degree == "yes":
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

# Challenge 2: Login information checker
has_email = input("Do you have an email? (yes/no): ")
has_phone = input("Do you have a phone number? (yes/no): ")
if has_email == "yes" or has_phone == "yes":
    print("You can log in.")
else:
    print("You cannot log in.")

# Challenge 3: logged in status checker
is_logged_in = input("Are you logged in? (yes/no): ")
if not is_logged_in == "yes":
    print("You are not logged in.") 
else:
    print("You are logged in.")