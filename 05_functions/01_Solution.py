## Baisc Function SUntax
    # Write a funtion to calculate and return the square of a number
    
#function definition --> def

def square(number):
    return (number ** 2) # '**' is used for power --> **2 means square, ||ly, **3 --> cube
    
result = square(5)
print(result)
#or 
print(square(5))

#we can directly give the command of print in function, but, it will directly print it and we cannot use the return of the function in a variable ot something

def cube(num):
    print(num**3)
    
res = cube(3) #27 is printed when read cube(3)
print(res) # print 'None' bcz 'res' m kuch store nhi hua