class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting... "


class Bike(Vehicle):
    def __init__(self, brand, gears):

        super().__init__(brand)  # you cannot use self argument with in super()
        self.gears = gears

    def ride(self):
        return f"i am riding in {self.gears} gear : On this brand : {self.brand}"


v = Bike("honda", 5)
print(v.ride())
