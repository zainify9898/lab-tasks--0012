class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


s1 = Student("Ali", 20, "Computer Science")
s2 = Student("Ahmed", 22, "Artificial Intelligence")

print("Student 1:")
s1.display()

print("\nStudent 2:")
s2.display()