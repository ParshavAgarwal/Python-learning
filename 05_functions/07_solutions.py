## Function with *args
    # Write a number that takes variable number of arguments and return their sum
    
def sum_all(*args):  # '*' is most important as yhi batata hain ki multiple arguments hain
    
    print(*args)   # will print the values # 1 2 3 4
    print(args)    # will print the values in 'tuple' # (1, 2, 3, 4)
    for i in args:  #therefore, we can use loop to do somthing
        print(i * 2, end=' ') #2 4 6 8 10
    
    #we can also use loop to sum all instead of sum function, now that we know what is in 'args'
    return sum(args)

print(sum_all(1,2,3,4))