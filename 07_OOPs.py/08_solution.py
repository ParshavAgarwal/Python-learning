## Property Decorator
    # Use a property decorator in the Car class to make the model attribute read-only
    
class Car:
    car_count = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.car_count +=1
        
    def full_name(self):
        return f"{self.brand}{self.__model}"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
tesla = ElectricCar("Tesla", "S", "87kwh")

safari = Car("TATA", "Safari")
# safari.model = "City"  #this is Okay even jab model ko Private kar diya BEFORE  @property decorator
# safari.model = "City" --> we can't make changes in model after @property decorator
Car("TATA", "Nexon")  

print(safari.model)  # City --(before)  # Safari --(After)
# print(safari.model)  # 'str' object is not callable # after also bcz humnare moderator n hme use Property ki tarah access karne ko de diya hain

