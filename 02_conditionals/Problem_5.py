# Weather activity Suggestion
    # Suggest an activity based on weather (eg; Sunny - Go for a walk, Rainy - Read a book,Snowy - Build a Snowman)

weather = input("Enter tday's weather: ")
weather = weather.lower()

if weather == "sunny":
    activity = "Go for a Walk"
elif weather == "rainy":
    activity = "Read a Book"
elif weather == "snowy":
    activity = "Build a snowman"
    
print(activity)