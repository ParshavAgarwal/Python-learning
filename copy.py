l1 = [1,2,3]
l2 = l1  #l2 is assigned to same reference as l1

print(l1, l2)

l1[1] = 22  #l2 will also change
print (l1, l2) 

#Copy
l1 = [1,2,3]
l2 = l1  #l2 is assigned to same reference as l1
l2 = [1,2,3] #another reference is created

print(l1, l2)

l1[1] = 22 #l2 will not change as it is directed to another memory
print (l1, l2)

## It is not assigning to same memoring but creating a copy or another memory because it is Mutable and can be changed, therefore, if not told - it will create another (in case if changes happend) 

h1 = [4,5,6]
h2 = h1[:] #using the concept of slicing to create a copy *(not assigning to same)

h1[1] = 11
print(h1,h2)

#Checking
m = [1,2,4]
n = m

print(m==n)  #checking if the Object or value is same
print(m is n) # checking if Both are Directed to same Reference

n = [1,2,4]
print(m==n) #True Bcz Same Value
print(m is n) #False Because Diff Ref
