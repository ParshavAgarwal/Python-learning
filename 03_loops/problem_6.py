#Factorial Calculator
    # Compute the factorial of a number using while loop
    
number = 5
factorial = 1

while number > 0:
    factorial = factorial * number # facotial *= number
    number = number - 1

print(factorial)