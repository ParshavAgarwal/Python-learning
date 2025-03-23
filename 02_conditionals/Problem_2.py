#Movie Ticket Pricing
    # movie tickets are priced based on age : $12 for adult(18 & over), $8 for children. Everyone gets
    # a $2 discount on wednesday.

age = 24
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $",price)