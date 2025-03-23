## Class ineritance and isinstance() Function
    # Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectriceCar
    
class Car:
    car_count = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count +=1
        
    def full_name(self):
        return f"{self.brand}{self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
        
my_tesla = ElectricCar("Tesla", "S", "87kwh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))