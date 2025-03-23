chai = "Masala Chai"
first_char = chai[0]

print(first_char)

slice_chai = chai[0:6] #slice kar rhe hain # 0th - 5th char ,, last number countable nhi hain

num_list = "0123456789"

print(num_list[:]) #whole list
print(num_list[:7]) # 0123456
print(num_list[5:]) #56789
print(num_list[0:7:2]) #0246 # 1 term hop or every 2nd term

tea = "   Lemon Tea    "
print(tea)
print(tea.strip()) # () bcz it is a method like lower(), upper() # strip will remove unnceccesary spaces

print(chai.replace("Masala", "Lemon")) #will relace Masala -> Lemon for this print only
print(chai) #original chai nhi badli hain

Chai = "Lemon, Masala, Ginger "
print(Chai.split()) #Splitting in a list,, But koi guidance nhi hain to apne hisab se karega
print(Chai.split(", " )) # ,space ko hatake slpit hoga

#find --> will find the position of the word
print(chai.find("Chai"))

tea = "Lemon Tea Tea tea"
#count --> to count the word
print(tea.count("Tea"))

#format --> till fill in the blank
chai_type = "Masala"
quantity = 3
order = "I ordered {} cup of {} Chai" #here {} are not for dict. bcz it is in string # {} is working as place holders
print(order.format(quantity, chai_type))

#List to String

chai_variety = ["Lemon" , "Ginger" , "Masala"]
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))

#print each char
for _ in chai:
    print(_)
    
#print " " in a string
print("He said, \"it is great\"")

#print as it is -->  r""
print("Masala\nchai")
print(r"Masala\nChai")