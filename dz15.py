class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Car(Transport):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self.color = color

class Plane(Transport):
    def __init__(self, name, speed, width):
        super().__init__(name, speed)
        self.width = width

class Ship(Transport):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self.color = color

car = Car('bmw', 100, 'red')
plane = Plane('pobeda', 1000, 250)
ship = Ship('boat', 30, 'black')

print(f'Car name : {car.name}, speed: {car.speed}, color: {car.color}')
print(f'Plane name : {plane.name}, speed: {plane.speed}, width: {plane.width}')
print(f'Ship name : {ship.name}, speed: {ship.speed}, color: {ship.color}')