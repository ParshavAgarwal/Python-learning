## Function Returning MUltiple Values
    # Create a function that returns both area and circumference of a circle given it's radius

import math

def circle(radius):
    area = 2 * math.pi * (radius**2)
    circumference = 2 * math.pi * radius #math.pi gives the actual value of pi
    return area, circumference

a, c = circle(4)

print("Area:",a, "Circumference:",c) #this will give very lengthy values

# For precisions upto 2 or 3 places

import math

def circle_stat(r):
    area = 2 * math.pi * (r**2)
    circumference = 2 * math.pi * r
    return round(area, 2), round(circumference, 2)  # rounding to 2 decimal places
    #return area, 2, circumference, 2   #we can remove round() method as 'f-string' helps us to formatting it to 2 decimals #round() is used for round up

a, c = circle(4)

print(f"Area: {a: .2f}, Circumference: {c: .2f}")  # formatting to 2 decimal places