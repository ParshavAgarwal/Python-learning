## Multiple Inheritance
    # Create two class Battery and Engine, and let the ElectriceCar class inherit from both, demonstrating multiple inheritance
    
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class Battery:
    def info_battery(self):
        return "This is Battery"
    
class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCar(Car, Battery, Engine):
    # def __init__(self, brand, model):
    #     super().__init__(brand, model)
    pass     # we can also just use pass bcz hum kuch kar nhi rhe h hain is upar wali info ka
        
        
my_tesla = ElectricCar("Tesla", "S")
print(my_tesla.engine_info())
print(my_tesla.info_battery())