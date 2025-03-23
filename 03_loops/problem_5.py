#Find the First Non-Repeated character
    # Given a string, find the non-repeated char
    
input_str = "teeterababa"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is :",char)
        break
