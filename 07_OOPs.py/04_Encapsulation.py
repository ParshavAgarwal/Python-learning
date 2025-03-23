## Encapsulation
    # Modify the Car class to encapsulate the brand attribute, making it private, and provide getter method for it.
    
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # kisi bhi variable k aage '__' double underscore laga do, then it becomes 'Private'
        self.model = model
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
my_car = Car("TATA", "Safari")
# print(my_car.brand)    # ERROR
# print(my_car.__brand)  # ERROR
print(my_car.get_brand())

print(my_car.full_name()) #it is running kyoki apan private variable ko publuc method k through access kar rhe hain
