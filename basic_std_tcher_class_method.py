class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Teacher Age: {self.age}")
        print(f"Teacher Subject: {self.subject}")


student1 = Student("ali", 22)
student1.display_info()
teacher = Teacher("tahseen", 111, "math")
teacher.display_info()
