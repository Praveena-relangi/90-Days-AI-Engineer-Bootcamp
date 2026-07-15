with open("01-python\Day 06\student.txt","r") as student_file:
    print(student_file.read())

option = int(input("Choos your option: "))
if option == 1:
    print("Replacing existing text with new text")
    with open("01-python\Day 06\student.txt","w") as student_file:
        student_file.write("Welcome to 90 days AI Bootcamp challenge conducted by PN Tech life")
elif option == 2:
    print("adding or appending new text to the existing text")
    with open("01-python\Day 06\student.txt","a") as student_file:
        student_file.write("\n Maintain consistency to achieve your goals. Lets learn with PN Tech life!!!!!")
else:
    print("read the file and print")
    with open("01-python\Day 06\student.txt","r") as student_file:
        print(student_file.read())
