# Validate Input
    # Keep asking the user for an input until they enter a number btw 1 and 10
    
while True:
    number  = int(input("Enter a number btw 1 and 10:"))
    if 1 <= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid....Try Again!!") 