## Polymorphism
    # Demostrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes but with different behaviours
    
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Disel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electricity"
    
safari = Car("TATA", "Safari")
tesla = ElectricCar("Tesla", "Model S", "98kwh")

print(tesla.fuel_type())
print(safari.fuel_type())
