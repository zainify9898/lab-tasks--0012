class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


class Graduate(Student):
    def __init__(self, name, age, course, research_topic):
        super().__init__(name, age, course)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print("Research Topic:", self.research_topic)


g1 = Graduate("Ali", 23, "Computer Science", "Artificial Intelligence")

g1.display()