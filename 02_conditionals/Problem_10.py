#Pet Food Recommendation
    # Recommend a typpe of pet food based on the pet's species and age. (eg; Doge: <2 year - puppy food; Cat: >5 year - Senior Car food)
    
pet = "Cat"
age = 4

if pet == "Cat":
    if age <5:
        food = "Junior Cat Food"
    else:
        food = "Senior cat food"

elif pet == "Dog":
    if age <2:
        food = "puppy food"
    else:
        food = "Dog food"
        
else:
    print("We don't have any info on",pet)
    exit()

print ("Appropriate food for your pet is", food)