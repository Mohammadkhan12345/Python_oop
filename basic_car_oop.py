class Car:
    def __init__(self, brand, model, year, milage):
        self.brand = str(brand)
        self.model = str(model)
        self.year = int(year)
        self.milage = int(milage)


my_car = Car("honda", "city", 2008, 123456)
my_car = Car("toyota", "corolla", 2010, 123456)
my_car = Car("suzuki", "alto", 2012, 123456)
my_car = Car("nissan", "leaf", 2014, 123456)

print(my_car.brand)
