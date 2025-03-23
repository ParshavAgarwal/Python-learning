## Default Paramter Value
    # Write a function that greets a user. If no name is provided, it should greet them with a default name

def greet(name = "User"):
    return "Hello," + name + "!"

print(greet("Parshav")) #name diya to hmara diya hua name use karega
print(greet()) #name nhi duya to default name use karega jo paramter m diya hain