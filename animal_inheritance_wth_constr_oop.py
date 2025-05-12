class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Cat(Animal):
    def speak(self):
        return f"{self.name} meow "


class Dog(Animal):
    def speak(self):
        return f"{self.name} bark "


catty = Cat("Cat")
doggy = Dog("Dog")
print(catty.speak())
print(doggy.speak())
