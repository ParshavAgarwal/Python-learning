## Function with **kwargs
    # Create a Function that accepts any number of keyword arguments and prints them in the format-  key: values.
    
def print_kwargs(**kwargs):
    
    #we need loop for this because hum key aur value dono de rhe hain
    for key, value in kwargs.items(): # items() bcz hme ek unit chahiye
        print(f"{key} : {value}") #using f-string
        
print_kwargs(name="Shaktiman", power="Fly")
print_kwargs(name="spider-man", enemy = "GG", age="recent adult")