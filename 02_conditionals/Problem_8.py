#Password Strength Checker
    #Check if a passord is "Weak", "Medium", or "Strong". Criteria: <6 chars(Weak), 6-10 char(Medium), >10 chars(Strong)

password = "Secure@pass"
password_len = len(password)  #basic optimization // baar baar calculate nhi karna padega

if password_len < 6 : #len --> length or in this case char
    strength = "Weak"
elif password_len <= 10 :
    strength = "Medium"
else:
    strength = "Strong"
    
print ("Your Password is", strength)
