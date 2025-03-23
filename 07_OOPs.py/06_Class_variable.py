## Class Variable
    # Add a class variable to Car that keeps the track of number of car created
    
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
        
tesla = ElectricCar("Tesla", "S", "87kwh")

#we can also call class without using variables.

safari = Car("TATA", "Safari")
Car("TATA", "Nexon")  #koi object declare nhi hua so we can't print it, but call ho raha hain

print(Car.car_count)