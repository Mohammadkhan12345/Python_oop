class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"Brand :{self.brand}"


class car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

    def drive(self):
        print(f"my car is {self.brand} and it's Fuel type is {self.fuel_type}")

# ye ek tareekha ha car ki class ko instance bananay ka or us kay methods ko call krnay ka


my_Car = car("honda city", "Petrol")

my_Car.start()
my_Car.drive()
