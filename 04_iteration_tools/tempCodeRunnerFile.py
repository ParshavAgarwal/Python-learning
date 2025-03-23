f = open('chai.py')  #File will run in python shell of (Whole folder) (right click on folder)
# f.readline() #will read one line at a time (ek baar kiya to ek line) and will give lines of 'chai.py'
# f.__next__() #same work as above but y raw tareeka hain, jesa internal work hota hain #Core Syntax jo iterable banata hain

# #we can always loop instead of readlines -- again and again
# for line in open('chai.py'):
#     print(line, end ='') # '' is there so ki lines skip (Space extra) na ho
    
# # Syntax is Different for 'While' loop
# while True:
#     line = f.readline()
#     if not line: break #if not line --> readline does not read any line
#     print (line) #when line is there