# Assignment q1
user_input = eval(input("Enter your total bill amount: " ))
if user_input<=0 :
    disc_per = -1
    print("Invalid bill amount")
elif user_input>=5000:
    disc_per = 20
    print("You are getting 20% discount")
elif user_input>=3000 and user_input<=4999 :
    disc_per = 15
    print("You are getting 15% discount")
elif user_input>=1000 and user_input<=2999 :
    disc_per = 10
    print("You are getting 10% discount")
else :
     disc_per = 0

if disc_per != -1:
    discount_amt = (user_input*(disc_per/100))
    final_amt = user_input - discount_amt
    print (user_input)
    print (discount_amt)
    print (final_amt)

# Assignment q2
#    - Age under 12 (Child)        -> Rs. 150
#    - Age 12 to 59 (Adult)        -> Rs. 250
#    - Age 60 and above (Senior)   -> Rs. 180

age = eval(input("Enter your age: "))
day = eval(input("Enter whether its Weekday(0) or Weekend(1): "))

if age < 0 or day < 0 or day >1:
    ticket_prise = -1
    week_status = -1
elif age <12:
    ticket_prise = 150
elif age >= 12 and age <= 59:
    ticket_prise = 250
else:
    ticket_prise = 180


if day == 0:
    extra_charge = 0

elif day == 1:
    extra_charge = 50
else:
    print("please provide correct weekday status")


if ticket_prise != -1 or week_status ==0 or week_status ==1:
    final_amt = ticket_prise + extra_charge
    print(final_amt)
else:
    print("please provide valid inputs")