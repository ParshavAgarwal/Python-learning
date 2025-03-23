username = "Chai_aur_Python"  #directly memory m daal dii

# Scopes -->  {} in all languages,,, in python we use ':' indentation instead of {}

## INVESTIGATION kar rhe hain, (experiments)

def func():
    username = "chai"
    print(username) # will print 'chai' when called
    
print(username)  # Chai_aur_Python -- globally declared hain
func()

## 2
x = 99
def func2(y):
    z = x + y # x is globally defined above
    return z

result = func2(1)
print(result) 

#Now, we are assuming the same x = 99, that is globally defined
def func3():
    global x # means ki ab hum is function m X k saath kuch bhi karenge, wo global k saath hi kar rhe hain
    x = 12  # global x will 12
    # apne ko global nhi use karna chahiye bcz isse confusion hota hian
    
func3()
print(x)  # 12

print(func2(8)) # ab global x change ho gaya hain, so func2 m bhi x dusra jayega

x = 99 #changing it again

## 3

def f1():
    x = 80
    def f2():
        print(x)
    f2()
f1()  # calling f1() --> f2 bhi execute hoga

# something similar -- CLOSURE

def f3():
    x = 79
    def f4():
        print(x)
    return f4 # return hame pura 'definition' hi return kar raha hain, with bagage ,i.e, apan jis def m return kar rhe hain vaha k koi variable ya value
myResult = f3()
myResult() #same result


def chai(num):
    def actual(x):
        return x ** num
    return actual #return the definition -- actual

f = chai(3)
g = chai(4)

print(f)  # <function chai.<locals>.actual at 0x0000026EC369D800>
print(g)  # <function chai.<locals>.actual at 0x0000026EC369D8A0>

print(f(2))  # 2**3
print(g(3))  # 3**4