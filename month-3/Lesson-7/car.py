class Car:
    def __init__(self, name, color, price, speed):
        self.name = name
        self.color = color
        self.price = price
        self.speed = speed

    def __repr__(self):
        return f"{self.name} - {self.price}"


class Factory:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.cars = []

    def __call__(self, *args, **kwargs):
        for car in args:
            if isinstance(car, Car):
                self.cars.append(car)


kia = Factory(name="Kia", year=2005)
gm = Factory(name="GM", year=2000)

k8 = Car(name="K8", color="white", price=35000, speed=280)
k5 = Car(name="K5", color="black", price=32000, speed=220)
kia(k8, k5)

print(kia.cars)
