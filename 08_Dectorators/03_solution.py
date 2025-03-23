## Cache Return Values
    # Implementing a decorator that caches the return values of a function, so when it's called with the same arguments, the cached value is returned instead of re-ececuting the function
    
import time

def cache(func):
    cache_value = {} # dictionary, bcz easy to access with keys and values. --- keys as a index kaam kar lenge
    
    def wrapper(*args):
        if args in cache_value:        # args (key) as Index
            return cache_value[args]   # return the value at particular key
        
        result = func(*args)
        cache_value[args] = result  # agar naya 'args' hain to cache m stor kawalo
        return result
    return wrapper

@cache
def long_run_func(*args):
    time.sleep(3)
    return sum(args)

print(long_run_func(3,2,4))  # took it's time (3 sec)
print(long_run_func(3,2,4))  # immediately from the cache
print(long_run_func(4,3,2))  # took time, bcz we rearranged the arguments
print(long_run_func(5,6,2))  # took it's time