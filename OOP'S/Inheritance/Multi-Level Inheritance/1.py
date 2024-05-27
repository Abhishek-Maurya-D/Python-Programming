class Car:
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = ToyotaCar("Swift")
car1 = Fortuner("Diesel")
print(car1.start())
print(car1.stop())
# print(car1.name)
print(car1.type)