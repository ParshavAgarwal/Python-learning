x = ('Masala', 'Giner', 'Lemon')
y = enumerate(x)
print(y) # <enumerate object at 0x0000015A3A8905E0>
# enumerate karke y list bai h, vo bhi (key-value) pairs ki...
print(list(y)) # [(0, 'Masala'), (1, 'Giner'), (2, 'Lemon')]

## file handling
file = open('youtube.txt', 'w') # w -> write mode, m open kar rhe hain,, agar file nhi hogi to y use create kar dega
# but ise causiously karte hain taaki kabhi luch overwrite na ho jaye

# Jab bhi causiously kuch karna ho then we use, try-catch
try:
    file.write("chai aur python")
finally: 
    file.close() # remember to close the file

# 2nd method for file handling

with open('youtube.txt', 'w') as file:
    file.write("Hello all")
    #isme closing y apne aap sambhal leta hain
