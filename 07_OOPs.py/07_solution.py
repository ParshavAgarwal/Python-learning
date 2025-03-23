## Static Method
    # Add a static method to the Car class that returns  general descritpion of a car.
    
#   static methods woh hote hain jo class ke andar define hote hain, but kisi specific instance (object) se related nahi hote. Yeh methods
    
class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand}{self.model}"
    
    @staticmethod  # --> it is a decorator
    def general_description():
        return "Cars are amazing!!"
    
    
#     safari.general_description() directly safari object ke andar nahi hota.
# Python jab object me method nahi dhoondh pata, to woh uske class me check karta hai.
# Static method instance ke saath bind nahi hota, isliye self nahi use kar sakte.
# Object ke through call karne se bhi Python usko class se resolve kar leta hai.
    

safari = Car("TATA", "Safari")

print(safari.general_description()) # Python object ke class me method ko dhundhkar usko call kar leta hai 🚀

# safari.general_description() actually internally convert ho jata hai → Car.general_description().

print(Car.general_description())


# Static methods ko class se call karna best practice hai, par agar object se call karenge to bhi Python usko class se resolve karke chala dega! 🚀💡



##  Jab object se static method nahi chalega:
# Static method tab error dega jab tu self ko pass karne ki koshish karega ya instance variables access karne lagega.
# Example:

# python
# Copy
# Edit
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
    
#     @staticmethod
#     def show_brand():
#         return self.brand  # ❌ Error, 'self' use nahi kar sakte

# c1 = Car("Toyota")
# print(c1.show_brand())  # ❌ AttributeError: 'staticmethod' object has no attribute 'brand'