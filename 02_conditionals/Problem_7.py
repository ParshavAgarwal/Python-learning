# Coffee Customization
    # Customize a coffee order: "Small", "Medium", "Large" with an option for "Extra Shot" of Expresso

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with an extra shot of expresso"
else:
    coffee = order_size + "coffee"

print(coffee)
