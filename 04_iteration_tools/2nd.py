# f = open('chai.py')  #File will run in python shell of (Whole folder) (right click on folder)
# f.readline() #will read one line at a time (ek baar kiya to ek line) and will give lines of 'chai.py'
# f.__next__() #same work as above but y raw tareeka hain, jesa internal work hota hain

# #we can alsouse loop instead of readlines -- again and again
# for line in open('chai.py'):
#     print(line, end ='') # '' is ther so ki lines skip (Space extra) na ho
    
# # Syntax is Different for 'While' loop
# while True:
#     line = f.readline()
#     if not line: break #if not line --> readline does not read any line
#     print (line) #when line is there
    
## ABove was for 'files'

## For other Iterable objects like 'List'
mylist = [1,2,3,4]
I = iter(mylist) #we need iter tool or method for iteration  # File have their own inbuild iter tool

#f = open('chai.py') #in this (for file)  [ iter(f) = f ]**  only for file

print(I) # <list_iterator object at 0x000001B30D6498A0>
print(I.__next__()) # 1
print(I)  # Location is not changed  # <list_iterator object at 0x0000017A939E98D0>
#iter object will only remain at first address
print(I.__next__()) #2
print(I.__next__()) #3
print(I.__next__()) #4

#from line 21 - in case of file and list
#print(iter(f) is f) #for file # will run in shell of folder #TRUE
# f = iter(f) = f.__iter__(), means agar hum in teeno ko alag alag 'is' se puchenge equal ki to it will return 'TRUE'

print( print(I) is mylist ) #FALSE

# Dict is also iterable
#manual iteraion -->
D = iter({'a':12, 'b':45})

print(D)
print(D.__next__())
#or
print(next(D))
# print(D.__next__()) #commonly used #iteration will stop here

#range is also itetable

R = iter(range(5))
print(R)
print(next(R))
print(next(R))
print(next(R))
print(next(R))
print(next(R))