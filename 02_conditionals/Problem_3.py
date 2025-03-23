#Grade Calculator
    # Assign a letter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(60 Below)

score = int(input("Enter the student's score: "))

if score > 100:
    print("Enter a valid score..")
    exit()

if score >=90:
    print("A grade")
elif score >=80:
    print("b grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("Fail")
