# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return f"hey! this is {self.name}"


# class Dog(Animal):
#     def speak(name):
#         super().__init__(name)

#         print("bark")


# class Cat(Animal):
#     def speak(name):

#         print("meow")


# cat = Cat("catty")
# dog = Dog("doggy")
# print(cat)
# print(dog)


class Animal:
    def sound(self):
        print("ye kuch janwar hain un ki awazon k saath")


class Cat(Animal):
    def meow(self):
        print("billi meow karti hai")


class Dog(Animal):
    def bark(self):
        print("kutta bark krtaa hai")


cat = Cat()
dog = Dog()
janwar = Animal()

janwar.sound()
cat.meow()
dog.bark()
