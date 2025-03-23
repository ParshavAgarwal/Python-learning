# Muiltiplication Table Printer
    # Print the multiplication table for a given number upto 10, but skip the fifth iteration
    
number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number,"x",i,"=", number*i)

