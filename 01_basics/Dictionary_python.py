chai_types = {"Masala": "Spicy", "Black": "bitter", "green": "mild"}
print(chai_types)

print(chai_types["green"])
print(chai_types.get("green"))

#diff btw normal print and get
#chai_types.get("Gingery") #return nothing and no errors
#print(chai_types["Masalaa"]) #return nothing and errors

print(chai_types)
chai_types["green"] = "fresh"
print(chai_types)  #green = fresh

#LOOP
for chai in chai_types:
    print(chai) #all keys will print
    
for chai in chai_types:
    print(chai, chai_types[chai]) #chai, and value accessor

for key,values in chai_types.items(): # Only for Dictionary,, 'items' mathod is necessary - item: key + value
    print(key,values)
    
#CONDITION
if "Masala" in chai_types:
    print("I have Masala chai")
    
print(len(chai_types)) # 3 --> total items

#adding new item
chai_types["earl grey"] = "cittrus"
print(chai_types)

#POP
chai_types.pop("Black") #we have to give key bcz in dict. there is no sequence
print(chai_types)

chai_types.popitem() #no parameter req. # jo last add kii hain vhi niklegi
print(chai_types)

del chai_types["green"] #will delete it from memory
print(chai_types)

chai_types_copy = chai_types.copy()

## Dict in Dict {{}}

tea_shop = {
    "chai" : {"Masala" : "Spicy", "Ginger": "Zesty"},
    "tea" : {"Black" : "Bitter", "Green":"Mild"}
}

print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["tea"]["Black"])

squared_nums = {x:x**2 for x in range(1,6)}
print(squared_nums)
squared_nums.clear()
print(squared_nums) #empty

#Diff approach

keys = {"Masala", "Ginger", "Green"}
default_value = "Delecious"

new_dict = dict.fromkeys(keys, default_value) #dict is a keyword for dictionary beside {}
print(new_dict) # 'Delicous' will be assigned to keys

new_dict = dict.fromkeys(keys, keys)
print(new_dict) #sabhi m sabhi assigned