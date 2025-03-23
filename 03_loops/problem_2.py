#Sum of Even Numbers
    # Calculation the sum of even number up to a given number n.
    
n = int(input("Enter the value of n: "))
sum_even = 0

for i in range(1,n+1): #n+1 bcz last no. exclude hota hain
    if i % 2 == 0:
        sum_even += i
    
print("Sum of the even numbers is",sum_even)