## Timing Function Execution
    # Write a decorator that measures the time a function takes to execute
    
import time

# we want to create a 'Toll' for the functions, ki agar us function ko call kiya then they have to go through a particular function or 'Toll' or "decorator"

def timer(func): #timer function k andar parameter bhi ek function hain
    
    def wrapper(*args, **kwargs): # *args -> unlimited arguments,, **kwargs -> key words args
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer # <-- humne 'timer' func ko decorator bana diya, means ki jab bhi example_func call hoga, it have to go through 'timer' ,, that's our Toll
def example_func(n): # this is an example function that will be paramter for timer
    time.sleep(n)
    
example_func(3)