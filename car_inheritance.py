class Car:
    def __init__(self, name, brand, color, price, engine, speed):
        self.name = name
        self.brand = brand
        self.color = color
        self.price = price
        self.engine = engine
        self.speed = speed

    def display_info(self):
        return f"Car Name: {self.name} ,Brand: {self.brand} ,color: {self.color} ,price: {self.price} ,engine: {self.engine} ,speed: {self.speed} "


class electric_Car(Car):

    def details(self, battery_capacity, model, year):
        self.battery_capacity = battery_capacity
        self.model = model
        self.year = year
        return f"{self.display_info()} , battery : {battery_capacity} , model : {model} , year : {year} "


gari = Car("city", "honda", "blue", 2000000, "1.3L", 180)
gari1 = electric_Car("leaf", "nissan", "white", 3000000, "1.5L", 200)
gari2 = electric_Car("corolla", "toyota", "black", 2500000, "1.4L", 190)
gari3 = electric_Car("alto", "suzuki", "red", 1500000, "1.0L", 160)
print(gari1.details("80 kwh", "x", 2022))
print(gari.display_info())
