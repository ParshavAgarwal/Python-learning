# Transportation Mode selection
    # Choos a mode of transport based on the distance (eg; <3km: Walk, 3-15km: Bike, >15km: Car)

distance = int(input("Enter the distance: "))

if distance < 3:
    transport = "Walk"
elif distance < 15:
    transport = "Bike"
else:
    transport = "Car"
    
print("your mode of transport should be",transport)