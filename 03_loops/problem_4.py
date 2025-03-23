# Reverse a String
    # Reverse a srtin using loop

input_string = input("Enter the string: ")
reversed_str1 = ""
reversed_str2 = ""

for char in input_string:
    reversed_str1 = char + reversed_str1
    reversed_str2 = reversed_str2 + char
    #placement bhi farak kar deta hain
    
print("When char + revesed_str --> ",reversed_str1)
print("When reversed_str + char --> ",reversed_str2)
