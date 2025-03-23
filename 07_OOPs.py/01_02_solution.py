## Basic Class and Objest
    # Create a Car class with attributes brand and model. Then create an instance of the class
    
class Car: 
    def __init__(self, brand, model):  ## __init__ --> Constructor 
        # self ek connection establish karta hain, y batata hain ki y variable ise point karta hain.....   Like 'this' in JAVAscript
        self.brand = brand     # self.brand --> class k andar ka variable
        self.model = model
        
    def full_name(self): # y ek context deta hain.. y batat h ki ishi variable ka baat ho raha hain... #you need this to access varibles in methods in class
        return f"{self.brand} {self.model}"  # f"{}" -> f string
    
    
my_car = Car("toyota", "corolla")  ## Car() --> method (blue print or form)
print(my_car.brand)
print(my_car.model) 
print(my_car.full_name()) 

my_new_car = Car("TATA", "Safari")
print(my_new_car.full_name())