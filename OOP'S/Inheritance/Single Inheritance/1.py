class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
    
car1 = ToyotaCar("Fortunar")
car2 = ToyotaCar("Prius")

print(car1.start())
print(car1.color)