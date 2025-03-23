## Debugging Function Call
    # Create a Decorator to print the function name and the values of its arguments every time the function is called
    
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join( str(arg) for arg in args ) # ', ' -> shows/reads different args divided by a comma(,)
                                                          # join() -> is an iterable method, or makes the readuing of the args iterable/loop
                                                          # str(arg) --> converts arg into string
                                                          # fir loop chalta hain to read all the args and store it in args_value
        kwargs_value = ', '.join( f"{k} = {v}" for k,v in kwargs.items() ) #items() -> k&v ek unit
        print(f"{func.__name__} has args- {args_value} and kwargs- {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def Hello():
    print("Hello!!")

@debug
def Greet(first_name,last_name, greeting = "Hello"):
    print(f"{greeting}, {first_name} {last_name}")
    
    
Hello()
Greet("Parshav", "agarwal", greeting="Namaskar!")  # kawrgs_value main greeting tabhi jayega jab hum greeting input main denge, {Default greeting count nhi honge}
Greet("Vada", "Pav")