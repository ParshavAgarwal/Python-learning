#Age Group Categorization
    #classify a person's age group: Child(<13), teenager (13-19), adult(20-59), senior(60+)

age = int(input("provide me with an age: ")) #input-> takes input as string ,, int()-> covert string into int

if age < 13:
    print("child")
elif age < 20:      #elif --> else if
    print("teen")
elif age < 60:
    print("Adult")
else :
    print("senior")