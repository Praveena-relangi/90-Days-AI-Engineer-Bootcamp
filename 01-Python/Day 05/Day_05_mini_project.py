class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("\n------Student Details ------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
    def result(self):
        if self.marks >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")

student1 = Student("Praveena", 25, 98)
student2 = Student("Niranjan", 30, 91)

student1.display()
student1.result()

student2.display()
student2.result()