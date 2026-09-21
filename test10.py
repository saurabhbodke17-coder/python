# id() builtin function
# val = "abc"
# print(id(val))

# upper , lower , title --> string methods

# nested if else 
# if else inside if else 

# driving licence 
# age > 18 and and < 70
# nationality should be indian 
# then you will gett driving licence

age = eval(input("Enter your age: "))
nationality = input("Enrter your nationality: ")

if age >= 18 and age <= 70:
    if nationality.lower() == "indian":
        print("You are eligible for licence")
    else:
        print("Not allowed")    
else:
    print("You are not allowed")

