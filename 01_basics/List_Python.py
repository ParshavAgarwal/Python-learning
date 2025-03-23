tea_variety = ["Black", "Green", "White"]
print(tea_variety)

print(tea_variety[-1])
print(tea_variety[0:2]) #2nd position will not be included

tea_variety[2] = "Herbal"
print(tea_variety)

tea_variety[1:2] = "Lemon"
print(tea_variety) #Through slicing, it will take 'lemon' as Array --> 'l','e','m','o','n'

tea_variety[1:-1] = ["Lemon"] #format
print(tea_variety)

tea_variety[1:] = ["Green"]
print(tea_variety) # 1 - end (pos value)  <--> with one or more

tea_variety[:] = ["Herbal", "Black", "Oolong"]
print(tea_variety)

print(tea_variety[1:1]) #will return empty
#we will use this in cases -- eg
tea_variety[1:1] = ["Masala", "test"]
print(tea_variety) #['Herbal', 'Masala', 'test', 'Black', 'Oolong']

#deletion or insert nothing
print(tea_variety[2:3])
tea_variety[2:3] = [] #insert nothing
print(tea_variety)

#loop
for tea in tea_variety: #tea is a vairable indication like 'i'
    print(tea)

for tea in tea_variety: 
    print(tea, end="-")
    
#conditional
if "White" in tea_variety:
    print("\nIt is here")
else:
    print("\nNot here.....adding")
    tea_variety.append("White") #append --> add at end
    print("added")

print(tea_variety)

if "White" in tea_variety:
    print("\nIt is here")

#POP
tea_variety.pop()
print(tea_variety) #White is removed

#remove
tea_variety.remove("Black")
print(tea_variety) #Black is removed

#ADD / insert
tea_variety.insert(1, "green") #pos, value
print(tea_variety)

#Copy ***
tea_variety_copy = tea_variety.copy()  #a copy will be created, **Reference alag alag honge
t_copy = tea_variety # it will have same reference

tea_variety_copy.append("Tadaka")
print(tea_variety) #nothing changes
print(tea_variety_copy) # "tadaka" will be added

t_copy.append("green")
print(t_copy)
print(tea_variety) #it is also affected because refrence is same and it is mutable

#Using range
print(range(10))
squared_nums = [x**2 for x in range(10)] #x**2 -> x power two
print(squared_nums) # x = 0-9 bcz 10 is excluded

cubic = [y**3 for y in range(1,6)]
print(cubic) # y is from 1 to 5 -- bcz again 6 is excluded ## Because Python is an exclusive language
