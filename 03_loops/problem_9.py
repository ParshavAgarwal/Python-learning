# List Uniqueness Checker
    # Check if all elements in a list are unique. If Duplicate is found, exit loop and print the duplicate
    # items = ["apple", "banana", "orange", "apple", "mango"]
    
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set() #it is empty at first

for item in items:
    if item in unique_item: #returns True or False
        print("Duplicate:", item)
        break
    else:
        unique_item.add(item) #adding items 1 by 1 if not present already (duplicate)
    