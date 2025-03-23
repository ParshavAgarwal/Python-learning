## Polymorphism in Functions
    # write a func. multiply that multiplies two numbers, but can also accept and multipy strings
    
#Python already follows polymorphism in its operations

def multiply(p1, p2):
    return p1*p2

print( multiply(4,6) )
print( multiply('f', 5) )
print( multiply(5,'f') )
#print(multiply('f','f')) #can't directly multipy strings into strings