class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        print(f"my name is : {self.name} and my age is {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def Teaching(self):
        print(f"my name is {self.name} and i will teach {self.subject}")


class Math_Teacher(Teacher):
    def __init__(self, name, age, subject, exp):
        super().__init__(name, age, subject)
        self.exp = exp

    def details(self):
        print(
            f"my name is {self.name} and my current experience is {self.exp} years and i will teach you {self.subject} subject")


t = Math_Teacher("khan", 22, "political sciences", 2)
t.Introduce()
t.Teaching()
t.details()
