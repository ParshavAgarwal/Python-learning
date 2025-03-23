tea_types = ("black", "ginger", "oolong")
#sab kuch same as list wagera -- slicing dicing, -1 position, etc

#difference
print(tea_types[0])
## tea_types[0] = "Masala" #error -> 'tuple' object does not support item assignment
#it is immutable

print(len(tea_types))

more_tea = ("herbal", "masala")
all_tea = more_tea + tea_types
print(all_tea) #y list m bhi hota hain

##
print(tea_types)
(black, ginger, oolong) = tea_types
print(black)
print(oolong)

#class type pata karo
print(type(tea_types))