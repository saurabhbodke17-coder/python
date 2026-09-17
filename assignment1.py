"""
=============================================================================
                          PYTHON ASSIGNMENT 1
Topics Covered: 
  - User Input & Type Conversion (test7.py): input(), int(), float(), eval()
  - Conditional Statements (test8.py): if, elif, else, and, or, ternary operator
=============================================================================
"""

# =============================================================================
# QUESTION 1: Shopping Mall Discount Calculator
# =============================================================================

"""
Problem Statement:
Write a Python program to calculate the discount and final payable amount 
for a customer based on their total bill amount.

Requirements:
1. Ask the user to enter the total bill amount (use float or eval).
2. Input Validation:
   - If the bill amount is 0 or negative, print: "Invalid bill amount!"
3. Discount Rules:
   - If bill amount is Rs. 5000 or more   -> 20% discount
   - If bill amount is Rs. 3000 to 4999  -> 15% discount
   - If bill amount is Rs. 1000 to 2999  -> 10% discount
   - If bill amount is below Rs. 1000    -> No discount (0%)
4. Calculate:
   - Discount amount = bill_amount * (discount_percentage / 100)
   - Final amount = bill_amount - discount_amount
5. Print:
   - Original Bill Amount
   - Discount Percentage & Discount Amount
   - Final Payable Amount

Sample Test Cases:
- Input: 6000  -> 20% discount (Rs. 1200.0), Final Amount: Rs. 4800.0
- Input: 3500  -> 15% discount (Rs. 525.0),  Final Amount: Rs. 2975.0
- Input: 800   -> No discount, Final Amount: Rs. 800.0
- Input: -50   -> "Invalid bill amount!"
"""

# Write your solution for Question 1 below:
user_input = eval(input("Enter your total bill amount: " ))
if user_input<=0 :
    disc_per = 0
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
    print("you are not getting any discounts")

discount_amt = (user_input*(disc_per/100))
final_amt = user_input - discount_amt

print (user_input)
print (discount_amt)
print (final_amt)



# =============================================================================
# QUESTION 2: Movie Ticket Booking System
# =============================================================================

"""
Problem Statement:
Write a Python program to determine the ticket price for a movie based on the 
viewer's age and the day of the week.

Requirements:
1. Ask the user for:
   - Their age (integer input)
   - Day type (string input: "weekday" or "weekend")
2. Validate Age:
   - If age < 0 or age > 120, print: "Invalid age!"
3. Base Ticket Price according to age:
   - Age under 12 (Child)        -> Rs. 150
   - Age 12 to 59 (Adult)        -> Rs. 250
   - Age 60 and above (Senior)   -> Rs. 180
4. Day Charge:
   - If day is "weekend", add an extra charge of Rs. 50 to the ticket price.
   - If day is "weekday", no extra charge.
5. Use a ternary operator to print whether the customer gets a free popcorn coupon:
   - If final ticket price is greater than Rs. 250, print "Free Popcorn Coupon: YES",
     otherwise print "Free Popcorn Coupon: NO".
6. Print:
   - Category (Child / Adult / Senior)
   - Final Ticket Price

Sample Test Cases:
- Age: 10, Day: "weekday" -> Child, Ticket Price: Rs. 150, Free Popcorn: NO
- Age: 25, Day: "weekend" -> Adult, Ticket Price: Rs. 300, Free Popcorn: YES
- Age: 65, Day: "weekend" -> Senior, Ticket Price: Rs. 230, Free Popcorn: NO
- Age: -5, Day: "weekday" -> "Invalid age!"
"""
