# Fruit Ripeness Checker
    # Determine if a fruit is ripe, overripe or unripe based on its color. (e.g., Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)

fruit = "Banana"
color = "Green"

if fruit == "Banana":
    if color == "Yellow":
        print("Ripe")
    elif color == "Green":
        print("Unripe")
    elif color == "Brown": #elif bcz har color k liye check nhi karna hain
        print("overripe")

else:
    print("We don't have any info on this fruit")
    
